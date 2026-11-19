# Q511: droplet speed at t = 0.2 s (m/s)

- 2D simulation, 60 fps (file fps = question_fps). t = 0.2 s means frame 12. The drop has left the view by then (it is visible only in frames 0–10), so the answer has to be extrapolated from the free-fall fit.
- Track: scene/tracks/drop.csv mask centroids, using the record's render-index mapping (video frame 7 duplicates frame 6, and render step 8 is missing). Frame 7 is excluded. With that mapping, one quadratic fits frames 0–10 to within 0.4 px.
- Fit (fit.py): a_y = 31.69 px/frame², a_x = -0.47 px/frame². The vertex sits at frame -0.044, so the drop starts from rest at frame 0.
- Scale: prior a = 9.7 m/s² = 114,100 px/s² (scalar-speed acceleration), giving 8.50e-5 m/px.
- Speed at frame 12 = |p(12) - p(11)| × 60 = 21,954 px/s, which is **1.866 m/s**.
- Check: the fit windows 0–6, 1–10 and 3–10 all give 1.866 m/s, within ±0.0005. The ideal check from rest at frame 0 is a(2i-1)/(2·fps) = 9.7·23/120 = 1.859 m/s, which agrees within 0.4%.
- Confidence: high. The remaining uncertainty is whether the reference used a·t (1.94 m/s) instead of the backward difference. I followed the stated backward-difference convention.
