# Q567 – height of the table lamp (m); prior: black cat speed = 0.94 m/s

fps = question_fps = 24, so no re-timing. The camera is static.

## Scale from the prior (measure.py)
- I took the cat's x-track from scene/tracks/cat.csv and fitted a line over all 50 frames. The slope is 17.8 px/frame for the mask centroid, bbox centre, torso centre and nose (17.76–17.82 px/frame), and the mean per-frame dx is 17.8–18.0 px.
  - Speed = 17.81 × 24 = 427.5 px/s, so the scale at the cat's depth is 0.94 / 427.5 = 2.199e-3 m/px.
  - The cat's y stays constant, so it walks at a fixed depth.

## Lamp pixel height (measure.py, frame 0, from column intensity profiles)
- Top of the finial: y = 512, the first row darker than the wall at x = 1517.
- Base contact with the table top: y = 800, a dark contact line at x 1505–1525.
- Height = 288 px. This matches the scene record (512–800).

## Plain 2D answer
288 × 2.199e-3 = 0.633 m.

## Perspective check (second route)
The lamp stands on the table near the wall, so it is farther from the camera than the cat.
- The camera looks level. The lamp-stem centreline (vert.py) is vertical to within 1 px over 135 px at 555 px off-centre, so the pitch is close to 0 and the horizon is near y ≈ 540 (±50).
- Rows below the horizon: cat paw plane ≈ 1025 (485 px below), table front feet ≈ 995–1003 (≈ 460 px), lamp base at 40 % of the way back across the table top (rows 790–815).
- Depth ratio lamp/cat ≈ 1.07 × 1.05 ≈ 1.09–1.13, depending on where the horizon is. That gives a lamp height ≈ 0.69–0.72 m.

## Answer
The depth correction is real but its size depends on assumptions (horizon, the floor row under the lamp). I answered **0.68 m**: it leans towards the perspective-corrected value and stays close to the plain 2D value of 0.633. Confidence is moderate, with about ±7 % uncertainty.
