# q1292 – average speed of the bicycle (whole clip)

File fps = question_fps = 24. Depth times t=0.58 s -> f14, t=1.58 s -> f38.
White car = the white van in scene/ (starts from rest, constant acceleration); bike = cyclist.

Tracks from scene/tracks (van.csv, cyclist.csv) checked in fit.py:
- Van: quadratic fit of ref_x over frames 2-71 / 22-71 / 36-71 -> a = 307.2-307.5 px/s^2 (resid ~0.5 px). Constant image size and y -> moves parallel to the image plane at constant Z.
- Cyclist: linear fit -> 427.4 px/s (17.81 px/frame), no acceleration (quadratic term ~0), constant y and size -> constant Z.

Focal length from the van's two depths (30.065 m at f14, 29.307 m at f38) with constant Z, principal point (1080,540):
f = 2256 px, Z_van = 29.17 m. Check against prior: 307.4 px/s^2 x 29.17/2256 = 3.97 m/s^2 (prior 4) -> consistent within 1%.
Bike depth with f=2256: Z_bike = 27.04 / 26.95 m -> 27.0 m.

Route 1 (geometric f): v = 427.4 x 27.0 / 2256 = 5.12 m/s.
Route 2 (prior scale ratio): v = 427.4 x 4 x 27.0 / (307.4 x 29.17) = 5.15 m/s.

Note: frames 0 and 1 are identical (duplicate first frame). Counting the zero step f0->f1 in the mean of per-frame
speeds would give 70/71 of that = 5.05 m/s. Answer 5.12 m/s (steady riding speed; ±1.5%).
Confidence: high.
