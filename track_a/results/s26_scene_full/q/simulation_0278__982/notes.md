# Q982: whale displacement from 0.5 s to 1.0 s

- 2D top-down render at 24 fps (the file and question_fps agree). t = 0.5 s is frame 12 and t = 1.0 s is frame 24.
- Motion: the whale translates rigidly to the left at constant speed from frame 1 onward. Frames 0 and 1 are identical. Track: blowhole template in scene/tracks/whale.csv.
- Blowhole x is 990.43 at frame 12 and 919.92 at frame 24, so the displacement is 70.51 px. y stays constant.
- Scale: the prior speed is 1.67 m/s. The mean per-frame step over frames 1–71 is 5.870 px, which is 140.88 px/s, giving 0.011854 m/px.
- Displacement = 70.51 × 0.011854 = 0.836 m. This equals 1.67 × 0.5 = 0.835 m, as expected for constant speed.
- Second route (check.py): phase correlation on the head region gives 69.8 px for frame 12 → 24 (0.827 m), and per-frame shifts of 5.83–6.00 px. The two routes agree within 1%.
- Answer: 0.835 m. Confidence is high.
