# q_954 — height of the phoenix (m)

Prior: phoenix acceleration at 2.0 s = 2 m/s². 2D clip, static camera, fps 24 (= question_fps, so no re-timing).

## Scale from the prior (fit.py)
The bird flies left at roughly constant acceleration, starting from rest at frame ~0 (the quadratic fit puts the vertex at frame -1 to +1).
Quadratic fits of x(frame) to several reference points (frames 0-71 / 2-71):
body_s_x 279-282, body_x 282-286, centroid_x 283-284, bbox_x0 283-288, bbox_cx 280-282 px/s².
Second difference over one wingbeat period (25 frames), so that the flapping cancels: body_s_x 281, centroid_x 286, bbox_x0 282 px/s².
The cubic fits show the acceleration stays about the same through the clip (~275-305 near frame 48).
Adopted value: a_px = 284 px/s² (±1.5 %), giving a scale of 2 / 284 = 0.00704 m/px.

## Height
Vertical extent of the mask bbox, re-measured in code (height.py) and checked on an overlay image (frames/chk_0.png):
frame 0 = 404 px (y 372-775), wings down (f12/f37) = 462-463 px, wings level (f71) = 252 px. Mean over the clip = 390 px, median = 412 px.
Answer reading: the AABB at frame 0, which is also close to the clip mean and median: 404 × 0.00704 = **2.85 m**.
Other readings: mean over the clip 2.74 m, maximum (wings down) 3.26 m, minimum (wings level) 1.77 m.

## Check / confidence
The independent reference points and both methods (global quadratic, period second difference) agree on the scale to within about ±2 %.
The main uncertainty is which frame or pose the reference height uses, because the flapping changes the height by up to ±15 % around the frame-0 value.
