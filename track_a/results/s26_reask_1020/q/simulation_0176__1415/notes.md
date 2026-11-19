# q_1415 — length of the airplane (simulation_0176)

The file and the question are both 24 fps, so frame = round(t*24). The depth at t=0.5 s is frame 12 and at t=1.0 s is frame 24.

## Method
- `measure.py`: subtracts the per-pixel median sky from each frame and builds the plane's mask at thresholds 10, 18 and 30. For frames 5–32
  it records the leftmost point (the nose; threshold 10 also catches the translucent nose glazing), the rightmost point (the tail /
  stabiliser tip) and the nose y. Results are in extents.json.
- `solve.py`: the nose positions are back-projected with the given nose distances (284.98 m at frame 12, 305.627 m at frame 24), using a principal point
  of (960, 540). The focal length is solved so that the 3D nose displacement over 12 frames equals 153.582/24 × 12 = 76.79 m.
  This gives **f = 2695 px** (horizontal FOV 39°). The motion direction is (−0.983, 0, 0.185), so the plane flies level, leftward, and recedes slightly.
- Length: the tail point is N − L·dir, along the flight path, and L is solved so that it projects onto the measured tail x. Results: frame 12 gives 47.8 m,
  frame 24 gives 49.2 m, frames 9–30 give 47.7–50.1 m, median 48.5 m. The naive depth × width / f gives 49.4 m at both frames.

## Checks
- Holding f fixed, the straight constant-velocity path through the two depth anchors reproduces the nose x track over frames 7–30 to within 1 px RMS. f between 2500 and 2700
  fits about equally well, so the track supports f but cannot pin it down.
- The apparent width ratio between frames 12 and 24 is 468/436 = 1.073, which matches the depth ratio 305.6/285.0 = 1.072.
- Second route, which needs no f: L ≈ pixel length / pixel speed × 6.399 m/frame. Over frames 10–28 this gives 47.5–50.6 m (about 48–49 m).
- If the depth were to a mid-fuselage origin instead of the nose, f would be 2760 and L about 47 m.
- Realism: 48 m is long for this T-tail business/regional jet (real ones are about 30–36 m). However, the prior speed is the only scale, and
  there is no standard object in the scene to contradict it. The rock stack comes out about 55 m tall at 296 m, which is plausible. So I keep the prior's scale.

## Answer
48.5 m. Confidence is moderate: the methods agree to about ±3%, and the main uncertainty is where the nose and tail edges fall.
