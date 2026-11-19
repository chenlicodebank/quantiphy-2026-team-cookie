# Q91 — distance yellow car ↔ black-and-white car at t = 1.0 s

fps 24 (file and question agree) → frame 24. 2D top-down render; prior: yellow car length = 5.67 m.

## Measurements (measure.py, own segmentation, same mask idea as scene/)
- Frame 24 body boxes: yellow x 1172–1481 (centre 1326.5, y centre 401.5), white x 1069–1375 (centre 1222.0, y 539.5).
  This matches scene/tracks (yellow cx 1326.5, white 1222.5).
- dx: 104.5 px from box centres; 105.9 from cx_xcorr; 104.2 from velocity × 23 moving frames (cars level at frame 0,
  4.53 px/frame relative speed). dy = 138 px (constant). Pixel distance ≈ 173.1–173.9 px.
- Scale: the yellow car's pixel length is 304 px near the image centre (frame 55) and 310 px at frame 24. Off-axis
  perspective makes it longer there, because the vertical end faces show. So the centre value 304 px is the true
  top-view length → 5.67/304 = 0.01865 m/px.

## Result
173.2 px × 0.01865 = **3.23 m**. Range across choices: 3.16 (L = 310) to 3.24 (dx from xcorr).
The second route uses the dx from relative velocity instead of the box centres: 3.225 m. The routes agree.
Confidence: good (within ~2–3%). The main uncertainty is the perspective scale (304 vs 310 px).
