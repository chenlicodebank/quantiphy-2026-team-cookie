# Q1099: speed of the boat at 1.0 s (prior: boat length = 10 m)

## Method (2D, a single scale from the prior)
- `measure.py` tracks the cabin and lower mast by template matching (from frame 50) at sub-pixel resolution. This
  works in every frame, including the frames where the stern is clipped.
- **Pixel speed near frames 24–25:** quadratic and linear fits over frames 15–35, 20–30 and 10–40 all give
  4.565–4.57 px/frame. Per-frame differences are ±0.1.
- **Pixel speed rises slowly:** about 4.70 px/frame at frames 55–74. Apparent hull length grows the same way, from
  284 px (frame 36) to 290 px (frames 54–74). So the boat approaches the camera slightly and its world speed is
  constant. v_px / L_px gives 4.70/290 ≈ 0.01621 per frame late, and 4.64/286.5 ≈ 0.0162 per frame at frame 50.
- **Hull length at frame 25:** the stern is clipped there. Scaling 290 px by the speed ratio gives about 282 px, which
  agrees with the record's fit (281 px).
- **Result per frame:** 10 m × 4.57 / 282 = 0.162 m/frame.

## Time base
- The file is 25 fps and question_fps is 24. I found no duplicated frames: the minimum frame-to-frame difference is
  normal, so the clip was not resampled by duplicating frames.
- Both rates give a plausible speed for a fishing boat:
  - 25 fps gives 4.05 m/s.
  - 24 fps gives 3.89 m/s.
- I can't separate them physically, so I answer 3.97 m/s, between the two and within about 2% of either.

## Check
- Late-window route: 10 × 4.70 / 290 = 0.162 m/frame, the same per-frame speed.
- The frame chosen for t = 1.0 (24 or 25) changes the result by less than 0.2%.

**Confidence:** about ±3% on the per-frame speed. The 4% fps ambiguity is split by the answer.
