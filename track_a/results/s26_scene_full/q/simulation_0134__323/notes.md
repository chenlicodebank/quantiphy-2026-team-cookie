# q_323: acceleration of the bread slice at t = 1.75 s

2D simulation, 24 fps (fps = question_fps, so no re-timing). t = 1.75 s gives frame 42.
Convention: a = (speed(42) - speed(41)) x fps, where speed(i) = |p(i) - p(i-1)| x fps.

## Toast position (track.py, track2.py)
The toast is rigid and moves only vertically. I tracked it by normalized template matching (vertical shift only,
with a sub-pixel parabola fit) using templates cut from the upper part of the toast in frames 43, 42 and 44,
and the top strip only. The templates stay above the slot lip in frames 40-45. All four templates agree to 0.1 px.
Positions relative to frame 43: f40 80.4, f41 31.8, f42 7.8, f43 0, f44 32.9, f45 110.2 px.
Speeds: 48.6 (f41), 24.0 (f42), 7.8, 32.9, 77.3 px/frame.
Speed change at frame 42: 24.0 - 48.6 = -24.6 px/frame^2, which is -14,180 px/s^2.
Correction to scene record: the record's top_y at frame 41 (866) is about 5 px too high, probably because of a
blurred bump on the top edge. I looked at the zoomed frame and the top edge is at about 872, which matches the
template result (871.8). Using the record's value would have given -34 px/frame^2, which is wrong.

## Scale (toaster.py)
Prior: toaster height 0.166 m. The toaster spans from the top of the slot cover at y ≈ 1115 (frames 0 and 43,
columns 400-615) to the bottom of the feet / cream base at y ≈ 1397.5 (columns 280-320 and 710-720). That is
H ≈ 283 ± 3 px. The record's 276 px used the top of the dark recess under the base, not the foot bottom.
Scale: 0.166 / 283 = 5.87e-4 m/px.
Sanity check: toast height 232 px = 0.136 m and toaster width 430 px = 0.25 m. Both are plausible.

## Answer
|a| = 14,180 px/s^2 x 5.87e-4 m/px ≈ 8.32 m/s^2. The toast is decelerating while it rises, so the signed value
is negative; the answer is reported as a magnitude.
Second route: independent templates (frame 42 and frame 44 references, and the top-edge strip) give the same
Δspeed (-24.57 to -24.68 px/frame^2). The main uncertainty is the scale (±1-3%; 276 px would give 8.53).
Note: the motion is not a clean parabola. The rise slows by about 16-25 px/frame^2, while the fall speeds up by
about 42 px/frame^2. So the answer depends on the exact per-frame convention, which I followed.
Confidence: moderate-high.
