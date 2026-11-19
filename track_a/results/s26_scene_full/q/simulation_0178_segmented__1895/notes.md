# Q1895: displacement of the big elephant

**Data.** This is a 2D clip at 24 fps with 60 frames (t = 0 to 2.458 s). question_fps is also 24, so there is no re-timing issue. The prior is the big elephant's speed, 2.313 m/s. There is no depth_info.

**Reading of the question.** "Displacement" means the net straight-line displacement of the big (adult) elephant from the first frame (0) to the last frame (59).

**Measurement** (`check.py`, run on `scene/tracks/adult.csv`):
- The mask centroid x moves at a steady 7.008 px/frame. A linear fit leaves a residual of only 1.5 px std, which is leg-swing jitter.
- The slopes for the first and second halves are 7.18 and 7.00 px/frame, so the speed is constant.
- The vertical bob is 8 px. The path is straight and horizontal, with no stops or turns.

**Answer.** The motion is uniform and straight, so displacement = speed × elapsed time = 2.313 × 59/24 = **5.686 m**.

**Second route.** I took a scale of 2.313 / (7.008 × 24) = 0.01375 m/px from the prior. I applied it to the net centroid shift between frame 0 and frame 59 (416.3 px), which gives 5.72 m. Using the bbox centre (418 px) gives 5.75 m. Both are within 1% of the first route; the small difference is the walk-cycle phase at the end frames.

**Confidence:** high. The main risk is if the reference used a different time window.
