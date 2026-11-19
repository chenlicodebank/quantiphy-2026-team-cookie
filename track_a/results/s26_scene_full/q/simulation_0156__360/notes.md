# Q360 – length of the turtle (m); prior: shark speed = 7 m/s

The clip is a 2D underwater scene with a static camera, rendered at 24 fps (question_fps is also 24). Both animals swim leftward and are seen side-on. I used one metres-per-pixel scale, taken from the shark's speed.

## Shark pixel speed (from scene/tracks/shark.csv, checked against the frames)
- Mask centroid, frames 14–30 (shark fully in frame): (1404.6 − 477.0)/16 = 58.0 px/frame
- Nose x0, frames 0–13: (1781 − 1031)/13 = 57.7 px/frame
- Tail tip x1, frames 14–45: (1887 − 119)/31 = 57.0 px/frame
- I used 57.7 px/frame = 1385 px/s, so the scale is 7/1385 = 0.00505 m/px (the routes give ±1 %).

## Turtle length
Zoomed crops (crops.py → frames/t16, t38, t42, t45, t47) show that the turtle is side-on the whole clip. Only the
front flippers stroke, which changes the horizontal extent.
- The carapace alone is about 280 px in both frame 16 and frame 42.
- Head/front flipper to rear-flipper tip: frame 42 is about 905→1208 = 303 px, frame 45 about 835→1143 = 308 px, and frame 38 about 990→1293 = 303 px.
- Mask bbox_w for frames 36–47 ranges from 299 to 340 px, with a median of about 312 px. The higher values come from a flipper pointing forward.
- I took a length of about 305–310 px, which gives 0.00505 × 307 ≈ 1.55 m. The plausible range is 1.52–1.60 m.

## Checks
- Shark length: 911 px × 0.00505 = 4.6 m, which is plausible for a great white.
- Turtle speed: about 21 px/frame, which is about 2.5 m/s.
- A 1.55 m turtle is plausible for a leatherback.

Confidence: moderate-high. The main uncertainty is whether the reference length includes the flippers (±5 %).
