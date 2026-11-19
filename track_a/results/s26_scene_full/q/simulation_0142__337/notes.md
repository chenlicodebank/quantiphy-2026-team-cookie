# Q337: floor tile side length (m). Prior: walking speed = 1.693 m/s

fps = question_fps = 24, so no re-timing. The camera is static and the man walks parallel to the image plane at constant depth.

## Method
1. Median background (`bg.py`). Square floor tiles in one-point perspective.
2. `vpfit.py`: I searched for the vanishing point that makes the longitudinal joints sharpest when projected onto
   u = (x - xv)/(y - yv). Result: VP = (960, 540), the image centre, so the camera axis is horizontal.
   The joints are equally spaced in u: du = 0.4457 (six intervals, 0.4448–0.4469). The joint spacing at image row y
   is therefore 0.4457·(y − 540) px.
3. Depth row of the man (`feet.py`): planted near-foot soles are at y = 904 and planted far-foot soles at y = 898.
   The pelvis (origin) is between them, at y ≈ 901, where the tile spacing is 160.9 px.
4. Pixel speed (`speed.py`): the pelvis track averages 18.78 px/frame (head over whole gait cycles 18.82–18.87).
   Near-foot plants repeat every 471.3 px per 25 frames (18.85 px/frame); far-foot plants repeat every 465 px
   (18.60 px/frame). The near/far ratio matches the perspective ratio 364/358.
5. T = tile_px / speed_px_per_frame × 1.693 / 24.

## Results
- Pelvis track at row 901: 0.604 m
- Near foot at row 904: 0.607 m
- Far foot at row 898: 0.605 m
- Mean of both feet at row 901: 0.606 m

Answer: **0.605 m**.

The routes agree to within ±0.3 %. Sanity check: the man is 492 px tall at the 0.00376 m/px scale, which gives
about 1.85 m. The tile is about 0.6 m, a common tile size. Confidence: high (about ±2 %).
