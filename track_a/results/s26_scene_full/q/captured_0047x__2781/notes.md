# q_2781 – yoga ball displacement 1.0 s → 1.5 s

File fps = question_fps = 24, so the frames are 24 and 36. Camera: f = 0.5959·1280 = 762.75 px, principal point (640, 360).
The depth_info line for t = 1.5 s says "soccer_ball", but the clip has only one ball (the yoga ball). I read it as the yoga ball's depth at frame 36.

## Measurement
- Script `conefit.py` fits the sphere silhouette as a cone. Outline points come from the green-key foreground. Points on the image border and the person-contact zone are dropped. Every outline ray should make the same angle β with the centre ray. The fit gives the projected 3D centre, so it handles the off-axis ellipse stretching and the partial arc at frame 36.
  - Frame 24: centre (517.3, 539.5), β = 5.197°. The scene record gives (516.6, 543.4).
  - Frame 36: centre (365.1, 662.2), β = 7.676°. The record gives (367.7, 659.8). The ball is cut by the bottom edge in this frame, but the fit RMS is 0.14°.
- Back-projection with the given distances, centre = d · unit ray (`disp.py`):
  - P24 = (−0.387, 0.566, 2.403)
  - P36 = (−0.476, 0.523, 1.320)
  - **|P36 − P24| = 1.087 m**

## Checks
- Prior check: 1.087 m / 0.5 s = 2.17 m/s average speed. The prior gives 2.146 m/s at 1.0 s, so the given depths fit the prior velocity.
- Route 2 uses depth from apparent size (R = d·sin β calibrated at frame 24, R = 0.226 m).
  - It predicts a depth of 1.69 m at frame 36, against the given 1.497 m.
  - That gives a displacement of 0.92 m and a speed of about 1.8 m/s at 1.0 s, which is below the prior.
  - The given depth at 1.5 s is about one ball radius shorter than the size-based depth, probably a surface-vs-centre effect in the depth measurement. The reference uses the given depths, and those match the prior, so the answer uses them.
- If the centre at frame 36 is moved by ±30 px (an annotator clicking the visible part), the result changes by only about 1–2 %, because the displacement is mostly along depth (Δz ≈ 1.08 m).

Confidence: moderate–high (±3 %) under the given-depth convention.
