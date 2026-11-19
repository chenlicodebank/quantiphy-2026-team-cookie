# q3249 – acorn displacement 2.20–2.30 s (cm)

Prior: acceleration of acorn 2.00–2.30 s = 0.77 m/s². fps = question_fps = 30 → frames 60–69 (prior), 66→69 (question).
Planar 2D horizontal motion, single scale = 0.77 / pixel acceleration (annotator convention).

Reference point: stem knob x in background-stabilised coords (scene/tracks/acorn.csv `ref_stem_x`), checked visually
on frames 60, 66, 69 (view.py → frames/). The bbox centre is biased by motion blur that grows with speed, so not used.

measure.py:
- displacement 66→69: 1256.2 − 904.1 = 352.1 px
- pixel acceleration over 60–69: (v69 − v60)/0.3 with forward-difference v → 3660 px/s²; linear fit of v → 3527;
  quadratic fit of x → 3420; mean 2nd difference → 3771.
- d = 352.1 × 0.77 / a → 7.41 / 7.69 / 7.93 / 7.19 cm. Raw (unstabilised) stem coords give 6.9–7.7 cm.

Answer: 7.5 cm (centre of the stem-based estimates). Confidence moderate (±5%); the main uncertainty is
how the annotators computed the pixel acceleration from noisy second differences.
