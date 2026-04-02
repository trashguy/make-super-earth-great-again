#!/usr/bin/env python3
"""
Convert original WEM files to WAV, then transcribe with Whisper.
Outputs a mapping of WEM ID -> transcribed text for voice line matching.
"""
import subprocess
import json
import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

VGMSTREAM = Path("tools/vgmstream/vgmstream-cli")
ORIGINALS_DIR = Path("output/originals")
WAV_DIR = Path("output/originals_wav")
TRANSCRIPTION_FILE = Path("output/originals_transcriptions.json")


def convert_wem_to_wav(wem_path: Path) -> Path | None:
    """Convert a single WEM to WAV using vgmstream."""
    wav_path = WAV_DIR / f"{wem_path.stem}.wav"
    if wav_path.exists():
        return wav_path
    result = subprocess.run(
        [str(VGMSTREAM), "-o", str(wav_path), str(wem_path)],
        capture_output=True, text=True
    )
    if result.returncode == 0 and wav_path.exists():
        return wav_path
    return None


def main():
    WAV_DIR.mkdir(parents=True, exist_ok=True)

    # Step 1: Convert all WEMs to WAV
    wem_files = sorted(ORIGINALS_DIR.glob("*.wem"))
    print(f"Converting {len(wem_files)} WEM files to WAV...")

    converted = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(convert_wem_to_wav, wem_files))

    for wem, wav in zip(wem_files, results):
        if wav:
            converted.append((wem.stem, wav))
        else:
            print(f"  FAILED: {wem.name}")

    print(f"Converted: {len(converted)} / {len(wem_files)}")

    # Step 2: Transcribe with Whisper
    print(f"\nLoading Whisper model (base.en)...")
    import whisper
    model = whisper.load_model("base.en")

    transcriptions = {}
    total = len(converted)

    print(f"Transcribing {total} audio files...")
    for i, (wem_id, wav_path) in enumerate(converted):
        try:
            result = model.transcribe(
                str(wav_path),
                language="en",
                fp16=False,  # CPU-safe
            )
            text = result["text"].strip()
            transcriptions[wem_id] = text
            if (i + 1) % 50 == 0 or i == 0:
                print(f"  [{i+1}/{total}] {wem_id}: {text[:80]}")
        except Exception as e:
            print(f"  ERROR transcribing {wem_id}: {e}")
            transcriptions[wem_id] = ""

    # Save transcriptions
    TRANSCRIPTION_FILE.write_text(json.dumps(transcriptions, indent=2))
    print(f"\nSaved {len(transcriptions)} transcriptions to {TRANSCRIPTION_FILE}")

    # Print summary
    empty = sum(1 for v in transcriptions.values() if not v)
    print(f"  Non-empty transcriptions: {len(transcriptions) - empty}")
    print(f"  Empty/failed: {empty}")

    # Show some samples
    print(f"\nSample transcriptions:")
    for wem_id, text in list(transcriptions.items())[:20]:
        print(f"  {wem_id}: {text[:100]}")


if __name__ == "__main__":
    main()
