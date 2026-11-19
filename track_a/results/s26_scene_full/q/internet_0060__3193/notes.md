# q_3193 — displacement of the box, 0.00 s → 2.00 s

- Times: frame 0 and frame round(2.00×30) = 60. The file's 30.014 fps gives the same frames.
- The box (pink packet) is held at the left edge until frame ~52, then falls along image +x. The clip is rotated 90°, so image +x is down. It hits the floor strip at frame 65.
- Scale from gravity: I fitted a quadratic to the packet's x position over the free-fall frames 53-64 (fit.py, using scene/tracks/packet.csv).
  The pixel acceleration comes out at 9400-10600 px/s² depending on the point and the frame window
  (bbox_cx 9956, centroid 10259; second differences excluding the release and impact frames give 10125).
  I used a = 10100 px/s², so the scale is 9.8/10100 = 9.70e-4 m/px. As a check, the 100 px packet comes out at about 9.7 cm, which is plausible.
- Positions:
  - Frame 0: the packet spans x ≈ 45–138, y ≈ 540–645 (checked visually in frames/f0.png; the fingers cover the left edge), so its centre is about (85–90, 592).
  - Frame 60: the blurred packet spans x ≈ 564–675, so its centre is about (617, 606).
  - Pixel displacement ≈ 527–539 px. The camera drifts −9 px in x by frame 60; correcting for it adds about 9 px. I took 535 px.
- Displacement = 535 × 9.70e-4 ≈ 0.52 m.
- Second route: the leading (right) edge moves 131 → ~670 px (539 px), which gives 0.52 m.
- Confidence: moderate. The main uncertainty is the fitted pixel acceleration (±5%).
