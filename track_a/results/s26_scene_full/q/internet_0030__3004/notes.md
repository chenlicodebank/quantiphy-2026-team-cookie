# q3004 — boat displacement 0.5 s → 1.37 s (internet_0030)

Prior: speedboat length = 3.2 m. Internet video, so I used one planar scale = 3.2 m / boat pixel length.

## Time base
The file runs at 29.153 fps and the question at 30 fps. 1.37 s ≈ 41/30 = 1.367 s, which is the clip's last frame at 30 fps, so I used
question_fps = 30: frames round(0.5·30) = 15 → round(1.37·30) = 41. Both rates give plausible boat speeds (about 7 m/s), so physics
cannot choose between them. With 29.153 fps the frames would be 15 → 40 and the answer 5.94 m (4% lower).

## Measurements (script: measure.py, using scene/tracks/boat.csv)
- I checked the record on 4× zoomed crops at frames 0 and 40. The bow tip and the orange stern marker match the CSV within about 1 px
  (frame 0: stern ≈ 400, bow ≈ 607; frame 40: stern ≈ 977, bow ≈ 1166).
- The camera pans right at about 0.75 px/frame, so I used positions relative to the background (`*_stab` columns).
- Boat point = midpoint of bow and stern. Stabilised Δx from frame 15 to 41 = 381.5 px (Δy ≈ −1.9 px, negligible). A local linear fit
  (±3 frames) at each end gives 381.8 px.
- Boat length in pixels falls from 208 px (frames 0–4) to 190 px (frame 41), probably from slight yaw. I used the clip mean,
  197.8 px, as the single scale: 3.2 / 197.8 = 0.01618 m/px.

## Result
381.5 px × 0.01618 m/px = **6.18 m**.

## Cross-checks
- Bow only: 6.10 m. Stern only: 6.25 m.
- Other choices of length: median 196.7 px gives 6.21 m; the interval-mean length gives 6.28 m; the frame-0 length (208 px) gives 5.87 m.
- File fps (frames 15 → 40): 5.94 m.

Confidence: moderate. The main uncertainty is which frame the annotators used for the pixel length (±3–5%) and the fps choice (4%).
