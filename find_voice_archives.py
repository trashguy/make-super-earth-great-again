#!/usr/bin/env python3
"""
Find all voice pack archives by scanning game data for archives
with ~700-800 wwise_stream entries (matching Voice 4's 785).
"""
import os
import sys
import types
import struct
from pathlib import Path

sys.modules["pyaudio"] = types.ModuleType("pyaudio")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "tools", "hd2-audio-modder"))

from core import Mod

GAME_DATA = Path(os.path.expanduser(
    "~/.local/share/Steam/steamapps/common/Helldivers 2/data"
))

# Known Voice 4
KNOWN = {"ce6b3d08283efc3d": "Voice 4 (Male, Robbie Daymond)"}

def main():
    # Find all archives that have a .stream companion (voice archives use streaming)
    stream_files = sorted(GAME_DATA.glob("*.stream"))
    print(f"Found {len(stream_files)} archives with .stream files")

    # Filter to ones that also don't have .gpu_resources (voice-only, not textures)
    candidates = []
    for sf in stream_files:
        archive_id = sf.stem
        toc = GAME_DATA / archive_id
        gpu = GAME_DATA / f"{archive_id}.gpu_resources"
        if toc.exists() and not gpu.exists():
            # Check stream file size - voice packs are typically 5-30MB
            stream_size = sf.stat().st_size
            if 1_000_000 < stream_size < 50_000_000:
                candidates.append((archive_id, stream_size))

    print(f"Candidates (stream-only, 1-50MB): {len(candidates)}")
    print()

    # Try loading each and count audio sources
    results = []
    for archive_id, stream_size in candidates:
        try:
            mod = Mod(archive_id, None)
            ok = mod.load_archive_file(str(GAME_DATA / archive_id))
            if not ok:
                continue
            sources = mod.get_audio_sources()
            count = len(sources)
            stream_mb = stream_size / (1024 * 1024)
            label = KNOWN.get(archive_id, "")
            results.append((archive_id, count, stream_mb, label))
        except Exception as e:
            pass

    # Sort by entry count, show ones in the 600-900 range (likely voice packs)
    results.sort(key=lambda x: x[1], reverse=True)

    print(f"{'Archive ID':<20} {'Entries':>8} {'Stream MB':>10}  Label")
    print("-" * 65)
    for archive_id, count, stream_mb, label in results:
        marker = " <---" if 600 <= count <= 900 else ""
        if label:
            marker = f" <--- {label}"
        print(f"{archive_id:<20} {count:>8} {stream_mb:>10.1f}  {marker}")


if __name__ == "__main__":
    main()
