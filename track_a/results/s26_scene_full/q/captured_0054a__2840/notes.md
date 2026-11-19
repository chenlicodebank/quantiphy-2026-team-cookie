# q_2840 – velocity of the pink ball at 1.5 s (frame 36)

Answer: **4.6 m/s** (confidence moderate: the plausible range is about 3.7–5.0).

## Identification
- "pink ball" = the pale, pinkish ball (scene/ `pale_ball`) thrown by the standing person. "green ball" = the tennis ball (`yellow_ball`).
  "white ball" = the soccer ball. "orange ball" = the basketball.
- The file is 24 fps, the same as question_fps. t = 1.5 s is frame 36, two frames before the pink ball bounces (f38).
- **The video has dropped frames.** Both thrown balls jump by about 2 frames of motion between f35 and f36 (the yellow ball moves 21, then 51, then 23 px in x), and the basketball jumps between f11 and f12.
  A ballistic fit puts the gap at about 1.03 extra frame intervals.

## Pink ball track (`track_pink.py` -> `pink_track.csv`)
- Background subtraction (median of all frames) plus a pale, low-saturation, non-yellow mask. The centre is the midpoint of the blur streak along its main axis.
- The scene record's f36 and f37 points covered only part of the streak. They are corrected to (397.3, 536.2) and (376.2, 609.6), which fit the ballistic model within 2 px.

## Depth / scale (`ballistic.py`, `sens.py`, `pink_vel.py`)
- 3D ballistic fit (f = 762.8 px, g = 9.81 m/s², camera nearly level, about 2° down, judged from the room's vanishing lines). It includes a fitted time gap at f35->36 and covers yellow f23-36 and pink f22-37, with rms 0.5-0.7 px.
  The gravity scale gives a yellow-ball depth of Z ≈ 3.35-3.43 at f24, which agrees with the tennis ball's pixel size (3.4).
  The given green-ball depth is 3.039, so I rescale the geometry by 3.039 / Z_fit (0.89-0.91) to the given-depth convention.
  This puts the pink ball at Z ≈ 3.15 at f24 and Z ≈ 2.18 at f36.
- **Convention check with the prior:** back-projecting the basketball with depth used as Z, as in the method card ((u-cx)/f, (v-cy)/f, 1) × depth, and interpolating linearly between the given depths at f12 and f24,
  gives a 5-frame-smoothed speed at f12 of 2.16-2.20 m/s, against the prior's 2.21. With depth used as Euclidean range it gives only 1.72, so I used the Z convention.

## Pink velocity at f36 (Z convention, scaled positions; tilt 0-4° gives these ranges)
- Raw forward difference f36->f37: 4.78-4.88
- Mean of forward-difference speeds f34..f38 (includes the dropped-frame jump and the bounce): 4.64-4.75
- Physical instantaneous speed from the ballistic model: 4.40-4.50
- 5-frame position smoothing, or a vector mean across the bounce: 3.6-3.7. This is low because the bounce at f38 reverses the vertical motion.
- I chose 4.6, between the physical value and the frame-difference values.

## Caveats
- The reference used measured per-frame depth for the pink ball, which is not given. The given depths disagree with the geometry by about 5-20% between objects (basketball size vs depth 0.95, tennis ball 0.89, soccer ball 1.2 as Z).
- The faint streaks at f36 and f37 carry about ±5 px of error, roughly ±7% of the per-frame motion.
