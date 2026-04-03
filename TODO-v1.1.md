# v1.1.0 TODO

## Trim wordy lines

158 lines where the original is 1-3 words but the Trump version is 5+ words.
These need to be shortened to match the quick bark/callout pacing of the originals.

### Priority 1: Non-verbal / screams (replace with real clips or very short AI)
- [ ] 61: `*Maniacal laughter*` → currently a full sentence, needs actual laugh
- [ ] 142: `Ouch!` → "Ow! That hurt! Very unfair!" should just be "Ow!"
- [ ] 143: `AHHH!` → "AHHH! They got me! Can you believe it?!" should just be a scream

### Priority 2: 1-word originals bloated to sentences
- [ ] 66: `Contact!` (1w → 5w)
- [ ] 76: `Heavy!` (1w → 5w)
- [ ] 78: `Dropships!` (1w → 7w)
- [ ] 83: `Bughole!` (1w → 14w)
- [ ] 84: `Squids!` (1w → 5w)
- [ ] 85: `Illuminate!` (1w → 8w)
- [ ] 113: `Reinforcing!` (1w → 7w)
- [ ] 131: `Hellbomb.` (1w → 6w)
- [ ] 253: `Danger!` (1w → 5w)
- [ ] 273: `Move!` (1w → 6w)
- [ ] 280: `RUN!!!` (1w → 8w)
- [ ] 285: `Negative.` (1w → 6w)
- [ ] 288: `Nevermind.` (1w → 5w)
- [ ] 331: `Tie!` (1w → 7w)

### Priority 3: 2-word originals bloated to 8+ words
- [ ] 22: `I'm out!` (2w → 12w)
- [ ] 39: `Reloading you!` (2w → 12w)
- [ ] 19: `Last reload!` (2w → 10w)
- [ ] 67: `Enemy spotted!` (2w → 9w)
- [ ] 75: `Enemy elite!` (2w → 11w)
- [ ] 77: `Aerial enemy!` (2w → 9w)
- [ ] 89: `Bot fabricator!` (2w → 9w)
- [ ] 97: `Requesting orbital!` (2w → 8w)
- [ ] 116: `Requesting sentry!` (2w → 8w)
- [ ] 120: `Requesting vehicle!` (2w → 7w)
- [ ] 122: `Requesting walker!` (2w → 8w)
- [ ] 145: `MY ARM!` (2w → 8w)
- [ ] 152: `MY LEG!` (2w → 9w)
- [ ] 163: `Feels gooooood.` (2w → 11w)
- [ ] 180: `Administering meds!` (2w → 10w)
- [ ] 220: `Tagging map.` (2w → 10w)
- [ ] 278: `Hold position.` (2w → 8w)
- [ ] 281: `Steering clear!` (2w → 10w)
- [ ] 292: `I'm sorry.` (2w → 12w)
- [ ] 298: `Entering shuttle.` (2w → 9w)
- [ ] 308: `Visibility decreasing.` (2w → 8w)
- [ ] 328: `Let's play!` (2w → 10w)
- [ ] 329: `I win!` (2w → 9w)

### Priority 4: Remaining 3-word originals (trim where possible)
Full list of 3-word originals with 7+ Trump words — trim to ~5 words max where it makes sense.

## Fix monotone delivery

130 of 336 lines (39%) use "normal" emotion which sends NO direction to the TTS.
Another 51 use "confident" which is too calm.

### Changes needed:
- [ ] Rework EMOTION_MAP in generate.py with stronger prefixes:
  - `normal` → `"(in a natural speaking voice) "` or `"(conversationally) "`
  - `confident` → `"(boldly and confidently) "`
  - `excited` → `"(excitedly, with high energy) "`
  - `urgent` → `"(urgently, with intensity) "`
  - `angry` → `"(angrily, with real frustration) "`
  - `shouting` → `"(shouting loudly) "`
- [ ] Add new emotions: `bragging`, `rallying`, `mocking`
- [ ] Re-audit emotion assignments — combat lines should mostly be `excited`/`shouting`, not `normal`
- [ ] Categories that need emotion bumps:
  - `samples` (12 lines, mostly `normal`) → `confident` or `bragging`
  - `pickup` (16 lines, mostly `normal`/`confident`) → more variety
  - `marking` (9 lines, all `normal`) → needs some energy
  - `ping` directions (18 lines, all `normal`) → fine as-is, these should be flat
  - `terminal` (5 lines, mostly `normal`) → `confident`
  - `weather` (4 lines, all `normal`) → fine as-is
- [ ] Regenerate all affected lines after emotion rework

## Loudness normalization (mastering)

AI clips are ~-18 to -24 LUFS, real clips are ~-14 to -22 LUFS. Need to normalize all clips
to a consistent loudness before WEM conversion so nothing is louder/quieter than anything else.

- [ ] Add a normalization step to the pipeline (ffmpeg `loudnorm` filter, target -20 LUFS)
- [ ] Apply to both AI-generated WAVs and real source clips
- [ ] Run after all WAVs are finalized, before `convert_to_wem.sh`

## Real Trump clips (from YouTube sources)

10 clips extracted and trimmed, ready to replace AI versions for short/non-verbal lines:

- [ ] 01_youre_fired → grenade [40]
- [ ] 03_laughing → maniacal laughter [61]
- [ ] 04_this_is_great → various excited
- [ ] 05_here_we_go_again → deployment
- [ ] 07_get_out_joe → enemy callout
- [ ] 08_looks_like_hell → enemy outpost / combat
- [ ] 10_its_on_fire → combat fire lines
- [ ] 11_ready → deployment
- [ ] 13_god_bless → extraction / victory
- [ ] 14_yeah → response [283] yes/affirmative

## Speed up AI-generated lines

AI TTS is too slow/drawn out compared to in-game pacing. Apply 1.18x tempo (no pitch change)
to all AI-generated WAVs using ffmpeg `atempo=1.18`. Do NOT apply to real Trump clips.

- [ ] Add atempo=1.18 step to pipeline (after generation, before WEM conversion)
- [ ] Skip real clips (candidate_clips/) — only apply to AI output
- [ ] Skip short pings/numbers/directions if they already sound fine at 1x

## Other v1.1 changes
- [ ] (add your other changes here)
