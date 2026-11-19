# q1053 – eave-to-eave width of the small house

File fps 22.892 and question fps 24. I used the scene/ frame numbers and t = frame/24.

## Focal length (from the bird prior: length 1.19 m)
- Bird tip-to-tail pixel extent comes from a mask of the difference to the median background (birdmask.py), on
  wings-level frames 1, 2, 10, 11, 18, 19, 27, 28 and 36: 171, 171, 160, 158, 157, 157, 167, 172 and 167 px.
- The bird's depth is interpolated from the depth_info (34.584 m at t=0, 33.999 m at t=1) and converted to Z with the
  off-axis ray factor (solve.py). The per-frame f is 4490–4920 px, median 4726 and mean 4703. I used f ≈ 4750
  (HFOV ≈ 23°). The spread across frames comes from the bird's pose, about ±5%.
- The bird flies almost parallel to the image plane (heading about 6° toward the camera), so foreshortening is
  negligible.

## Eave span
- Outermost roof-board pixels at the front gable, frame 0 (eaves.py, zoomed crops): left x ≈ 81.3 (y≈773) and
  right x ≈ 1026 (y≈783). The span is 944.7 px. The camera is static.
- The house origin's distance is 55.083 m, which gives Z_origin ≈ 54.9 m. The eave tips are on the front face, which
  is about half the house depth closer to the camera than the origin.
- Front-face depth check from the ground plane: I took the cart's distance (30.374 m, ground centre at v≈1250) and
  the house front base (v≈1170), with a horizon row between 1040 and 1070 (distant hills sit at v≈1075–1090). This
  gives Z_front ≈ 48–54 m, i.e. a house about 6–10 m deep, which fits a roughly square footprint. I took
  Z_front ≈ 51–51.5 m.
- Width = 944.7 × 51.3 / 4750 ≈ 10.2 m. Range: 10.0 m (Z_front=50) up to 11.0 m if the eaves were at the origin's
  depth.

## Confidence
Moderate. The main uncertainties are f (±5%, from the bird pose) and the front-face depth (±5%).
Answer: 10.2 m.
