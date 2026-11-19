# q_789 – height of each glass window (m)

Prior: speed of the horse at the back = 0.874 m/s. 2D scene (horses walk side-on along the brick wall, same ground line
as the windows' wall), fps 24 = question_fps.

* "Horse at the back" = the trailing (left, chestnut) horse, horse_brown. Sanity: with its scale the horse is ~2.1 m
  long and the window ~1.2 m (plausible); the tan horse's scale would give a 1.3 m horse and 0.6 m windows (implausible).
* Brown horse speed (speed.py, frames 0-48, before the loop reset at 49): linear-fit slopes of ref_x / rump edge /
  bbox edges / mask centroid = 3.24, 3.23, 3.26, 3.16, 3.22 px/frame; net ref_x 151.4 px / 48 = 3.15. Visual check of
  rump at frames 0 and 48 (≈159 → ≈310 px) gives ≈3.15 px/frame. Adopted 3.2 px/frame = 76.8 px/s.
  (Template matching tm.py failed — locked onto brick texture; not used.)
* Scale = 0.874 / 76.8 = 0.01138 m/px.
* Window height (window.py, frame 0, column profiles through the unobstructed right window): top of window at
  y ≈ 845, bottom/sill edge at y ≈ 951-952 → 107 px (scene record: all three windows 107 px tall).
* Height = 107 × 0.01138 ≈ 1.22 m (range 1.20-1.24 for speed 3.15-3.26 px/frame).

Confidence: moderate-high; main uncertainty is the brown horse's px speed (±2%) and the reading of "at the back".
