# Q345: acceleration of the train at t = 0.5 s (frame 12, 24 fps)

The file fps and question_fps are both 24, so no re-timing is involved.

Scale: the prior says a side window (the wide one, not the narrow door windows) is 1.8 m wide. I measured the near-layer window opening
in code (`winedge.py`, gradient peaks of row profiles at y = 520/600/680) on six window instances in frames 7, 8, 9, 10, 14 and 16:
347.1, 346.1, 349.1, 349.0, 351.4 and 354.3 px, giving a mean of 349.5 px (sd 2.7). By eye on frame 12 the window is about 355 px. I used 350 px, so the scale is 0.00514 m/px.

Motion: the near-layer per-frame shift grows linearly, so the acceleration is constant.
- Record (scene/, NCC column profiles, 12 frames): slope 3.199 px/frame², rms 0.8 px.
- My own check from window-edge tracking (`fitcheck.py`, 7 frame pairs): slope 3.39 px/frame². Single edge shifts agree with the record's line to about 1-2 px.
I used about 3.25 px/frame², weighted toward the record's denser fit.
The window width and the shift are measured on the same near layer, so the perspective/layer factor cancels.

a = 1.8/350 × 3.25 × 24² ≈ 9.6 m/s². The two routes give 9.49 (record slope) and 10.07 (edge slope).
Confidence: moderate. The uncertainty is about ±5%, mostly from the slope.
