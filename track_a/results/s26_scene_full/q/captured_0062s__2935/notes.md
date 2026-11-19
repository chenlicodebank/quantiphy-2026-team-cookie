# q_2935 – length of the white box (cm)

The object is the small white drink carton (the `carton` in scene/) at about (517, 495) px. It stays still for the whole clip.
Its depth from depth_info is 2.082 m at t = 1.4 s (frame 34). The file fps and question_fps are both 24. Camera: f = 0.5959·1280 = 763 px, principal point (640, 360).
The prior (the board's velocity) is not needed for a static object's size.

## Measurement
- `box_corners.py`: averages the carton crop over all 49 frames, segments it against the green background,
  and finds the outline polygon and the red end face. The overlay is `frames/box_poly.png`.
- The carton lies on its side. Its long axis points up-right in the image, away from the camera. Visible are the white top face, the red-brown near end face and a thin right side face.
- Corners (px):
  - top face: far edge (521.7,463.7)–(541.6,469.8), near edge (492.0,507.5)–(511.5,513.6)
  - bottom of the red face: (491.9,519.1)–(513.3,525.2)
  - so the long edges are ≈53 px, the width edges ≈20.8 px and the end face is ≈11.5 px tall
- The long axis is strongly foreshortened, because it points largely along the line of sight on a floor seen at about 40°. So the
  plain "depth × px / f" rule is wrong here: it gives 14.4 cm from the 53 px edge, or 19.0 cm from the 69.5 px silhouette diagonal.

## Main route: perspective cuboid fit (`cuboid_fit.py`)
The model is a cuboid whose centre is at 2.082 m. The unknowns are the camera pitch and roll, the box's yaw, L, W and H.
It is fitted to the 6 corners:
- roll free: pitch 35.2°, roll 3.0°, **L = 17.44 cm**, W 5.86, H 4.26, rms 0.34 px
- roll = 0: pitch 36.2°, **L = 16.98 cm**, W 5.98, H 4.30, rms 0.44 px
- Monte Carlo with ±0.7 px corner noise (`cuboid_mc.py`): L median 17.3 cm (16.7–18.2) with roll free, 17.0 cm (16.5–17.5) with roll 0.

## Second route: floor plane from depth_info (`geom.py`)
- I back-projected the centres of the board, bag, teddy bear and box using their given distances and fitted a plane. Its normal
  implies a camera pitch of about 36.3°, which matches the cuboid fit on its own. The board's centre sits 11 cm off the plane, so this plane fit is loose.
- Intersecting the top-face corner rays with a plane parallel to the floor at the box-top height gives L = 16.2–17.6 cm.
- Holding the cuboid fit at pitch 36.3° gives L = 16.96 cm. A pitch of 32–40° gives 18.0–16.3 cm.
- The bin's rim ellipse also points to a steep downward view, consistent with this.

## Answer
L ≈ 17.1 cm, with the carton's cross-section about 6.0 × 4.3 cm. That is plausible for a slim drink carton (~0.45 L).
Confidence is moderate: about ±5%, set mainly by the pitch uncertainty and sub-pixel corner placement.
