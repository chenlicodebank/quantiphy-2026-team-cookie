# q_2463 — distance travelled by the book (cm)

Lab video, 24 fps (file rate = question_fps = 24). f = 0.5959*1280 = 763 px, principal point (640,360).
Book track: scene/tracks/book.csv (mask centroid; checked on the frame at t=1.0 and it matches the book). The book is at rest frames 0-18,
slides down the ramp frames 19-28, tips onto the table frames 28-31, slides on the table, and is at rest from frame 36.

## 3D reconstruction (path.py, path2.py)
- Given depths: frame 24 (t=1.0) 1.0685 m -> P24; frame 29 (t=1.2) 0.977 m -> P29.
- Ramp direction from slope_far (top-edge centre, px (804,360.5), 1.243 m) and slope_near (bottom-edge
  centre, px (659.5,478.5), 0.990 m); ramp length 36.7 cm. Ramp-phase centres = point on the 3D line through
  P24 parallel to the ramp, closest to each pixel ray. Rest depth on the ramp comes out 1.130 m.
- Table phase: fitting a plane to the table corners is ill-conditioned (rays almost parallel to it), so I didn't use it.
  The resting depth comes from (a) book size: length 0.1945 m (132 px at 1.130 m) -> 151 px on the table gives 0.983 m;
  (b) interpolating between ramp-bottom 0.990 m and table-left 1.035 m along the image row gives 1.007 m. Depth is
  interpolated from P29 (0.977 m) to that rest depth.
- Path length = sum of frame-to-frame 3D steps over all frames.

## Results
- Unsmoothed: 39.3-39.8 cm; 3-frame smoothing: 38.2-38.6; 5-frame smoothing: 37.8-38.2. Ramp part ~22 cm
  (straight-line ramp displacement P0->P28 is 22.0 cm), table part ~16.5-17 cm. Net displacement 35 cm.
- Check against the prior: speeds of 0.71 m/s at t=1.0 after 0.21 s of motion give a mean acceleration of ~3.4 m/s²,
  and a quadratic fit over the ramp gives 2.3 m/s². The prior is 2.8 m/s², so the scale is consistent within the noise.
- Answer: 38.3 cm, the middle of the smoothed estimates. Confidence: moderate (about ±7%). The table-phase depth and
  the smoothing convention are the main uncertainties.
