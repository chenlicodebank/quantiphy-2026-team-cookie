# Q326: speed of the cup at t = 1 s (m/s)

Prior: cup diameter = 0.087 m. No depth_info. The file's fps and question_fps are both 24, so t = 1 s is frame 24, and the speed is the backward difference over frames 23 to 24.

## Geometry (what the scene record missed)
- The cup is a tapered tumbler lying on its side. Its closed **base** (a flat, strongly saturated navy disc with S≈200 against S≈90 on the body)
  faces the camera, and the wider **rim** end points away from it.
- The "rotation" in the record is **perspective only**. The cup slides along +x with its axis parallel to the camera's z axis:
  - The rim-top x is linear in the base-centre x (frames 12-31: slope 0.919, rms 1.4 px), and the two coincide at x = 957 ≈ image centre. So the
    cup is exactly end-on at the image centre and turns only apparently.
  - The silhouette top stays at y = 830 and the base bottom at y = 995 in every frame, so the depth is constant.
  - The base disc keeps the same size, about 97 x 95 px.
- Vanishing point: the cooktop's left edge and the toaster base's right side meet at (956, 560). So the camera is level and the principal point x ≈ 960.
- Slope 0.919 = z_base / z_rim. Cross-check: the ground-plane geometry (horizon at 560, base bottom at 995, rim top at 830, rim width) needs ≈ 0.91.

## Scale
- Rim diameter = the widest silhouette row near the rim, measured at sub-pixel level in the end-on frames 17-21: 128-130 px, taken as 128.5 px (`rimw.py`).
  The rim plane is nearly parallel to the image, so this holds at rim depth: 128.5 / 0.087 = 1477 px/m.
- At base depth: 1477 / 0.919 = 1607 px/m. This implies a base diameter of 0.060 m, which is plausible.
- The cup only translates (no yaw, constant depth). Every point therefore moves the same world distance, and each point is converted with the scale at its own depth.

## Speed at frame 24
| Route | Raw diff 23→24 (px) | m/s | Cubic fit over frames 18-30 (px) | m/s |
|---|---|---|---|---|
| Rim top x, rim scale (does not depend on k) | 34.13 | 0.5546 | 34.18 | 0.5555 |
| Base disc centre, base scale | 37.41 | 0.5587 | 36.72 | 0.5483 |

**Answer: 0.555 m/s.** The cup is slowing down at about 2 px/frame²; this is the backward difference at frame 24.

Confidence: good. The two independent routes agree within 1-2%. The main uncertainty is the rim pixel width (±1.5%).
Scripts: `disc2.py` (base disc), `rim.py` (silhouette top), `fitk.py` (depth ratio), `rimw.py` (rim width), `speed.py`.
