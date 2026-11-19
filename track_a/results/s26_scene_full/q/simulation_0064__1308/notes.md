# Q1308 — height of the white car (the white/grey full-size van), metres

Answer: **2.07 m** (moderate confidence, roughly ±10 %; the focal length is the main uncertainty).

File fps 24 = question_fps 24. Depth times t=0.58 → frame 14, t=1.58 → frame 38.

## Measurements (scripts in this folder)
- `tmatch.py`, `tmatch2.py`, `tmatch3.py`: template matching of the van's front face, giving the
  horizontal scale kx (∝ 1/Z of the front face) and the image position for every frame.
  `widths.py`: direct edge-to-edge body widths. Front-face width at hood level is 120.7 px (f14) and
  132.7 px (f38). That is a Z ratio of 0.912, confirmed by kx (0.915) and the ground row (0.908).
- `vprof.py`: vertical profiles through the van. Rows at f14: roof-top silhouette 141, windscreen
  top 178, ground/shadow line ≈314. At f38: 162, 205, ≈350.
- `height.py`: box model on the ground plane. Horizon v_h = −121 (street vanishing point in the
  record; the van's own track gives −98). Camera height and the distance to the front ground line
  come from the given origin distance (origin = van centre, 2.6 m behind the front, 1.05 m high). The
  roof-top silhouette is taken as the rear roof edge, about 5 m behind the front.
  - f = 2250: H = 2.15 (f14) and 2.02 (f38); varying the box offsets gives 1.96–2.25.
  - H scales roughly as 1/f: f = 2000 gives 2.27–2.42, f = 2500 gives 1.81–1.94.

## Focal length
- Acceleration prior: the van's depth proxy (1/kx) is not quadratic in time. Its acceleration rises
  from about 2.6 to 6 m/s², with a mean of about 4 m/s² using the depth-based Z scale. This agrees
  with the depths but hardly constrains f: the motion is almost along the line of sight, and the
  from-rest constant-a assumption gives anything from f ≈ 850 to 2000 depending on the start time.
- Ground-plane consistency between the pedestrian (far left of frame) and the taxi at f38 gives
  f ≈ 1750 ± 400. That is too imprecise to use.
- Square-intersection check (cross-street width = main-street width): this is a rough guess that
  points to f ≈ 2050–2250.
- Real-scale consistency with the given depths: the pedestrian comes out 1.67 m at f = 2250, the
  taxi's projected length 5.1 m (Crown Vic 5.38 m), and the van's body width 1.9–2.0 m. These point
  to f ≈ 2150–2380. I used f ≈ 2250–2300.
- Caveat: the given van distances shrink by 10.7 % between f14 and f38, but the image says 8.8 %.
  The two frames therefore give heights about 7 % apart (2.15 vs 2.02); I averaged them.

## Result
Taking f ≈ 2250–2300 and averaging the two frames gives H ≈ 2.04–2.08 → **2.07 m**. This is
consistent with a Chevrolet Express-type van (about 2.1 m).
