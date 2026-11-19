# Q1600 — height of the vase (m)

The file rate and question_fps are both 24. The camera is static, and I assume the principal point is at the image centre (960, 540).

## Focal length (from the cat prior)
- Prior: cat speed 0.94 m/s. Depths: 4.199 m at frame 0 and 4.481 m at frame 24.
- For each candidate focal length f, I back-project the cat's origin proxy at frames 0 and 24 using the given depths. I then solve for the f that makes the distance between the two 3D points 0.94 m (`focal.py`, `focal2.py`).
  - Torso centroid with a quadratic or cubic fit over 50 frames gives f = 2080–2087.
  - Mask centroid gives 2103–2118, and the bbox centre gives 2121–2133. Raw (unfitted) values fall in the same range.
  - **I use f = 2100 px (about ±2%).**

## Bench and table-top plane (`edge.py`, `slab2.py`)
- Leg bottoms in pixels: front-left (FL) (1407.5, 841), back-left (BL) (1329.5, 827), front-right (FR) (1626.5, 823).
- The closest leg, FL, is at 5.69 m, so z = 5.511. That puts the floor at (v − cy)·z = 1659 px·m, which is about 0.79 m below the camera.
- The mirror bottom (6.407 m) gives a floor depth of 0.81 m. That agrees with a nearly level camera.
- Leg positions in 3D: the axis from FL to FR is rotated 27° in depth.
- I fitted a rectangular table top, centred on the leg footprint, to the slab's silhouette edge measured in luminance (rms 0.15 px):
  - K = Y_top·f = 683 px·m, which puts the table top 0.325 m below the camera (table about 0.47 m high).
  - Its rotation came out at 27.8°, which matches the 27° leg axis.
  - A coarser fit gives K = 675.

## Vase
- Silhouette: rim top at v ≈ 469.4, bottom contact at v ≈ 654.3 (column profiles in `vase.py`). That is about 185 px tall.
- Rim width is 36 px (r ≈ 0.05 m) and base width 53 px (r ≈ 0.076 m).
- Front of the base: z = 683 / 114.3 = 5.98 m, so the vase centre is at z ≈ 6.05 m. This is in front of the leaning mirror (bottom z = 6.16), as it should be.
- Height: H = Y_top + (cy − v_top)·z_rimfront / f = 0.325 + 70.6 × 6.00 / 2100 = **0.527 m**.

## Checks
- Simple route (centre depth × pixel height / f): 6.05 × 184.8 / 2100 = 0.532 m.
- With K = 675: 0.520 m.
- With f ranging over 2080–2130: 0.520–0.532 m.

**Answer: 0.527 m**, with an estimated uncertainty of about ±3%. The main uncertainties are which point on the cat is its origin (this sets f) and the 1-px reads on the table-top edge (these set the vase depth).
