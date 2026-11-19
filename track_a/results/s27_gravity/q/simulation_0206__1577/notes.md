# q1577: width of the typewriter (m) -> 0.29

Clip: 3D Blender render, 2124x1080, 24 fps (question_fps = 24, same as the file). Prior: free fall at 9.8 m/s^2 before 0.45 s.
depth_info: typewriter 4.32 m at t=0, 4.501 m at t=0.5 (frame 12, just after landing; same pixel point as the rest pose).

## Camera (fit_fall.py, fit_fall2.py)
- Model: origin P(t) = 4.32*ray(u0,v0) + 0.5*9.8*t^2*D, where D = world-down in camera coordinates (pitch theta, small roll),
  starting from rest at frame 0 (the scene track shows v0 ~ 0). I fit f, theta, roll, u0, v0 and the landing time to the bbox-centre
  track for frames 2-9 (scene/tracks, checked), with the constraint that the trajectory reaches the 3D point
  4.501*ray(frame-12 ref) when it lands.
- Result: f = 2807 px (2779-2811 across frame subsets and +-10 px on the landing point), pitch 15.8-16.1 deg down,
  landing at frame 10.2 (matches the record: still in the air at f10, on the desk at f11), pixel rms 2 px.
  Without the depth constraint, the fit is ill-conditioned in pitch, but f still comes out at 2730-2880.
- Checks: the revolver (depth 4.704) and the desk corners (3.593 / 5.009) put the desk top at 1.38-1.47 m below the camera
  along the vertical. The typewriter footprint gives 1.40, which is consistent. Revolver ~0.26 m and clock ~0.14 m are plausible sizes.

## Width (footprint.py, boxfit.py)
- Width = shorter horizontal extent = the typewriter's front-to-back depth (its length is the left-right extent, ~0.45 m
  including the carriage knobs: 291 px at ~4.33 m during the fall).
- At rest (frame 29), the typewriter is yawed so that its left side panel is visible. Its bottom corners, read on enhanced zooms, are:
  back-left (1098,664), front-left (1252,696), front-right (1365,638). I back-projected them onto the desk plane. The plane height
  was chosen so that the centre of the footprint lies under the origin (4.501 m), which gives 1.399 m (consistent with the desk/revolver checks above).
  - Side (front-to-back) = 0.281 m, front edge = 0.354 m, and the corner angle is 91 deg. A 90 deg corner is a self-check of f and pitch:
    a pitch of 12 deg would give 80 deg.
  - With the plane height in the 1.40-1.46 range: side 0.281-0.293 m.
- 3D box fit to the rest silhouette (convex hull, IoU 0.85): front-to-back extent 0.288 m.
- Above the back of the base, the carriage and paper table end only ~3-5 px further back (nearly vertical silhouette edge at x~1095),
  which adds ~0.01 m.
- Final: 0.29 m (range 0.28-0.30).

## Caveats
- If the reference uses a world-axis AABB of the yawed resting pose rather than the object's own front-to-back depth, the value
  could differ (it is unknown how the world axes are aligned with the camera). In the first frames the typewriter faces the camera almost squarely.
- Confidence: moderate. The geometry is self-consistent (90 deg footprint corner, desk height matches the other depths).
