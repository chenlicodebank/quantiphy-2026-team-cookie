# q_532 – length of the typewriter (m)

Prior: magnifying glass acceleration before 0.5 s = 9.8 m/s^2 (free fall, frames 0-10; impact at frame 11 = 0.458 s).
question_fps = file fps = 24.

## Scale (track.py, fit.py)
- Re-tracked the glass myself (difference to frame 29, largest blob, frames 0-10). Bbox-centre y matches the scene
  record (200.5 ... 857.5). Quadratic fits from frame 0/1/2/3: 7435 / 7412 / 7425 / 7437 px/s^2; the record's
  ref_y gives 7444 / 7421. Taking a = 7430 px/s^2 gives scale = 9.8 / 7430 = 1.319e-3 m/px.
- Sanity check: the glass is 164 px long in the air, so 0.216 m. That's plausible for a magnifying glass.

## Typewriter (tw_extent.py, frames/tw_lines.png, frame 29)
- Longer horizontal extent = left to right across the keyboard. Base flange runs from x ~509 to ~825 px (316 px). The
  left platen knob ends at ~517 px and the upper body at ~797 px. So the horizontal extent is about 305-316 px.
- 310-316 px x 1.319e-3 = 0.41-0.42 m. The typewriter's front edge (y~1040) is slightly closer to the camera than the
  glass's landing plane (ring bottom y~1018), so its pixels are a little magnified. Taking that into account, the answer is 0.41 m.
- Plausibility: a portable typewriter is about 0.30-0.45 m wide, so this is consistent.

Confidence: moderate-high (scale is good to ~1%; pixel extent and depth difference to ~4%).
