# q_1996 — speed of the soccer ball at t = 0.5 s

- 2D clip with one faint grey ball on white. It moves horizontally to the right and slows down steadily. fps = question_fps = 24, so t = 0.5 s is frame 12.
- `measure.py` re-measures every frame. It uses an intensity-weighted centroid and three size estimates: area-equivalent diameter, second-moment diameter and half-max extents.
  - Diameter, frames 2–50: area-equivalent median 50.0 px; vertical second-moment median 49.3 px. Vertical size is not affected by motion blur. Near frame 12 the estimates are 49–51 px.
  - Adopted diameter: 49.7 px (±1). Scale = 0.344 / 49.7 = 0.006922 m/px.
- `speed.py` finds the step from frame 11 to 12, using the reference backward difference of the smooth track:
  - quadratic fit over frames 2–50: 31.68 px/frame (rms 0.5 px);
  - quadratic fits over frames 2–22 and 2–30, and a cubic over 2–50: 31.65–31.66;
  - linear local fits: 31.57.
  - The raw single-frame step is 30.9 (noise ±1.5 px), and the mean step over frames 9–15 is 31.45.
- Speed = 31.66 × 24 = 759.8 px/s × 0.006922 = **5.26 m/s**.
- Second route: the record's 49 px bbox diameter gives 5.33 m/s, and a 50 px diameter gives 5.23 m/s.
- Confidence: about ±3%. The diameter of this soft-edged mask is the main uncertainty.
