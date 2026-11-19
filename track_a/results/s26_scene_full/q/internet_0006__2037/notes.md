# q_2037 – average speed of the white car (prior: lane width = 3.66 m)

Static top-down drone shot (the background drifts by 1.7 px at most), so image motion is ground motion.

Scale: I took brightness profiles across the road at frame 120, averaged over 60-row bands at y = 300, 700,
1000, 1300 and 1600 (profile.py). Left asphalt edge x ≈ 522.5, centre line x ≈ 559, right edge x ≈ 598.
Left lane = 36.5 px, right lane = 39 px, so one lane = 37.75 px (half of the 75.5 px road).
Scale = 3.66 / 37.75 = 0.0970 m/px.

Motion: I used the white-car template-match track from scene/ (frames 0–152, while the car is fully in frame;
it agrees with the mask centre to within about 1 px). The mean per-frame displacement is 8.69 px/frame; the net
displacement is the same (1386 → 83 in y, nearly straight). Second route, by thirds of the path:
8.57, 8.66 and 8.83 px/frame, a slight rise toward the top that is probably wide-angle stretch near the frame edge.

Time base: question_fps is 30 and the file runs at 29.68 fps; they differ by 1 %. I used 30.
- 8.69 × 30 × 0.0970 = 25.3 m/s
- at 29.68 fps: 25.0 m/s

Answer: 25.2 m/s (about 56 mph, plausible on a country road). Confidence is moderate. The main
uncertainty is how the annotator measured the lane width in pixels: anything from 36.5 to 39 px gives a
spread of about ±3 %.
