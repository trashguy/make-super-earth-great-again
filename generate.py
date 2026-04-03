#!/usr/bin/env python3
"""
Helldivers 2 Trump Voice Mod - Batch Audio Generator

Uses Fish Audio API to generate all voice lines in Trump's voice.

Usage:
    # Set your API key
    export FISH_API_KEY="your-key-here"
    # Or create a .env file with FISH_API_KEY=your-key-here

    # Generate all lines
    uv run python generate.py

    # Generate a specific category
    uv run python generate.py --category combat

    # Regenerate specific lines (by index)
    uv run python generate.py --only 42 43 44

    # Preview what would be generated (dry run)
    uv run python generate.py --dry-run

    # Use a different voice model
    uv run python generate.py --model-id YOUR_MODEL_ID
"""

import argparse
import os
import sys
import time
import json
from pathlib import Path

import httpx
import ormsgpack

from voice_lines import VOICE_LINES

# Fish Audio "POTUS 47" model - high-rated Trump voice
DEFAULT_MODEL_ID = "e58b0d7efca34eb38d5c4985e378abcb"

API_URL = "https://api.fish.audio/v1/tts"
OUTPUT_DIR = Path("output/wav")

# Map our emotion tags to Fish Audio format hints
EMOTION_MAP = {
    "normal": "",
    "confident": "(boldly and confidently) ",
    "excited": "(excitedly, with high energy) ",
    "angry": "(angrily, with real frustration) ",
    "urgent": "(urgently, with intensity) ",
    "shouting": "(shouting loudly) ",
    "whispering": "(whispering) ",
}


def get_api_key() -> str:
    """Get API key from env or .env file."""
    key = os.environ.get("FISH_API_KEY")
    if key:
        return key

    env_file = Path(".env")
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line.startswith("FISH_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")

    print("Error: FISH_API_KEY not set.")
    print("  export FISH_API_KEY='your-key-here'")
    print("  or create .env with FISH_API_KEY=your-key-here")
    print()
    print("Get your key at https://fish.audio (account settings)")
    sys.exit(1)


def generate_line(
    client: httpx.Client,
    api_key: str,
    model_id: str,
    text: str,
    output_path: Path,
    emotion: str = "normal",
) -> bool:
    """Generate a single voice line via Fish Audio API."""
    emotion_prefix = EMOTION_MAP.get(emotion, "")
    full_text = f"{emotion_prefix}{text}"

    payload = {
        "text": full_text,
        "reference_id": model_id,
        "format": "wav",
        "latency": "normal",
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/msgpack",
        "model": "s2-pro",
    }

    try:
        response = client.post(
            API_URL,
            content=ormsgpack.packb(payload),
            headers=headers,
            timeout=30.0,
        )
        response.raise_for_status()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(response.content)
        return True

    except httpx.HTTPStatusError as e:
        print(f"  HTTP error {e.response.status_code}: {e.response.text[:200]}")
        return False
    except httpx.TimeoutException:
        print(f"  Timeout generating: {text[:50]}...")
        return False
    except Exception as e:
        print(f"  Error: {e}")
        return False


def make_filename(index: int, line) -> str:
    """Create a descriptive filename for a voice line."""
    # Sanitize the original line for use in filename
    safe = line.original[:40].replace(" ", "_").replace("!", "").replace("?", "")
    safe = "".join(c for c in safe if c.isalnum() or c == "_")
    return f"{index:03d}_{line.category}_{safe}.wav"


def main():
    parser = argparse.ArgumentParser(description="Generate Trump voice lines for HD2 mod")
    parser.add_argument("--category", "-c", help="Only generate lines from this category")
    parser.add_argument("--only", "-o", nargs="+", type=int, help="Only generate specific line indices")
    parser.add_argument("--dry-run", "-n", action="store_true", help="Preview without generating")
    parser.add_argument("--model-id", "-m", default=DEFAULT_MODEL_ID, help="Fish Audio model ID")
    parser.add_argument("--delay", "-d", type=float, default=0.1, help="Delay between API calls (seconds)")
    parser.add_argument("--resume", "-r", action="store_true", help="Skip lines that already have output files")
    parser.add_argument("--workers", "-w", type=int, default=5, help="Concurrent API workers (default 5)")
    args = parser.parse_args()

    api_key = get_api_key() if not args.dry_run else "dry-run"

    # Filter lines
    lines = list(enumerate(VOICE_LINES))
    if args.category:
        lines = [(i, l) for i, l in lines if l.category == args.category]
    if args.only:
        only_set = set(args.only)
        lines = [(i, l) for i, l in lines if i in only_set]

    if not lines:
        print("No lines matched the filter.")
        return

    # Prepare output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Save a manifest for later WEM mapping
    manifest = []

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Generating {len(lines)} voice lines...")
    print(f"Model: {args.model_id}")
    print(f"Output: {OUTPUT_DIR}/")
    print()

    if args.dry_run:
        for i, line in lines:
            filename = make_filename(i, line)
            emotion_prefix = EMOTION_MAP.get(line.emotion, "")
            print(f"  [{i:3d}] {line.category:12s} | {filename}")
            print(f"         Original: {line.original}")
            print(f"         Trump:    {emotion_prefix}{line.trump}")
            print()
        print(f"Total: {len(lines)} lines")
        return

    # Generate with concurrent workers
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import threading

    success = 0
    failed = 0
    skipped = 0
    lock = threading.Lock()

    # Filter out already-done lines if resuming
    todo = []
    for i, line in lines:
        filename = make_filename(i, line)
        output_path = OUTPUT_DIR / filename
        if args.resume and output_path.exists():
            with lock:
                skipped += 1
                manifest.append({
                    "index": i, "category": line.category,
                    "original": line.original, "trump": line.trump,
                    "emotion": line.emotion, "filename": filename,
                })
            continue
        todo.append((i, line, filename, output_path))

    if skipped:
        print(f"Skipped {skipped} existing files")

    print(f"Generating {len(todo)} lines with {args.workers} workers...")

    def worker(item):
        i, line, filename, output_path = item
        client = httpx.Client()
        try:
            ok = generate_line(client, api_key, args.model_id, line.trump, output_path, line.emotion)
            return (i, line, filename, output_path, ok)
        finally:
            client.close()

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(worker, item): item for item in todo}
        done_count = 0
        for future in as_completed(futures):
            i, line, filename, output_path, ok = future.result()
            done_count += 1
            if ok:
                size_kb = output_path.stat().st_size / 1024
                print(f"  [{done_count}/{len(todo)}] {filename} ({size_kb:.1f} KB)")
                with lock:
                    success += 1
                    manifest.append({
                        "index": i, "category": line.category,
                        "original": line.original, "trump": line.trump,
                        "emotion": line.emotion, "filename": filename,
                    })
            else:
                print(f"  [{done_count}/{len(todo)}] FAILED: {filename}")
                with lock:
                    failed += 1

    # Save manifest
    manifest_path = OUTPUT_DIR / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))

    print()
    print(f"Done! Generated: {success}, Skipped: {skipped}, Failed: {failed}")
    print(f"Manifest: {manifest_path}")
    print()
    if failed > 0:
        print(f"To retry failed lines, run again with --resume")


if __name__ == "__main__":
    main()
