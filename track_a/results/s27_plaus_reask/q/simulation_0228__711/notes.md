# q_711 — width of the beach chair (m)

Prior: speed of the black cat = 1.041 m/s (the "dog" in scene/ is this black cat). No depth_info. File fps = question_fps = 24.
Top-down 2D-type render, static camera → one metres-per-pixel scale from the cat's pixel speed.

## Scale
- From scene/tracks/dog.csv (centroid track checked; clean black mask): net displacement 0→49 = 267.2 px → 5.453 px/frame;
  linear fit slope 5.456 px/frame; mean of per-frame steps 5.478 (slightly inflated by gait jitter).
- Pixel speed 5.453 × 24 = 130.9 px/s → s = 1.041 / 130.9 = 0.00795 m/px (0.00792 using the per-frame mean; 0.5 % spread).

## Chair width (shorter horizontal extent, across the lounger)
- Three identical front loungers. Outer frame edges measured from row-averaged column profiles (edges2.py, rows 290–450)
  and checked on 3× zooms (frames/c3–c5.png): left 750.5–944.5 (194.0 px), middle 1011.5–1205 (193.5 px),
  right 1270.5–~1466 (~195.5 px). Mean ≈ 194.3 px.
- The backrest top looks wider (e.g. 742–944, 1272–1487) only because it is raised toward the camera: both outer edges
  scale about the image centre by the same factor 1.041 (left lounger left edge 750.5→742, right lounger right edge
  1466→1487; middle lounger left edge 1011.5→1013 as predicted), so the world width is constant ≈ the seat-frame width.
- 194.3 px × 0.00795 = 1.545 m. The seat rail sits higher than the cat's body, so it is magnified slightly more
  (estimated ~1–2 % from the 4 % backrest magnification); corrected ≈ 1.52 m. Answer 1.53 m.

## Checks / caveats
- Same scale gives cat length with tail 108 px → 0.86 m, body 0.65 m (plausible-ish cat), swim ring 1.15 m, deck tiles
  1.15 m, lounger length 339 px → 2.7 m. The loungers are oversized vs a real one (≈0.7 m wide), i.e. the chair asset is
  large relative to the cat; the geometry here is a simple planar scale with the motion fully in the image plane, so there
  is no alternative route that would change it. Answer kept on the prior's scale.
- Second route: per-frame-mean speed scale gives 194.3 × 0.00792 = 1.54 m (same).
Confidence: moderate (scale solid; main risk is the asset-scale oddity).
