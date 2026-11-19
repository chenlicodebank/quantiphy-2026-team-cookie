# q_860 – acceleration of the box at t = 1 s (simulation_0253)

Prior: box width (side parallel to the slope) = 0.611 m. No depth_info. fps = question_fps = 24 (t = 1 s → frame 24).
24 fps is physically plausible: the result (≈6 m/s² on a ≈45° ramp) is below g·sin45° = 6.9 m/s², which means
modest friction.

## Track / record check
- The scene/ record covers the right object (the only moving object: the cardboard box sliding down the ramp), frames 15–44 unclipped.
- Frame 27 duplicates frame 28 (the 26→27 step is twice a normal step), so frame 27 is excluded everywhere.
- I re-measured the box's along-slope silhouette edges per frame (b*-gain vs the empty frame 0, half-max crossing at
  sub-pixel precision, median over 31 profile lines) → `edges.py`, `edges.json`.

## Scale
- The silhouette's along-slope width is 108 px (frame 15) → minimum 92.5 px (frames 26–31) → 115 px (frame 44). Early on
  the downhill end face shows, late the uphill end face shows (plus blur). At the minimum only the front face shows:
  front-face width = 92.49 px ⇒ K = 151.4 px/m at t_c = 28/24 s.
- Perspective: the image acceleration drops from ≈830 px/s² (frames 15–33) to ≈686 px/s² (frames 28–44), the ramp band
  narrows from 49.8 to 45.8 px downhill (`across.py`), and the box's across-slope extent shrinks. So the ramp recedes from the
  camera and one constant m/px scale would be biased.

## Model (`projfit.py`)
Points on a 3D line map projectively: s_img = s_c + K·x/(1+g·x), with x = V(t−t_c) + A/2·(t−t_c)² (constant 3D acceleration).
Fitted to the clean front-face edges (uphill edge for frames 15–28, downhill edge for frames 28–44, body points ∓w/2):
- K fixed from the measured width: A = 5.96 m/s², g = 0.0071 /m, rms 0.51 px
- K free (the scale comes only from w = 0.611 m via the edge offset): A = 6.15 m/s², K = 149.2 px/m (i.e. 91.2 px width, within 1.4% of the measured 92.5), rms 0.44 px
- Second route, other reference points (K fixed): mask centroid A = 6.01; edge midpoint A = 6.05.
- Naive check: mean per-frame speed difference over frames 17–26 = 907 px/s² × 0.611/92.49 = 5.99.

## Answer
A ≈ 6.0 m/s² (spread across routes 5.96–6.15). Rigid-body sliding has constant acceleration, so this is also the value at t = 1 s.
Confidence: good (±3%). The main uncertainty is the front-face pixel width (±1 px).
