# Building TrumpDivers Voice Pack

Full build pipeline for generating, converting, and packaging the mod from scratch.

## Requirements

- Linux (tested on Arch)
- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- Wine (for WAV to WEM conversion)
- ffmpeg
- Helldivers 2 installed via Steam (Proton)
- ~$1-5 in [Fish Audio](https://fish.audio) credit for voice generation

## Setup

```bash
git clone https://github.com/trashguy/make-super-earth-great-again.git
cd make-super-earth-great-again
uv sync
```

## Step 1: Generate Trump voice lines

Create a Fish Audio account at https://fish.audio, add credit, and grab your API key.

```bash
echo 'FISH_API_KEY=your-key-here' > .env
```

Preview what will be generated:
```bash
uv run python generate.py --dry-run
```

Generate all 336 voice lines:
```bash
uv run python generate.py
```

Generate a single category to test:
```bash
uv run python generate.py --category grenade
```

Regenerate specific lines that sound off:
```bash
uv run python generate.py --only 42 43 44
```

Resume after interruption (skips existing files):
```bash
uv run python generate.py --resume
```

Output: `output/wav/*.wav` (336 files)

## Step 2: Install Wwise (one-time)

Wwise is required to convert WAV to the game's WEM audio format. The official Wwise Launcher is broken on Linux, so we have a custom downloader that talks to Audiokinetic's API directly.

```bash
uv run python tools/download_wwise.py
```

This downloads Wwise 2023.1.7.8574 Authoring and extracts it into your Wine prefix at `~/.wine/drive_c/Program Files (x86)/Audiokinetic/`.

You may also need the VC++ runtime:
```bash
winetricks vcrun2015
```

## Step 3: Convert WAV to WEM

```bash
./convert_to_wem.sh
```

Batch-converts all 336 WAVs to Vorbis-encoded WEM files via WwiseConsole under Wine.

Output: `output/wem/*.wem` (336 files)

## Step 4: Extract and transcribe original voice lines

Extract the original Voice 4 audio from your game install and transcribe with Whisper for category matching:

```bash
uv run python extract_originals.py
uv run python transcribe_originals.py
```

`extract_originals.py` pulls all 785 WEM files from the Voice 4 archive (`ce6b3d08283efc3d`).

`transcribe_originals.py` converts them to WAV via vgmstream and runs OpenAI Whisper (base.en model) to get text transcriptions. This runs on CPU and takes a few minutes.

Output: `output/originals_transcriptions.json`

## Step 5: Match originals to Trump lines

```bash
uv run python match_lines.py
```

Fuzzy-matches each of the 785 original voice lines to the closest Trump replacement by text similarity and keyword-based category detection. A "Reloading!" original gets a Trump reloading line, "Grenade!" gets "You're fired!", etc.

Output: `output/wem_mapping.json`

## Step 6: Build and package the mod

```bash
uv run python build_mod.py
```

Loads the game's Voice 4 archive, replaces all 785 WEM audio sources with category-matched Trump WEMs, writes the patch files, and packages everything into a distributable zip.

Output:
- `output/mod/ce6b3d08283efc3d.patch_0` — patch data
- `output/mod/ce6b3d08283efc3d.patch_0.stream` — audio data (~28 MB)
- `output/mod/manifest.json` — mod manager manifest
- `output/dist/TrumpDivers-Voice-Pack-v1.0.0.zip` — ready to distribute

## Release Workflow

Rebuild against the current game version and package:
```bash
./release.sh
```

Check if the game was updated since the last build:
```bash
./release.sh --check
```

Rebuild and create a GitHub release:
```bash
./release.sh --publish
```

Or use the Claude Code skill:
```
/ship
```

## Customization

### Change the voice model

The default model is Fish Audio's "POTUS 47" (`e58b0d7efca34eb38d5c4985e378abcb`). Use any Fish Audio model:

```bash
uv run python generate.py --model-id YOUR_MODEL_ID
```

### Edit voice lines

All Trump dialogue is in `voice_lines.py`. Edit the `trump` field on any `VoiceLine` entry and regenerate:

```bash
uv run python generate.py --only 42  # regenerate just line 42
```

### Replace a different voice pack

Change `VOICE4_ARCHIVE` in `extract_originals.py` and `build_mod.py` to target a different voice:

| Voice | Archive ID |
|-------|-----------|
| Voice 1 (Female) | Check community spreadsheet |
| Voice 2 (Male) | Check community spreadsheet |
| Voice 3 (Female) | Check community spreadsheet |
| Voice 4 (Male) | `ce6b3d08283efc3d` |

## Project Structure

```
make-super-earth-great-again/
  voice_lines.py              # 336 Trumpified voice line definitions
  generate.py                 # Fish Audio TTS batch generation
  convert_to_wem.sh           # WAV -> WEM conversion via Wine + Wwise
  extract_originals.py        # Extract original WEMs from game archive
  transcribe_originals.py     # Whisper speech-to-text on originals
  match_lines.py              # Fuzzy-match originals to Trump lines
  build_mod.py                # Build patch files and package zip
  release.sh                  # One-command rebuild + GitHub release
  tools/
    download_wwise.py         # Audiokinetic API downloader (bypasses broken launcher)
    hd2-audio-modder/         # HD2 audio modding library (cloned at setup)
    vgmstream/                # WEM -> WAV decoder (downloaded at setup)
    filediver-cli/            # HD2 asset extractor (downloaded at setup)
  output/
    wav/                      # Generated Trump WAV files
    wem/                      # Converted Trump WEM files
    originals/                # Extracted original WEM files
    originals_wav/            # Converted original WAV files
    originals_transcriptions.json
    wem_mapping.json          # Original -> Trump WEM mapping
    mod/                      # Built patch files + manifest
    dist/                     # Distributable zip
```
