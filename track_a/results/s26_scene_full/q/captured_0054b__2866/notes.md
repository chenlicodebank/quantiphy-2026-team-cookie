# q 2866 – orange ball (basketball) displacement 0.5 s → 1.0 s

- File fps = question_fps = 24, so the frames are 12 and 24.
- Orange ball = the scene record's "basketball". I checked its centres on 3x zoomed crops (frames/f12.png, frames/f24.png):
  frame 12 at (716.3, 536.4) and frame 24 at (537.8, 385.9) px. Both match the visible ball to about 1–2 px.
- Lab method card: f = 0.5959·1280 = 762.8 px, principal point (640, 360). Each centre is back-projected along its
  unit ray, scaled by the given Euclidean distance (2.24 m at 0.5 s, 1.81 m at 1.0 s).
  - P12 = (0.217, 0.502, 2.172) m
  - P24 = (-0.240, 0.061, 1.793) m
  - **Displacement = 0.740 m.** If the depth is instead read as z-depth, the result is 0.782 m.
- Prior check: interpolating the depth linearly between the two given values gives per-frame speeds near frame 12 of
  about 1.8 m/s, and 3.7 m/s across the skipped capture at 11→12. A 5-step mean over frames 10–15 is about 2.18 m/s,
  close to the prior of 2.21. So the scale is consistent.
- Second route: the summed per-frame path length from frame 12 to 24 (interpolated depth) is 0.751 m. That is close
  to the straight-line 0.740, as expected for an almost straight roll.
- Caveat: the apparent diameter shrinks from 75 to 63 px while the given distance drops from 2.24 to 1.81 m. The
  implied diameters (0.22 vs 0.15 m) disagree, so the depth_info and the apparent size are inconsistent. I followed
  the given depths, as the reference convention does.
- Confidence: moderate-high for the reference convention (±5%).
