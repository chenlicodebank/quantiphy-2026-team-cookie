# q_2850: velocity of the white ball at 1.0 s (frame 24)

File fps = question_fps = 24, so t = 1.0 s is frame 24.

## Object
"White ball" = the small whitish-grey ball (scene/ calls it `grey_ball`), thrown by the standing person.
It leaves the hand at frame 23. At frame 24 it is free at (569, 271), about 17 px across.
- Its depth_info distance (3.0735 m) fits a small ball of about 0.065 m at 17 px. It also matches the "green"
  (yellow-green tennis) ball, 3.039 m, still in the thrower's hand.
- The soccer ball (white with black patches, ~68 px) would come out 0.27 m in diameter at 3.07 m, which is
  impossible. So it is not the asked object.

## Measurements (measure.py, fit*.py, sizevz.py)
- Centroid and minor-axis diameter of the mask, frames 23–41, from the difference against a median background.
- Image velocity at frame 24: about (−8.9, −9.3) px/frame (central difference). At Z = 3.04 m (from the
  3.0735 m distance), the lateral 3D speed is about 0.95–1.05 m/s.
- The depth component dominates the uncertainty. The ball flies toward the camera.
  1. **Size growth:** a linear fit of 1/D over frames 24–35 gives d(dist)/dt between −1.9 and −2.4 m/s.
  2. **Floor bounce geometry:**
     - The floor is about 0.79 m below the camera with roughly 0° pitch. This comes from the basketball centres
       back-projected with the given depths, and the standing person's feet.
     - The bounce point is at image bottom ≈ 689 px, frame 38 (one capture frame dropped at 35→36). That
       gives Z ≈ 1.83 m at about 15 true frames after frame 24, so VZ ≈ −1.95 m/s.
  3. **Gravity-ballistic 3D fits** of u, v over frames 24–35 with the depth constraint:
     - VZ is poorly constrained, from −1.4 to −1.8 m/s for pitch 0–3°.
     - |V| comes out 1.93–2.23 m/s, with 1.7–2 px RMS residuals. There is some tension with gravity: the
       image vertical acceleration is about 20 % lower than 9.81 m/s² predicts at 3.04 m.
- With VZ = −1.7 / −2.0 m/s, the speed at frame 24 from back-projected per-frame positions is:
  - forward difference (5-frame mean): 1.88 / 2.14 m/s
  - central or quadratic fit: 1.96 / 2.21 m/s
- Prior check (orange ball, 2.21 m/s at frame 12): my estimate with the given depths is about 1.8–1.9 m/s.
  The reference may run a little high (per-frame depth noise, and the 11→12 frame gap).

## Answer
2.1 m/s. Likely range 1.8–2.3. Confidence is moderate, because the toward-camera component is inferred, not
directly measured.
