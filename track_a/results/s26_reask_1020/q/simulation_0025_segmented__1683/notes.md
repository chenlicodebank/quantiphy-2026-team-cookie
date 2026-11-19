# q_1683 — average speed of the eagle (m/s)

File is 25 fps (75 frames); question_fps = 24 is used for all timing (t=1 s -> frame 24, t=2 s -> frame 48,
per-frame speed x 24).

## Focal length: from the person's height, not the 1.3 m/s prior
- The person's distance barely changes (114.8319 -> 114.8356 m), so the origin stays still while the body walks.
- In the image the body moves only 0.535 px per frame (x -0.52 and y +0.13 px/frame, 12.8 px/s at 24 fps).
  If that motion were all sideways at 1.3 m/s, then f would be about 1130 px. That makes the person 5.5 m tall,
  which is impossible. So the person mostly walks toward the camera (narrow frontal/three-quarter view, feet move
  down the image). The toward-camera part should show as a 3 % size change, which is too small to measure here:
  mask height and area give contradictory trends.
- Instead, the scale comes from the person, who is the standard object. Measured height from feet to the top of
  the head (`head.py`, `human.py`; the white head is faint) is about 55.5 px (53–57 px) at 114.83 m. For a
  1.75 m adult, f = 55.5 x 114.83 / 1.75 ≈ 3640 px (about 3450–3860 px for heights of 1.65–1.85 m).
- Check: at f = 3640 the person moves sideways at 0.41 m/s, so about 1.24 m/s is toward the camera. That fits
  the 1.3 m/s prior and the feet moving down the image (camera about 9 m high).

## Eagle (`bird.py`)
- The track is the mask centroid from scene/tracks/bird.csv, using frames 0–62. Frames 63–66 are cut by the
  image edge and were left out. I checked this track against the sheet frames.
- Model: a constant 3D velocity, projected through a pinhole camera (principal point 480,480). It is fitted to
  the pixel track and to the given distances (116.0475 m at frame 24, 108.2756 m at frame 48).
- The x residuals have an rms of 2.4 px and show no trend, so the constant-velocity fit is good. The vertical
  residuals (±9 px) come from the wing flaps.
- Size check: the largest wingspan in each flap cycle grows 46 -> 48 -> 55 px, which matches the bird getting
  closer (124 -> 104 m).
- Result: V = (8.09, 0.08, -8.04) m/s, speed **11.41 m/s** at f = 3640.
- Second route: back-project the smoothed centroids at frames 24 and 48 using the given distances. This gives
  11.40 m/s.
- Sensitivity to f: 3300 px gives 12.05 m/s and 4000 px gives 10.87 m/s.
- Plausibility: the projected wingspan is about 1.55 m. The bird flies at about 45° to the image plane, so the
  wings are foreshortened, and the real span is about 2.2 m, a realistic eagle.

Answer: 11.4 m/s. Confidence moderate (±5–7 %, mainly from the assumed person height and so the focal length).
