#!/usr/bin/env python3
"""
Match original voice line transcriptions to our Trump voice lines.

Reads the Whisper transcriptions and fuzzy-matches each original to the
closest Trump replacement by category and text similarity.

Outputs a mapping file: {original_wem_id: trump_wem_filename}
"""
import json
import re
from difflib import SequenceMatcher
from pathlib import Path
from collections import Counter

from voice_lines import VOICE_LINES, VoiceLine

TRANSCRIPTION_FILE = Path("output/originals_transcriptions.json")
MAPPING_FILE = Path("output/wem_mapping.json")
TRUMP_WEM_DIR = Path("output/wem")


def normalize(text: str) -> str:
    """Normalize text for comparison."""
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text


def similarity(a: str, b: str) -> float:
    """Text similarity score 0-1."""
    return SequenceMatcher(None, normalize(a), normalize(b)).ratio()


# Keyword-based category detection for when fuzzy match isn't enough
CATEGORY_KEYWORDS = {
    "reload": ["reload", "reloading", "mag", "magazine", "ammo", "canister", "ice", "coolant", "team reload", "changing"],
    "grenade": ["grenade", "fire in the hole", "liber-tea", "throwing"],
    "combat": ["get some", "democracy", "freedom", "liberty", "kill", "burn", "fire", "taste"],
    "enemy": ["contact", "enemy", "spotted", "engaging", "patrol", "outpost", "bugs", "bug", "squids", "illuminate", "dropship", "heavy", "aerial", "bot", "fabricator", "wildlife", "fauna", "animal", "bughole", "hive"],
    "stratagem": ["eagle", "orbital", "support weapon", "supplies", "reinforc", "sentry", "fortif", "vehicle", "walker", "equipment", "hellbomb", "sos", "flare", "tacpac", "air support", "calling down", "requesting"],
    "injury": ["bleed", "blood", "hit", "arm", "leg", "wound", "stim", "hurt", "ouch", "ahh", "broken"],
    "healing": ["feels good", "freedom never", "my life for", "my body for", "liberty heal", "liberty save", "stim", "meds", "administering", "helldivers never die", "no pain"],
    "deployment": ["reporting", "duty", "landed", "ready to", "liberate", "joining", "loadout", "weapons ready", "let's do", "rolling out", "drop point", "strategy"],
    "samples": ["sample", "biosample", "biological"],
    "pickup": ["package", "artifact", "legendarium", "e710", "uranium", "saffron", "canister", "technology", "scrap"],
    "marking": ["dropping", "marking", "tagging", "high-value", "critical item", "pin"],
    "ping": ["north", "south", "east", "west", "meters", "close", "far", "objective", "intel", "danger", "alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "code", "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "up", "down", "left", "right", "here", "there", "found", "sub-objective", "primary", "tactical", "extraction point"],
    "movement": ["follow", "move", "hold position", "fall back", "run", "on my way", "heading", "steering", "on my position", "on it"],
    "response": ["affirmative", "negative", "cancel", "nevermind", "yes", "no", "thank", "sorry", "nice", "done", "take it", "don't need"],
    "extraction": ["extraction", "shuttle", "get in"],
    "jumppack": ["jump pack", "skies", "liberty leap"],
    "terminal": ["terminal", "equipment"],
    "weather": ["visibility", "obscure", "target"],
    "patriotic": ["fight for", "soldier", "democracy", "liberty", "prosperity", "super earth", "way of life", "protect", "win", "tie", "play", "good one"],
}


def detect_category(text: str) -> str | None:
    """Detect voice line category from transcribed text using keywords."""
    text_lower = text.lower()
    scores: dict[str, int] = {}
    for category, keywords in CATEGORY_KEYWORDS.items():
        score = 0
        for kw in keywords:
            if kw in text_lower:
                score += len(kw)  # longer matches = more specific = higher weight
        if score > 0:
            scores[category] = score
    if scores:
        return max(scores, key=scores.get)
    return None


def find_best_trump_match(original_text: str, category: str | None) -> tuple[int, float]:
    """Find the best matching Trump voice line index.
    Returns (index into VOICE_LINES, similarity score)."""
    best_idx = 0
    best_score = 0.0

    for i, line in enumerate(VOICE_LINES):
        # Similarity to the original text
        score = similarity(original_text, line.original)

        # Bonus for matching category
        if category and line.category == category:
            score += 0.3

        if score > best_score:
            best_score = score
            best_idx = i

    return best_idx, best_score


def make_trump_filename(index: int) -> str:
    """Reconstruct the Trump WEM filename from voice line index."""
    line = VOICE_LINES[index]
    safe = line.original[:40].replace(" ", "_").replace("!", "").replace("?", "")
    safe = "".join(c for c in safe if c.isalnum() or c == "_")
    return f"{index:03d}_{line.category}_{safe}.wem"


def main():
    if not TRANSCRIPTION_FILE.exists():
        print(f"ERROR: {TRANSCRIPTION_FILE} not found.")
        print("Run transcribe_originals.py first.")
        return

    transcriptions = json.loads(TRANSCRIPTION_FILE.read_text())
    print(f"Loaded {len(transcriptions)} transcriptions")

    # Build mapping
    mapping = {}  # {original_wem_id: trump_wem_filename}
    category_stats = Counter()
    match_scores = []
    unmatched = []

    for wem_id, text in transcriptions.items():
        if not text:
            # Empty transcription (grunt, scream, etc.) - use a combat/patriotic line
            category = "combat"
        else:
            category = detect_category(text)

        trump_idx, score = find_best_trump_match(text, category)
        trump_filename = make_trump_filename(trump_idx)

        # Verify the Trump WEM exists
        trump_path = TRUMP_WEM_DIR / trump_filename
        if not trump_path.exists():
            print(f"  WARNING: {trump_filename} not found!")
            continue

        mapping[wem_id] = trump_filename
        category_stats[VOICE_LINES[trump_idx].category] += 1
        match_scores.append(score)

        if score < 0.3:
            unmatched.append((wem_id, text, trump_filename, score))

    # Save mapping
    MAPPING_FILE.write_text(json.dumps(mapping, indent=2))
    print(f"\nSaved mapping ({len(mapping)} entries) to {MAPPING_FILE}")

    # Stats
    avg_score = sum(match_scores) / len(match_scores) if match_scores else 0
    print(f"\nMatch quality:")
    print(f"  Average similarity: {avg_score:.2f}")
    print(f"  Good matches (>0.5): {sum(1 for s in match_scores if s > 0.5)}")
    print(f"  Okay matches (0.3-0.5): {sum(1 for s in match_scores if 0.3 <= s <= 0.5)}")
    print(f"  Weak matches (<0.3): {sum(1 for s in match_scores if s < 0.3)}")

    print(f"\nCategory distribution of replacements:")
    for cat, count in category_stats.most_common():
        print(f"  {cat:15s}: {count}")

    if unmatched:
        print(f"\nWeakest matches (may need manual review):")
        for wem_id, text, trump_file, score in sorted(unmatched, key=lambda x: x[3])[:20]:
            print(f"  [{score:.2f}] '{text[:50]}' -> {trump_file}")


if __name__ == "__main__":
    main()
