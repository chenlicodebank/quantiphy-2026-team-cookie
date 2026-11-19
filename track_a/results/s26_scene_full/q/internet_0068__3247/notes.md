# q_3247 – displacement of the acorn between 2.00 s and 2.10 s (cm)

Prior: acorn acceleration 2.00–2.30 s = 0.77 m/s². No depth_info. Internet clip, 2D side view; fps = question_fps = 30,
so 2.00 s = frame 60, 2.10 s = frame 63, 2.30 s = frame 69. Acorn fully visible over frames 59–72.

Method (annotator convention: one scale = prior world value / prior pixel value):
- Positions in background-stabilised (ref = frame 99) pixels, using the record's camera transforms.
- My own track (bgsub.py): warped each frame to ref, subtracted a median background (frames 85–99), and took the midpoint
  of the mask's left/right edges in a stem band (y 540–575) and a cap band (y 610–700). The stem track agrees with the
  record's ref_stem_x to ±3 px. The cup band is unreliable (shaded half of the cup missing from the mask) and is not used.
- Pixel acceleration over 60–69 with several estimators (quadratic fit; (v69−v60)/9 forward; backward; mean centred
  second difference; mean forward second difference):
  stem 3464, 3650, 4050, 3825, 4320; cap 4244, 4000, 4450, 3645, 4500 px/s². The acorn's acceleration is not
  constant (the per-frame steps go 85→127 px with some jitter), so the estimators spread by about ±12 %. I used the median, 4025 px/s².
- Scale = 0.77 / 4025 = 1.91e-4 m/px. Sanity check: cap width ≈ 320 px → 6.1 cm, height ≈ 420 px → 8 cm, which is plausible for a toy acorn.
- Displacement frames 60→63: stem 283.8 px, cap 275.5 px (record stem 283.9); mean 279.7 px.
- Answer = 279.7 × 1.91e-4 = 0.0535 m = **5.35 cm**.

Second route: the record's ref_stem_x on its own gives 5.6–6.7 cm and my cap track gives 4.8–5.3 cm, depending on
the estimator. The answer depends mostly on how the prior's acceleration was estimated from noisy clicks.
Confidence: moderate (about ±12 %).
