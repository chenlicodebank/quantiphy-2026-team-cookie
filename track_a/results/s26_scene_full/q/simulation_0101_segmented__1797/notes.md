# q_1797: average speed of the boat (m/s)

Prior: shark acceleration = 1 m/s^2. This is a 2D clip at 24 fps (file fps = question_fps), so one m/px scale applies to the whole frame.

## Measurements (measure.py → meas.json, fit.py)
- Segmentation: any pixel more than 12 levels from white. The boat is the part above y = 740 and the shark the part below.
- Shark x positions over frames 1–72 fit a quadratic well:
  - mask centroid: a = -86.0 px/s^2 (rms 0.5 px)
  - darkness-weighted centroid: -86.2 px/s^2
  - snout: -87.3 px/s^2
  - tail tip: -85.5 px/s^2
  - first half alone: -84.5 px/s^2; second half alone: -83.1 px/s^2
  - The cubic term is negligible, so the acceleration is constant.
  - Adopted value: 86 px/s^2, giving a scale of 1/86 m/px.
- Boat moves at constant velocity:
  - bow (leftmost pixel): -428.9 px/s from a linear fit (rms 1 px); hull-band bow: -429.0 px/s; stern edge after frame 27: -430.9 px/s. A quadratic fit gives about 0 acceleration.
  - Mean of the per-frame speeds: 17.92 px/frame over frames 2–72, or 17.67 px/frame if the stationary first step (frames 0 to 1 are identical) is included.

## Result
- v = 429 px/s / 86 px/s^2 × 1 m/s^2 = 4.99 m/s, which is about 5.0 m/s.
- Second route: the mean of per-frame bow speeds (17.92 × 24 / 86) gives 5.00 m/s. Including the zero first step gives 4.93 m/s.
- Confidence: high, within about 3%.
