# Q1540 – acceleration of the blue car (light-blue utility cart) at t = 1 s

The file fps and question_fps are both 24, so t = 1 s is frame 24. By the convention a = (speed(24) - speed(23)) x fps,
i.e. (x22 - 2 x23 + x24) x fps² in world units. The camera is static, and the cart moves right to left parallel to the image
plane: its rows stay constant and its tyre size stays constant (~77 px from frame 31 to frame 41). So every rigid point,
including the origin, has the same world acceleration, and a single m/px scale taken in the tracked plane is enough.

## Where the candidates part ways
- **Pixel acceleration at frame 24.** C1 and C5 get ≈0.50–0.52 px/f². C2 and C3 get ≈0.40 because they fitted the noisy
  record track (±2 px). C4 gets 1.6 px/f² from bbox-centre speeds, which is wrong: the bbox mixes in pixels from the
  occluding car and from yaw.
- **Tyre pixel diameter (the scale).** C1 uses 75.0 px (vertical dark extent), C5 uses 73.0 px (partial-arc circle fits),
  C3 uses 74.5 px, and C4 uses 78 px.

## My measurements
- **Tracking (`track.py`).** Masked-SSD template matching against frame 36, ignoring yellow (car) pixels, with
  sub-pixel parabola peaks. I used several patches:
  - rear roof + handle + rear light panel (clean from frame 22 on)
  - light panel (clean from frame 23)
  - lower body + wheels (frames 27-41)
  - The body/wheel-plane motion equals the light-panel motion to within 0.2 % (452.5 vs 451.8 px over frames 27→41).
- **Motion model (`fit.py`).**
  - Per-frame steps of the light panel rise from 31.75 (22→23) to a flat maximum of 33.7 px/f at about frame 30, then fall
    symmetrically to 29.0 (40→41).
  - This is a Blender Bezier ease-in/out (smoothstep, exactly cubic in time). A joint fit of the record's early frames
    0-20 and my light track gives i0 = -0.1, T = 59.2 frames, Δ = 1329 px.
  - Second difference at frame 24:
    - joint smoothstep fit: 0.4975 px/f²
    - light-panel cubic / smoothstep fit, frames 23-41: 0.520
    - frames 26-41: 0.527
    - rear patch: 0.486-0.498
    - quartic fits: 0.49-0.51
  - The ideal ease from i0 = 0, T = 59 gives 0.503. **Adopted: 0.505 px/frame²** (cart speeding up, so positive).
- **Scale: cart tyre (front tyre, frames 31-41; `tire_circle.py`, `tire_ext.py`, `rim.py`).**
  - Full-ring gradient circle fits give 77.2 px (median of 11 frames). Ellipse fits at frames 31 and 41 give
    78.9 x 77.5 and 77.4 x 77.2 px. The horizontal gradient width at the centre rows is 76.5-78 px, and is 77-78 px at
    frame 31, where the tyre is at the image centre column.
  - The vertical extent along the centre column is only 74.5 px. The bottom merges with the contact shadow / floor, and
    the top tucks under the sill trim. Both of these shorten the vertical extent, whereas viewing from above could only
    lengthen it. So I take the horizontal / full-ring value.
  - This horizontal value is also the one that matches the direction of motion.
  - Adopted D = 77.0 px, so the scale is 0.369 / 77.0 = 0.004792 m/px in the wheel/side plane.
  - Sanity checks: cart height 325 px gives 1.56 m. The ground-contact row ratio gives Z_cart/Z_car = 1.24, so the
    yellow car's 1148 px side length gives ≈4.5 m. Both are plausible.

## Answer
a = 0.505 px/f² x 576 x 0.004792 m/px = **1.39-1.40 m/s²** (answer 1.40).

## Second route and spread
- Pixel acceleration across the independent patches and windows is 0.49-0.52, i.e. ±3 %.
- For the scale, a tyre of 74.5 px (vertical extent) would give 1.44 m/s²; that matches C1. C5's 73 px would give 1.47.
- I agree with C1 and C5 on the motion. I differ by about 3-6 % on the tyre pixel size, preferring the horizontal /
  full-ring silhouette of 77 px. I reject C2 and C3 (they under-read the curvature from the noisy record track) and C4
  (bbox-centre speeds).

## Confidence
Good: about ±4 %.
