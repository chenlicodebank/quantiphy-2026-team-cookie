# q_2177 — basketball diameter (cm)

Lab video, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959*1280 = 762.8 px, principal point (640, 360).
depth_info for the ball: t=0 (frame 0) 1.3210 m; t=1.8 (frame 43) 1.5835 m; t=1.92 (frame 46, apex) 1.5795 m.

## Pixel diameter (fit2.py)
The background was blurred by SAM2, so there is a ~16 px halo of blurred ball colour outside a sharp mask edge. The mask edge
sits inside the true silhouette. I put the edge at the half level of (R-G) between the background and the ball plateau
(80th percentile, so seams are excluded), sampled on rays every 4 deg, and then fitted a circle with outlier rejection.
On frames 0-25 only the upper half is used because the hands cover the lower half.
- frame 0: D = 142.7 px (frames 0-25 give 140.4-142.7). The record's threshold mask gives 145.3, which is slightly outside the half level.
- frame 43: D = 105.1 px (record 108). frame 46: D = 108.9 px (record 112). Horizontal-only widths agree within about 1 px.

## Size = d * D_px / f (lab method card)
- t=0:    1.3210 * 142.7 / 762.8 = 24.7 cm
- t=1.8:  1.5835 * 105.1 / 762.8 = 21.8 cm
- t=1.92: 1.5795 * 108.9 / 762.8 = 22.6 cm
Mean = 23.0 cm. With the record's pixel diameters: 25.2 / 22.4 / 23.2 cm (mean 23.6).
Off-axis correction (the sphere's image is enlarged by about 1/cos(theta)) would lower these by 3-7 %: 23.1 / 20.9 / 21.7 cm.

## Consistency / second route
- The depths and the image sizes do not agree perfectly. Between frames 43 and 46 the size grows by 3.6 % while the given depth
  changes by only 0.25 %. So depth_info carries a few percent of noise, and frame 0 gives a value about 9 % above the rebound frames.
  I averaged the three stated times.
- Gravity check: the 3D track uses Z from apparent size, and the rise covers frames 38-48. It gives D ≈ 29-32 cm, but it is very
  sensitive to the pixel-size noise in Z, so it is not reliable. A drop-height check (release frame 28 to bounce frame 37, with or
  without the suspected dropped frame) gives 19-23 cm, which is also highly sensitive to timing. Neither is used. Both are only loosely
  compatible with ~22-24 cm.
- Sanity: basketball sizes 5/6/7 are 22/23/24.3 cm. 23 cm sits in the middle of these.

Answer: 23.0 cm. Confidence moderate (about ±6 %), because the three depth readings disagree.
