# q_436 — acceleration of the box, 0–0.3 s (m/s^2)

Prior: acceleration of the box after 0.75 s = 2.338 m/s^2 (sliding down the ramp). depth_info: none.
fps = question_fps = 24, so no re-timing. t = 0–0.3 s is frames 0–7: the box falls freely, straight down, from rest.
It lands on the ramp between frames 7 and 8.

## Method
2D scene, with the fall and the slide in about the same plane. I used one px→m scale, so
a_fall = 2.338 × (a_fall_px / a_slide_px).

- The record's centroid track (scene/tracks/box.csv) gives a_fall ≈ 2250 px/s². That value is biased: the silhouette
  changes during the fall (the visible top face shrinks and bbox_h drops 235→218 px), and that moves the centroid.
- I re-measured with my own tracker (`track2.py`). It does masked template matching of the box's own pixels from each
  frame to the next, with sub-pixel peaks, and stays above the occluding crates (y < 860). The output is `steps_tm.csv`.
  - Fall step lengths for frames 1–7: 2.28, 6.42, 11.19, 15.42, 19.53, 23.82, 27.74 px. These grow linearly; the
    residuals are under 0.3 px and the line reaches zero at frame 0.44 (the expected value from rest at t=0 is 0.5).
    The slope is 4.27 px/frame², which gives **a_fall = 2459 px/s²** (2446 for frames 2–7).
  - Slide step lengths for frames 13–34 rise linearly from 19.3 to 42.1 px, with an rms residual of 0.4 px. This gives
    **a_slide = 591–599 px/s²** for windows 13–34, 14–34 and 16–34. It is 620 for frames 14–24 (around the prior's
    0.75 s) and 573 for frames 20–34.
- Result: 2.338 × 2459/595 = 9.66 m/s². The range over the windows is 9.3–10.0.

## Second route / sanity check
This is a Blender rigid-body render, so free fall should be g = 9.81. For that to hold, the slide in pixels would need
2459 × 2.338/9.81 = 586 px/s², which is inside the measured 573–620 range. The prior also fits physically: on a slope of
about 28° with friction about 0.25, g(sinθ − μcosθ) ≈ 2.3–2.5 m/s². The pixel route (9.66) and the physics value (9.81)
differ by 1.5%.

Answer: **9.8 m/s²**. Confidence is high (about ±3%).
