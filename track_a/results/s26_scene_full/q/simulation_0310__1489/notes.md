# Q1489: forklift speed at t = 2.0 s (frame 48, question_fps = file fps = 24)

Answer: **4.45 m/s**

## Method
1. **Track**: I used the orange-panel centroid from scene/tracks/forklift.csv (about 1 px noise). The image path is a straight line and the camera is static.
2. **Line model** (`linemodel.py`): for a given focal length f (principal point 1280,720), P24 = 16.7953·ray(24) and
   P48 = 19.0980·ray(48). The forklift moves in a straight line, so every frame's ray is intersected with the
   line P24→P48, which gives the path coordinate s(t). The camera pitch θ follows from requiring this line to be horizontal.
3. **Focal length from the height prior (2.47 m)** (`recon.py`, `points.json`): at frames 24 and 48 I picked these points by hand
   and checked them on zoomed overlays (frames/mk_*.png):
   - the ground contacts of the near front and near rear wheels;
   - the top corners of the near and far mast uprights.
   The contacts are put on the ground plane, with the camera height set so that the vehicle centre lies at the given depth.
   The mast top is placed 0–0.3 m ahead of the front axle, and its height above the ground is solved for.
   Setting that height to 2.47 m gives f = 3650–4040 px across all the assumptions I varied (mast offset a, origin height z0
   from 0 to 1.1 m, origin ±0.4 m along the body). Frames 24 and 48 agree within 1 %. Best estimate: f ≈ 3800 px (horizontal FOV ≈ 37°).
   - Checks: the rear roof crossbar sits vertically above the rear wheel centre and comes out at 2.48 m, so roof and mast
     have the same height and the 2.47 m prior holds whichever one is the top. The wheelbase comes out at 1.83 m, the
     mast-upright spacing at 0.62 m, and the contacts are parallel to the heading within 1°.
   - Two independent cues agree: the lean of the tree trunks puts the vertical vanishing point at y ≈ 11000 (f ≈ 3800–4000),
     and the wheel ellipse axis ratio (about 0.61 measured, 0.64 predicted) is consistent.
4. **Motion** (`fitmotion.py`): s(t) fits uniform acceleration from rest very well (rms 1.7 cm, t0 = 0.02 s):
   a ≈ 2.27 m/s². Speed at frame 48 by the backward difference |p48 − p47|·24, taken from the quadratic fit, is 4.46.
   - Other estimates: cubic fit 4.44; fit with t0 = 0 gives 4.45; window 0–36 gives 4.42; window 36–72 gives 4.44; the raw per-frame values are noisy (4.30–4.68).
   - Between f = 3700 and 3900 the answer runs 4.52 to 4.38.

## Second route
`route2.py` intersects the centroid rays with the horizontal plane at the centroid height, fixed by D24 only.
It reproduces D48 = 19.098 exactly and gives a backward-difference speed of 4.46 at f = 3800.
This route is not fully independent: it shares the pitch with the line model.
The independent check on f is the tree vanishing point plus the plausible wheelbase.

## Confidence
Moderate-high. The main error is f (about ±3 %), plus the unknown position of the Blender origin (about 1 %). Expected error is about 3–5 %.
