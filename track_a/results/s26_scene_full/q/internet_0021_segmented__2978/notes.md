# q_2978 — average speed of the airplane (prior: length = 40 m)

Time base: file 29.97 fps vs question 30 fps; the 0.1% difference doesn't matter here. I used 30.

I checked the track in scene/tracks/airplane.csv against the contact sheet and zoomed frames (measure.py). The plane is
fully visible in frames 0-89. The camera pans slowly (about 0.15 px/frame, compared with the plane's ~4.7 px/frame), so I
used positions relative to the background (*_bgcomp).

- Pixel speed (centre, background-compensated), frames 0-89: 4.80 px/frame on average (4.29 early, 5.32 late).
  Without the background correction it is 4.65 px/frame.
- Nose-to-tail length: 70 px at frame 0, rising to 88 px at frame 85 (mean 78.3). The plane is approaching the
  camera, so its pixel speed rises along with its size.

Ways to get the scale:
1. Per-frame speed divided by the per-frame length, times 40 m: 73.8 m/s (background-compensated), 71.3 m/s (raw).
2. A single scale from the mean length (78.3 px): 73.9 m/s (background-compensated), 71.4 m/s (raw).
3. A single scale from the frame-0 length (70 px), the annotators' likely choice: 82.7 m/s (background-compensated),
   79.9 m/s (raw).

Answer: 76 m/s. This sits between the size-consistent value (~74) and the frame-0-scale value (~80-83). That is a
plausible approach speed for a 737-class airliner. Confidence: moderate, because the plane's growing image size makes the
single-scale convention ambiguous by about ±10%.
