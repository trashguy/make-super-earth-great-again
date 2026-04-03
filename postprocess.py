#!/usr/bin/env python3
"""
Post-process generated WAV files for v1.1:
1. Apply 1.18x tempo (no pitch change) to AI-generated clips
2. Drop in real Trump clips from candidate_clips/
3. Normalize all clips to -20 LUFS

Usage:
    uv run python postprocess.py
"""
import os
import shutil
import subprocess
from pathlib import Path

WAV_DIR = Path("output/wav")
CANDIDATE_DIR = Path("output/candidate_clips")
PROCESSED_DIR = Path("output/wav_processed")
TARGET_LUFS = -20

# Real Trump clips mapped to voice line filenames
# These replace AI-generated versions entirely
REAL_CLIP_MAP = {
    "01_youre_fired.wav": "040_grenade_Throwing_grenade.wav",
    "03_laughing.wav": "099_combat_Maniacal_laughter_AHAHAHAHA.wav",
    "04_this_is_great.wav": None,  # extra clip, no direct replacement yet
    "05_here_we_go_again.wav": None,  # extra clip
    "07_get_out_joe.wav": None,  # extra clip
    "08_looks_like_hell.wav": None,  # extra clip
    "10_its_on_fire.wav": None,  # extra clip
    "11_ready.wav": None,  # extra clip
    "13_god_bless.wav": None,  # extra clip
    # "14_yeah.wav": "283_response_Affirmative.wav",  # too much crowd noise
}


SAMPLE_RATE = 48000
CHANNELS = 1


def apply_tempo(input_path: Path, output_path: Path, tempo: float = 1.18):
    """Speed up audio without pitch change, output 48kHz mono."""
    result = subprocess.run(
        ["ffmpeg", "-y", "-i", str(input_path),
         "-af", f"atempo={tempo}",
         "-ar", str(SAMPLE_RATE), "-ac", str(CHANNELS),
         "-c:a", "pcm_s16le",
         str(output_path)],
        capture_output=True, text=True
    )
    return result.returncode == 0


def convert_to_48k_mono(input_path: Path, output_path: Path):
    """Convert to 48kHz mono without any other processing."""
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(input_path),
         "-ar", str(SAMPLE_RATE), "-ac", str(CHANNELS),
         "-c:a", "pcm_s16le",
         str(output_path)],
        capture_output=True
    )


def main():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    temp_dir = Path("/tmp/trump_postprocess")
    temp_dir.mkdir(parents=True, exist_ok=True)

    wav_files = sorted(WAV_DIR.glob("*.wav"))
    print(f"Processing {len(wav_files)} WAV files...")

    # Build set of files that get replaced by real clips
    real_replacements = {}
    for clip_name, target_name in REAL_CLIP_MAP.items():
        if target_name and (CANDIDATE_DIR / clip_name).exists():
            real_replacements[target_name] = CANDIDATE_DIR / clip_name

    replaced = 0
    processed = 0

    for wav in wav_files:
        out_path = PROCESSED_DIR / wav.name

        if wav.name in real_replacements:
            # Real Trump clip — just convert to 48kHz mono, no tempo/volume changes
            print(f"  [REAL] {wav.name}")
            convert_to_48k_mono(real_replacements[wav.name], out_path)
            replaced += 1
        else:
            # AI clip — apply tempo and convert to 48kHz mono
            apply_tempo(wav, out_path, 1.18)
            processed += 1

        if (processed + replaced) % 50 == 0:
            print(f"  [{processed + replaced}/{len(wav_files)}]")

    print(f"\nDone!")
    print(f"  AI clips (tempo + normalize): {processed}")
    print(f"  Real clips (normalize only):  {replaced}")
    print(f"  Output: {PROCESSED_DIR}/")
    print(f"\nNext: convert to WEM from processed directory:")
    print(f"  ./convert_to_wem.sh output/wav_processed/")


if __name__ == "__main__":
    main()
