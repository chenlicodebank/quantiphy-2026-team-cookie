# Q44: speed of the yellow car at 2.5 s (m/s)

- This is a top-down 2D scene. There is only one vehicle: a yellow/peach sedan, tracked in scene/tracks/car.csv. t = 2.5 s is frame 60 at 24 fps (the file's fps and question_fps are both 24). At that frame the car is finishing its right turn, with heading about 1°.
- **Scale:** the prior gives car length = 5.44 m. The car's mean PCA mask length is 222.5 px. Its horizontal bbox length at frames 64–71, where heading is about 0°, is 220.4 px. Using 222.5 px gives 0.02445 m/px.
- **Speed** (measure.py): I fitted quadratics to the positions around frame 59.5–60.
  - Centroid: 6.81–6.82 px/frame over the windows 52–68, 56–64 and 55–71.
  - Mid-point of the front and rear axis ends: 6.81–6.87 px/frame.
  - Front and rear ends: 6.79–6.91 px/frame.
  - The mean raw step over frames 50–70 is 6.79 px/frame. The speed is almost constant over the whole clip, at 6.74–6.90 px/frame in every 10-frame block.
- **Result:** 6.81 px/frame × 24 / 222.5 px × 5.44 m ≈ 4.00 m/s. Using the 220.4 px bbox length instead gives 4.03 m/s.
- **Second route:** the clip-wide mean step of 6.81 px/frame gives the same 4.0 m/s.
- **Confidence:** high, about ±2%.
