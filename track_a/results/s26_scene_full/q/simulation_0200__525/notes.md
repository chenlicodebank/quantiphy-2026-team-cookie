# Q525 — diameter of the bottle's neck (m)

Time base: the file's fps and question_fps are both 60, so I used 60 fps.

## Scale from the prior (the drop's acceleration is 9.7 m/s²)
- The drop falls straight down at x ≈ 1175 px, next to the bottle and at about the same depth (it comes off the
  pipette tip just to the right of the neck). Treated as 2D with one scale.
- `neck_profile.py` fits a quadratic to the record's track over frames 2–11. The centre gives a = 28.869 px/frame²,
  and the sharp top tip of the drop gives a = 28.871 px/frame², from a separate set of points. The second differences
  run 27–30 and are uniform. a = 28.87 × 3600 = 103,930 px/s², so the scale is 9.7 / 103,930 = **9.333e-5 m/px**.

## Neck width in pixels (frame 13, no drop in view)
- Zoomed crop `frames/neck_crop.png` (x 720–1060, y 380–580, shown at 3×) plus horizontal gradient profiles.
- Plain glass cylinder of the neck (between the threads): x ≈ 780 to 986, which is **≈ 206 px**.
- Outer edge of the thread crests: x ≈ 772 to 1003, which is ≈ 231 px. The bottom collar/flange is ≈ 255 px (762–1017), and I did not
  count it as the neck.
- Taken: 212 px, near the cylinder but leaning a little toward the threads, because it is unclear which one the
  question means.

## Answer
212 px × 9.333e-5 = **0.0198 m**. The range is 0.0192 m (cylinder only) to 0.0216 m (thread crests).

## Check
The body is 369 px wide, which gives 0.034 m. A 30 ml dropper bottle is about 32–35 mm wide with an 18 mm neck finish.
The neck-to-body ratio of 0.57 is plausible, so the scale makes sense.
Confidence: moderate. The scale is good to about 1%. The main uncertainty is whether the threads count as part of the
neck (±6%).
