# Q1417: rear (main) landing-gear wheel diameter. Answer: 1.49 m

The file is 24 fps and question_fps is 24, so t = 0.5 s is frame 12 and t = 1.0 s is frame 24. The camera is static.

## Scale (focal length) from the prior and depth_info
- Speed 153.582 m/s, so the plane moves 76.79 m in 12 frames (frame 12 to frame 24).
- Nose distances: 284.98 m at frame 12 and 305.627 m at frame 24.
- I back-projected the image points with the principal point at the image centre and solved |P24 − P12| = 76.79 m for f (`focal.py`, `solve.py`):
  - Using the nose tip (1080,142) → (389,162): f = 2691 px (HFOV 39.3°).
  - Using the mask centroid (in case depth_info really refers to the origin): f = 2790 px.
- Check: a constant-velocity 3D line projected back into the image matches the observed x track over frames 10–30 to within a few px (noisier at the nose tip because the nose glazing is translucent).

## Wheel pixel size (`wheels.py`, `wheels2.py`, overlays in frames/wheel*.png)
- The main gear shows two wheels (left and right gear, separated by parallax). They overlap up to frame 21 and are separate from frame 22 on.
- The tyre mask is the darkness relative to the empty sky in frame 39, upsampled ×8 and thresholded at half the peak darkness. I fitted an ellipse to each blob.
- The major axis is 13.5–14.1 px over frames 22–26, about 13.8 px. That is the diameter, because the minor axis is foreshortened by the oblique view.
- The wheels show no motion blur (they stay round).

## Wheel depth and size
- The wheel follows the nose's 3D path, offset about 3.5 m below it. Its 3D point is the point on the wheel's ray closest to the nose's 3D line, giving z ≈ 290–294 m (nose-f route).
- D = z × px / f:
  - Nose-based f: 1.495, 1.507, 1.486, 1.503, 1.521 m (frames 22–26).
  - Centroid-based f: 1.480, 1.494, 1.475, 1.495, 1.514 m (frames 22–26).
- The two routes agree within 1%. Answer: **1.49 m**.

## Confidence
The main uncertainty is the pixel diameter. The threshold choice gives ±0.5 px, or about ±4%. The nose point and focal length add about 2%. Real CRJ-type main wheels are about 1.0 m, but this render is not at real-world scale: the plane also measures about 46 m long here, against about 36 m in reality.
