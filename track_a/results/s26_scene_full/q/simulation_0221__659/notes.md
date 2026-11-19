# q_659: speed of the vacuum cleaner at t = 0.5 s

- The clip is a 2D top-down render at 24 fps, and question_fps is also 24, so no re-timing is needed. t = 0.5 s is frame 12, and speed = |p(12) - p(11)| x 24.
- **Pixel step.** I re-measured with `measure.py`: frame 12 is the template, and I matched it in frames 6-15 with normalized cross-correlation and a sub-pixel parabolic peak (scores 0.97-1.0).
  The steps are 10.15, 11.29, **12.29**, 13.26, 14.28 px/frame for frames 10-14. The vacuum accelerates smoothly, at about 1 px/frame².
  The circle-fit track in the scene record gives 12.46 for frame 12. That track is noisier: its neighbouring steps are 11.28 and 13.10. I used the template value, 12.29 px/frame.
- **Scale.** The prior gives a diameter of 0.438 m. The vacuum's apparent diameter is 122.7 px near frame 12 (x ≈ 1600) and about 120.5 px near the image centre, where the side wall does not inflate it. I used 122.0 px, which gives 0.003590 m/px.
- **Speed.** 12.29 x 24 x 0.003590 = 1.059 m/s. Choosing a diameter between 120.5 and 122.9 px moves this between 1.05 and 1.07.
- **Second route.** The track's circle-fit step gives 12.46 x 24 x 0.00359 = 1.07 m/s. Averaging the steps either side of frame 12, (11.29 + 13.26) / 2 = 12.28, gives 1.058.
- **Answer: 1.06 m/s.** Confidence is high, within about 2%.
