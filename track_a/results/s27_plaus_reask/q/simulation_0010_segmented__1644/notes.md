# q1644 — height of the house's door (m)

The file's frame rate is 22 fps and question_fps is 24. Times are converted with 24 fps, so frame i is at t = i/24.

## Focal length from the bird (prior: length 1.19 m; depth 34.584 m at t=0 s and 33.999 m at t=1 s)
- The bird flies across the view, left to right. Its body (beak to tail) lies roughly horizontal in the image.
- I looked at frames where the wings do not reach past the beak or tail. I read the beak-to-tail extent from
  zoomed frames and from the bbox in scene/tracks/bird.csv:
  - f11: 141 px
  - f18–20: about 142 px
  - f29: 148 px
  - f3–4 (161 px) were not used: the swept wings make them too long.
- The depth changes by about 0.6 m/s while the bird moves about 3.3 m/s sideways, so its heading is about 10° off
  the image plane. Correction: ×1/0.985.
- Depth at each frame was interpolated or extrapolated linearly from the two given values:

  | frame | depth (m) | f (px) |
  |---|---|---|
  | f11 | 34.32 | 4128 |
  | f20 | about 34.1 | 4210 |
  | f29 | 33.88 | 4278 |

- Result: f ≈ 4206 px, about ±4% (hfov ≈ 25.8°).

## Door
- The doorway and the plank door leaf were measured in code on frame 0 (measure.py), using column profiles:
  - The dark opening runs from y = 878 to 1158, where the segmentation's ground cut starts.
  - The leaf runs from y ≈ 880 to 1162–1166.
- Door height in pixels: 284 px.
- The distance to the house origin is 55.083 m. Converted to optical-axis depth that is about 54.8 m (the origin is
  about 410 px off-axis).
- The door is on the front gable wall, so it is closer than the house origin, which is probably at the centre of the
  footprint. The front wall is about 9 m wide, so I assumed a house depth of about 4–5 m, which puts the door at
  Z ≈ 52.5 m. That house depth is an assumption; the clip cannot measure it.
- Door height = 284 × 52.5 / 4206 = 3.55 m.
  - If the door were at the depth of the origin: 3.70 m.
  - If the door were 4.5 m in front of the origin: 3.41 m.

## Plausibility
- The scene is large. A 1.19 m crow-like bird is about 2.6× a real crow, so the prior is unrealistic and the scene
  is treated as scaled. Other sizes on the same scale:
  - Cart wheel: about 1.36 m.
  - House front: about 9 m wide.
- The door/bird size ratio is consistent with that scale.
- Second route: the pixel ratio door/bird is 284/145 and the depth ratio is about 52.5/34.1. Then
  1.19 × 1.96 × 1.54 × 0.985 ≈ 3.5 m, which agrees.

Confidence: moderate, about ±6%. The main uncertainties are the door's depth relative to the house origin and the
bird's apparent length while flapping.
