# q_1862 – speed of the astronaut at t = 2 s

File fps = question_fps = 24, so t = 2 s -> frame 48. 2D video, single object (astronaut) on a white background, rising up the image.

## Scale (prior: height of astronaut = 2.2 m)
- Own mask (min RGB < 225, largest blob; `measure.py`): at rest, frames 0-2, the figure stands upright (axis ~94°). Its vertical bbox extent is 90, 91, 90 px (mean 90.3 px). Main-axis length is 90.9 px at f0.
- SAM 3 segment of "astronaut" at f0: vert_px 90, length_px 91.0. This agrees with my measurement to within 1 %.
- Scale = 2.2 / 90.3 = 0.02436 m/px.

## Motion at frame 48 (`speed.py`)
- Own centroid, raw per-frame |p(i)-p(i-1)| for i = 45..52: 4.87, 5.25, 5.14, 4.66, 5.00, 4.71, 5.11, 4.59 px. The jitter of about ±0.3 px comes from mask noise.
- Local quadratic fits of x(t), y(t) around f48, evaluated as the backward difference 47->48: 4.958 (±3 frames), 4.934 (±5 frames), 4.943 (±7 frames) px/frame.
- Second route, bbox centre: 4.997, 4.916, 4.919 px/frame. Mean of raw speeds over f46-50: 4.95 (centroid) and 5.03 (bbox).
- SAM 3 track (`tracks/astronaut_0.csv`): from f43 to f53 the centre moves from (1305.0, 360.8) to (1308.0, 312.0), i.e. 4.89 px/frame. My centroid gives 4.90 px/frame over the same span.
- SAM segment at f47/f48: centroids (1306.4, 339.0) and (1306.3, 335.3), a raw step of 3.7 px. My raw step is 4.65 px. The two raw single-frame steps differ by more than 3 %. Smoothed, both sources give about 4.9-4.95 px/frame, so the gap is per-frame mask jitter (about ±0.5 px on each mask's centroid), not a real difference. I use the smoothed value.
- At f48 the motion is near its peak (speed ~5 px/frame from f30 to f50), so the derivative is not sensitive to the choice of window.

## Answer
v = 4.94 px/frame × 24 fps × 0.02436 m/px = **2.89 m/s**. Using 90 px or 91 px for the height gives 2.87-2.90 m/s.

Confidence: good (about ±3 %). The scene/ record was checked and agrees with these measurements.
