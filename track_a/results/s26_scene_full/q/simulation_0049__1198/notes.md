# q1198 – height of the walking person (simulation_0049)

Answer: **1.93 m**. File fps and question_fps are both 33, so t = 1 s is frame 33 and t = 2 s is frame 66.

## Key finding: the human depth_info does not match where the mesh is
The pedestrian's feet (y ≈ 771 at f33) are lower in the image than the bike's tyre contact (y ≈ 759 at f33).
The bike is at 14.1 m. Both stand on near-level ground, so the person's mesh must be closer than the bike, at about
12–13 m, and not at the 19.04 m given. This holds for any focal length. So the human "origin" used for depth_info
sits about 6 m from the mesh.

Its *change* in distance, 1.23 m/s, does match the mesh's speed (see route B). The size answer uses the mesh
geometry, not the 19 m value. If you took 19.04 m at face value you would get about 2.9 m, which conflicts with the
ground geometry.

## Focal length (manhole circle), manhole.py / manhole2.py / fcircle.py
- I fitted ellipses to the manhole on the road (centre 685.6, 840.3) using sub-pixel mid-level iso-contours:
  - inner dark cover: axis ratio 0.153–0.156
  - outer ring: 0.163–0.166
- I then projected a ground circle exactly (camera level, principal point (960, 537)):
  - ratio 0.154 → f = 1930
  - ratio 0.159 → f = 1870
  - ratio 0.164 → f = 1810
- **f = 1870 ± 60 px.**
- Vanishing point: the bike's ground track and the right curb line meet at (960.6, 534), so the camera is level and
  looking straight down the road.
- Check from the bike: with a speed of 4.87 m/s and depths of 14.1134 / 18.9543 m, the origin's offset from the
  motion axis is 1.6–1.9 m. At f ≈ 1870 that matches the bike origin sitting on the ground, at the tyre-contact
  pixel (≈240 px from the vanishing point). This is consistent with the manhole result.

## Ground plane from the bike (geom.py)
- I fitted the tyre-contact y over all 99 frames to y = y_h + fH / (Z(t) − δ). Here Z(t) is linear and constrained
  by the two bike depths (origin on the ground).
- Result: y_h = 537.5, fH = 2944–2958 px·m, δ = 0.67 m (rear contact in front of the origin), v_z = 4.866 m/s,
  rms 0.77 px.
- Camera height H = fH / f = 1.58 m.

## Pedestrian (scene keyframes, every 7 frames, spot-checked)
- I checked head top and lowest shoe on 4× crops at f30–39 (head ≈ 483–484, shoe ≈ 770–771). They agree with the
  record.
- **Route A (ground plane):** height = h_px · (H − s) / (y_feet − y_h), where s is the sidewalk (curb) height.
  - s = 0 → 1.933 (mean over 15 keyframes; mid-stance peaks 1.955)
  - s = 0.05 → 1.87
  - s = 0.10 → 1.81
- **Route B (no ground plane needed):** fit 1/h_px as linear in t, with the mesh moving away at Δd = 1.23 m/s from
  depth_info.
  - Z33 = 12.64 m, height = 1.937 m at f = 1870.
  - The same fit on the feet gives H − s = 1.594 m, against H = 1.582 m from the bike. So s ≈ 0: the two routes
    agree only if the sidewalk is nearly flush with the road.
- Curb face in the image: 1–3 px wide where it is about 50–80 px from the vanishing point, so s ≲ 0.05 m. This is
  consistent with s ≈ 0.

## Result and confidence
- Height ≈ 1.93 m (routes A and B agree at s ≈ 0). The bbox height while walking is about 1.91–1.96 across the gait.
- Uncertainty:
  - f: ±3 %
  - curb height: up to −3 % if s = 0.05
  - Overall about ±5 %.
- The answer would be wrong if the reference used the 19 m human depth literally; that would give about 2.9 m.
