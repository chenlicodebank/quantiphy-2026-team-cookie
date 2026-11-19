# Q1757 – average speed of the moving bicycle (m/s)

Clip: 3D segmentation render, 1920x766, 33 fps (file rate = question_fps = 33). Static camera. The cyclist (rider + bike, one
mask) rides toward the camera and leaves through the bottom edge from frame 60; last seen at frame 91.

## Method
- Depth_info gives the bike's camera distance at t=1 s (frame 33, 16.4919 m) and t=2 s (frame 66, 11.9277 m).
  Back-project a bike reference pixel at each time: X = d * unit_ray((u-cx)/f, (v-cy)/f, 1). Displacement over 1 s = |X2 - X1|.
  This mostly depends on Δd = 4.564 m. The lateral part depends on the angle between the rays (≈200 px / f).
- Focal length: walking pedestrian (1.8 m) bbox height is 200 px at depth 11.93 m, so f ≈ 1325 naive, and ≈1380 with
  foreshortening from the camera's downward pitch. Kiosk vanishing points give ≈1130, which is rough. Joint fits (fit.py, fit2.py)
  with ground-plane constancy are poorly conditioned: pitch and cy aren't identified, maybe because the frame is cropped. But every fit gives a 1-s displacement of 4.93–4.96 m.
- Sensitivity (speed.py): with f from 1000 to 1600 and reference points pelvis-estimate, handlebar or saddle, the displacement is 4.84–5.22 m.
  The plausible f = 1250–1400 gives 4.90–5.06.
- Constancy check (const.py): I fitted the image track (frames 0–79) with motion along the 3D line X1→X2, adding a quadratic time term.
  Speed is near-constant (pelvis track: 4.86→4.96 m/s across the clip for cy=200; at most ±5% for cy=383). So the mean of the per-frame speeds
  ≈ the 1-s chord: 4.88–4.91 with f = 1300, and 4.78–5.07 over all f and cy tried.

## Answer
4.95 m/s (estimated uncertainty ±3%). Second route: the per-frame mean speed from the constrained trajectory fit, 4.75–5.07 m/s, agrees.
Note: the bike origin pixel is unknown. The rider pelvis estimate, the handlebars and the saddle all give results within 1–2% of each other.
