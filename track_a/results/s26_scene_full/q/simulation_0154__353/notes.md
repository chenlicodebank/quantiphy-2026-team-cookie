# q353 — length of the shark (prior: shark speed = 7 m/s)

2D scene with a static camera. The shark swims horizontally at constant apparent size, so one metres-per-pixel scale applies. The video rate is 24 fps (question_fps is also 24).

## Pixel speed
- **Head/gill patch** (`speed.py`, consecutive-frame template matching): speed rises from 57.5 to 61.3 px/frame over frames 6–34. Mean about 60.
- **Dorsal-fin patch** (`speed2.py`, frames 16–34): steady at 58.9 px/frame.
- **Rear and tail patches**: 56–60 px/frame. The body undulates, so each patch differs a little.
- **Long-baseline averages from the scene track:**
  - snout, f8→f30: 58.95 px/frame
  - tail tip, f15→f46: 58.42 px/frame
- **Adopted:** 59.0 px/frame = 1416 px/s (about ±1.5%).
- **Scale:** 7 / 1416 = 0.004944 m/px.

## Pixel length
- **Full length**, snout tip to tail tip, frames 15–30: median 915.5 px (scene record, checked on frame 18).
- **The faint snout cap** (about x 780–840 at f18) is real snout geometry with a faded render. It is included because the world bounding box includes it.

## Answer
- 915.5 px × 0.004944 = **4.53 m**.
- **Alternatives:** the opaque length only (about 880 px) gives 4.35 m. Speed bounds of 58.4–60 px/frame give 4.45–4.57 m.
- **Confidence:** moderate-high, within about 3%.
