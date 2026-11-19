# q_1844 — smallest horizontal distance between the two cars

2D top-down video at 24 fps (question_fps is also 24). One metres-per-pixel scale applies everywhere.

**Scale:** the prior gives the black car's speed as 26.085 m/s. Its mean per-frame step (template-fit centres from
scene/tracks, clean frames 4–45) is 27.13 px/frame, std 0.6, so the speed is close to constant. That makes
651 px/s and 0.0401 m/px. Using frames 2–48 instead gives 27.17 px/frame and 0.0400 m/px.
Sanity check: the car lengths come out at 4.6 m (dark) and 5.0 m (silver), which is plausible.

**Distance:** the distance between the two centres grows steadily from the first frame (86.5, 86.2, 90.8, 94.8,
98.3, 102 px …) up to about 218 px. So the minimum is at the start (frames 0–1, which are a duplicated first
render), at about 86.2–86.5 px. I checked the frames visually: frame 0 has both cars side by side at the top
edge, and in frame 5 the centres are about 100 px apart.

**Second route:** the centres in frames 0–1 depend on a template fit, because the cars are clipped by the top
edge. Extrapolating the clean trend in frames 2–5 back to frame 1 gives 86.8–87.2 px. That agrees within 1 %.

**Answer:** 86.5 px × 0.0400 m/px ≈ 3.46 m (range 3.45–3.49). Confidence: good, about ±2 %.
