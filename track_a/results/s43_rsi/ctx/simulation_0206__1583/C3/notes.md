# Q1583: length of the letter (paper slip) under the gun. Answer: 0.13 m

The file and the question both run at 24 fps. 3D Blender scene with a static camera; the principal point is taken at the image centre (1062, 540).
The slip is static, so I used frame 0.

## Where the earlier answers part ways
- C1 = 0.11, C2 = 0.148, C3 = 0.20.
- All three find the same visible slip corners to within about 2 px:
  - left tip L ≈ (1320, 625)
  - front corner F ≈ (1362.5, 643.3)
  - right tip R ≈ (1415, 634.5); the back corner is hidden under the gun.
- They differ in the **tilt of the desk plane**. That tilt sets how much the receding side L–F is foreshortened, and L–F is the longer side.
  - C1 forced a plane through three depth points (near corner, far-right corner, gun). That plane has about 3.4° of roll and a steeper normal, giving L–F = 0.09 m.
  - C2 assumed zero roll and made both corners lie at the same height, which gives a 11.6° pitch and L–F = 0.147 m.
  - C3 used a planar pixel-extent guess (115 px horizontally at the gun depth), which ignores foreshortening entirely, so I reject it.

## My measurement
- **Vertical vanishing point** (`lines.py`, `calib.py`, `verticals.py`): Hough lines on 10 desk-leg edges give VP_y = (1055, 11966).
  - The x of the VP is about cx, so roll ≈ 0. This rules out C1's 3.4° roll, which would put VP_y at x ≈ 440.
  - The pitch is tan θ = f / 11426, about 13.5° at f = 2750.
  - Check: the measured leg slopes (+0.048 on the left, −0.056 on the right) and the lamp pole (≈ 0.03) match this VP. C2's 11.6° would predict +0.040, −0.047 and 0.025, which do not match.
- **Focal length**, from three routes:
  1. Typewriter free fall (`fall.py`, `fallfit.py`), using the prior g = 9.8 at 4.32 m. I tracked a keyboard template over frames 1–8 (rms 0.6–1 px) with the fall direction set by VP_y. This gives f = 2695 with the initial velocity free, or 2830–2865 if the fall must start from rest.
  2. Gun-depth consistency (`size.py`): the desk plane through the near corner (3.593 m) puts the gun origin (4.704 m) 2.7 cm above the desk at f = 2700, 1.3 cm at 2770 and −1.1 cm at 2900. A revolver lying flat should have its origin about 2 cm up, which means f ≈ 2700–2800.
  3. Other routes are looser. The far-right corner depth gives f ≈ 2550–2630 if it is the front-right corner, or about 3050 if it is the back-right one. Desk-rectangle orthogonality is ill-conditioned and gives about 2950.
  - I chose f = 2750 (range 2700–2800).
- **Paper tip under the shadow** (`paperview.py`): in Lab b*, the warm paper colour (b ≈ 139 even in shadow) stops at x ≈ 1415, y ≈ 634.5. Beyond that it matches the desk (b ≈ 129). So R is the real corner and F–R is a complete side.
- **Back-projection onto the desk plane** (`final.py`, f = 2750; the near-corner plane and the gun-minus-2 cm plane agree to within 1%):
  - L–F (front-to-back) = 0.1295 m. It is 0.134 at f = 2700 and 0.125 at f = 2800. With C2's corners it is 0.129; with C1's it is 0.118.
  - F–R (along the desk front) = 0.110 m.
  - The slip's depth is about 4.65 m, consistent with the gun at 4.704 m.
- The slip is aligned with the desk (F–R is parallel to the front edge), so its bounding-box length is the longer side, about 0.13 m. The width is about 0.11 m.

## Second-route check
- The front paper sheet on the same plane at f = 2750 measures about 0.19 × 0.30 m (A4/letter-like) with corner angles of 84–95°. That size is plausible, so the scale is plausible.
- The two independent plane heights (near-corner depth vs gun depth) agree.

## Verdict
I agree with none of the earlier answers. C2's corners are right, but its pitch is too shallow, so its L–F is about 14% too long. C1's plane has a roll that the vertical lines do not support.

Confidence: moderate, about ±6%. The main uncertainty is f (2700–2800 → 0.125–0.134) plus about 1 px on the tips.
