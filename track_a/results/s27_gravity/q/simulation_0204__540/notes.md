# Q540 – typewriter length (m)

Prior: magnifying glass falls with a = 9.8 m/s^2 before 0.5 s. 2D video, file fps = question fps = 24.

Scale (fit.py): quadratic fit of magnifier y over free-fall frames 0-11 (scene/tracks/magnifier.csv, checked
against frames): bbox-centre a = 7445 px/s^2 (frames 2-11: 7453), mask centroid a = 7431 (7408); rms residual
0.3-0.5 px. Second differences scatter around 7400-7500. Using a = 7440 px/s^2 -> 9.8/7440 = 1.317e-3 m/px.

Typewriter: front view, so its longer horizontal extent (left-right) is the horizontal pixel extent. Zoomed grid
crop of frame 29 (frames/tw.png) and row scans (tw.py): base plate left edge x≈487, right edge (base/right knob)
x≈797-798 -> 311 px (scene record 312 px).

Length = 311 x 1.317e-3 = 0.410 m.

Checks: the magnifier's own size at this scale is 162 px -> 0.21 m total, lens ≈0.136 m (a large reading glass,
plausible); a portable typewriter 0.41 m wide is realistic. The typewriter sits a little further back than the
magnifier's fall plane (base bottom y≈1033 vs. magnifier rest bottom y≈1046), so with perspective it could be a
few percent larger. I didn't apply that correction, following the 2D single-scale convention.
Confidence: good (~5%).
