#!/usr/bin/env bash
#
# release.sh - Rebuild the mod against the current game version and package a release
#
# Usage:
#   ./release.sh              # rebuild + package
#   ./release.sh --publish    # rebuild + package + create GitHub release
#   ./release.sh --check      # just check if game was updated since last build
#
# Version format: v1.0.0-hd22468630
#                 ^semver ^HD2 Steam build ID

set -euo pipefail

PROJECT_DIR="$(dirname "$(realpath "$0")")"
cd "$PROJECT_DIR"

MOD_VERSION="1.1.0"
STEAM_APPS="$HOME/.local/share/Steam/steamapps"
MANIFEST="$STEAM_APPS/appmanifest_553850.acf"
GAME_DIR="$STEAM_APPS/common/Helldivers 2"
LAST_BUILD_FILE="$PROJECT_DIR/.last_build_id"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
get_game_build_id() {
    grep -oP '"buildid"\s+"\K[0-9]+' "$MANIFEST"
}

get_last_build_id() {
    if [[ -f "$LAST_BUILD_FILE" ]]; then
        cat "$LAST_BUILD_FILE"
    else
        echo "none"
    fi
}

save_build_id() {
    echo "$1" > "$LAST_BUILD_FILE"
}

# ---------------------------------------------------------------------------
# Check
# ---------------------------------------------------------------------------
do_check() {
    local current last
    current=$(get_game_build_id)
    last=$(get_last_build_id)

    echo "Current HD2 build: $current"
    echo "Last mod build:    $last"

    if [[ "$current" == "$last" ]]; then
        echo "No update needed."
        return 1
    else
        echo "Game was updated! Rebuild recommended."
        return 0
    fi
}

# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
do_build() {
    local build_id
    build_id=$(get_game_build_id)
    local full_version="v${MOD_VERSION}-hd${build_id}"
    local zip_name="Make-Super-Earth-Great-Again-${full_version}.zip"

    echo "============================================"
    echo "  TrumpDivers Release Build"
    echo "  Version: ${full_version}"
    echo "  HD2 Build: ${build_id}"
    echo "============================================"
    echo ""

    # Step 1: Check if Trump WAVs exist (don't regenerate - costs money)
    if [[ $(find output/wav -name "*.wav" -size +0c 2>/dev/null | wc -l) -lt 300 ]]; then
        echo "ERROR: Less than 300 WAV files in output/wav/"
        echo "Run 'uv run python generate.py' first (requires Fish Audio API key)"
        exit 1
    fi
    echo "[1/5] Trump WAV files: OK ($(ls output/wav/*.wav | wc -l) files)"

    # Step 2: Check if WEM files exist, rebuild if needed
    local wav_count wem_count
    wav_count=$(ls output/wav/*.wav 2>/dev/null | wc -l)
    wem_count=$(ls output/wem/*.wem 2>/dev/null | wc -l)
    if [[ "$wem_count" -lt "$wav_count" ]]; then
        echo "[2/5] Converting WAV to WEM..."
        ./convert_to_wem.sh
    else
        echo "[2/5] Trump WEM files: OK ($wem_count files)"
    fi

    # Step 3: Extract and transcribe originals from current game version
    echo "[3/5] Extracting and transcribing original voice lines..."
    uv run python extract_originals.py
    uv run python transcribe_originals.py

    # Step 4: Match originals to Trump lines
    echo "[4/5] Matching voice lines..."
    uv run python match_lines.py

    # Step 5: Build mod and package
    echo "[5/5] Building mod package..."
    uv run python build_mod.py

    # Rename the zip with the full version
    local src_zip="output/dist/Make-Super-Earth-Great-Again-v${MOD_VERSION}.zip"
    local dst_zip="output/dist/${zip_name}"
    if [[ -f "$src_zip" && "$src_zip" != "$dst_zip" ]]; then
        mv "$src_zip" "$dst_zip"
    fi

    save_build_id "$build_id"

    echo ""
    echo "============================================"
    echo "  Release ready!"
    echo "  ${dst_zip}"
    echo "  Version: ${full_version}"
    echo "============================================"
}

# ---------------------------------------------------------------------------
# Publish to GitHub
# ---------------------------------------------------------------------------
do_publish() {
    local build_id
    build_id=$(get_game_build_id)
    local full_version="v${MOD_VERSION}-hd${build_id}"
    local zip_name="Make-Super-Earth-Great-Again-${full_version}.zip"
    local zip_path="output/dist/${zip_name}"

    if [[ ! -f "$zip_path" ]]; then
        echo "Zip not found, building first..."
        do_build
    fi

    echo ""
    echo "Publishing ${full_version} to GitHub..."

    # Check if tag already exists
    if git rev-parse "$full_version" >/dev/null 2>&1; then
        echo "Tag ${full_version} already exists!"
        echo "Bump MOD_VERSION in release.sh if this is a new mod version."
        exit 1
    fi

    git tag -a "$full_version" -m "Release ${full_version} for HD2 build ${build_id}"

    gh release create "$full_version" \
        "$zip_path" \
        --title "TrumpDivers Voice Pack ${full_version}" \
        --notes "$(cat <<EOF
## TrumpDivers Voice Pack ${full_version}

Replaces Helldiver Voice 4 (Default Male 4) with 336 AI-generated Trump voice lines.

**Built for HD2 Steam build \`${build_id}\`**

### Install
- **Arsenal**: Drag and drop the zip onto the mod list
- **Manual**: Extract both files to \`Helldivers 2/data/\`

### Uninstall
Delete \`ce6b3d08283efc3d.patch_0\` and \`ce6b3d08283efc3d.patch_0.stream\` from the data folder.
EOF
)"

    echo ""
    echo "Published! https://github.com/$(git remote get-url origin | sed 's/.*github.com[:/]\(.*\)\.git/\1/')/releases/tag/${full_version}"
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
case "${1:-}" in
    --check|-c)
        do_check
        ;;
    --publish|-p)
        do_build
        do_publish
        ;;
    --help|-h)
        echo "Usage:"
        echo "  ./release.sh              Rebuild mod against current game version"
        echo "  ./release.sh --check      Check if game was updated since last build"
        echo "  ./release.sh --publish    Rebuild and create GitHub release"
        echo ""
        echo "Version: v${MOD_VERSION}-hd\$(game_build_id)"
        ;;
    *)
        do_build
        ;;
esac
