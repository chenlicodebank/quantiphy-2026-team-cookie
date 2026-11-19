# q_502 — speed of the bubble at t = 0.5 s (m/s)

File fps = question_fps = 30, so t = 0.5 s -> frame 15. Speed = |p(15) - p(14)| x 30. 2D scene, static camera.

## Scale (prior: horizontal width of the "skynova" text = 0.00188 m)
The brand text runs vertically (rotated 90°) down the left of the bottle label; only "NOVA" is in frame, so its
horizontal extent equals the letter height. `measure_text.py` (white, low-saturation threshold) and
`text_profile.py` (half-level edges of the per-column 99th-percentile whiteness) give x = 1105.6 -> 1185.3,
**width 79.7 px** (same in frames 0, 15, 49). Scale = 0.00188 / 79.66 = 2.360e-5 m/px.
SAM 3 ("NOVA text", frame 15) gives 89 px (x 1102–1190). That is 12 % more, so I compared both on a 4x zoom
(`check_sam.py`, `frames/text_check.png`). The SAM outline sits a few px outside the letters and includes a spurious
blob. My green edge lines sit on the letter edges, so I used 79.7 px.

## Bubble motion
`track_bubble.py`: sub-pixel template matching (100 px template of the bubble at frame 15) over frames 5–28.
p14 = (772.94, 1375.67) and p15 = (764.00, 1381.00), so the step is **10.41 px/frame**. Neighbouring steps are 9.09, 9.29,
10.35, [10.41], 11.14, 11.03, 11.62 for steps 12–18 (smooth acceleration). Their linear trend at step 15 is about 10.4.
- Second route: the scene/ hull-centroid track (independent mask method). Its frame 14->15 step is 11.95 px, but its
  centroids are noisy (±1 px). The mean of its steps 12–18 is 10.43 px/frame, which agrees with template matching.
- SAM 3 ("air bubble", frames 14 and 15): the mask is a loose blob about 149 px wide around the bubble, which is
  about 105 px across (see `frames/bubble_check.png`). Its centroid moves (+1.8, +1.1) px between frames 14 and 15, which
  is the wrong direction. It does not follow the bubble's motion well enough to measure speed, so I did not use it. The
  template-match centre (764, 1381) at frame 15 lies on the bubble centre (green circle in the check image).

## Answer
v = 10.41 px/frame x 30 x 2.360e-5 m/px = **0.00736 m/s** (7.4 mm/s).
Confidence: moderate-high. The scale is good to about 1 % if the prior's "horizontal width" means the rotated text's
horizontal extent. The per-frame step is good to about ±0.3 px (3 %).
