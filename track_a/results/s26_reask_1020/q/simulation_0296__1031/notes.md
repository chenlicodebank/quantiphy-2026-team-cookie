# Q1031 — length of the butterfly's wings (m)

The scene is 2D: a top-down view, a static camera, one butterfly at constant depth. File fps and question fps are both 24.

## Scale from the prior (speed 0.32 m/s)
- Track: `scene/tracks/butterfly.csv` ref point (thorax). Checked with `scale.py`.
- Mean per-frame step over frames 1–71: 15.64 px/frame. A linear fit of x gives 15.65 px/frame.
- Steps between frames at the same wing phase (open wings at 18→39, 39→60 and 18→60): 15.41 px/frame. Mask jitter during the wing folds slightly inflates the per-frame steps.
- I took 15.5 ± 0.15 px/frame = 372 px/s, which gives **8.60e-4 m/px** (range 8.52–8.65e-4).

## Wing size
- My own background-difference mask (`measure.py`, overlay in `frames/mask_18.png`) fits the wings well.
- Wingspan (tip to tip across the body, wings flat), in px:
  - Scene record: max 261, plateau 254–261.
  - My mask: 262–267, which includes a few px of blur halo.
  - Adopted value: **260 px**, which gives **0.224 m** (0.2225 with the mean-step scale).
- Extent along the body axis with the wings open: about 191 px, which gives 0.164 m.

## Reading
"Length of the wings" is taken as the tip-to-tip extent of the wings (the wingspan, which is also the longest horizontal extent of the open wings): **0.223 m**.
- Alternative reading: the extent along the body or flight direction, 0.164 m.

## Check
- The two speed routes (all steps vs phase-matched) differ by 1.5 %.
- Wingspan px values from two independent masks agree within about 2 %.
- 0.22 m is large for a butterfly but fits a scene modelled at large Morpho scale; there is no other standard object to compare against.
- Confidence: moderate. The measurement is solid; the main risk is which dimension "length" refers to.
