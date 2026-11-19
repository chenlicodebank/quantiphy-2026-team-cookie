# Q2317 – soccer ball diameter (cm)

Lab video, 24 fps (file rate = question_fps), 1280x720. f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
depth_info: soccer ball at 2.80 m from the camera (ball centre).

## Pixel diameter (measure.py, profile.py, overlay.py)
- Mask = |frame - frame with ball elsewhere| (f0 used as background for late frames, f47 for early ones), various thresholds.
- Unblurred near-apex frames f45–47: width 46–47 px at moderate threshold; raw RGB row profiles at f46 give edges at
  x≈526 and ≈570 (44–45 px); the 8x zoom with my own grid (frames/my46.png) shows x 525.6–570.6, y 392–438, so 45 x 46 px.
- Held frames f0–3: height 45–46 px (width is mixed with the hand). In-flight bbox_w in scene/ tracks: 44–48.
- Adopted D_px = 45.5 px (ball near the image centre, so off-axis correction is negligible).

## Size
D = 2.80 m x 45.5 / 762.8 = 0.167 m = **16.7 cm** (range 44–47 px gives 16.2–17.3 cm).

## Second route (gravity_check.py: prior g = 9.8 m/s^2)
- Free fall f30–35, quadratic fit: 2859 px/s^2 -> 3.43 mm/px -> 15.6 cm.
- Rise after the bounce, f41/42–48: 1965–2126 px/s^2 -> 21–23 cm.
- These two disagree with each other: the record notes a dropped/irregular camera frame near f35/36, and the windows are short
  and include motion blur. So the gravity route is only a rough check. Its mean (~19 cm) brackets the depth-based value.
  The depth-based method card is how the reference is made, so I use it.

Confidence: moderate-high (±5%) on the 16.7 cm value given the stated depth.
