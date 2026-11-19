# q_1192: width of the telephone booth (simulation_0048)

The answer is **1.37 m**, but the confidence is low (the likely error is ±15–20 %). The booth is the grey box with a
square cap, posters on its right side and the base out of frame (the "kiosk" in scene/). The file rate and
question_fps are both 33 fps. Only frame 0 is needed, because the booth and the camera do not move.

## Camera (from the image, not from depth_info)
- **Vertical vanishing point** (955.6, 7983): an LSD fit over 67 vertical segments on the booth, the walls and the
  building (`lines.py`).
- **Booth top face.** The four cap edges were fitted to sub-pixel accuracy (`corners.py`, `rightedge.py`). The
  corners are FL (1100.6, 386.9), FR (1415.4, 418.0), BR (1465.6, 349.3) and BL (1189.9, 326.3). The front/back
  vanishing point is (−3340, −52) and the left/right one is (1769, −67), so the horizon is at y ≈ −62.
- **Focal length.** If the two top-face directions are perpendicular and the principal point is at the centre, then
  f = 1816 px and cy = 369. Leaving cx free gives f = 1839, cy = 380, cx = 932. This is `solve_cam.py`; pitch is
  about 13.5°.
- **Checks.** With this camera:
  - the cap is a square: per metre of depth below the camera, front 0.705, back 0.706, left 0.719, right 0.721, and
    the corner is 89.4°;
  - the walker scaled to 1.8 m stays on a flat ground (camera 4.47–4.57 m above it over all 15 keyframes, slope 0.2°;
    `flatcheck.py`);
  - the cyclist's head height is a constant 0.39 × the camera height.
- **What fails.** f ≈ 1200, which is what the walker depths would require, gives a non-parallelogram cap (corner 104°)
  and a sloping ground.

## Conflict in depth_info
- At f ≈ 1816 the walker at the given 11.93 / 10.82 m would be only 1.26 m tall. Making him 1.8 m tall (the exact
  prior) needs 16.8 / 15.6 m.
- The bike depths (16.49 / 11.93 m) would put the road 0.7 m below the sidewalk at that scale. The walker depths would
  put it 2 m below. Neither depth set matches the image under any single camera.
- I therefore took the scale from the prior (walker head-to-sole height 1.8 m). This gives a camera 4.50 m above the
  sidewalk, the cyclist's head about 1.8 m above the road, and a walking speed of about 1.2 m/s, all consistent. If
  the walker depths were the true scale instead, every length would be ×0.71 (width about 0.7–1.0 m).

## Booth size
- Width (front) = 0.705 Δ and side = 0.72 Δ, where Δ is the depth of the cap top below the camera. The footprint is
  square, so width ≈ length.
- Booth height = 4.50 − Δ (the ground is flat).
- The booth's base is below the image, so there is no direct anchor for Δ. The bounds (`booth2.py`, `layout.py`,
  `curb.py`) are:
  - the cap must not overhang the curb's sidewalk edge (u = −0.82 m): Δ > 1.38, so W > 0.97 m (and height < 3.1 m);
  - the base of the back-right body edge must lie below the frame (it is visible down to y = 766): Δ < about 2.15,
    so W < 1.52 m (and height > 2.35 m).
- Chosen value: Δ ≈ 1.95. This gives a booth height of about 2.55 m (a typical booth height) and a gap of about
  0.33 m from the cap to the curb (typical placement). The result is **W ≈ 1.37 m**; the side is 1.40 m.
- **Range:** 0.97 m (booth flush with the curb and 3.1 m tall) to 1.52 m.

## Second-route checks
- The two calibrations (cx fixed and cx free) change the per-Δ width by less than 1 %.
- Edge blur (depth of field) could not separate the booth's depth from the walker's: σ is about 0.6–1 px for the
  booth, the walker and the curb, and about 2.5 px only for the blurred blue wall in front.
- No shadow or ground contact of the booth is visible.
- The remaining uncertainty is the booth's height (Δ), not the camera.
