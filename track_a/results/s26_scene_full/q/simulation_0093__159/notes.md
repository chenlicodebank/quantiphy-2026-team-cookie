# Q159: speed of the car at 1.0 s (frame 24 at 24 fps)

- 2D side view with a static camera. The car (white pickup) moves +x at constant speed. fps = question_fps = 24.
- Script: `measure_car.py`. It segments the car per frame by |RGB - bg| at three thresholds and also computes the mask centroid.
- Car pixel length: 91–92 px where the car crosses the image centre (frames 2–6, x ≈ 960). It grows to ~96 px at frame 24
  and ~98 px at frame 37 because the end face comes into view off-centre (perspective). The true side length is
  taken from the centre crossing: 91.75 px. Scale = 5.67 / 91.75 = 0.0618 m/px.
- Pixel speed: centroid step 20.29 px at frame 24 (one-frame backward difference). The mean over frames 2–37 is 20.15 px/frame,
  and the steps are constant to within ±0.3 px.
- Speed: 20.15 × 24 × 0.0618 = 29.9 m/s (mean). From the frame-24 step alone: 30.1. From the centred 23–25 difference: 29.96.
- Second-route check: using the bbox-centre track from scene/ (mean 20.13 px/frame) gives the same result.
  If the length were taken at frame 24 (96 px), the result would be 28.6 m/s (−4%). I rejected that because the extra length is the end face.
- Answer: 30.0 m/s. Confidence: high (within ~3%).
