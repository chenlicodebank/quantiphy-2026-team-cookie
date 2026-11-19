# q_796 – length of the house (simulation_0239)

Prior: speed of the horse at the back = 0.874 m/s. No depth_info. fps = question_fps = 24.

## Which horse
The brown horse is "at the back" under both readings: it trails the white horse (x 746 vs 969, both walking +x), and it is
the upper one, nearer the house, in this top-down view.

## Scale from the prior (tm.py, speed.py)
I tracked the brown horse by template matching (body crop from frame 0) over frames 0–48. Frame 49 is the animation-loop
reset, so I left it out. Rump template: 2.62–2.63 px/frame, steps 1.8–3.9 px. The record's torso centroid gives 2.46–2.51
and its full-mask centroid 2.61–2.69. I used 2.63 px/frame = 63.1 px/s, which gives s = 0.874/63.1 = 0.01385 m/px. This
scale holds at the depth of the horse's back, about 1.4 m above the ground. Check: the horse is 143 px long → 1.98 m.

## House geometry (edges.py, tiles.py, zoomed crops)
- The camera looks straight down with the principal point near (960, 540). Three independent fits put it at
  x ≈ 954–967 and y ≈ 520–554.
- Main block (ridge runs top–bottom along x = 1020). Side eaves are straight vertical lines at x = 658.5 and 1362.5 →
  **704 px**. Gable ends: eave corners at y = 95 / 717.5, ridge ends at 18 / 745. The ridge is magnified by
  1 + k = 1.165, so the main ridge is 0.142·D_e above the main eaves (D_e = camera depth of the main eaves).
- Cross gable (ridge runs left–right at y = 380). Apexes at x = 614 / 1427, eave corners at 645.5 / 1386, eaves at y = 272 / 513,
  k = 0.098.
- The valley triangles have their base corners at (≈843, 515) and (≈1180, 515) and their apex at (1020, 415). From these, the cross-gable
  eaves sit at depth 0.923·D_e (both corners give 0.923), i.e. higher than the main eaves. The main ridge meeting the cross
  slope at y = 415 reproduces this to 0.3 %. The tile pattern gives an independent check: the cross-gable tiles look 4.6 % larger,
  which gives 0.93·D_e.
- Converted to world units (×D_e/f): main eaves span X −301…+402 (704 px). Cross gable ends span −290.6…+393 (683.5), so they
  lie inside the main eaves. Y extent = 623 px at eave depth. **Length = X extent = main-block eave-to-eave = 704 px at
  the main-eave depth.**

## Perspective correction between the horse and the house
The tile foreshortening on both roofs (rib period vs. course period, with the perspective term corrected) gives
cosθ_cross / cosθ_main = 0.65. Combined with tanθ_main = f/2475 and tanθ_cross = f/1351, this gives f ≈ 2900 px
(range 2400–3300). That is close to Blender's default 50 mm lens at 1920 px width (2667 px). Then D_back = s·f ≈ 40 m.
The step from the main eaves up to the cross-gable eaves is 0.077·D_e ≈ 3 m, about one storey, so the main eaves are taken
at about 3 m above the ground.
D_e/D_back = 1 − (3.0 − 1.4)/40.2 = 0.960.

**Length = 704 × 0.01385 × 0.960 = 9.36 m**

## Checks and sensitivity
- The two valley corners and the ridge/valley apex give one consistent 3D roof model.
- With no perspective correction (everything on the horse scale) the length would be 9.75 m. If the cross-gable ends were
  wrongly taken as the extent, at main-eave depth, it would be 740 px → 10.3 m. The geometry rules this out.
- Main eaves 2.5–3.5 m and f in 2400–3300 → 9.25–9.45 m. If the main block were two storeys (eaves about 6 m) → 8.7 m.
- Confidence: moderate, about ±5–8 %. The scale comes from the averaged horse speed and is good to about 2 %; the main
  uncertainty is the eave height.
