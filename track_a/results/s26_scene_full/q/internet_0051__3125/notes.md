# q3125 — width of the green car (mint Fiat 500, rear view)

Convention: internet video, single planar scale = prior / pixel value. fps 30 = question_fps (no re-timing).

Scale (prior: rider average speed 2.07 m/s):
- Rider reference point (bbox centre, pan-removed) from scene/tracks/rider_scooter.csv, recomputed in measure.py:
  mean |dx| = 17.61 px/frame -> 528.4 px/s (net displacement gives the same value). Raw image coords: 519.8 px/s (pan ~1.6%).
- Scale = 2.07 / 528.4 = 0.003918 m/px.

Car width in pixels (frame 45, rider has passed, car not occluded; zoomed grid crops frames/fiat.png, left2.png, right.png,
colour mask frames/mask45.png):
- Right edge of rear body x ≈ 1364-1366 (mask and visual agree over frames 30-49).
- Left edge of rear face x ≈ 1150 at bumper level, ≈1158 at taillight level.
- Rear width ≈ 208-216 px, taken as 214 px (scene record said 215).
- The full horizontal image extent including the receding left side panel is ≈1102-1366 = 264 px (-> 1.03 m); that is
  the side seen in perspective, not width, so it is not used.

Answer: 214 px x 0.003918 = 0.84 m. Using raw-image speed instead: 0.85 m. Range 0.81-0.85 over the edge choices.
The car is farther away than the rider, so the planar convention gives far less than the real Fiat 500 width (1.63 m);
this is expected under the annotators' single-scale method.
Confidence: moderate (the main uncertainty is which edges the annotator used for the car width).
