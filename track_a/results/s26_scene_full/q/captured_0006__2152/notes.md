# q_2152 — width of the toy (cm)

Lab video, 24 fps (file and question_fps both 24), 1280x720, f = 0.5959*1280 = 762.8 px.
depth_info: t=1.0 s (f24) Z=1.402 m; t=1.2 s (f29) Z=1.065 m. Prior (g = 9.8) is not needed for a size.

## Method
- The toy (yellow plush with beige anonymised face) is in free flight at f24; seen almost face-on, roughly round
  outline (W ≈ H). f29 is heavily motion-blurred (vertical streak), so it is not usable for a size.
- `measure.py`: HSV yellow mask restricted to a 140 px ROI around the scene/ track centre (without the ROI the
  largest yellow blob is a static background object — fixed), convex hull, extents. Overlay checked in
  frames/mask_f24.png: hull follows the toy's outline.
- `halfmax.py`: yellowness (saturation on yellow hues) thresholded at 35/50/65 % between background and peak.

## Key measurements (f24, Z = 1.402 m)
- Horizontal extent: 54 px (S>=120 hull), 58 px (S>=80 hull), 54 px (half-max), 51–59 px (65 %–35 %).
- Width = 1.402 * 55 / 762.8 = 0.101 m → ~10.0 cm (range 9.9–10.7 cm).

## Second route
- Neighbouring flight frames with depth linearly interpolated between f24 and f29: f23 10.4, f25 9.6, f26 9.5,
  f27 9.1 cm (half-max). Equivalent diameter at f24: 53–57 px → 9.8–10.5 cm. All consistent with ~10 cm
  (the drift is from the approximate linear depth interpolation and slow tumbling).
- scene/ record: equiv_diam 50 px at f24 → 9.2 cm (its mask excludes some edge pixels).

Answer: 10.0 cm. Confidence: moderate (±7 %); "width" taken as the horizontal extent across the toy's face.
