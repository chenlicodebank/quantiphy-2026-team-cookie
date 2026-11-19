# q_2797 — distance trashbin ↔ shoe (m)

Lab video, 24 fps (file fps = question_fps = 24), t=1.0 s → frame 24. Both objects static (scene/static_check: ±0.3 px).
Camera per lab card: f = 0.5959×1280 = 762.8 px, (cx, cy) = (640, 360).

Measurement (measure.py, frame 24, foreground mask vs per-row background, overlay frames/check.png):
- Bin: bbox centre (726.5, 534.5) (top-left corner slightly includes the person's leg); record bbox centre (728, 538);
  centroid (725.6, 534.5).
- Shoe: bbox centre (284, 657.5), centroid (286.8, 658.2).
Back-projection along the unit ray × Euclidean depth (bin 2.977 m, shoe 2.231 m):
- bbox centres: 1.564 m; centroids: 1.555 m. Using record centre (728, 538) changes it by <0.01 m.
- Check with depth read as z-depth instead of ray distance: 1.579 m (+1%).
Sanity: shoe length 85 px × 2.231/762.8 ≈ 0.25 m, bin width 95 px × 2.977/762.8 ≈ 0.37 m — plausible real sizes.
The prior (yoga ball speed) isn't needed; the scale comes from depth_info + the fixed lab focal length.

Answer: 1.56 m. Confidence: high (±3%, depending mainly on where the annotator clicked the centres).
