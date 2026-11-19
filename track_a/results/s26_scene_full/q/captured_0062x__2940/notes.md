# q_2940 – width of the whiteboard (cm)

File fps = question_fps = 24. t = 1.4 s -> frame 34. Lab camera: f = 0.5959 x 1280 = 762.8 px, pp (640, 360).

## Method (measure.py, size_speed.py)
- The board is a mask (white, low saturation). Robust lines are fitted to the central 70 % of each of its 4 sides (so the
  rounded corners and knobs are left out), and the corners are where those lines cross (overlay frames/ov34.png).
- The board is a flat rectangle lying on the floor, seen at an oblique angle. Its two vanishing points with f = 763 give
  edge directions that are orthogonal to within 0.1-2 deg in every frame 20-48 (this checks f). The plane normal is
  stable (spread < 3 deg), median n = (-0.127, 0.787, 0.604).
- The plane goes through the board centre (the diagonal intersection), back-projected at the given depth of 2.815 m (frame 34).
  The corner rays are intersected with that plane to get the side lengths in 3D.

## Results
- Frame 34, using its own normal: 81.9 x 63.3 cm. Using the median floor normal: 81.9 x 61.3 cm.
- Every frame 20-48 on the same floor plane: short side 61.1-62.2 cm (median 61.6), long side about 82 cm (consistent).
- A naive reading (min-rect width 123.4 px x 2.815 / f = 45.5 cm) ignores foreshortening, because the short side runs
  away from the camera, so it was rejected.
- Sanity check: about 82 x 61 cm is close to a standard 80 x 60 cm whiteboard.

## Second-route check (the prior)
The centre is tracked on the floor plane. Its backward-difference speed at frame 34 is 1.52 m/s. A 5-frame forward-difference
average over frames 33-37 is 1.86 m/s, because it takes in the dropped frame at 35->36 (a double step of 3.19 m/s). The
prior of 1.934 m/s is matched to within about 4 % when the reference's smoothing window includes the dropped frame. So the
metric scale is consistent and no rescaling is needed.

## Reading of "width"
Width = the shorter horizontal extent, since the board lies flat: about 61.5 cm (answer). The other reading (the long
side, i.e. the width of a hanging whiteboard) would be about 82 cm.
Confidence: good, ±3 % on the short side.
