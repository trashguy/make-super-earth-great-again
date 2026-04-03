#!/usr/bin/env python3
"""
Export all 4 helldiver voice packs as CSVs with WEM IDs and transcribed text.
"""
import csv
import json
import os
import subprocess
import sys
import types
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

sys.modules["pyaudio"] = types.ModuleType("pyaudio")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "tools", "hd2-audio-modder"))

from core import Mod

GAME_DATA = Path(os.path.expanduser(
    "~/.local/share/Steam/steamapps/common/Helldivers 2/data"
))
VGMSTREAM = Path("tools/vgmstream/vgmstream-cli")
OUTPUT_DIR = Path("output/gist")

VOICES = [
    ("voice1_female_erica_lindbeck", "76b0a0e66d61aa15", "Voice 1 - Female (Erica Lindbeck)"),
    ("voice2_male_yuri_lowenthal", "b98c5b68db4cca84", "Voice 2 - Male (Yuri Lowenthal)"),
    ("voice3_female_julie_nathanson", "e8e43494a3d38e6c", "Voice 3 - Female (Julie Nathanson)"),
    ("voice4_male_robbie_daymond", "ce6b3d08283efc3d", "Voice 4 - Male (Robbie Daymond)"),
]


def convert_wem_to_wav(args):
    wem_path, wav_path = args
    subprocess.run(
        [str(VGMSTREAM), "-o", str(wav_path), str(wem_path)],
        capture_output=True
    )
    return wav_path


def process_voice(name, archive_id, display_name):
    print(f"\n{'='*60}")
    print(f"  {display_name}")
    print(f"  Archive: {archive_id}")
    print(f"{'='*60}")

    # Check for cached transcriptions
    cache_file = OUTPUT_DIR / f"{name}_transcriptions.json"
    if cache_file.exists():
        print(f"  Using cached transcriptions from {cache_file}")
        transcriptions = json.loads(cache_file.read_text())
    else:
        # Load archive
        mod = Mod(name, None)
        mod.load_archive_file(str(GAME_DATA / archive_id))
        sources = mod.get_audio_sources()
        print(f"  {len(sources)} WEM entries")

        # Extract all WEMs
        tmp_dir = Path(f"/tmp/voice_export_{name}")
        tmp_dir.mkdir(parents=True, exist_ok=True)

        print(f"  Extracting WEMs...")
        wem_wav_pairs = []
        id_map = {}  # wav_path -> (short_id, full_id)
        for short_id, audio in sources.items():
            full_id = audio.get_id()
            wem_path = tmp_dir / f"{full_id}.wem"
            wav_path = tmp_dir / f"{full_id}.wav"
            if not wav_path.exists():
                with open(wem_path, "wb") as f:
                    f.write(audio.get_data())
                wem_wav_pairs.append((wem_path, wav_path))
            id_map[str(full_id)] = short_id

        # Convert to WAV in parallel
        if wem_wav_pairs:
            print(f"  Converting {len(wem_wav_pairs)} WEMs to WAV...")
            with ThreadPoolExecutor(max_workers=8) as pool:
                list(pool.map(convert_wem_to_wav, wem_wav_pairs))

        # Transcribe
        print(f"  Transcribing with Whisper...")
        import whisper
        model = whisper.load_model("base.en")

        transcriptions = {}
        wav_files = sorted(tmp_dir.glob("*.wav"))
        for i, wav_path in enumerate(wav_files):
            full_id = wav_path.stem
            try:
                result = model.transcribe(str(wav_path), language="en", fp16=False)
                transcriptions[full_id] = result["text"].strip()
            except Exception:
                transcriptions[full_id] = ""
            if (i + 1) % 100 == 0:
                print(f"    [{i+1}/{len(wav_files)}]")

        # Cache transcriptions
        cache_file.write_text(json.dumps(transcriptions, indent=2))
        print(f"  Cached transcriptions to {cache_file}")

    # Reload archive to get ID mapping
    mod = Mod(name, None)
    mod.load_archive_file(str(GAME_DATA / archive_id))
    sources = mod.get_audio_sources()

    # Build CSV
    csv_path = OUTPUT_DIR / f"{name}.csv"
    rows = []
    for short_id, audio in sorted(sources.items()):
        full_id = audio.get_id()
        text = transcriptions.get(str(full_id), "")
        rows.append({
            "wem_short_id": short_id,
            "archive_file_id": full_id,
            "size_bytes": len(audio.get_data()) if audio.get_data() else 0,
            "text": text,
        })

    # Sort by text for readability
    rows.sort(key=lambda r: r["text"].lower())

    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["wem_short_id", "archive_file_id", "size_bytes", "text"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"  Saved {csv_path} ({len(rows)} rows)")
    return csv_path


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Use Voice 4 existing transcriptions as cache
    v4_cache = OUTPUT_DIR / "voice4_male_robbie_daymond_transcriptions.json"
    if not v4_cache.exists():
        existing = Path("output/originals_transcriptions.json")
        if existing.exists():
            import shutil
            shutil.copy2(existing, v4_cache)
            print(f"Copied Voice 4 transcriptions to cache")

    csv_files = []
    for name, archive_id, display_name in VOICES:
        csv_path = process_voice(name, archive_id, display_name)
        csv_files.append(csv_path)

    print(f"\n{'='*60}")
    print(f"  All done! CSVs in {OUTPUT_DIR}/")
    print(f"{'='*60}")
    for f in csv_files:
        print(f"  {f.name}")


if __name__ == "__main__":
    main()
