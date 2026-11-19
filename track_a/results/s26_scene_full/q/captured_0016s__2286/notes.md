# Q2286 — soccer ball diameter (cm)

Lab video, 24 fps (file fps = question fps = 24), 1280x720. f = 0.5959*1280 = 762.8 px.
depth_info: ball at t = 1.5 s (frame 36) is 1.402 m from the camera.

## Method (lab method card)
D = Z * d_px / f, where d_px is the ball's apparent diameter at frame 36.
Frame 36 is free flight with motion blur along the path (up-right), so the diameter is the hull width
ACROSS the blur (minimum caliper width), not the streak length.

- measure.py: low-saturation/bright + dark threshold in a crop, largest component, convex hull,
  minimum caliper width. Frame 36: min width 96.2 px (max 116.4 = blur streak). Overlay frames/mask36.png
  shows the hull follows the ball edge, maybe 1-2 px short on the left.
- scene/ record (independent auto mask): mask_width 98.3 px at frame 36.
- Adopted d_px = 97.2 px -> D = 1.402 * 97.2 / 762.8 = 0.1786 m ≈ 17.9 cm.

## Checks
- Neighbouring frames 37/38 (less blur, slightly farther): 92-98 px, consistent with ~97 px at frame 36.
- Per-route: 96.2 px -> 17.7 cm; 98.3 px -> 18.1 cm.
- Off-axis note: the ball is ~24° off the optical axis. Applying the tangential foreshortening (cos θ) would give
  ~16.3 cm, but the card's convention (depth x pixel / f) is used. A 17-18 cm ball is smaller than a size-5 ball
  (22 cm) but plausible for a small/kids' ball.
- Gravity prior not needed for size.

Confidence: moderate (±3-4 % from pixel width; convention for off-axis is the main risk).
