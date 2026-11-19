# q_1894: height of the small elephant (m)

- 2D side-view clip, 24 fps (fps = question_fps, so there is no re-timing), white background. Both elephants walk right on a common ground line at y ≈ 692 px, so they are at the same depth and one m/px scale applies to both.
- `measure.py`: mask is darkest RGB channel < 230; components under 30 px are dropped; the two animals are split at the widest empty column gap. Output is in `meas.csv`.
- **Big elephant speed in px:**
  - Linear fit of the mask centroid x: 7.008 px/frame.
  - Mean per-frame 2D centroid step: 7.07 px/frame.
  - Trunk-front x fit: 7.06 px/frame.
  - Used 7.04 px/frame, which is 169.0 px/s.
- **Scale:** 2.313 / 169.0 = 0.01369 m/px.
- **Small elephant height:** median 153 px across 60 frames (range 148–158, from the walk cycle). 153 × 0.01369 = **2.09 m** (range 2.03–2.16).
- **Second route:** the big elephant's height is 228 px, which gives 3.12 m. That is a plausible adult elephant, and a calf/adult ratio of 0.67 is consistent. The centroid and trunk-front speed estimates agree to within 1%.
- **Confidence:** fairly high. The main uncertainty is the walk-cycle height variation (±3%) and the reference point used for speed (±1%).
