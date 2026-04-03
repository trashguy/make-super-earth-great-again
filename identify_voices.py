#!/usr/bin/env python3
"""
Identify which archive is which voice pack by extracting a sample
and comparing audio characteristics.
"""
import os
import sys
import types
import subprocess
from pathlib import Path

sys.modules["pyaudio"] = types.ModuleType("pyaudio")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "tools", "hd2-audio-modder"))

from core import Mod

GAME_DATA = Path(os.path.expanduser(
    "~/.local/share/Steam/steamapps/common/Helldivers 2/data"
))
VGMSTREAM = Path("tools/vgmstream/vgmstream-cli")
SAMPLE_DIR = Path("output/voice_samples")

# The 4 archives with exactly 785 entries
CANDIDATES = [
    "76b0a0e66d61aa15",
    "b98c5b68db4cca84",
    "ce6b3d08283efc3d",
    "e8e43494a3d38e6c",
]


def extract_samples(archive_id: str, num_samples: int = 5):
    """Extract a few WEM samples from an archive, convert to WAV."""
    mod = Mod(archive_id, None)
    mod.load_archive_file(str(GAME_DATA / archive_id))
    sources = mod.get_audio_sources()

    # Pick samples from the middle (avoid short number callouts at edges)
    sorted_ids = sorted(sources.keys())
    step = len(sorted_ids) // (num_samples + 1)
    sample_ids = [sorted_ids[step * (i + 1)] for i in range(num_samples)]

    out_dir = SAMPLE_DIR / archive_id
    out_dir.mkdir(parents=True, exist_ok=True)

    for sid in sample_ids:
        audio = sources[sid]
        wem_path = out_dir / f"{sid}.wem"
        wav_path = out_dir / f"{sid}.wav"

        with open(wem_path, "wb") as f:
            f.write(audio.get_data())

        subprocess.run(
            [str(VGMSTREAM), "-o", str(wav_path), str(wem_path)],
            capture_output=True
        )

    return list(out_dir.glob("*.wav"))


def main():
    SAMPLE_DIR.mkdir(parents=True, exist_ok=True)

    for archive_id in CANDIDATES:
        print(f"\n=== {archive_id} ===")
        wavs = extract_samples(archive_id, num_samples=5)
        print(f"  Extracted {len(wavs)} samples to {SAMPLE_DIR / archive_id}/")
        for w in sorted(wavs):
            print(f"    {w.name}")


if __name__ == "__main__":
    main()
