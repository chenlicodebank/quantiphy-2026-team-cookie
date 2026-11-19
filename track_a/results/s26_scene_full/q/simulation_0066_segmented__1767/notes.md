# q_1767: length of the turning yellow car (taxi)

**Answer: 4.95 m.** Plausible range is about 4.75–5.3 m, mostly because the focal length is uncertain.

The file rate and question_fps are both 24. Depth times map to frames: t = 0.58 s is frame 14 and t = 1.58 s is frame 38. The yellow car is the `taxi` track in scene/. It is the only yellow car; it turns right and drives straight and side-on from about frame 50.

## Scale (focal length f)
- Principal point is taken as the image centre and roll as 0. The prior gives the white van an acceleration of 4 m/s², starting from rest.
- **Van kinematics** (`van_f*.py`, `van_lk*.py`, `van_selfcons.py`, `van_joint.py`):
  - Rigid LK points on the van fit a uniform-acceleration projective model with rms ~0.2–0.4 px.
  - The fitted start is t0 ≈ −0.5 to 0 frames, which makes the 14→38 path 0.5·4·((38−t0)²−(14−t0)²)/576 = 4.33–4.42 m.
  - The 3D displacement |P38 − P14| comes from the given distances and the van's ray (centroid, or the ground centre with k = 0.3).
  - This gives f ≈ 800–850 with the centroid ray, or 880–935 with the ground-centre ray.
  - Using the depth-derived vanishing point instead makes the result unstable as the frame window changes (f from 844 to 1300). That vanishing point is not consistent with the image's uniform-acceleration fit, so I did not trust it.
- **Vanishing points** (`vp_img.py`, `vp_edges.py`, `vp_f.py`):
  - The van's vanishing point comes from its body edge lines (frames 62/66/68/71) and from where the van and cyclist tracks cross. Estimates range over (557–654, 25–79).
  - With a level horizon through it, the taxi's late straight path is assumed perpendicular to the van; it is 86–89° in the 3D model.
  - This gives f ≈ 840–1000, with ≈ 890 for the median vanishing point.
- **Chosen value: f ≈ 900 px** (range 840–1000), horizon about row 50–60, pitch about 28°.
- Sanity check: the pedestrian would be about 2.3 m tall (bh ≈ 93 px at 21 m), so assets are not consistently at real scale. I did not use this.

## Taxi length
- **Route 1, late straight frames 50–71** (`taxi_len3.py`):
  - The taxi's centre is placed on its constant-height plane, anchored at the exact depth at frame 38. Its depth at frames 50–71 is then 16.1–17.0 m.
  - Heading comes from the 3D track.
  - The car model is a rounded-corner plan (corner radius r = 0–0.5 m, W/L = 0.36–0.40) spanning bumper heights of 0.3–1.1 m. Its projected x-extent is matched to the mask x-extent (404–471 px).
  - L is stable across frames (±0.02–0.05 m).
  - Results by focal length:
    - f = 880: 4.90–5.15 m
    - f = 920: 4.80–5.03 m
    - f = 1000: 4.72–4.87 m
- **Route 2, frame 38 only** (`taxi_f38.py`):
  - Uses the exact given depth of 16.549 m, with heading from the mask's principal axis (−19°).
  - At f = 900: 4.78–5.15 m (4.89–5.06 with r = 0.3).
  - This agrees with route 1 to within about 2%.
- **Models I rejected:** a plain box (L×W×H) does not fit. Its top corners lean outward under perspective and it ignores rounded corners, so it underestimates L, and its y-extents miss by 50–70 px.

## Confidence
Moderate. The fit within a given f is good to about ±3%. The main uncertainty is f itself (about ±8%), followed by where the vehicle origin sits (centre or ground; about ±2%).
