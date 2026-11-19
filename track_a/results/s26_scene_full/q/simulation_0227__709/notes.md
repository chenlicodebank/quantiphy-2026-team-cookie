# Q709: speed of swimming ring (flamingo float) at t = 0.5 s

- 2D video, static camera, 24 fps (file and question rates are the same), so t = 0.5 s is frame 12.
- Scale comes from the prior (cat speed 1.041 m/s). The cat walks at a steady speed:
  - scene body centroid: 5.378 px/frame on average over frames 0–49;
  - my own 8-frame template matching of the cat (check.py): 5.465 px/frame, with 11 windows ranging 5.24–5.68.
  - I used 5.42 px/frame = 130.1 px/s, so the scale is 1.041 / 130.1 = 0.00800 m/px.
- Float speed at frame 12, from the one-frame backward difference |p12 − p11|:
  - scene record (ref_cx and ref_cy from template matching): 9.80 px/frame;
  - my independent template match of frame 11 → 12 (check.py): 9.87 px/frame. The neighbouring steps rise smoothly (9.43, 9.87, 10.25).
  - I used 9.83 px/frame.
- Answer: 9.83 / 5.42 × 1.041 = 1.888 m/s.
- Caveat: the cat stands slightly behind the coping and the float is in front of it, so their depths differ a little. The video is 2D and I could see no strong perspective, so I used one scale for both. Taking either estimate of the cat's speed alone moves the answer by about ±1%.
- Confidence: good, within about 3–5%.
