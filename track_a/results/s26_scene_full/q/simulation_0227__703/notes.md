# Q703: black cat length including the tail

- This is a 2D video. The camera is static and the cat walks to the right at a steady pace, parallel to the image plane. The file runs at 24 fps, which matches question_fps.
- **Pixel speed.** I fitted a line to x against frame for each reference point in scene/tracks/cat.csv (speed.py). I checked visually at frame 24 that the cat's box is right: tail at x≈650, nose at x≈750.
  - body centroid: 5.39 px/frame
  - mask centroid: 5.50 px/frame
  - box centre: 5.53 px/frame
  - left edge (x0): 5.45 px/frame
  - right edge (x1): 5.62 px/frame
  - I used about 5.47 px/frame, which is 131.3 px/s.
- **Scale.** 1.041 m/s ÷ 131.3 px/s = 0.00793 m/px.
- **Length.** The cat's horizontal box, tail included, has a mean width of 98.7 px (median 98.5, range 87–111). This gives 98.7 × 0.00793 ≈ 0.78 m.
- **Alternatives.** Rump to nose (84.5 px) would be 0.67 m. The largest box width (111 px) would be 0.88 m.
- **Check.** Using the body-centroid speed instead gives 0.0080 m/px and 0.79 m. A real cat measures about 0.75 m including its tail, which is consistent.
- **Confidence:** moderate. The tail is held up, so the horizontal extent depends on the cat's pose.
