# q1253: average speed of the walking pedestrian over the whole clip (m/s)

Video: 3D Blender scene, 2160x1080, 24 fps (file fps = question_fps = 24), 72 frames. Static camera.
Prior: the white car (the cargo van) accelerates at 4 m/s^2. depth_info gives camera distances at t=0.58 s (f14) and t=1.58 s (f38).

## Focal length (focal.py, focal_check.py)
- Van origin = bbox centre (patch_cx + 26 px, row 745.5). 3D points at f14 and f38 come from depths 43.812 and 43.003 m. Every frame's
  position is the point on that straight line closest to its pixel ray. Speeds use a 1-frame difference. f is chosen so that the
  linear fit of speed against time has slope 4 m/s^2.
  -> f = 2199-2216 px (patch track, different windows); 2136-2173 px (bbox cx). Taken as f ~ 2200 px (HFOV ~52 deg).
- Check: the cyclist's 3D path (from its two depths) is parallel to the van's path at f ~ 2420 px. That is an independent and
  noisier value, used as the upper bound of the f range.

## Pedestrian (ped2.py, scale_track.py, final.py)
- Pelvis 3D points at f14 (u 609, v 776) and f38 come from the depths 30.968 / 29.817 m, with the pelvis kept at a constant height
  (camera horizon at row 702). The pedestrian walks almost straight toward the camera, slightly to the left
  (direction x,z = -0.14, -0.99). |P38 - P14| = 1.23 m in 1 s.
- Every frame: the point on that horizontal line whose image column equals the tracked body-axis column. The track is the record's
  u for f0-22 (eye readings) and the template track for f23+, re-measured with my own multi-scale NCC (agrees within ~0.5 px),
  then Savitzky-Golay smoothed (9, 2).
- Check of the straight-line model against depth: the multi-scale NCC body scale at f66-71 relative to f38 is ~1.043, which gives
  D ~ 28.6 m. The line model gives 28.6 m at f68.5, so they agree. Scale estimates before f22 fail because the van and taxi
  pass behind the pedestrian.
- On zoomed frames the pedestrian stands with legs together at f0 and is in full stride by f8. They start from rest, so the clip
  average is below the steady walking speed.
- Mean of the per-frame speeds over f1..71: 0.990 m/s (f = 2200). The motion is monotonic, so this equals net/time.
  Range over f 2000-2420 and both u tracks: 0.981-1.006. The steady walking speed over f24-71 is ~1.07 m/s, and 1.23 m/s over f14-38.
- Frame 1 duplicates frame 0. Leaving out its zero speed gives 1.002.

Answer: 0.99 m/s. Confidence moderate: the early-phase u comes from eye readings, and how the reference averages the walk-start phase is uncertain.
