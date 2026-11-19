# q_328 – length of the toaster (m); prior: cup diameter = 0.087 m

Time base: fps = question_fps = 24. Only static sizes are needed, so timing does not matter here.

## Geometry
The camera looks straight down at a kitchen counter. The toaster's slots, the circular cooktop rings and the
cup lying on its side (wide end up in the image, near y≈520) show this. The burner rings fit near-circles
(burners.py), so the image plane is parallel to the counter. The cup's wide end shows almost no elliptical cap
(|v|≈20 px from the image centre), while its narrow end (|v|≈238) shows a small cap. Together these put the
nadir/principal point near the image centre (959.5, ~540).

The toaster shows clear perspective. Its right end face is visible, and the seam band running lengthwise
across the top bends down that face (band.py, frames/band_right.png). The left end is hidden. A single
2D metres-per-pixel scale would therefore overstate the size of the tall toaster compared with the cup, which
lies close to the counter.

## Measurements (frame 0 for the toaster; frames 17-28 for the cup)
- Cup wide-end width: 118-122 px. I used 120 px (measure.py; the scene record gives the same). Its axis is
  at height D/2 = 0.0435 m.
- Toaster red-body mask: x 52-485, but most rows run 56-482 (the 485 is the protruding band). The naive single
  scale gives 426 px × 0.087/120 = 0.309 m (434 px would give 0.315 m).
- Seam band |v| from the image centre: 300.3 px on the flat top, 280 px where it meets the right silhouette.
  So Z(right tangent)/Z(top) = k_s ≈ 1.073. Shading of the right end agrees: a rounded corner at x 420-455, then
  a flat wall at x 455-482.
- Left silhouette u = -903 px (upper corner of the hidden left end); right silhouette u = -477 px (at k_s).

## Model (model.py)
L = [903(1+ε) − 477·k_s]·Z_top/f, with f/Z_cup = 120/0.087 and Z_cup = Z_top + H_top − 0.0435.
The result depends only weakly on the assumed toaster height (0.15-0.25 m), giving L = 0.270-0.275. The implied
f is about 3100 px (HFOV about 34°). For k_s = 1.063-1.083, L = 0.278-0.267.

## Second route
I also used the flat-wall top edge on the right (x = 455, |u| = 504.5) together with the left silhouette, both
at the wall-top depth: L = 398.5 px × (Z_wall/f) ≈ 0.274 m. This agrees with the band route (0.272).

## Answer
L ≈ 0.272 m.

Caveats:
- The slot pair is centred at x ≈ 238. That is about 18 px left of the flat top's centre in this model, so the
  slots are slightly off-centre. If the slots were exactly centred, a steeper perspective would follow, which
  the band's curved path contradicts.
- A white base plate under the toaster reaches x ≈ 497. If it belongs to the toaster model, L would be about
  4 % larger.
- Without perspective correction the answer would be 0.31 m.

Confidence: moderate (about ±6 %).
