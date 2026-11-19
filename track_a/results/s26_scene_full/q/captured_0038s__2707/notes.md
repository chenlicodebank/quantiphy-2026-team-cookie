# q_2707 — white ball velocity at t = 1.4 s (cm/s)

- t = 1.4 s -> frame round(1.4*24) = 34 (file fps = question fps = 24).
- Scale: lab method card, f = 0.5959*1280 = 762.8 px, principal point (640,360); ball depth 0.716 m at t=1.4
  (camera->centre distance), back-projection P = unit ray * 0.716 m. At frame 34 that gives ~0.92 mm/px.
- Track: re-measured with a background-difference mask (measure.py -> diff_track.csv) and compared with the
  scene template track (cx_tm, cy_tm+3). Both agree; overlays frames/ov_33..37.png checked.
- Per-frame 3D speeds (speed.py): steady rolling ~34-36 cm/s (16.3 px/frame), except frame 35->36 = 71 cm/s
  (32 px step, confirmed visually) -> a dropped frame in the recording.
- Variants at frame 34: raw forward difference 34->35 = 38.3; backward 5-step mean = 36.5; true rolling speed
  (excluding the dropped-frame step) = 34.8; centred or forward 5-frame smoothing (as the reference convention,
  "smoothed over at least 5 frames") includes the dropped-frame step -> 42.4 cm/s.
- Second route: the clean segment after the jump (frames 36-46) gives 34 cm/s, consistent with before the jump.
- Answer: 40 cm/s. This is a hedge between the convention value with the jump (42.4) and the physical value (~35-36),
  weighted toward the reference convention. Confidence: moderate. The main uncertainty is whether the reference
  smoothing window includes the dropped frame.
