---
name: ship
# Inspired by https://github.com/Jagg111/COI-ResearchQueue
description: End-to-end release workflow for the TrumpDivers voice mod. Handles pre-flight checks, version bump, mod rebuild, and GitHub release creation.
---

You are running the `/ship` release workflow for the TrumpDivers Helldivers 2 voice mod. Walk through each step in order. Stop and report clearly if anything fails.

---

## Step 1 — Pre-flight checks

Run all checks. If any fail, report what's wrong and stop.

1. Run `git status --porcelain` — must be empty (clean working tree)
2. Run `git branch --show-current` — must be `master`
3. Run `gh auth status` — must succeed
4. Confirm Trump WAV files exist: `ls output/wav/*.wav | wc -l` — must be 300+
5. Confirm Trump WEM files exist: `ls output/wem/*.wem | wc -l` — must be 300+

If everything passes, say "Pre-flight checks passed." and continue.

---

## Step 2 — Detect game version

1. Read the HD2 build ID from `~/.local/share/Steam/steamapps/appmanifest_553850.acf` (the `buildid` field)
2. Read `.last_build_id` if it exists and compare
3. Show the user the current and last build IDs
4. If they differ, warn that the game was updated and the mod will be rebuilt against the new version

---

## Step 3 — Version bump decision

1. Read `MOD_VERSION` from `release.sh` and show the current version
2. Run `git tag --sort=-creatordate` to find the most recent tag. If none, note this is the first release.
3. Run `git log $prevTag..HEAD --pretty=format:"%s"` to show commits since last release
4. Ask the user which bump to apply:
   - **Patch (0.0.X)** — bug fixes, line tweaks, regenerated audio
   - **Minor (0.X.0)** — new voice lines, new categories, new features
   - **Major (X.0.0)** — full rework or major game update forced rebuild
5. Wait for the user to choose before continuing.

---

## Step 4 — Rebuild the mod (if needed)

1. Update `MOD_VERSION` in `release.sh` with the new version
2. Update `MOD_VERSION` in `build_mod.py` with the new version
3. Check if a rebuild is actually needed. A rebuild is needed if ANY of these are true:
   - The game build ID changed since `.last_build_id` (archive may have changed)
   - `voice_lines.py` was modified since the last tag (Trump lines changed)
   - `output/wem/` has fewer files than `output/wav/` (WEM conversion incomplete)
   - `output/wem_mapping.json` does not exist
   - `output/dist/` has no zip file
4. If a rebuild IS needed, run the full pipeline:

```bash
uv run python extract_originals.py
uv run python transcribe_originals.py
uv run python match_lines.py
uv run python build_mod.py
```

5. If a rebuild is NOT needed, just repackage:

```bash
uv run python build_mod.py
```

6. Verify the zip was created in `output/dist/`
7. Show the user the output file name and size

---

## Step 5 — Draft changelog

1. For every commit since the last tag, summarize the player-visible changes
2. Write bullets using these rules:
   - Write for players, not developers
   - Lead with a label: "Fixed:", "Added:", "Changed:", "Improved:"
   - Omit commits with no player-visible effect (build changes, README edits, code cleanup)
   - One bullet per logical change
3. Show the bullets inline and ask: "Any tweaks before I publish?"
4. Wait for approval.

---

## Step 6 — Commit, tag, and release

Once the user approves:

1. Rename the zip to include the full version tag: `TrumpDivers-Voice-Pack-v{VERSION}-hd{BUILD_ID}.zip`
2. Stage changed files (`release.sh`, `build_mod.py`, `.last_build_id`)
3. Suggest a commit message: `Release v{VERSION}-hd{BUILD_ID}`
4. Wait for the user to confirm the commit
5. After commit, create the tag and GitHub release:

```bash
git tag -a "v{VERSION}-hd{BUILD_ID}" -m "Release v{VERSION}-hd{BUILD_ID}"
gh release create "v{VERSION}-hd{BUILD_ID}" \
    "output/dist/TrumpDivers-Voice-Pack-v{VERSION}-hd{BUILD_ID}.zip" \
    --title "TrumpDivers Voice Pack v{VERSION}-hd{BUILD_ID}" \
    --notes "{changelog}"
```

---

## Step 7 — Done

Confirm the release was created. Show the release URL.

Remind the user:
- The release is live on GitHub
- To install locally: `cp output/mod/ce6b3d08283efc3d.patch_0* ~/.local/share/Steam/steamapps/common/Helldivers\ 2/data/`
- Upload the zip to other mod sites (GameBanana, Thunderstore, Modding Discord) if desired
