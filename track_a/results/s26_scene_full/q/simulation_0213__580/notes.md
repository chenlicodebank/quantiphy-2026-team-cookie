# q_580 — width of the floor mirror (m)

Prior: speed of the black cat = 0.94 m/s. No depth_info. fps = question_fps = 24 (no re-timing issue).

## Scale from the cat (cat_speed.py)
- The cat walks steadily left→right. Linear fits over the visible frames (0-22, 44-49) give: nose 17.76 px/frame
  (rms 0.7 px), centroid 17.81, bbox centre 17.71, torso 17.86. I use 17.78 px/frame = 426.7 px/s.
- Cat-lane scale = 0.94 / 426.7 = 0.002203 m/px.

## Mirror pixel width (mirror_edges.py, mirror_fit.py, mirror_width.py, zoom crops frames/lrail.png, rrail.png, bot.png; frame 49)
- The mirror leans against the wall: top at y≈390, bottom bar on the floor at y≈967.5. Both rails shift right going down,
  which is consistent with pure lean perspective about cx≈960 (x−960 scales by ≈1.034 from top to bottom for both edges).
- Outer frame edges (luminance + colour R−B transitions): top (y≈400) 1632 → 1873 = 241 px; y≈760 1646 → 1892 = 246 px;
  extrapolated to the base y=967.5: ≈1654 → 1903 = 249 px (agrees with the zoom of the bottom bar).
- The left rail looks wider than the right/top rails (25 vs 20/18 px); part of that is the frame's visible left side face
  (a darker 2-3 px strip). Removing ~3 px gives a front-face width of ≈246 px at the base depth (238 px at the top).
- The record's scene.json box (1632-1872, 241 px) is the top-row width only.

## Depth correction (the mirror is behind the cat's lane)
- Camera is level (floor/wall line horizontal; lamp-shade bottom rim at y=607 is a nearly flat ellipse that sags ~2 px,
  so the horizon is a little above it, y≈540-570). I use y_h≈550.
- Floor-contact rows: cat midline ≈1019 (paws 1016-1023), mirror base 967.5.
  Scale ratio mirror base / cat lane = (1019−550)/(967.5−550) = 1.123 (1.110 for y_h=500, 1.140 for y_h=600).

## Result
- Width = 246 px × 1.123 × 0.002203 m/px = 0.609 m → **0.61 m**.
- Second route: the top-width (238 px front face) scaled by the measured lean depth ratio 1.034 gives the same 246 px at the base.
  Without the side-face correction the result is 0.616 m. A naive single 2D scale with no depth correction would give
  241 × 0.002203 = 0.53 m, but the perspective (the mirror stands at the wall, behind the cat's lane) clearly calls for the correction.
- Confidence: moderate. The main uncertainty is the horizon row and the lane depth ratio (±2%), plus the edge and side-face definition (±2%).
