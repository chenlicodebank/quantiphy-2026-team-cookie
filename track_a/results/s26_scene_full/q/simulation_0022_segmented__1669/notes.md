# q_1669 — height of the boat (prior: length = 10 m)

The file runs at 25 fps and the question at 24 fps. No timing is needed: this is a size ratio.

## Method
- The boat is seen almost broadside, about 148 m away. That makes the field of view narrow (f ≈ 4300 px), so
  perspective across the boat is small. Height / length = its pixel height / its pixel width.
- `measure.py` builds a foreground mask (255 − min(RGB) > 12), removes the island (frame-0 mask, unless the
  pixel changed), and keeps the components on the boat. It takes the full bbox (bow tip to stern/rudder, antenna
  top to rudder bottom) in frames 35–74, where the boat is fully in view. The overlay (frames/ov_60.png) shows the
  mask covering the whole boat.
- Pixel width 286–296 (median 291) and height 281–296 (median 289). Per-frame h/w: median 0.990,
  mean 0.990 ± 0.011.
- Height = 0.990 × 10 m ≈ **9.9 m**.

## Checks
- Geometry from depth_info: with f = 290 px × 147 m / 10 m ≈ 4260 px, the origin moves about 3.9 m/s to the
  left. Lateral motion alone reproduces only about 0.24 m/s of the 1.77 m/s drop in distance, so the boat also
  approaches at about 1.5 m/s. That fits the small apparent growth (+2.4 % in width from f36 to f72).
  - If the boat is yawed about 21° along its path, its projected width is L·cosθ + (W/2)·sinθ ≈ 9.34 + 0.65 ≈ 10.0 m.
    So yaw barely changes the width scale.
  - The vertical extent runs from the antenna top to the rudder bottom, both on the centreline. Camera elevation
    therefore only enters as cos φ (≈ 1).
- Other frame windows: frames 35–47 give ratio ≈ 0.983, 48–59 ≈ 1.005, 60–74 ≈ 0.985. All are within ±2 %.

## Confidence
Good: ±3 %. The faint antenna tip and rudder edge carry ±2–3 px.
