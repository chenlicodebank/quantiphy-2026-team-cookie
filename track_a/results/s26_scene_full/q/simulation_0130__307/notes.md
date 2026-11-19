# Q307: speed of the white airplane at 1.0 s

Prior: the car's speed is 11.155 m/s. The "car" is the small tug that tows the airliner through a rigid towbar. This is a 2D top-down scene with a static camera, at 24 fps (the file rate and question_fps agree).

## Measurements
- **Scene record.** Per-frame displacements from scene/tracks:
  - plane: 5.244, 5.245 and 5.250 px/frame (means over frames 1-24, 24-48 and 48-71);
  - tug: 5.240, 5.250 and 5.249 px/frame.

  Both move at a constant speed with no trend, and the towbar gap stays constant. Frames 0 and 1 are identical, so motion starts after frame 1.
- **My own check (check.py).** I made a template-match from frame 24 to frames 12 and 36:
  - plane: 5.250 and 5.244 px/frame;
  - tug: 5.236 and 5.254 px/frame;
  - x drift: 0.

## Answer
The plane is rigidly towed, and its pixel speed equals the tug's to within 0.1 %. So the plane's speed at frame 24 (t = 1.0 s) equals the car's speed: **11.155 m/s**. As a scale check, 11.155 / (5.247 × 24) ≈ 0.0886 m/px, which makes the plane about 37 m long and gives it a wingspan of about 34 m. Both are plausible for an airliner.

Confidence: high.
