# Q1003: length of the plane (m)

The prior is plane speed = 22.16 m/s. The scene is a 2D top-down view with a static camera, so one metres-per-pixel scale comes from the jet's pixel speed.
The file is 24 fps, but question_fps is 25 and is used here, as the rules require.

## Speed in pixels
- `scene/tracks/jet.csv` ref_x for frames 2–59 is linear, with steps of 34.25–34.53 px/frame.
- A straight-line fit gives a slope of 34.398 px/frame, so 34.398 × 25 = 859.95 px/s.
- Scale: 22.16 / 859.95 = 0.025769 m/px.

## Length in pixels (re-measured)
- `measure2.py` builds a diff mask of the jet frame against a frame where the jet is far away (it does not overlap), with the threshold set to 45:
  - frame 24 vs 50: x 1114–1679, 566 px
  - frame 40 vs 10: 567 px
  - frame 30 vs 60: 568 px
- The overlay in `frames/m2_24.png` shows the mask covering the whole jet, from the missile tips on the left to the tail-cone tip on the right.
- The scene record gives 562 px. My diff masks include a little blur and closing growth, which adds about 2–4 px.
- I took 564 ± 4 px.

## Result
- 564 × 0.025769 = 14.53 m, answered as **14.5 m**.
- If the file's 24 fps were used instead, the result would be 15.1 m.

## Checks
- Wingspan: 720 px → 18.6 m.
- Tank hull: 246 px → 6.3 m, which is a realistic tank hull (about 6–7 m). This supports the scale.
- A 14.5 m jet length is realistic for a fighter (an F-16 is 15 m).

Confidence: good, about ±3%.
