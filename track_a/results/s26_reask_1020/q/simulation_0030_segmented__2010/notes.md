# Q2010 — length of the eagle (m)

Prior: eagle speed 12 m/s (exact). depth_info: r(t=1 s)=106.642 m, r(t=2 s)=111.231 m. question_fps = 24
(file is 25 fps; frames are used as frames, t = frame/24). The bird leaves the frame at frame 37-39, so the t=2 s
depth (frame 48) is only used through the motion model.

## Geometry (measure.py)
- Straight line, constant speed: r(t)^2 = r1^2 + 2 p1·v (t-1) + v^2 (t-1)^2  ->  p1·v = 427.9 m^2,
  radial speed at t=1: 4.01 m/s, transverse 11.31 m/s (motion 70.5 deg from line of sight, sin = 0.942).
- Image track (scene/tracks/bird.csv centroids, uncut frames 0-36, checked): dx/dframe = 15.15-15.4 px/frame
  (linear / quadratic fits over whole wing-beats), y nearly constant.
- Focal = pixel rate / angular rate (r1·v_t / r^2 per frame): 3350-3500 px depending on frame, ~3420 px at
  frame 24 (HFOV ~16 deg). Metres per pixel = r(frame)/f ≈ 0.0304 (f0) … 0.0320 (f36).
- Scale sanity (standard object): wings-up vertical extent 35 px ≈ 1.1 m (half-span ~1 m raised, i.e. wingspan
  ~2 m) — realistic eagle, so scale accepted.

## Length (extent.py, crops.py)
- The eagle is seen in roughly three-quarter side view; its body axis lies mostly along image x. In wings-up
  frames (10-13, wings near vertical, minimal x contribution) the x-extent of the bird is 20-22 px
  (thresholds 20-120 on darkness) -> 0.62-0.67 m projected.
- De-foreshortening: body along travel => /0.959 (at f12) -> 0.66-0.70 m; wings-level frames (x-extent 33-35 px)
  suggest the wing axis is ~33 deg from the line of sight, i.e. body ~57 deg -> /0.84 -> 0.75-0.79 m.
- Answer: 0.73 m (middle of 0.66-0.79). Realistic eagle length (0.7-1.0 m).

## Confidence
Moderate-low: the bird is only ~20-35 px, body length must be separated from flapping wings, and the
foreshortening angle is uncertain (±10 pct).
