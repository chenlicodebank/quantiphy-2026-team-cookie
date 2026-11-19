# Q55 – length of the turning yellow car (prior: white car length = 6 m)

- I identified the objects on the frames. The "turning yellow car" is the tan/peach sedan that turns right into the horizontal road (`tan_car` in scene/). The "white car" is the white van (`white_van`).
- The video is a 2D top-down scene with a static camera. Both vehicles move on the same ground plane, so the answer is the pixel-length ratio × 6 m.
- fps: the file and the question both give 24, so no re-timing is involved. Time does not matter for a size question anyway.

## Main route (body.py)
- I built a median background over the whole clip.
- Each frame's body mask keeps pixels that are brighter than the background or whose chroma changed. Shadows only darken the grey asphalt, so this excludes them. I then applied an open/close, kept the largest component, and took the min-area rect.
- I checked the overlays visually: `frames/mask_white_van_36.png` and `frames/mask_tan_car_30.png` hug the body outlines.
- Results over all 72 frames:
  - Van length: median 235 px at thr 20 and 234 px at thr 30, spread ±1.5 px. It is stable along its whole path.
  - Tan car length: median 221.3 px at thr 20 and 216.6 px at thr 30. It is stable through the turn.
  - Length ratio: 0.926–0.942, so the car is 5.55–5.65 m long.

## Second route (measure.py, edges.py, scene/vehicle_sizes.json)
- The record's thr-25 body extents give a van of 233–236 px and a tan car of 218.5–219 px. The ratio is 0.93, so 5.57–5.63 m.
- The along-axis edge profiles relative to an empty frame give 0.89–0.91, about 5.4–5.5 m. These are slightly low because they include the van's soft shadow and its end faces, which perspective shows near the image edges (van length 242–247 px at f0/f71 against 231–233 px near the centre).

## Answer
5.6 m (ratio ≈ 0.933 × 6 m). Confidence is good, about ±3%.
