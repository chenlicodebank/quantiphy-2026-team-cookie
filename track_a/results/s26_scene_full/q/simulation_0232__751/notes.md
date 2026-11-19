# Q751 – speed of the paper airplane at t = 1 s (frame 24)

The "paper airplane" is the thin light-grey flying object the scene record calls the "arrow" (it is the only flying
object; frames 7–41). 2D scene, fps = question_fps = 24, so no re-timing.

Scale (from the prior, cat speed = 0.714 m/s): cat torso-centroid track (scene/tracks/cat.csv) goes from x 255.9 to
702.1 over 49 frames, giving a net 9.11 px/frame. The mean per-frame step is 9.19, inflated by gait jitter, and a linear
fit gives 8.96. I used 9.11 px/frame = 218.6 px/s, so the scale is 0.714 / 218.6 = 0.003267 m/px.

Airplane pixel speed at frame 24:
- Record ref points: step 23→24 = 66.1 px. Neighbouring steps are 71.1 (22→23), 67.3 (24→25) and 65.5 (25→26), so speed
  falls smoothly through the apex (frame 23) and the 66.1 is a low-noise outlier.
- My own measurement (measure.py: median-background difference, midpoint of the mask ends, frames 21–25 fully
  segmented with lengths of 128–132 px) gives steps of 69.6 (23) and 69.0 (24).
- Smoothed estimate: 68.7 px/frame, or 1649 px/s.

Speed is 1649 × 0.003267 = 5.39 m/s (range 5.19 using the raw record step to 5.41). Answer: **5.35 m/s**.

Second route: my independent segmentation agrees with the record's midpoints to within 1–2 px at frames 23–24.
Confidence: medium-high, ±4%. One possible issue I can't resolve: the airplane may fly at a different depth than the
cat on the desk. The image has nothing to measure that by, so I used the single 2D scale.
