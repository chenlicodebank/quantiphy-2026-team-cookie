# q3189 — length of the pink box (cm); prior g = 9.8 m/s^2

Scene: the clip is rotated 90 deg. Image +x is "down". The pink packet is dropped at frame ~52 and falls along +x
until it hits the floor strip at frame 65. It rests from frame ~78 at about (1383, 969).

Time base: the file is 30.014 fps and the question says 30. The difference is negligible, so I used 30 fps.

Pixel acceleration (fit.py, scene track checked against the frames):
- Quadratic fits of the x position (camera-corrected centroid, bbox centre, raw centroid) over windows between
  frames 53 and 65 give 10.7–11.8 px/frame^2. The core window 53–64 gives 11.4 (centroid) and 11.1 (bbox).
- The mean second difference over 52–65 is 11.75. The per-frame increments shrink slightly later in the fall
  (drag on a light packet).
- Adopted value: 11.3 px/frame^2, which is 11.3 x 900 = 10170 px/s^2.
- Scale = 9.8 / 10170 = 9.64e-4 m/px.

Box length: measured along the main motion direction (x) on the clear rest frames 79–99. The bbox is 99.9 x 99.5 px
and the minAreaRect is 98.9 x 98.4 px. A zoomed crop of frame 87 confirms about 97–100 px. During flight the
blur-free width is about 97–100 px too. Length = 100 px.

Length = 100 x 9.64e-4 m = 9.64 cm, so the answer is **9.6 cm**.

Second check: the box is square, so either side gives the same length. Using the full range of acceleration
estimates (10.7–11.8 px/frame^2) puts the answer between 9.2 and 10.2 cm. A real snack packet of about 9–10 cm is
plausible.

Confidence: moderate-high. The main uncertainty (about ±5%) is which window the annotator used for the
acceleration.
