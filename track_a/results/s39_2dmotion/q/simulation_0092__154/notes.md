# Q154 — speed of the car at 1.0 s (m/s)

Prior: car length = 5.67 m. 2D video; file fps = question fps = 24, so t = 1.0 s → frame 24.

## Method
- `measure_car.py`: background (RGB 78,79,86) difference > 12 below row 590, 3x3 opening → per-frame car bbox,
  saved to `car_track.csv`. Camera is static and the car moves horizontally at constant speed.
- Pixel speed: the linear fit of bbox centre over frames 3-65 gives 28.458 px/frame (x0 28.449, x1 28.468,
  mask centroid 28.476). The backward step at frame 24 is 28.5 px. The scene record says 28.45, which agrees.
- Scale: car length in pixels (bbox, inclusive) is 129-130 px near the image centre (frames 30-40) and 131 px at frame 24.
  It grows to 137-138 px near the image edges because the end faces show at off-axis positions. I used 130 px, the
  side-on length near the centre → 5.67/130 = 0.04362 m/px.
- Speed = 28.458 × 24 × 0.04362 = **29.79 m/s**.

## SAM 3 check
- SAM 3 "car" segment, frame 24: box 1185.3–1318.1 (132.8 px), centroid x 1252.8. My mask: 1186–1316 (131 px),
  centre 1251. That is a 1.4 pct difference.
- Frame 33: SAM 130.4 px vs mine 129 px (1.1 pct). Frame 23→24 centroid step: SAM 28.8 px vs mine 28.5 px.
- All differences are under 3 pct. The overlay shows the mask fits the car tightly, so no further check was needed.

## Second route / sensitivity
- If I use the frame-24 length (131 px) instead, the speed is 29.56 m/s. With SAM's 133 px it is 29.12, and with
  the minimum of 129 px it is 30.02. The spread is about ±1.5 pct around the answer.
- The frame-24 backward step (28.5 px) instead of the fit gives 29.83 m/s.

Confidence: high (about ±2 pct).
