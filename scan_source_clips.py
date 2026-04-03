#!/usr/bin/env python3
"""
Scan source audio clips with Whisper to get timestamped transcriptions.
Outputs segments with timestamps so we can find usable clips.
"""
import json
import os
from pathlib import Path

import whisper

SOURCE_DIR = Path("output/source_clips")
OUTPUT_DIR = Path("output/source_clips/transcriptions")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    model = whisper.load_model("base.en")
    wav_files = sorted(SOURCE_DIR.glob("*.wav"))
    print(f"Found {len(wav_files)} source files\n")

    for wav in wav_files:
        out_file = OUTPUT_DIR / f"{wav.stem}.json"
        if out_file.exists():
            print(f"[cached] {wav.name}")
            continue

        print(f"Transcribing: {wav.name}...")
        result = model.transcribe(
            str(wav),
            language="en",
            fp16=False,
            word_timestamps=True,
        )

        # Extract segments with timestamps
        segments = []
        for seg in result["segments"]:
            segments.append({
                "start": round(seg["start"], 2),
                "end": round(seg["end"], 2),
                "duration": round(seg["end"] - seg["start"], 2),
                "text": seg["text"].strip(),
            })

        output = {
            "source_file": wav.name,
            "total_segments": len(segments),
            "segments": segments,
        }

        out_file.write_text(json.dumps(output, indent=2))
        print(f"  {len(segments)} segments -> {out_file.name}")

    # Now print a combined summary sorted by potential usefulness
    print(f"\n{'='*80}")
    print("ALL SEGMENTS - sorted by duration (short clips first)")
    print(f"{'='*80}\n")

    all_segments = []
    for jf in sorted(OUTPUT_DIR.glob("*.json")):
        data = json.loads(jf.read_text())
        source = data["source_file"]
        for seg in data["segments"]:
            seg["source"] = source
            all_segments.append(seg)

    # Sort by duration - short clips are most useful for voice lines
    all_segments.sort(key=lambda s: s["duration"])

    # Print short ones first (under 3 seconds = potential voice line replacements)
    print("### Short clips (under 3 seconds) - potential voice line replacements:\n")
    short = [s for s in all_segments if s["duration"] <= 3.0]
    for s in short:
        print(f"  [{s['start']:>7.2f}-{s['end']:>7.2f}] ({s['duration']:.1f}s) {s['text'][:80]}")
        print(f"    Source: {s['source']}")

    print(f"\n### Medium clips (3-6 seconds):\n")
    medium = [s for s in all_segments if 3.0 < s["duration"] <= 6.0]
    for s in medium:
        print(f"  [{s['start']:>7.2f}-{s['end']:>7.2f}] ({s['duration']:.1f}s) {s['text'][:80]}")
        print(f"    Source: {s['source']}")

    print(f"\n### Longer clips (6+ seconds) - may contain extractable moments:\n")
    longer = [s for s in all_segments if s["duration"] > 6.0]
    for s in longer[:30]:  # limit output
        print(f"  [{s['start']:>7.2f}-{s['end']:>7.2f}] ({s['duration']:.1f}s) {s['text'][:80]}")
        print(f"    Source: {s['source']}")

    print(f"\nTotal: {len(short)} short, {len(medium)} medium, {len(longer)} long")

    # Save combined for reference
    combined_path = OUTPUT_DIR / "_all_segments.json"
    combined_path.write_text(json.dumps(all_segments, indent=2))
    print(f"Saved combined segments to {combined_path}")


if __name__ == "__main__":
    main()
