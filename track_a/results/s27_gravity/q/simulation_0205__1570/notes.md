# Q1570: height of the typewriter (m). Answer: 0.193 m

The file and question_fps are both 24. The camera is static and the typewriter does not move. I used the last frame (29).

## Camera (fitfall.py)
- The camera is a pinhole with its principal point at the image centre. The magnifier is placed at frame 0 using its depth (4.2401 m) and its pixel position.
- The model is a free fall at g = 9.8 along an unknown "down" direction g_hat, with a free v0 and a small horizontal drift.
- The fit used the bbox-centre pixel track for frames 0–11. It was constrained so that the frame-12 point (depth 4.4097 m) lies on the trajectory horizontally. The vertical drop is not constrained there, because of the bounce.
- Result: f = 2636 px (hfov 44°). The camera pitches down about 13.4°. Pixel residuals are under 0.6 px.
- The drop from frame 0 to frame 12 is 1.05 m. A free fall to impact at about frame 11.2 gives about 1.08 m, so these agree.

## Check against the desk (desk.py, rect.py)
- I placed the near desk corner (697,893) at 3.593 m and the far-right corner (1993,657) at 5.009 m. With g_hat, their heights agree within 1.6 cm, so the "far right" corner is the front-right one.
- I then put the other two corners on that plane. The four corners form a rectangle with angles of 91.2, 92.5, 85.6 and 90.6°. The desk measures 2.45 × 1.05–1.13 m: a large desk, but self-consistent.

## Typewriter (profile.py, rowprof.py, height2.py)
- From pixel profiles:
  - Rear-left bottom corner, the leftmost point of the outline on the desk: (859,703).
  - Front-left bottom: (940,757). Front-right bottom: (1147,723).
  - Top of the paper rest: y = 590 at its left end (x = 861), y = 573 at x = 1000.
- On the desk plane, the footprint is 0.375 × 0.325 m with a corner angle of 88.6°, which is plausible.
- Height = the vertical line above a base point that projects onto the top pixel.
  - Above the rear-left corner: 0.194 m. The predicted top u is 857 against 861 observed, so the paper rest sits directly above the rear edge.
  - Second route, the top at x = 1000 above a point on the rear edge: 0.192 m.
- Robustness:
  - Fits using the lens-centre or mask-centroid tracks (f ≈ 2645–2651, different tilt): 0.191–0.194 m.
  - Moving the desk-plane height by 3 cm changes the result by less than 0.005 m.
  - A ±5 cm uncertainty in where the top sits front-to-back gives ±0.012 m. The edge alignment argues against a large offset.

Answer: 0.193 m (paper-rest top to base). I'm moderately confident, at about ±5%.
