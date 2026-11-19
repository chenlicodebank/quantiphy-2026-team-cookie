# q_2873 – speed of the white ball at t = 1.0 s (frame 24)

Lab video, 24 fps (the file rate and question_fps are the same), 1280x720. f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
Given: the white ball is 1.235 m from the camera at t = 1.0 s. The prior: orange ball speed 2.21 m/s at t = 0.5 s, distance 2.24 m.

## Track
- `scene/tracks/white_ball.csv` checked on zoomed frames 22–26: the centres are correct (within about 2 px).
- `seg.py` re-segments the white ball in frames 21–46 (background difference + low saturation + bright). It gives the hull
  centroid and the mask width across the motion direction (the diameter under motion blur). Masks are in frames/seg_*.png.
  The frame 24 and 26 masks leak a little. Frame 26 width corrected by eye to 36 px.
- One capture is skipped between frames 35 and 36 (see the scene notes). The fits use real time for frames 36 and later.

## Prior check (`vel.py`)
- Basketball depth from its apparent size, with a linear 1/width fit, calibrated to 2.24 m at frame 12.
- 3D central 5-frame difference at frame 12: 2.24 m/s. Mean of the per-frame speeds over frames 10–14: 2.17 m/s.
  Prior: 2.21. So "3D velocity, smoothed over about 5 frames around t" reproduces the prior.
- The orange-ball distance at t = 1.0 s (1.81 m) does not fit its apparent size: 62 px would mean about 2.6 m.
  That value was not used.

## White ball velocity
1. Route A (`vel.py`): depth from the blurred width, then a linear trend.
   - Lateral-only speed at a fixed 1.235 m, central 5 frames: 1.71 m/s.
   - Adding the depth rate from the width trend gives 1.94–2.31 m/s.
   - This route is unreliable: the widths are flat (about 38–40 px) over frames 21–25 and only drop after frame 26.
     A linear fit forces a steep depth rate at frame 24.
2. Route B (`proj.py`, `proj3.py`): 3D projectile fit to the pixel track, frames 21–35 (or 37).
   - The free gravity direction comes out as camera (-0.15, 0.66, 0.73), a camera pitched about 45° down.
   - This agrees with the vanishing point of the vertical wall lines, at about (367, 1157) → (-0.24, 0.70, 0.67).
   - The ball diameter implied along the fitted path is consistent, about 5.4–6.8 cm, also at the bounce (about 2.6 m, 17 px).
   - The ball is near its highest point at frame 24, and its distance to the camera is near its minimum. So the depth
     rate is small there, which agrees with the flat widths.
   - With the frame-24 point fixed at 1.235 m: |V| = 1.74 (g free) and 1.77–1.78 (g = 9.81).
   - Mean of the per-frame forward speeds over frames 22–26: 1.76–1.82.

## Answer
1.77 m/s. Confidence: moderate. The lateral component (about 1.71) is solid. The depth component adds about 3–5 %.
If the reference depth readings were noisy, the reference value may be higher, about 1.9–2.0.
