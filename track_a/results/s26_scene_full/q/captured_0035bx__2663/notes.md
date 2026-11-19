# q_2663 — soccer ball diameter (cm)

Lab video, 24 fps (file and question_fps agree), 1280x720, f = 0.5959*1280 = 763 px.
t=0.9 s -> frame 22, t=1.4 s -> frame 34.

## Depth labels
At t=1.4 s both depth lines say "soccer_ball" (2.6020 and 2.3730). I worked out which is which:
- Basketball pixel diameter (orange mask, convex hull, area-equivalent / perpendicular to motion): f22 ~64-65 px,
  f34 ~68.7 px. With 2.7777 m at f22: 23.3 cm. At f34: with 2.602 m it gives 23.4 cm, with 2.373 m 21.4 cm. The prior is 23.2 cm,
  so basketball = 2.602 m and soccer = 2.373 m at t=1.4.
- This also fits the geometry: at f34 the soccer ball is lower in the image (v=496 vs 464), so it is nearer the
  downward-looking camera.
- The basketball check reproduces the prior to within 0.5-1 %, which confirms f = 763.

## Soccer ball pixel diameter (measure.py)
Mask = convex hull of pixels with min(BGR)<245 (or <235) inside a disk around the tracked ball. I measured extents in
36 directions, the extent perpendicular to the motion, and the area-equivalent diameter. Overlays are in frames/ov22.png and ov34.png.
- f20-23: ~60-61.5 px. At f22 the diameter is ~60.5 px, so 2.477*60.5/763 = 19.6 cm
- f32-35: ~60-62 px. At f34 the diameter is ~61.5 px, so 2.373*61.5/763 = 19.1 cm

## Answer
The two independent frames/depths give 19.6 and 19.1 cm. Their mean is **19.4 cm**.
Confidence: moderate-high (±4 %). The main uncertainty is the faint white-panel edge against the white background (±1 px, ±1.6 %).
