# Q64 – acceleration of the white car (white van) at 1.0 s

2D top-down render, 24 fps (file fps = question_fps, no re-timing). White car = `white_van` track (straight up the vertical road, starts at rest).

Scale: prior length 6 m. Body length measured in code (measure2.py: brightness profile down the van's centre strip vs the road,
bridging the dark windshield gap): 245 (f0), 242 (f20), 231 (f36), 229 (f50), 236 (f71) px. Visual check at f36 (frames/f36.png) gives 620–853 ≈ 234 px;
scene record body extent at thr 25 is 236 / 233 / 236 px. Using 235 px → 0.02553 m/px.

Motion: quadratic fits of y(t) (frames 34–35 excluded for the mask glitch), measure.py:
- centre ref_y, f0–71: a = 159.0 px/s²; f10–38: 161.0; f0–48: 159.5; f24–71: 160.1
- front edge: 159.6–161.9; rear edge: 158.3–158.9
Uniform acceleration, so a(1.0 s) = the constant ≈ 159.5 px/s² → 159.5 × 6/235 = 4.07 m/s² (4.06 with 236 px).
Second route: front/rear edge fits independently give 158.3–161.9 px/s² → 4.04–4.13 m/s².

Answer: 4.06 m/s². Confidence: good (~3 %); the main uncertainty is the pixel length (231–245 px).
