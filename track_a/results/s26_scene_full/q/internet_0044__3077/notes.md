# Q3077 – height of the green bottle (cm)

Prior: g = 9.8 m/s². Internet video, 30 fps (file fps = question_fps, so no re-timing). Following the annotators' convention,
I used one planar scale = 9.8 m/s² / (the ball's vertical pixel acceleration).

## Ball acceleration (measure.py, scene/tracks/ball.csv cy_f0, i.e. camera-stabilised)
- Quadratic fits of y per arc, using measured (not arc-filled, not edge-cut) flight frames: 20.05, 19.83, 18.84, 19.50, 19.67,
  19.60, 20.15, 19.94 px/frame² (one arc, 126-130, gave 25.0. It has only 5 frames and sits over the white bowl, so I dropped it as an outlier).
  The median is 19.83 px/frame².
- Second check: frame-to-frame second differences (annotator style) over 52 triples. The mean is 19.88 and the median 19.65 px/frame².
- Adopted value: 19.75 px/frame², i.e. 17775 px/s². Scale = 9.8 / 17775 = 5.51e-4 m/px.

## Bottle pixel height (frame 0, intensity profiles in measure.py)
- Top of the lip is at y ≈ 300.5, where the dark monitor gives way to a brighter glass edge at rows 300-301.
- Bottom: the bottle meets the desk at y ≈ 812.5 at its sides and ≈ 816 at the centre of the front base curve.
- Height ≈ 514 px (±3). The scene record gives 513.

## Answer
514 px × 5.51e-4 m/px = 0.283 m, so the answer is **28.3 cm**.
The plausible range from the spread in acceleration (19.6-20.0 px/frame²) is 28.0-28.6 cm. A real 750 ml bottle is about 30 cm tall, so this is plausible.
The ball passes in front of the bottle, so it is closer to the camera, and the planar convention slightly underestimates the true size.
I did not correct for this because the reference answers use a single scale. Confidence: good (about ±4%).
