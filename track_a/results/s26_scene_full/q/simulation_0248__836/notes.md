# Q836: speed of the front horse at 1 s (m/s)

- I treated the clip as 2D: a side view, a static camera and motion along image x. Both fps values are 24, so t = 1 s is frame 24.
- Front horse = horse_dun (the larger, light-brown one on the right). Back horse = horse_red. Prior: back horse speed = 0.874 m/s.
- The scene/ tracks for both horses cover frames 0-49 and match the frames on the sheet. Red frame 49 is a loop reset, so I excluded it.
- Both horses walk at a steady pace. I took the speed as a linear fit of x against frame (fit.py), which averages out the gait wobble:
  - Torso centroid: red 3.224 px/frame, dun 5.927 px/frame. Ratio 1.838 gives 1.607 m/s.
  - Mask centroid: red 3.219, dun 5.934. Ratio 1.843 gives 1.611 m/s.
  - x_max: 1.632 m/s. bbox centre: 1.650 m/s.
  - A window of frames 12-36 around t = 1 s gives 1.58 (torso) and 1.65 (centroid). The spread comes from gait phase, so the full-clip fit is the stronger estimate.
- Scale: one metres-per-pixel factor = 0.874 / (red px speed). The hoof rows (630 and 634) are nearly the same, so the depth difference is small. This may bias the answer by a few percent at most.
- Answer: 1.61 m/s. Confidence: moderate-high (about ±4%).
