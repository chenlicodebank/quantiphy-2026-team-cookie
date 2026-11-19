# q_3072: distance between the kettle and the plate (cm)

- The "white ball" in the prior is the small white ball (the record calls it an egg) rolling right to left. The "plate" is the white wavy bowl at the far left, and the kettle is the red Tefal kettle.
- Time base: the file and the question both run at 30 fps, so t = 1.0 s is frame 30.
- Pixel speed at frame 30: I used the drift-corrected track in scene/tracks/egg.csv. The forward difference x(31) − x(30) is 44.8 px/frame. A linear fit over frames 27-34 gives 45.05 px/frame. Speed ≈ 1344-1352 px/s.
- Scale = 33.38 / 1348 ≈ 0.0248 cm/px (a single planar scale, following the internet-video convention).
- Object extents at frame 30, from my own colour segmentation (measure.py; checked in frames/boxes.png):
  - kettle bbox [1164, 479, 1520, 766]
  - bowl bbox [125, 602, 509, 772]
  - These agree with the record's frame-0 boxes to within 7 px.
- Centre-to-centre distance between the boxes: 1022-1027 px, which is 25.2-25.5 cm (the horizontal part alone is 25.2-25.5 cm).
- Other reading: the edge-to-edge gap is about 649 px, or 16.1 cm. I did not use it, because "distance between" objects is taken centre to centre.
- Answer: **25.3 cm**.
- Second route: the record's boxes and my own segmentation, each combined with either speed estimate (forward difference or fit), give results within ±0.6%.
- Confidence: medium. The main uncertainty is which reference point the annotators used on each object (bbox centre vs. kettle body centre; the body centre would give about 24 cm). The real-world size implied by this scale is small (the ball would be about 2 cm), but the prior sets the scale.
