#!/usr/bin/env python3
"""
Export voice line ID mappings for all 4 helldiver voice packs.
Outputs one JSON file per voice pack with WEM short_id, archive_id, and transcribed text.

Uses Voice 4 transcriptions as the reference since all 4 share the same script.
"""
import json
import os
import sys
import types

sys.modules["pyaudio"] = types.ModuleType("pyaudio")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "tools", "hd2-audio-modder"))

from core import Mod

GAME_DATA = os.path.expanduser(
    "~/.local/share/Steam/steamapps/common/Helldivers 2/data"
)

VOICES = {
    "voice1_female_erica_lindbeck": "7c221cf5b12213ac",
    "voice2_male_yuri_lowenthal": "a0a29953a5d45065",
    "voice3_female_julie_nathanson": "5ab4204a4e0ccbe8",
    "voice4_male_robbie_daymond": "ce6b3d08283efc3d",
}

OUTPUT_DIR = "output/gist"


def extract_voice(name: str, archive_id: str, transcriptions: dict | None = None) -> list[dict]:
    """Extract all WEM IDs from a voice archive."""
    archive_path = os.path.join(GAME_DATA, archive_id)
    if not os.path.exists(archive_path):
        print(f"  Archive not found: {archive_path}")
        return []

    mod = Mod(name, None)
    ok = mod.load_archive_file(archive_path)
    if not ok:
        print(f"  Failed to load archive")
        return []

    sources = mod.get_audio_sources()

    # Build full_id -> short_id lookup
    entries = []
    for short_id, audio in sorted(sources.items()):
        full_id = audio.get_id()
        size = len(audio.get_data()) if audio.get_data() else 0

        entry = {
            "wem_short_id": short_id,
            "archive_file_id": full_id,
            "size_bytes": size,
        }

        # Add transcription if available (from Voice 4 reference)
        if transcriptions:
            text = transcriptions.get(str(full_id), "")
            if text:
                entry["text"] = text

        entries.append(entry)

    return entries


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load Voice 4 transcriptions as reference
    transcription_file = "output/originals_transcriptions.json"
    v4_transcriptions = {}
    if os.path.exists(transcription_file):
        v4_transcriptions = json.load(open(transcription_file))
        print(f"Loaded {len(v4_transcriptions)} transcriptions from Voice 4")

    for name, archive_id in VOICES.items():
        print(f"\nExtracting {name} ({archive_id})...")

        # Only Voice 4 has transcriptions mapped by archive_file_id
        # Other voices have different IDs but same lines, so we match by index
        is_v4 = archive_id == "ce6b3d08283efc3d"
        transcriptions = v4_transcriptions if is_v4 else None

        entries = extract_voice(name, archive_id, transcriptions)
        print(f"  {len(entries)} WEM entries")

        # If not Voice 4, try to match transcriptions by sorted index
        # (all voices share the same script in the same order)
        if not is_v4 and v4_transcriptions:
            v4_entries = extract_voice("v4_ref", "ce6b3d08283efc3d", v4_transcriptions)
            v4_texts = [e.get("text", "") for e in sorted(v4_entries, key=lambda x: x["wem_short_id"])]
            sorted_entries = sorted(entries, key=lambda x: x["wem_short_id"])
            if len(sorted_entries) == len(v4_texts):
                for entry, text in zip(sorted_entries, v4_texts):
                    if text:
                        entry["text_from_voice4"] = text
                print(f"  Matched {len(v4_texts)} transcriptions from Voice 4 by index")
            else:
                print(f"  WARNING: Entry count mismatch ({len(sorted_entries)} vs {len(v4_texts)}), skipping text match")

        # Save
        out_path = os.path.join(OUTPUT_DIR, f"{name}.json")
        output = {
            "voice_pack": name.replace("_", " ").title(),
            "archive_id": archive_id,
            "game": "Helldivers 2",
            "language": "English (US)",
            "total_wem_entries": len(entries),
            "note": "wem_short_id is used by hd2-audio-modder import_wems(). archive_file_id is the full Stingray file ID. Text transcribed via OpenAI Whisper base.en model - may contain minor errors.",
            "entries": sorted(entries, key=lambda x: x.get("text", x.get("text_from_voice4", "")))
        }
        with open(out_path, "w") as f:
            json.dump(output, f, indent=2)
        print(f"  Saved {out_path}")

    print(f"\nDone! Files in {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
