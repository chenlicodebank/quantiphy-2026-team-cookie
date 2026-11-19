# q_2823: width of the book (cm)

Book = the static white package with green print ("notebook" in scene/), lying flat on the floor and rotated about 30° in
the image. File fps = question_fps = 24, so t = 0.4 s is frame 10. f = 0.5959*1280 = 763 px, principal point (640, 360).
Depth of the book at 0.4 s is 2.082 m. The prior (bin velocity) is not needed for a size.

## Measurements (book_mask.py, geom.py, rectify.py, rect_mask.py)
- Book mask: the median of 6 frames with chroma green removed. Its convex-hull corners (px) are A(630,590), B(669,578),
  C(701,636) and D(660,653). The short edges are AB = 40.8 px and DC = 44.4 px. The long edges are AD = 69.8 px and
  BC = 66.2 px. The image min-area rectangle is 47.3 x 78.5 px.
- Floor plane: the centres of the book, cup and basketball were back-projected with their given depths. The plane was
  solved with assumed centre heights of 1-3 cm (book), 7.5 cm (cup) and 12 cm (ball). That gives a camera depression of
  about 36°, roll about 0 and camera height about 1.7 m. Check: the bin centre then comes out 8.5 cm above the floor,
  which is plausible.
- Route 1 (rectification): the hull corners were intersected with the floor plane at the top-face height (2 cm). That
  gives AB = 11.3 cm, DC = 11.5 cm, AD = 20.1 cm and BC = 19.3 cm. The corner angles are 88-93°, so the shape is close to
  a rectangle. The rectified centre is at a distance of 2.097 m, against the given 2.082 m. The width hardly depends on
  the plane height or tilt (11.2-11.7 cm), because the short edge lies mostly horizontal in the image.
- Route 2 (method card): 2.082 x pixel extent / 763. The short edges give 11.1 cm (AB) and 12.1 cm (DC), mean 11.6 cm.
  The axis-aligned min-area rectangle gives 12.9 cm. It overestimates because the hull is not a perfect rectangle (side
  faces and rounded corners). A min-area rectangle fitted on the floor plane gives 12.7-13.3 cm for the same reason.

## Answer
Width (the shorter horizontal side) is about **11.5 cm**. Length is about 19.5-20 cm (it includes a little of the side
face). Confidence is moderate, about ±1 cm: the edges are only about 42 px long and the segmentation edges are soft.
