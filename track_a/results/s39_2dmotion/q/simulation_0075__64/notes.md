# q64 – acceleration of the white car at 1.0 s (frame 24 at question_fps 24 = file fps)

The white car is the white van/minibus in the vertical road (scene `white_van`). It is also the prior's object (length 6 m).
It drives straight up from rest with constant acceleration.

## Scale (2D, one m/px from the prior)
- `length.py`: half-level edge crossings of the brightness profile along the van axis. At rest (f0/f1) the length is 234.3–234.8 px.
  At f24 and f50 the value is slightly shorter (motion blur softens the edges). The scene record gives 236 for the body at threshold 25.
  I use L = 235.5 px, so the scale is 6/235.5 = 0.02548 m/px.
- SAM 3 (`white van`, f24): box/length 243 px, width 90. This is 3.2% longer than my measurement. On the zoomed frame (frames/zoom24.png) the
  white body spans about y 722–958 (≈236 px). The profiles show a dark shadow band just ahead of and behind the body, which the SAM mask
  includes. My edge measurement is the right one. The SAM centroid (831.5, 839.7) agrees with my centre (≈831, 840.9) to about 1 px.

## Acceleration
- `measure.py`: own tracking of the bright body (bbox) in all 72 frames, followed by a quadratic fit of position against frame:
  - centre y: 0.2806 (f2–71), 0.2813 (f10–40), 0.2806 (f14–34) px/frame²; residual rms is 0.26–0.58 px
  - top edge: 0.2826 / 0.2808 / 0.2766; bottom edge: 0.2785 / 0.2817 / 0.2846
  - The acceleration is constant within the noise, so the speed-change convention at f24 equals the constant.
- Second route (`check_scene.py`): the scene record's ref_y fit gives 0.276–0.277 px/f², and the slope of its per-frame speeds is 0.2777.
  That mask includes shadow, and its length drifts from 247 to 241 px, which biases the result slightly low.
- Adopted value: 0.280 px/frame² = 0.280 × 24² = 161.3 px/s².
- a = 161.3 × 0.02548 = **4.11 m/s²**. With the scene record's 0.277, the result would be 4.07. With L = 234.5 px, it would be 4.13.

Confidence: good (about ±3%). The main uncertainty is the pixel length of the van (234–236 px).
