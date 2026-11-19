# q_2134 — speed of the toy truck at 0.50 s (cm/s); prior: sofa total height = 90 cm

## Scale (sofa.py, frame 0)
Red sofa at the left. I took its full vertical extent at the near (right) end, the way an annotator would read it:
- top: highest point of the rolled arm, y ≈ 128 (red mask at x 620-660)
- bottom: floor line under the base at the near corner (x ≈ 520-540). The red ends at y ≈ 537, then the dark gap
  under the sofa (legs/shadow) runs to y ≈ 552.
- pixel height ≈ 424 px, so the scale is 90/424 = 0.2123 cm/px.
The alternative reading (back top y≈155 to base y≈530 at the far left end, ≈375 px) would give a speed about 13% higher.

## Time base: 24 fps (question_fps)
The truck's per-frame steps alternate big and small (about 19-20 px, then 12-13 px; ratio ≈ 1.5). That fits a
60→24 fps pulldown (alternating 3 and 2 source frames). It does not fit a 24→19.68 resample, which would put a
double step every 4-5 frames, and that pattern is not there. So the frames are 24 fps frames whose container was
re-timed to 19.68. I use 24 fps: t = 0.50 s is frame 12, and speed = px/frame × 24.

## Truck motion near frame 12
The camera pans slightly. The floor (grout-line) shift from scene/tracks/camera_shift.csv is about 2.5 px/frame
around frame 12.
- Record (front_x, floor-compensated): f10→f14 = (834.2-770.3)/4 = 15.98 px/frame. f11→f13 = 16.45 px/frame.
- Independent template match of the truck body (truck_check.py), raw: f10 848.3 → f14 793.6 = 13.68 px/frame.
  Adding the floor shift (19.71-9.83)/4 = 2.47 gives 16.15 px/frame.
- The single-frame forward difference at f12 is 18.9 px floor-compensated (16.3 raw), but it is inflated by the
  pulldown jitter, so I averaged over the 2-frame cycle (f10-f14).
- Speed = 16.15 px/frame × 24 × 0.2123 cm/px = **82.3 cm/s**.

## Checks and spread
- Record vs template match: 15.98 vs 16.15 px/frame (agree within about 1%).
- If the armchair (far background) were used for camera compensation instead of the floor: 14.9 px/frame → 76 cm/s.
- If the file fps 19.68 were used: 67.5 cm/s.
Confidence: moderate. The main uncertainties are which sofa extent the annotators read and the time base.
