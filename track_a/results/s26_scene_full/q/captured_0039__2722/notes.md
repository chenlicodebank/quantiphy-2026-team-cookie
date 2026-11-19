# q2722 — white cup rim diameter (captured_0039)

File fps = question_fps = 24. Camera static; cup static (x724-795 in scene record, confirmed).

Method (lab method card): f = 0.5959*1280 = 762.8 px; size = depth * pixel extent / f.
- measure_cup.py, frame 24 (t=1 s): subpixel gradient-edge positions per row. The rim (top lip, rows y=380-398)
  spans x = 724.4 -> 794.6, width 70.1-70.2 px (body below narrows to ~69 px at y 400-414, tapered cup).
- Depth: distance_white_cup_camera = 0.874 m (to cup centre, pixel ~(760,437)).
  - Euclidean distance used directly: 0.874*70.2/762.8 = 8.04 cm.
  - Converted to z-depth (ray factor 1.017 -> Z = 0.859 m): 7.91 cm.
- Answer 8.0 cm (between the two; difference 1.7%).

Check: matches the scene record's 71 px top width; 8 cm is a typical mug/cup rim diameter.
Credit-card cross-check not clean (cards tilted/overlapping, at different depth). Confidence: good (±4%).
