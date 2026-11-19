# q_3015 – boat distance traveled 4.5 s → 7 s

Prior: boat length 3.5 m. 2D internet clip, static camera (record: shift < 0.2 px).

Time base: file 29.85 fps vs question 30 fps; frames 134–209 vs 135–210. Both give the same pixel displacement (120.5 px),
so the choice does not matter.

Checks: I viewed zoomed, gridded frames at t=4.5 (frame 134) and t=7.0 (frame 209). The hull tips (bow ≈555/430,
stern ≈790/673) match scene/tracks/boat.csv.

Measurements (measure.py):
- Hull-centre x: 673.5 → 553.0 = 120.5 px. A linear fit over the window gives 121.4 px. The 5-frame-smoothed path length
  is 120.5 px; the motion is straight, so path ≈ net. Bow alone moved 125 px and stern alone 116 px, because the
  approach makes the boat look bigger.
- Hull length in px: 236 at 4.5 s, 245 at 7 s, 241 averaged over the window, 232 median over the whole clip.
- Single scale 3.5 m / L_px:
  - window mean L gives 1.76 m
  - L at 4.5 s gives 1.80 m
  - clip median gives 1.83 m

Answer: 1.78 m. This is between the window-mean scale and the start-frame scale.
Second route: bow and stern displacements, each converted with the window-mean scale, give 1.81 and 1.68 m. Their mean
is 1.75 m, which agrees.
Confidence: moderate-high. The main uncertainty is which frame the annotators used for the pixel length (±3%).
