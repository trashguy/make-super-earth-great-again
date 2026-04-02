#!/usr/bin/env bash
#
# convert_to_wem.sh - Convert WAV files to Wwise WEM (Vorbis) via Wine + WwiseConsole
#
# Usage:
#   ./convert_to_wem.sh                    # converts all WAVs in output/wav/
#   ./convert_to_wem.sh output/wav/        # specify input dir
#   ./convert_to_wem.sh --setup            # install Wwise via wwiser-launcher
#
# Requires: wine, winetricks, zenity
# Wwise version: 2023.1.7.8574 (required for HD2 compatibility)

set -euo pipefail

WWISE_VERSION="2023.1.7.8574"
WWISE_INSTALL_DIR="$HOME/.local/share/wwise"
WWISER_LAUNCHER_DIR="$(dirname "$(realpath "$0")")/tools/wwiser-launcher"
PROJECT_DIR="$(dirname "$(realpath "$0")")"
DEFAULT_INPUT_DIR="$PROJECT_DIR/output/wav"
OUTPUT_DIR="$PROJECT_DIR/output/wem"
CONVERSION_PRESET="Vorbis Quality High"

# Find WwiseConsole.exe in the Wwise installation
find_wwise_console() {
    local candidates=(
        "$WWISE_INSTALL_DIR/Authoring/x64/Release/bin/WwiseConsole.exe"
        "$HOME/.wine/drive_c/Program Files (x86)/Audiokinetic/Wwise $WWISE_VERSION/Authoring/x64/Release/bin/WwiseConsole.exe"
        "$HOME/.wine/drive_c/Program Files/Audiokinetic/Wwise $WWISE_VERSION/Authoring/x64/Release/bin/WwiseConsole.exe"
    )

    # Also search common Wine prefixes
    for prefix in "$HOME/.wine" "$HOME/.local/share/wineprefixes"/*; do
        if [[ -d "$prefix" ]]; then
            while IFS= read -r -d '' f; do
                candidates+=("$f")
            done < <(find "$prefix" -name "WwiseConsole.exe" -print0 2>/dev/null)
        fi
    done

    for path in "${candidates[@]}"; do
        if [[ -f "$path" ]]; then
            echo "$path"
            return 0
        fi
    done

    return 1
}

# Setup: install Wwise via wwiser-launcher
do_setup() {
    echo "=== Wwise Setup ==="
    echo ""
    echo "This will install Wwise $WWISE_VERSION via wwiser-launcher + Wine."
    echo ""

    # Clone wwiser-launcher if needed
    if [[ ! -d "$WWISER_LAUNCHER_DIR" ]]; then
        echo "Cloning wwiser-launcher..."
        mkdir -p "$(dirname "$WWISER_LAUNCHER_DIR")"
        git clone https://github.com/ferdiu/wwiser-launcher.git "$WWISER_LAUNCHER_DIR"
    fi

    echo ""
    echo "Launching wwiser-launcher..."
    echo ""
    echo "  IMPORTANT: When prompted:"
    echo "    1. Select 'Install Packages'"
    echo "    2. Choose Authoring version: $WWISE_VERSION"
    echo "    3. Select at minimum: 'Authoring' package"
    echo "    4. For deployment platforms: select 'Windows'"
    echo "    5. Complete the installation"
    echo ""

    cd "$WWISER_LAUNCHER_DIR"
    python3 wwiser-launcher.py

    echo ""
    if CONSOLE=$(find_wwise_console); then
        echo "WwiseConsole.exe found at: $CONSOLE"
        echo "Setup complete!"
    else
        echo "WARNING: WwiseConsole.exe not found after installation."
        echo "You may need to locate it manually. Check your Wine prefix."
        echo "Then set WWISE_CONSOLE=/path/to/WwiseConsole.exe"
    fi
}

# Generate .wsources XML manifest
generate_wsources() {
    local input_dir="$1"
    local wsources_file="$2"

    # Convert to Windows path for Wine
    local win_input_dir
    win_input_dir=$(winepath -w "$input_dir" 2>/dev/null || echo "Z:$input_dir")

    cat > "$wsources_file" <<XMLEOF
<?xml version="1.0" encoding="UTF-8"?>
<ExternalSourcesList SchemaVersion="1" Root="$win_input_dir">
XMLEOF

    local count=0
    for wav in "$input_dir"/*.wav; do
        [[ -f "$wav" ]] || continue
        local basename
        basename=$(basename "$wav")
        # Skip 0-byte files
        if [[ ! -s "$wav" ]]; then
            echo "  Skipping 0-byte file: $basename"
            continue
        fi
        echo "  <Source Path=\"$basename\" Conversion=\"$CONVERSION_PRESET\"/>" >> "$wsources_file"
        ((count++))
    done

    echo "</ExternalSourcesList>" >> "$wsources_file"
    echo "$count"
}

# Main conversion
do_convert() {
    local input_dir="${1:-$DEFAULT_INPUT_DIR}"

    if [[ ! -d "$input_dir" ]]; then
        echo "Error: Input directory not found: $input_dir"
        exit 1
    fi

    # Count WAV files
    local wav_count
    wav_count=$(find "$input_dir" -name "*.wav" -size +0c | wc -l)
    if [[ "$wav_count" -eq 0 ]]; then
        echo "Error: No WAV files found in $input_dir"
        exit 1
    fi

    echo "=== WAV to WEM Conversion ==="
    echo "Input:  $input_dir ($wav_count WAV files)"
    echo "Output: $OUTPUT_DIR"
    echo "Codec:  $CONVERSION_PRESET"
    echo ""

    # Find WwiseConsole
    local console="${WWISE_CONSOLE:-}"
    if [[ -z "$console" ]]; then
        if ! console=$(find_wwise_console); then
            echo "Error: WwiseConsole.exe not found."
            echo "Run './convert_to_wem.sh --setup' first, or set WWISE_CONSOLE=/path/to/WwiseConsole.exe"
            exit 1
        fi
    fi
    echo "Using: $console"
    echo ""

    # Create temp working directory
    local tmpdir
    tmpdir=$(mktemp -d /tmp/wwise-convert-XXXXXX)
    trap "rm -rf '$tmpdir'" EXIT

    # Create a Wwise project via WwiseConsole
    # It requires the .wproj in a folder matching the project name, and the folder must NOT already exist
    local proj_name="hd2mod"
    local wproj="$tmpdir/$proj_name/$proj_name.wproj"
    local win_proj_path
    win_proj_path=$(WINEDEBUG=-all winepath -w "$wproj" 2>/dev/null || echo "Z:$wproj")

    echo "Creating Wwise project..."
    WINEDEBUG=-all wine "$console" create-new-project "$win_proj_path" 2>&1 | grep -v "^$" | grep -v "^[0-9a-f]*:fixme" || true

    if [[ ! -s "$wproj" ]]; then
        echo "  ERROR: Failed to create Wwise project."
        exit 1
    fi
    echo "  OK"

    # Generate .wsources manifest
    local wsources="$tmpdir/sources.wsources"
    echo "Generating conversion manifest..."
    local source_count
    source_count=$(generate_wsources "$input_dir" "$wsources")
    echo "  $source_count files to convert"
    echo ""

    # Convert
    local win_wsources win_output
    win_wsources=$(winepath -w "$wsources" 2>/dev/null || echo "Z:$wsources")

    mkdir -p "$OUTPUT_DIR"
    win_output=$(winepath -w "$OUTPUT_DIR" 2>/dev/null || echo "Z:$OUTPUT_DIR")

    echo "Converting $source_count WAV files to WEM..."
    echo ""

    WINEDEBUG=-all wine "$console" convert-external-source \
        "$win_proj_path" \
        --source-file "$win_wsources" \
        --output "$win_output" \
        2>&1 | while IFS= read -r line; do
            # Filter out Wine fixme noise
            [[ "$line" =~ ^[0-9a-f]+:fixme ]] && continue
            echo "  $line"
        done

    # WwiseConsole outputs to a Windows/ subdirectory — move files up
    if [[ -d "$OUTPUT_DIR/Windows" ]]; then
        mv "$OUTPUT_DIR/Windows/"*.wem "$OUTPUT_DIR/" 2>/dev/null || true
        rm -f "$OUTPUT_DIR/Windows/Wwise.dat" 2>/dev/null || true
        rmdir "$OUTPUT_DIR/Windows" 2>/dev/null || true
    fi

    local wem_count
    wem_count=$(find "$OUTPUT_DIR" -maxdepth 1 -name "*.wem" 2>/dev/null | wc -l)

    echo ""
    echo "=== Done ==="
    echo "Converted: $wem_count WEM files"
    echo "Output:    $OUTPUT_DIR/"

    if [[ "$wem_count" -lt "$source_count" ]]; then
        echo ""
        echo "WARNING: Only $wem_count of $source_count files converted."
        echo "Check Wine output above for errors."
    fi
}

# Main
case "${1:-}" in
    --setup|-s)
        do_setup
        ;;
    --help|-h)
        echo "Usage:"
        echo "  ./convert_to_wem.sh --setup         Install Wwise via Wine"
        echo "  ./convert_to_wem.sh [input_dir]      Convert WAVs to WEM"
        echo "  ./convert_to_wem.sh                   Convert output/wav/ to WEM"
        echo ""
        echo "Environment:"
        echo "  WWISE_CONSOLE=/path/to/WwiseConsole.exe   Override auto-detection"
        ;;
    *)
        do_convert "$@"
        ;;
esac
