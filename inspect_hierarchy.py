#!/usr/bin/env python3
"""
Inspect the Wwise hierarchy in the Voice 4 archive to find
named events/segments that we can use to map WEM IDs to voice lines.
"""
import sys
import os
import types

sys.modules["pyaudio"] = types.ModuleType("pyaudio")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "tools", "hd2-audio-modder"))

from core import Mod

GAME_DATA = os.path.expanduser(
    "~/.local/share/Steam/steamapps/common/Helldivers 2/data"
)
VOICE4_ARCHIVE = os.path.join(GAME_DATA, "ce6b3d08283efc3d")


def main():
    print("Loading Voice 4 archive...")
    mod = Mod("voice4", None)
    mod.load_archive_file(VOICE4_ARCHIVE)

    # Check hierarchy entries
    print(f"\nHierarchy entries: {len(mod.hierarchy_entries)}")
    for hid, entry in list(mod.hierarchy_entries.items())[:50]:
        print(f"  {hid}: {type(entry).__name__} - {getattr(entry, 'name', '?')}")

    # Check banks
    print(f"\nWwise banks: {len(mod.wwise_banks)}")
    for bid, bank in mod.wwise_banks.items():
        print(f"  Bank ID: {bid}")
        if hasattr(bank, 'hierarchy') and bank.hierarchy:
            h = bank.hierarchy
            print(f"    Hierarchy entries: {len(h.entries) if hasattr(h, 'entries') else '?'}")
            # Print first few entries
            if hasattr(h, 'entries'):
                for eid, e in list(h.entries.items())[:20]:
                    ename = getattr(e, 'name', None) or getattr(e, 'event_name', None) or ''
                    print(f"      {eid}: {type(e).__name__} {ename}")

    # Check audio sources - look at parent info
    sources = mod.get_audio_sources()
    print(f"\nAudio sources: {len(sources)}")
    for sid, src in list(sorted(sources.items()))[:10]:
        parents = getattr(src, 'parents', [])
        parent_info = []
        for p in parents:
            pname = getattr(p, 'name', None) or getattr(p, 'event_name', None) or type(p).__name__
            parent_info.append(f"{type(p).__name__}({pname})")
        print(f"  {sid}: parents={parent_info}")


if __name__ == "__main__":
    main()
