# q_1595 — length of the wooden bench (simulation_0211)

Answer: **1.07 m** (estimated range 1.04–1.10).

The "wooden bench" is the slatted reddish-brown piece of furniture that `scene/` calls `side_table`, under the lamp,
vase and mirror. The camera is static, so all bench measurements use frame 0. The file rate and question_fps are
both 24, so t=1.0 s is frame 24.

## Scale / camera
- Focal length (`focal.py`, `geom.py`): the cat's origin is at 4.199 m at f0 and 4.481 m at f24. The cat moves at
  0.94 m/s, so its displacement over 1 s is about 0.94 m. Back-projecting the torso centre (scene track) gives
  f = 2099 px; the mask centroid gives 2161 and the bbox centre 2145. A global fit of a straight, constant-velocity
  3D path to all 50 torso positions gives f = 2085 (rms 3.4 px). Adopted f ≈ 2100 px (hFOV ≈ 49°), principal point
  at the image centre.
- Floor plane (`bench3d.py`, `check_cat.py`): the closest-leg depth (5.69 m) is placed on the front-left leg foot
  (1407,840), and the mirror bottom-centre depth (6.407 m) on (1510,812). This gives pitch −0.8° and camera height
  0.71 m. Checks: the cat origin stays at a steady 0.19–0.21 m above this floor at f0 and f24. Requiring the
  back-wall and right-wall floor lines to be perpendicular gives an independent pitch of −0.1° (camera height 0.78 m).
- Bench measurements from a colour mask (`bench_mask.py`):
  - slab leftmost point (1288,659) = back-left top corner;
  - slab rightmost point (1667,657) = front-right top corner;
  - leg feet: front-left (1407,840), back-left (1331,825), front-right (1625,823).

## Length
Method: put the feet on the floor plane. The front vertical plane runs through the front feet, and the back plane is
offset from it by the back-left foot. Intersect the slab-end rays with these planes, then take the length along the
bench axis.
- The front feet run 2.4° off the back-wall line, so the bench is parallel to the wall. The slab-top height comes
  out at 0.46 m at both ends, which confirms the corner assignment.
- Bench width (feet) is about 0.35 m. Ambiguity: the asked "length" is the long horizontal side, along the wall.
- Results:
  - L = 1.067 m (f 2100, pitch −0.82, axis from the feet);
  - L = 1.103 m (same, with the axis from the wall line);
  - L = 1.058 / 1.085 m (pitch −0.09 from wall orthogonality);
  - L = 1.04–1.07 m with f between 2085 and 2160.
- Second route (crude frontal approximation): 380 px × 5.69 m / f = 1.03 m. This is a lower bound, because the
  bench is oblique to the image plane.

## Confidence
Moderate, about ±4%. The main uncertainties are f (spread of the cat reference points: ±1.5%), the floor pitch
(±1°, about ±1.5%), and the choice of bench axis, feet vs wall line (about ±2%).
