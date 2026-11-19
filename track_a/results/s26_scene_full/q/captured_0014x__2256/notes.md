# q_2256 – ball diameter (cm), captured_0014x (lab, 24 fps file = question_fps 24)

Method (lab card): D = depth x pixel diameter / f, f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
The acceleration prior gives no size; the scale comes from depth_info (ball 1.8180 m at t=0, 1.7288 m at t=0.6).

## Pixel diameter (code: profiles.py, measure.py, crops.py)
Horizontal width, measured at half-max between the local background and the ball interior on rows near the
centre (vertical motion blur does not stretch the horizontal width):
- frames 12-16 (rolling on the white board, clean edges): 27.6, 27.4, 27.2, 27.0, 27.1 px.
- frame 14 (t=0.6 -> frame round(14.4) = 14), depth 1.7288 m: 27.2 px -> **6.16 cm** (30%-threshold mask: 27.7 px -> 6.28 cm).
- depth per frame from the 3D slope line through the t=0 and t=0.6 centres (route2.py): frame 12 1.766 m -> 6.39 cm,
  frame 16 1.681 m -> 5.97 cm (the small downward trend probably comes from motion blur growing with speed).
- frames 0-6 (at rest, t=0, 1.818 m): 26.5-28.3 px (median about 27.4) -> 6.5 cm. Here the ball sits against the
  segmentation-replaced background, which leaves a dark fringe; frames 7-10 measure 29.5-31 px because of that fringe
  (-> 7.0 cm, rejected as inflated).

## Second route (route2b.py)
Ball on the wooden table at frame 22: half-max width about 30.5 px (rows 454-458). Its depth comes from intersecting
the ray with the table plane through the bottom of the slope: 1.49-1.58 m for camera pitch 25-45 deg -> 5.9-6.3 cm.
This agrees with the frame 14 value.

## Answer
6.3 cm: the frame-14 value (6.2-6.3), weighted slightly toward the slow, less blurred frames (6.4-6.5).
Confidence: moderate, about ±6%. The ball is only about 27 px wide, so ±1 px in the edge is ±3.7%.
