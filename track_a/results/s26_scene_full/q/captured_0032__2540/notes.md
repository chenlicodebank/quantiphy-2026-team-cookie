# q2540 — velocity of the tennis ball at t = 1.5 s (cm/s)

Lab video, 1280x720, 24 fps (the file rate and question_fps are the same). t = 1.5 s is frame 36. f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
Prior: tennis ball diameter 6.7 cm. depth_info at frame 36: tennis ball 1.183 m, ping-pong ball 1.353 m.

## Checks on the record
- The yellow_ball track is the tennis ball. At frame 36 it is rolling on the tabletop, toward the camera and to the left.
- A dropped frame between frames 35 and 36 is confirmed: both balls jump about twice their normal step. In every fit,
  frames ≥ 36 get time index frame+1, so frame 36 → frame 37 is one real interval and is not affected.
- The record's mask undersizes the ball. Re-measured in `measure.py` with a looser saturation threshold: about 42–44 px
  tall at frame 36. Expected from the given depth: 762.8 x 0.067 / 1.183 = 43.2 px. ✓
- The source looks upscaled from 640x360 (bounding boxes come in 2-px steps), so a single ball size is only good to about ±2 px.

## Method
The ball centre (sub-pixel u, v from `measure.py`) is back-projected along its ray. The depth at frame 36 is the given
1.183 m (a Euclidean distance, converted to optical-axis depth). Depth at the other frames comes from one of two routes:

1. **Table-plane route (main)**: the ball centre moves in a plane parallel to the tabletop, so its axial depth
   scales as 1 / (image distance below the tabletop's vanishing line).
   - Side-edge vanishing point fitted in code (`table_vp2.py`): (712, 347).
   - Roll: the wall seams lean by dx/dy ≈ −0.011 to −0.024 (`roll.py`), which gives a horizon slope of about +0.017.
     The table's near edge has slope 0.025 (`table_edges_h.py`).
   - u(τ) and v(τ) are quadratic fits over frames 30–41. The forward difference from frame 36 to frame 37 is used,
     and a 5-interval smoothed version is computed as well (`final_plane.py`).
   - Results:
     - horizon slope +0.0167, VP y 343 / 347 / 351 → **83.3 / 85.1 / 87.1 cm/s**
     - level horizon → 79–82
     - slope +0.025 → 85–90
     - slope −0.019 (from a noisy far-edge fit) → 74–76
2. **Apparent-size route (second check)**: depth ∝ 1 / pixel diameter, with 1/d fitted linearly over frames 30–41 or
   33–41 (`velocity.py`, `velocity_fit.py`) → **87–96 cm/s**.
   - The static ball at frame 10 is about 29.5–30 px against 43 px at frame 36, a ratio of about 1.45. This would put
     the horizon at about 361, and the wall seams also hint at a small upward pitch.
   - But the pixel sizes are only good to ±2 px, and the contact shadow inflates the vertical extent, so this route is noisier.
3. Ignoring depth change (constant 1.183 m) gives only about 60 cm/s. This is wrong: the ball clearly gets closer
   (its size grows from 35 to 48 px between frames 30 and 41).

The two routes disagree by about 10% (about 85 against about 92). The cause is the uncertain tabletop vanishing line,
which sets how fast the depth changes. The answer is taken between them, leaning on the plane route: **86 cm/s**.

If the reference smoothing spans the dropped frame without correcting for it, its value would be about 15% higher
(naive 5-frame window ≈ 90–118). That is another reason not to answer lower.

Confidence: moderate, about ±10%.
