# q_1852: acceleration of the rocket at t = 1 s (m/s^2). Prior: rocket length = 2.9 m

The video is 2D, with a static camera, at 24 fps (the file rate and question_fps are the same). t = 1 s is frame 24. The rocket flies in a straight line up and to the left along the launch axis from scene/axis (direction (-0.778, -0.629)). At frame 24 only its rear part is visible, because the nose has left through the top edge.

## Scale
- **Rocket length in pixels** (`length_profile.py`, `edges.py`): sub-pixel nose and tail edges are taken where the peak-contrast profile along the axis crosses 0.5, over frames 15-20 (rocket fully clear on white). Result: L = 224.6 px. The 10 %-width profile gives 225.1 and the 50 %-peak gives 225.2.
- **I used L = 225 px.**
- **scene/ value was wrong:** its 219.2-221.9 px came from percentile extents of a thresholded mask. That method clips the thin nose tip and the narrow nozzle.
- **SAM 3 check:** the SAM 3 mask at frame 18 is 226.6 px long (min to max along the axis), against my profile value of 226.0 at the same frame. These agree. My earlier percentile value (219-223) differed by more than 3 %. A zoomed look at the profile shows the tip and nozzle are real rocket pixels, so the profile/SAM value is the right one.
- **Scale:** 2.9 / 225 = 0.01289 m/px.
- **Alternative reading not used:** if "length" meant the world-axis horizontal extent of the tilted rocket (about 186 px), the answer would be about 21 % larger. I used the length along the rocket's axis (object dimension).

## Position series
- Nose edge minus a half-length (frames 7-21).
- Tail edge plus a half-length (frames 15-25; frames 13-14 are excluded because exhaust there makes the visible length 238-242).
- Sub-pixel template matching along the axis, using templates from frames 16, 18 and 20 (`tmatch.py`, frames 15-25).
- These are averaged in `fit_final.py`. Frame-to-frame jitter is about ±2-4 px (edge flicker in the segmented render), so a one-frame second difference is meaningless. I fitted smooth models instead.
- **SAM 3 track:** its centroids agree with my mask centroids within 0.3-1.4 px in frames 15-22. At frame 19 the SAM track jumped to the truck, so that frame was discarded.

## Model and result
- **Constant acceleration fits badly:** RMS 3.2 px over frames 7-25, against 1.35 px for a cubic. The acceleration clearly falls over time: windowed slopes of the step size give about 22 m/s^2 (frames 5-12), 16 (13-19) and 10 (19-25).
- **Ease-in curve fits well:** a Blender Bezier ease-in (smoothstep, i.e. a cubic) fits with its rest start at frame ≈ 0-1, which is consistent with a keyframe at the first frame.
- **Acceleration at frame 24** (reference convention: ((p24-p23)-(p23-p22))·fps² on the fitted curve):
  - Combined series, frames 7-25: 9.5 with a free start, 11.3 with the start fixed at frame 0.
  - Combined series, frames 9-25: 9.9 / 10.8.
  - Combined series, frames 12-25: 8.7 / 10.8.
  - Combined series, frames 7-21: 11.0 / 12.7.
  - Tail-only series: 10.2 / 11.5.
  - Template-only series (fixed start): 9.3.
- **Answer: 10.5 m/s^2.**

## Second-route check
The tail-edge series (independent of the nose and the pod region) gives 10.2-11.5. The slope of the step sizes over frames 19-25 gives 10.2.

## Confidence
Moderate, about ±15 %. The main risk is the motion model: a pure constant-acceleration reading of the late frames would give 12-14.
