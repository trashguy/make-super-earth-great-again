#!/usr/bin/env python3
"""
Download and install Wwise Authoring into a Wine prefix, bypassing the broken
wwiser-launcher.

The Audiokinetic blob-api now requires an 'X-client-version' header matching a
recent Wwise Launcher build.  wwiser-launcher doesn't send that header, so the
API returns 410 "Launcher version no longer supported."  This script adds the
header and walks the same API the official Electron launcher uses.

Usage:
    python3 download_wwise.py [--version YEAR.MAJOR.MINOR.BUILD]
                              [--prefix /path/to/wine/prefix]
                              [--cache-dir /path/to/cache]
                              [--with-sdk]
                              [--list-versions]

Defaults:
    version   = 2023.1.7.8574
    prefix    = ~/.wine
    cache-dir = ./wwise_cache
"""

import argparse
import base64
import json
import os
import subprocess
import sys
import hashlib
from pathlib import Path

try:
    import httpx
except ImportError:
    print("ERROR: 'httpx' module not found. Run: uv add httpx")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
LOGIN_URL = "https://www.audiokinetic.com/wwise/launcher/?action=login"
BLOB_API = "https://blob-api.gowwise.com"
# This header is required by the API as of 2025+; without it every non-launcher
# category endpoint returns HTTP 410.
CLIENT_VERSION = "2025.1.0.5135"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def decode_payload(response_json: dict) -> dict:
    """Decode the base64 payload wrapper used by all Audiokinetic API responses."""
    return json.loads(base64.b64decode(response_json["payload"]))


def get_guest_jwt() -> str:
    """Authenticate as a guest and return a JWT token."""
    r = httpx.post(LOGIN_URL, json={"email": "", "password": ""}, timeout=30.0)
    r.raise_for_status()
    payload = decode_payload(r.json())
    jwt = payload.get("jwt")
    if not jwt:
        print("ERROR: Failed to obtain guest JWT.")
        sys.exit(1)
    return jwt


def api_headers(jwt: str) -> dict:
    return {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json",
        "X-client-version": CLIENT_VERSION,
    }


def api_get(jwt: str, path: str, version_prefix: int = 0):
    """Signed GET against blob-api. Returns decoded payload data."""
    pfx = f"/v{version_prefix}" if version_prefix else ""
    url = f"{BLOB_API}{pfx}{path}"
    r = httpx.get(url, headers=api_headers(jwt), timeout=30.0)
    r.raise_for_status()
    decoded = decode_payload(r.json())
    status = decoded.get("statusCode")
    if status and status != 200:
        raise RuntimeError(f"API error {status}: {decoded.get('message', decoded)}")
    return decoded.get("data", decoded)


def list_wwise_versions(jwt: str):
    """Print all available Wwise versions."""
    data = api_get(jwt, "/products/versions/?category=wwise")
    bundles = data.get("bundles", [])
    print(f"{'ID':<35} {'Version':<25}")
    print("-" * 60)
    for b in sorted(bundles, key=lambda x: x.get("id", "")):
        print(f"{b['id']:<35} {b.get('versionName', '?'):<25}")
    return bundles


def version_to_bundle_id(version_str: str) -> str:
    """Convert '2023.1.7.8574' to 'wwise.2023_1_7_8574'."""
    parts = version_str.split(".")
    if len(parts) != 4:
        print(f"ERROR: Version must be YEAR.MAJOR.MINOR.BUILD (got '{version_str}')")
        sys.exit(1)
    return f"wwise.{'_'.join(parts)}"


def get_bundle_metadata(jwt: str, bundle_id: str) -> dict:
    """Fetch full bundle metadata including file list."""
    return api_get(jwt, f"/products/versions/{bundle_id}", version_prefix=4)


def get_file_download_url(jwt: str, bundle_id: str, file_id: str) -> str:
    """Get a signed CloudFront download URL for a bundle file."""
    data = api_get(jwt, f"/products/versions/{bundle_id}/file?filename={file_id}")
    url = data.get("url")
    if not url:
        raise RuntimeError(f"No download URL returned for {file_id}")
    return url


def sha1_file(path: Path) -> str:
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def download_file(jwt: str, bundle_id: str, file_info: dict, cache_dir: Path):
    """Download a single file if not already cached (with sha1 check)."""
    file_id = file_info["id"]
    dest = cache_dir / file_id
    expected_sha1 = file_info.get("sha1", "")
    size = file_info.get("size", 0)

    if dest.exists() and expected_sha1:
        actual = sha1_file(dest)
        if actual == expected_sha1:
            print(f"  [cached] {file_id} ({size:,} bytes)")
            return dest

    print(f"  [download] {file_id} ({size:,} bytes)")
    url = get_file_download_url(jwt, bundle_id, file_id)

    with httpx.stream("GET", url, timeout=120.0, follow_redirects=True) as r:
        r.raise_for_status()
        total = int(r.headers.get("Content-Length", 0)) or size
        downloaded = 0
        with open(dest, "wb") as f:
            for chunk in r.iter_bytes(chunk_size=65536):
                f.write(chunk)
                downloaded += len(chunk)
                if total:
                    pct = downloaded * 100 // total
                    bar = "#" * (pct // 2) + "-" * (50 - pct // 2)
                    print(f"\r    [{bar}] {pct}%", end="", flush=True)
    print()

    if expected_sha1:
        actual = sha1_file(dest)
        if actual != expected_sha1:
            print(f"  WARNING: SHA1 mismatch for {file_id}!")
            print(f"    expected: {expected_sha1}")
            print(f"    actual:   {actual}")

    return dest


def select_authoring_files(bundle_data: dict, with_sdk: bool = False) -> list:
    """Select the minimal set of files for Wwise Authoring on Windows x64."""
    files = bundle_data.get("files", [])
    selected = []
    for f in files:
        fid = f["id"]
        groups = {g.get("groupValueId", "") for g in f.get("groups", [])}
        # Core authoring files
        if fid == "Authoring.tar.xz":
            selected.append(f)
        elif fid == "Authoring.x64.tar.xz":
            selected.append(f)
        elif fid == "FilePackager.x64.tar.xz":
            selected.append(f)
        elif fid == "Authoring.MacExcludes.x64.tar.xz":
            selected.append(f)
        elif fid == "Authoring.Documentation.tar.xz":
            selected.append(f)
        # SDK files if requested
        elif with_sdk and fid == "SDK.tar.xz":
            selected.append(f)
        elif with_sdk and fid == "SDK.Windows_vc170.tar.xz":
            selected.append(f)
        elif with_sdk and fid == "SDK.FilePackager.tar.xz":
            selected.append(f)
    return selected


def extract_archives(cache_dir: Path, file_list: list, install_path: Path):
    """Extract tar.xz archives into the installation directory."""
    install_path.mkdir(parents=True, exist_ok=True)
    for f in file_list:
        archive = cache_dir / f["id"]
        if not archive.exists():
            print(f"  WARNING: {archive} not found, skipping")
            continue
        print(f"  Extracting {f['id']}...")
        result = subprocess.run(
            ["tar", "xf", str(archive), "--directory", str(install_path), "--skip-old-files"],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"    ERROR: tar failed: {result.stderr}")


def generate_launch_script(install_path: Path, version_str: str, prefix: Path):
    """Generate a shell script to launch Wwise Authoring under Wine."""
    script_path = install_path.parent / f"wwise_{version_str}.sh"
    script_content = f"""#!/bin/bash
# Launch Wwise {version_str} Authoring under Wine
# Generated by download_wwise.py

WINEPREFIX="{prefix}"
INSTALL_PATH="{install_path}"
COMMON_PATH_TO_BINARY="Authoring/x64/Release/bin"
EXEC_NAME="Wwise.exe"

export WINEPREFIX
export WWISEROOT="$(winepath -w "$INSTALL_PATH")"
export WWISESDK="${{WWISEROOT}}\\SDK"
export WINEDEBUG=-all

exec wine "${{INSTALL_PATH}}/${{COMMON_PATH_TO_BINARY}}/${{EXEC_NAME}}" "$@"
"""
    with open(script_path, "w") as f:
        f.write(script_content)
    os.chmod(script_path, 0o755)
    print(f"  Launch script: {script_path}")
    return script_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Download and install Wwise Authoring into a Wine prefix."
    )
    parser.add_argument(
        "--version", default="2023.1.7.8574",
        help="Wwise version (YEAR.MAJOR.MINOR.BUILD). Default: 2023.1.7.8574",
    )
    parser.add_argument(
        "--prefix", default=os.path.expanduser("~/.wine"),
        help="Wine prefix path. Default: ~/.wine",
    )
    parser.add_argument(
        "--cache-dir", default="./wwise_cache",
        help="Directory for caching downloaded archives. Default: ./wwise_cache",
    )
    parser.add_argument(
        "--with-sdk", action="store_true",
        help="Also download the Windows SDK (C++) files.",
    )
    parser.add_argument(
        "--list-versions", action="store_true",
        help="List all available Wwise versions and exit.",
    )
    parser.add_argument(
        "--download-only", action="store_true",
        help="Download archives but do not extract/install.",
    )
    args = parser.parse_args()

    print("Authenticating as guest...")
    jwt = get_guest_jwt()
    print("  OK")

    if args.list_versions:
        list_wwise_versions(jwt)
        return

    bundle_id = version_to_bundle_id(args.version)
    cache_dir = Path(args.cache_dir).resolve()
    cache_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nFetching bundle metadata for {args.version} ({bundle_id})...")
    bundle_data = get_bundle_metadata(jwt, bundle_id)

    file_list = select_authoring_files(bundle_data, with_sdk=args.with_sdk)
    total_size = sum(f.get("size", 0) for f in file_list)
    print(f"\nFiles to download ({len(file_list)} archives, {total_size:,} bytes total):")
    for f in file_list:
        print(f"  - {f['id']} ({f.get('size', 0):,} bytes)")

    print(f"\nDownloading to {cache_dir}...")
    for f in file_list:
        download_file(jwt, bundle_id, f, cache_dir)

    if args.download_only:
        print("\nDownload complete (--download-only). Archives saved to:")
        print(f"  {cache_dir}")
        return

    prefix = Path(args.prefix).resolve()
    install_base = prefix / "drive_c" / "Program Files (x86)" / "Audiokinetic"
    install_path = install_base / f"Wwise {args.version}"

    print(f"\nInstalling to {install_path}...")
    extract_archives(cache_dir, file_list, install_path)

    print("\nGenerating launch script...")
    script = generate_launch_script(install_path, args.version, prefix)

    print(f"\nDone! Wwise {args.version} installed to:")
    print(f"  {install_path}")
    print(f"\nTo launch: {script}")
    print(f"\nNote: You may need to install mfc140u.dll (64-bit) in your Wine prefix:")
    print(f"  winetricks vcrun2015")


if __name__ == "__main__":
    main()
