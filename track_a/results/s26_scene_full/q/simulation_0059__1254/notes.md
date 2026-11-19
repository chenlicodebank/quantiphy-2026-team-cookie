# Q1254: height of the walking pedestrian (m). Answer: 1.69 m

File fps = question_fps = 24, so there is no time-base issue. t=0.58 s is frame 14 and t=1.58 s is frame 38.

## Focal length (fit_f2.py)
- The prior is that the white car (the van) accelerates at 4 m/s². It starts from rest.
- I fitted a 3D straight-line, constant-acceleration (4 m/s²) model to the van's sub-pixel side-panel track (`patch_cx`, frames 2-71).
  The fit is constrained by the given van distances: 43.812 m at frame 14 and 43.003 m at frame 38.
  Principal point at the image centre.
- Result: f = 2210 px (hfov ≈ 52°). u-residual rms 0.28 px; the fitted start time is t0 ≈ -0.04 s.
- Varying the reference point on the van (panel +0/26/50 px, different heights) gives f = 2195-2222 px.
  Using the bbox centre instead gives 2163 px with a worse rms of 0.9 px.
- Sanity check: van size = 5.9 m long and 2.1 m tall, which is realistic for a cargo van.

## The pedestrian's feet are never visible
In every frame the garbage-bag pile in the foreground hides the feet. The legs disappear behind the bags at y ≈ 818.
So the record's `feet_y = 815` / height 110 px is **wrong**: that is the edge of the bags, not the soles. I had to reconstruct where the ground is.

## Ground-plane route (vp.py, tyres.py, curb.py, height.py)
- **Horizon:** I found the road-curb lines with a Hough transform on the clean background. Their vanishing point is at (1255, 705), so the horizon is at y = 705 and the camera pitches up 4.3°.
- **Camera height above the road**, from road contacts and the given distances at frame 38:
  - van rear tyre contact at y 801.5, near side taken as about 1 m closer than the van's centre: 1.818 m
  - cyclist rear-wheel contact at y 805.5: 1.818 m
  - The two values agree exactly.
- **Curb (the left sidewalk is raised):** the curb face shows as a band about 13 px tall at around (380, 933). That band is about 17 m away, so the curb is about 0.10 m high.
- **Head top:** at y 706.5 at frame 14 and 707 at frame 38. Using the given distances (30.968 and 29.817 m), it sits 0.023 m below camera height.
- **Height:** H = 1.818 − 0.101 − 0.023 = **1.694 m**. In the image, the feet would be at y ≈ 831, so the full height is ≈ 125 px.
  This is consistent with the feet being hidden below the bag edge at 818.
- **Sensitivity:**

  | change | H |
  |---|---|
  | horizon ±5 px | 1.67-1.72 m |
  | f ±20 px | ±0.015 m |
  | curb 10-16 px | 1.67-1.72 m |
  | van offset ±0.2 m | ±0.005 m |

## Second route (body proportion)
- The face/head measures about 16.5 px from head top to chin (frame 0). Assuming a standard head-to-height ratio of 7.5, the height is about 124 px.
- That matches the 125 px from the ground-plane route.
- Converted directly: the pedestrian is off-axis (cos 0.974), so the z-depth is 30.17 m, and 124 × 30.17 / 2210 = 1.69 m.

## Confidence
Moderate-good, about ±4%. The main uncertainties are the horizon line and the curb height, because the feet are hidden.
