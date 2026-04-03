# Changelog

## v1.1.0 (unreleased)

### Changed
- Trimmed all voice lines to match in-game pacing — average words per line cut from ~8 to 4.2
- Reworked emotion tags across all 336 lines — "normal" reduced from 130 to 42 (only pings/numbers)
- Added more "excited" (43 → 86) and "shouting" (23 → 37) delivery for combat energy
- Fixed TACPAC pronunciation (spelled phonetically as "tack-pack")
- Fixed Bughole pronunciation and regenerated with better delivery

### Added
- 10 real Trump audio clips extracted from rally/speech footage for non-verbal lines
- 1.18x tempo speedup on AI-generated lines (no pitch change) for snappier delivery
- Loudness normalization to -20 LUFS across all clips
- Voice pack archive ID discovery for all 4 helldiver voices
- CSV exports of all 4 voice packs with WEM IDs and transcribed text (public gist)

### Fixed
- Wordy lines reduced from 158 to 7 (short originals that were bloated into sentences)
- Non-verbal lines (screams, grunts, laughter) no longer replaced with full sentences

## v1.0.0 (2026-04-02)

### Added
- Initial release — 336 AI-generated Trump voice lines
- Replaces all 785 Helldiver Voice 4 (Default Male 4) callouts
- Category-matched via Whisper transcription + fuzzy matching
- Compatible with Arsenal, HD2ModManager, h2mm-cli
- Full build pipeline: Fish Audio TTS → Wwise WEM → hd2-audio-modder patching
