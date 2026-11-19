# Q426 – height of the big elephant (m)

2D side-view render, static camera, 24 fps (file fps = question_fps). Both elephants walk on the same ground line, so one
m/px scale applies.

## Scale from the prior (speed of big elephant = 2.313 m/s)
Pixel speed of the big elephant (horizontal walk, nearly constant):
- scene record: linear fit of mask centroid_x 6.88 px/frame; body-centroid fit 6.85; body edges 6.91–7.02; mean per-frame step 6.99.
- my check (speed_check.py): template match of the torso (frames 5–50) gives 7.12 px/frame.
Adopted 7.0 px/frame = 168 px/s → scale = 2.313 / 168 = 0.01377 m/px.

## Height
Mask height (top of head/back to feet) median 230 px (range 221–236) from scene tracks; I checked it on a zoomed frame 24
(top ≈ y 463, feet ≈ 691–693 → ≈ 228–230 px).

Height = 230 × 0.01377 = 3.17 m (range 3.12–3.22 m across the speed estimates 7.12–6.88 px/frame).
That is a plausible height for a large African elephant.

Confidence: moderate-high. The main uncertainty is which pixel speed matches the reference's "speed" (±2 %), plus ±2 % on the pixel height.
