# q_1695: average speed of the eagle (m/s)

Prior: eagle length = 0.8 m. depth_info: 100.14 m at t=1 s, 99.52 m at t=2 s, so the depth is nearly constant and the
bird flies almost parallel to the image plane. Radial motion is about 0.6 m/s, which adds less than 0.01 m/s to a
lateral speed of about 13 m/s.
File rate 25 fps, question_fps 24. Per-frame displacements are converted with 24 fps. The bird is visible in file
frames 0–47 and is removed by the segmentation from frame 48 on.

## Scale
Because the depth is constant, the metres-per-pixel scale is 0.8 m / (eagle length in px), and no separate focal
length is needed: f ≈ 24.5 × 100 / 0.8 ≈ 3060 px, a horizontal FOV of about 18°.
The eagle is seen side-on, flying left to right. Its beak-to-tail horizontal extent over the white background
(frames 0–20, `measure.py`):
- half-max threshold: 21–28 px, median about 23.
- 25 % threshold: 22–30 px, median about 25.
- The clearest side-on frames (6 and 18, wings edge-on) give 24–26 px.

Adopted value: 24.5 px, giving 0.03265 m/px.

## Pixel speed
Track from scene/tracks/bird.csv (ref_x, ref_y; checked on crops), frames 0–47:
- raw mean per-frame displacement: 16.94 px/frame.
- net displacement / frames: 16.78 px/frame.
- polynomial fits of degree 2–5: 16.74–16.96 px/frame.
- 12-frame (one wingbeat) moving average: 16.85 px/frame.

Adopted value: 16.85 px/frame.

## Answer
16.85 × 0.03265 × 24 = **13.2 m/s**.

## Second-route check
The smoothed, raw and net pixel speeds agree to within 1 %. Most of the uncertainty is in the pixel length of the
eagle (23–26 px), which gives a range of 12.4–14.1 m/s. If the 0.8 m "length" meant some other extent, such as the
wings in a particular pose, the answer would shift by the same ratio.

Confidence: moderate (±7 %).
