# Q185 — shark length (m), prior: boat length = 10 m

2D side-view scene (static camera, 24 fps, which matches question_fps). The answer uses one metres-per-pixel scale taken from the boat.

- Boat length (x-extent above the waterline, y 300–611, per-row sky subtraction) is 861/861/860 px at frames 0/10/30 (measure.py). The scene record gives 851–860, depending on how the stern edge is defined. I used 860 px, so the scale is 0.01163 m/px.
- Shark nose-to-tail x-extent (y 830–1000, per-row blue background subtraction, thresholds 30/60) is 276–281 px at frames 0/10/30/47/60, median about 278 px (shark.py). The scene record gives 274 ± 2.
- Shark length = 10 × 278 / 860 = **3.23 m**.

Check: the scene record's numbers (274/860) give 3.19 m, and the extremes of 274–281 px over 851–861 px give 3.18–3.30 m. A real shark of about 3 m next to a 10 m fishing boat is plausible.
Confidence: good. The main uncertainty is ±2 % from edge definition. The two objects are in different layers (surface and underwater), but nothing in the image shows a depth difference.
