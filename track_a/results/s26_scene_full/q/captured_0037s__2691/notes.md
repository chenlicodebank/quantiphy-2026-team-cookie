# q_2691 – velocity of the ping pong ball at t = 1.0 s (cm/s)

Lab video, 1280x720, 24 fps (file fps = question_fps = 24) -> t = 1.0 s is frame 24 (apex 2 of the bouncing ball).
f = 0.5959*1280 = 763 px, principal point (640, 360). depth_info: ball range 1.055 m at t = 1.0 s.

## Measurements (scripts in this folder)
- `measure2.py`: per-frame ball mask (RGB difference against a per-frame background = median of frames >= 8 away),
  centroid, extent across the blur direction (D35 = blur-free diameter), area and blur length -> `ball_meas2.csv`.
  Frame 24: centre (639.3, 352.1), D = 30.5 px (prior 4 cm at 1.055 m predicts 28.9 px: 5 % agreement, check of the
  depth/focal scale). Lateral motion at 24: about -13 px/frame.
- Range vs time (the ball comes toward the camera, D grows ~25 px -> ~42 px over frames 13-42): range taken as
  1.055 m x D(24)/D(i) with 1/D fitted linearly in time. Relative range rate per frame k:
  D35 fit 13-42: -0.0150, 16-34: -0.0145, 21-27 only: -0.0104 (noisy, short); blur-corrected stadium
  (area/length) diameter fit 13-42: -0.0165, 16-34: -0.0138. Adopted k = -0.0142 (dr/dt ~ -36 cm/s).
- 3D positions P = r x unit ray; velocity = forward difference of 5-frame-smoothed positions (lab convention):
  components at frame 24 ~ (-42 lateral, +25 down, -37 toward camera) cm/s -> |v| = 61.4 cm/s.
  (`final.py`; raw forward difference 60.3, 5-frame mean forward vector 61.4, central difference 54.1.)

## Checks
- k range -0.012 ... -0.0165 gives 58.4 ... 64.8 cm/s (smoothed forward difference).
- Route 2 tried: table plane from the five depth_info objects (`plane.py`) - plane is nearly grazing (camera ~17 cm
  above the table), bounce-contact ranges came out non-monotonic -> rejected as too ill-conditioned. Perspective of the
  x-track (`xproj.py`) is confounded by speed loss at bounces -> not used. The scale check (D(24) 30.5 px vs 28.9 px
  predicted) supports the depth/focal combination.
- The scene/ record's diam_est (25 px at frame 24) underestimates the diameter (white-threshold mask cut the shaded
  bottom of the ball); I re-measured.

## Answer
61 cm/s (confidence moderate: depth-rate component uncertain by ~ +-15 %, giving roughly +-5 % in the speed;
the convention choice (forward vs central difference) matters ~10 %).
