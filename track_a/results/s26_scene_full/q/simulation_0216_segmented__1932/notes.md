# q1932 vase height
2D side-on render, static camera, 24 fps (file fps = question_fps, no retiming).
Scale from prior: cat speed 0.94 m/s. Cat horizontal pixel speed from scene/tracks/cat.csv: linear fit of cx 423.6 px/s,
of dark_cx 427.3 px/s, net displacement 423.3 / 427.9 px/s -> ~425.4 px/s (steady walk, no vertical drift).
Scale = 0.94/425.4 = 0.002210 m/px.
Vase pixel height re-measured at frame 24 (non-white pixel rows in vase columns): top y=575, foot ends y~790 where it
meets the console top -> 216 px (matches static_objects.json bbox 575-790).
Height = 216 x 0.002210 = 0.477 m.
Check: mean per-frame step speed (428-430 px/s, inflated by gait jitter) gives 0.472 m; same within 1%.
Caveat: cat walks slightly in front of furniture (paws y~1021 vs furniture feet ~990), so a small perspective
difference is possible; single 2D scale used per convention. Confidence: moderate-high.
