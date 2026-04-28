#!/usr/bin/env python3
"""Generate a few bughole variants to pick from."""
import os
import sys
from pathlib import Path
import httpx
import ormsgpack

API_URL = "https://api.fish.audio/v1/tts"
MODEL_ID = "e58b0d7efca34eb38d5c4985e378abcb"

# Load API key
for line in Path(".env").read_text().splitlines():
    if line.startswith("FISH_API_KEY="):
        API_KEY = line.split("=", 1)[1].strip().strip('"').strip("'")
        break

variants = [
    "(urgently) Bug hole! Close it up! Shut it down! Shut it down now!",
    "(shouting) There's a bug hole! A big disgusting bug hole! Close it! Close it!",
    "(angrily) Bug hole right there! Nasty! Very nasty! We gotta shut it down, believe me!",
    "(excitedly) Bug hole! We found a bug hole folks! Somebody close that thing!",
]

out = Path("output/bughole_variants")
out.mkdir(parents=True, exist_ok=True)

client = httpx.Client()
for i, text in enumerate(variants):
    print(f"Variant {i}: {text}")
    payload = {"text": text, "reference_id": MODEL_ID, "format": "wav", "latency": "normal"}
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/msgpack", "model": "s2-pro"}
    r = client.post(API_URL, content=ormsgpack.packb(payload), headers=headers, timeout=30.0)
    r.raise_for_status()
    p = out / f"bughole_v{i}.wav"
    p.write_bytes(r.content)
    print(f"  -> {p} ({len(r.content)} bytes)")

client.close()
print("\nDone! Listen and pick your favorite.")
