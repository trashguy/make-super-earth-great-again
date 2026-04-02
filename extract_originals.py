#!/usr/bin/env python3
"""
Extract original WEM IDs and audio from Helldiver Voice 4 archive.
This lets us listen to the originals and map them to our Trump replacements.
"""
import sys
import os
import types

# Stub out pyaudio before importing core (it's only used for GUI playback)
sys.modules["pyaudio"] = types.ModuleType("pyaudio")

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "tools", "hd2-audio-modder"))

from core import Mod

GAME_DATA = os.path.expanduser(
    "~/.local/share/Steam/steamapps/common/Helldivers 2/data"
)
VOICE4_ARCHIVE = os.path.join(GAME_DATA, "ce6b3d08283efc3d")
OUTPUT_DIR = "output/originals"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Loading Voice 4 archive...")
    mod = Mod("voice4", None)
    ok = mod.load_archive_file(VOICE4_ARCHIVE)
    if not ok:
        print(f"ERROR: Failed to load archive {VOICE4_ARCHIVE}")
        sys.exit(1)

    sources = mod.get_audio_sources()
    print(f"Found {len(sources)} audio sources in Voice 4 archive")
    print()

    # Print all WEM IDs with sizes
    sorted_sources = sorted(sources.items(), key=lambda x: x[0])
    for wem_id, audio in sorted_sources:
        size = len(audio.get_data()) if audio.get_data() else 0
        print(f"  WEM ID: {wem_id:>12d}  Size: {size:>8d} bytes")

    # Dump originals as WEM files
    print(f"\nExtracting {len(sources)} original WEM files to {OUTPUT_DIR}/...")
    mod.dump_multiple_as_wem(list(sources.keys()), OUTPUT_DIR)
    print("Done!")

    # Save ID list for the packaging script
    id_list_path = os.path.join(OUTPUT_DIR, "wem_ids.txt")
    with open(id_list_path, "w") as f:
        for wem_id, audio in sorted_sources:
            size = len(audio.get_data()) if audio.get_data() else 0
            f.write(f"{wem_id}\t{size}\n")
    print(f"WEM ID list saved to {id_list_path}")


if __name__ == "__main__":
    main()
