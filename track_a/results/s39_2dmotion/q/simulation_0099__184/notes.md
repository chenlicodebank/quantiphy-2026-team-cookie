# q184 — speed of the shark at 1.0 s (m/s); prior: boat length = 10 m

File fps = question_fps = 24, so t = 1.0 s is frame 24. The video is 2D with a static camera.

## Scale (boat)
- `measure.py`: frame 0 minus frame 72 (by frame 72 the boat has left x<1400), threshold 18, opening, rows 150–600
  (above the reflection band). Boat horizontal extent at frame 0 is x 228–1087, so **860 px** (stern to bow tip).
  This matches the scene record (860).
- SAM 3 "boat" check: frame 0 box 231.0–1086.8 (859 px); frame 10 box 394.5–1249.3 (855 px; my mask gives 389–1249).
  The difference is under 0.6 %, because SAM trims the outermost stern pixel. I used 860 px.
- Scale = 10 / 860 = 0.011628 m/px.

## Shark motion
- The shark is still in frames 0–1, then moves left at a constant speed in a straight line, with y fixed at ≈904.
- In the scene record, ref_x goes from 799.72 at frame 2 to 562.72 at frame 24. That is 237.0 px over 22 frames, or
  **10.77 px/frame**, which matches the record's fitted −10.76 px/frame.
- The local one-frame difference at frame 24 is 10.84 px in the record and 10.90 px from my phase correlation of the
  body (frames 20–27 average 10.85). These per-frame values carry about ±0.1 px of noise from tail motion.
- SAM 3 "shark" masks on frames 23 and 24 give box centres 571.85 and 562.6. The frame-24 centre matches the record's
  ref_x of 562.72 to within 0.1 px. SAM's one-frame box difference (9.3 px) is noisier because the nose and tail edges
  change between masks, so I did not rely on it.
- The motion is uniform, so I used the robust constant 10.77 px/frame.

## Answer
v = 10.77 px/frame × 24 fps × 0.011628 m/px = **3.01 m/s**.

The local per-frame values (10.84–10.90 px) would give 3.03–3.04 m/s, less than 1 % away.

Confidence: high. The main assumption is that the boat and the shark are in the same plane (one scale), as the
benchmark convention requires.
