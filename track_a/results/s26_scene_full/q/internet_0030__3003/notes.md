# Q3003 — boat moving distance 0.5 s → 1.0 s (prior: speedboat length = 3.2 m)

**Time base:** I used question_fps = 30, so 0.5 s → frame 15 and 1.0 s → frame 30. The file's rate is 29.15 fps, which
would give frames 15 → 29. The two rates differ by only 3%, so physical plausibility can't tell them apart. I took the
rate stated with the question as the annotators' rate. With 15 → 29 the answer would be about 6.7% lower (about 3.38 m).

**Camera:** pans right at about 0.75 px/frame. The motion is measured against the background, as the annotators' rule says.

**Pixel displacement, frames 15 → 30 (stabilised against the background):**
- scene record: ref_x_stab 733.67 → 955.47 = 221.8 px. Bow 219.4 px, stern 224.2 px.
- second, independent route (check.py): template-match the whole boat (hull and canopy, no wake) from frame 15 into
  frame 30, minus the hill background shift found by phase correlation (−12.11 px). Result: 222.8 px; the canopy/cabin
  core alone gives 222.5 px. Both routes agree to within 1 px. Value used: 222.5 px.

**Scale:** bow-to-stern pixel length, i.e. the bow tip to the orange stern object, checked on 4x zooms at frames 0
and 41. It shrinks slowly from 208 px to 190 px because the boat yaws slightly. Over the question's frames 15–30 the
mean is 196.5 px (198.95 at frame 15, 194.1 at frame 30). That gives 3.2 / 196.5 = 0.01628 m/px.

**Answer:** 222.5 × 0.01628 = **3.62 m**.

**Sensitivity:** with the length from the whole clip (197.8 px) the answer is 3.60 m. With the frame-0 length (208 px)
it is 3.42 m. With the file's fps (frames 15 → 29) it is about 3.38 m.

**Confidence:** moderate to high. The main uncertainties are the annotators' choice of length frame and the frame rate.
