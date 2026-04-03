#!/usr/bin/env python3
"""
Build the Trump Voice Mod for Helldivers 2.

Uses the transcription-based mapping to replace each original voice line
with a category-matched Trump replacement.

Usage:
    uv run python build_mod.py
"""
import sys
import os
import types
import json
import uuid
import zipfile
from pathlib import Path

# Stub pyaudio (GUI-only dep)
sys.modules["pyaudio"] = types.ModuleType("pyaudio")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "tools", "hd2-audio-modder"))

from core import Mod

GAME_DATA = os.path.expanduser(
    "~/.local/share/Steam/steamapps/common/Helldivers 2/data"
)
VOICE4_ARCHIVE = os.path.join(GAME_DATA, "ce6b3d08283efc3d")
TRUMP_WEM_DIR = Path("output/wem")
MAPPING_FILE = Path("output/wem_mapping.json")
MOD_OUTPUT_DIR = Path("output/mod")
DIST_DIR = Path("output/dist")

MOD_NAME = "TrumpDivers Voice Pack"
MOD_GUID = "d0ca1d47-7247-4f0b-b33a-736172756d70"  # deterministic GUID
MOD_VERSION = "1.1.0"
MOD_DESCRIPTION = "Replaces Helldiver Voice 4 (Default Male 4) with Trump voice lines. 336 unique Trumpified voice lines mapped to all 785 in-game callouts by category."


def load_mapping() -> dict[str, str]:
    """Load the WEM ID -> Trump filename mapping."""
    if not MAPPING_FILE.exists():
        print(f"ERROR: {MAPPING_FILE} not found. Run match_lines.py first.")
        sys.exit(1)
    return json.loads(MAPPING_FILE.read_text())


def build_mod():
    # Load the category-matched mapping
    mapping = load_mapping()
    print(f"Loaded mapping: {len(mapping)} original WEM IDs -> Trump replacements")

    # Load the Voice 4 game archive
    print(f"\nLoading Voice 4 archive...")
    mod = Mod("trump_voice4", None)
    ok = mod.load_archive_file(VOICE4_ARCHIVE)
    if not ok:
        print(f"ERROR: Failed to load archive {VOICE4_ARCHIVE}")
        sys.exit(1)

    sources = mod.get_audio_sources()
    print(f"Original voice lines in archive: {len(sources)}")

    # Build a lookup from full file ID -> short_id
    # The mapping file uses get_id() (full archive file IDs),
    # but import_wems needs short_ids (dict keys in sources)
    full_to_short: dict[int, int] = {}
    for short_id, audio in sources.items():
        full_to_short[audio.get_id()] = short_id

    # Build the import mapping: {trump_wem_path: [original_short_ids]}
    wem_import: dict[str, list[int]] = {}
    matched = 0
    unmatched = 0

    for full_id_str, trump_filename in mapping.items():
        trump_path = str((TRUMP_WEM_DIR / trump_filename).resolve())
        if not os.path.exists(trump_path):
            print(f"  WARNING: {trump_filename} not found, skipping")
            unmatched += 1
            continue

        full_id = int(full_id_str)
        short_id = full_to_short.get(full_id)
        if short_id is None:
            unmatched += 1
            continue

        if trump_path not in wem_import:
            wem_import[trump_path] = []
        wem_import[trump_path].append(short_id)
        matched += 1

    print(f"\nMatched: {matched}, Unmatched: {unmatched}")
    print(f"Unique Trump WEMs used: {len(wem_import)}")

    # Import the WEMs
    print("\nImporting Trump WEMs into archive...")
    mod.import_wems(wem_import)
    print("  Import complete!")

    # Write the patch files
    MOD_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\nWriting mod patch...")
    mod.write_patch(
        output_folder=str(MOD_OUTPUT_DIR.resolve()),
        output_filename="ce6b3d08283efc3d.patch_0"
    )

    # Check output
    patch_file = MOD_OUTPUT_DIR / "ce6b3d08283efc3d.patch_0"
    stream_file = MOD_OUTPUT_DIR / "ce6b3d08283efc3d.patch_0.stream"

    if patch_file.exists():
        print(f"  {patch_file.name} ({patch_file.stat().st_size / 1024:.1f} KB)")
    if stream_file.exists():
        print(f"  {stream_file.name} ({stream_file.stat().st_size / (1024*1024):.1f} MB)")

    # Create manifest.json for Arsenal / HD2ModManager
    manifest = {
        "Version": 1,
        "Guid": MOD_GUID,
        "Name": MOD_NAME,
        "Description": MOD_DESCRIPTION,
        "IconPath": "icon.jpg",
    }
    manifest_path = MOD_OUTPUT_DIR / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    print(f"  manifest.json written")

    # Package as distributable zip
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    zip_name = f"Make-Super-Earth-Great-Again-v{MOD_VERSION}.zip"
    zip_path = DIST_DIR / zip_name

    # Copy icon into mod output
    icon_src = Path("images/icon_512.jpg")
    icon_dst = MOD_OUTPUT_DIR / "icon.jpg"
    if icon_src.exists():
        import shutil
        shutil.copy2(icon_src, icon_dst)

    print(f"\nPackaging {zip_name}...")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(manifest_path, "manifest.json")
        if icon_dst.exists():
            zf.write(icon_dst, "icon.jpg")
        if patch_file.exists():
            zf.write(patch_file, patch_file.name)
        if stream_file.exists():
            zf.write(stream_file, stream_file.name)

    zip_size_mb = zip_path.stat().st_size / (1024 * 1024)
    print(f"  {zip_path} ({zip_size_mb:.1f} MB)")

    print(f"\n{'='*50}")
    print(f"  BUILD COMPLETE!")
    print(f"{'='*50}")
    print(f"\nDistributable: {zip_path}")
    print(f"  Compatible with: Arsenal, HD2ModManager, h2mm-cli")
    print(f"  Voice pack replaced: Default 4 (Male)")
    print(f"  Lines replaced: {matched} / {len(sources)}")
    print(f"\nManual install:")
    print(f"  Copy these to Helldivers 2/data/:")
    print(f"    ce6b3d08283efc3d.patch_0")
    print(f"    ce6b3d08283efc3d.patch_0.stream")
    print(f"\nUninstall:")
    print(f"  Delete those two files from the data folder")


if __name__ == "__main__":
    build_mod()
