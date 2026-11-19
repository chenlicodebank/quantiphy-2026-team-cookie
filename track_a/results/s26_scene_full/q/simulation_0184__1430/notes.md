# q1430 – speed of the box at t = 1 s (frame 24 at question_fps 24; the file is also 24 fps)

Prior: acceleration of the box at t = 1.25 s (frame 30) = 1.58 m/s². Depths: 9.194 m at frame 0 and 9.096 m at frame 12.

## Measurements
- Free fall, frames 0–8 (record centroid; box level, cx constant, bbox width constant so no depth change, camera about level):
  the vertical image acceleration is a constant 4.00 px/frame², starting from rest at frame 0. With g = 9.81, that gives
  0.004258 m/px at the frame-0 depth, F ≈ 2118 px (HFOV ≈ 49°) and a box length of ≈ 1.43 m (fit2.py).
  The depth check gives d(f12) = 9.13 m against the given 9.096 m (a 0.4 % difference, which a 4 cm move toward the camera explains).
- Slide on the ramp: the record's silhouette centroid drifts about 23 px relative to the box texture between f30 and f44,
  so I tracked the box texture again in two independent ways:
  (a) a chained frame-to-frame template match (track_tm.py → tm_steps.csv)
  (b) a fixed frame-30 template with a scale search (track_ref.py → ref_track.csv).
  Depth along the slide comes from the apparent box length (Lref/Ls). Positions are back-projected to 3D and
  per-frame speeds are |p(i)−p(i−1)|·24 (fit4.py).
- Gravity-scaled results (frames 23–44), chain / ref:
  - linear-fit mean acceleration: 1.83 / 1.82 m/s²
  - fitted v(f24): 1.97 / 1.96 m/s
  - raw per-frame v24: 1.995 / 1.980 m/s
- The sliding speed shows a strong alternation from frame to frame: the speed rises in steps every 2 frames, so per-frame
  accelerations swing roughly between 0.5 and 3.5 m/s². There is no such alternation in the free fall, so it comes from
  the contact dynamics. Frame 30 falls in a phase change, where the measured per-frame a30 is 0.6–1.0 (noisy).

## Two routes
1. Gravity scale (g = 9.81 in Blender units): v(1 s) ≈ 1.96–1.99 m/s. The measured mean acceleration of 1.83 is 16 % above the prior.
   Per frame, a30 is noisy and alternating, so 1.58 is compatible with it within the noise.
2. Prior scale (treating 1.58 as the uniform acceleration, so v24 = 1.58 × v/a ratio): 1.67–1.70 m/s.
   This needs a gravity of 8.5 in GT units and does not explain the alternation, so I consider it less likely.

## Answer
I answer 1.95 m/s. This leans on route 1 (1.96–1.99), shaded slightly toward route 2.
Confidence is moderate: there is a ~15 % tension between the gravity scale and the prior.
