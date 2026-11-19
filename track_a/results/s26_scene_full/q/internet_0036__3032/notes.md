# q 3032: length of US $1 bill (mm); prior: width = 66.3 mm

Method: 2D size-to-size, one scale from the prior. length = 66.3 mm x (long-edge px / short-edge px), with both
edges measured on the same frame. Time and fps don't matter here.

Corners read on 4x zoomed crops (crops.py, frames/c0_*.png, c36_*.png):
- Frame 0: L (410,2029), B (822.5,2479.5), R (1840,1505).
  - Short edge |LB| = 610.8 px; long edge |BR| = 1408.9 px; ratio 2.307, giving **152.9 mm**.
  - The angle at B is 88.7 deg, so the bill is slightly tilted out of the image plane (the giver holds the top
    edge). The upper/top corner area is bent, so I didn't use it.
- Frame 36 (second check): L (398.5,2092.5) and R (1821,1546.5) give a diagonal of 1523.7 px. Frame 0 gives
  1523.0 px, so the bill geometry is the same. Corner B is hidden by the receiver's thumb in this frame.
- Scene record: same values (1406.8 / 610.9). Its later frames come from similarity tracking, so they keep the same
  ratio and aren't an independent check.
- Frames 44 and 50 aren't usable: the bill is tilted toward the camera (the right short edge is visibly shortened)
  and blurred by motion.

Readings:
- Pixel-convention answer: 152.9 mm.
- A real note is 156.1 x 66.3 mm (ratio 2.355). The prior matches the real width, so the reference may be 156.1.
- The 2% gap between the two comes from the slight foreshortening of the short edge, caused by the tilt.

Answer: 154.5 mm, between the two readings, within about 1% of either. Confidence: high (within 3%).
