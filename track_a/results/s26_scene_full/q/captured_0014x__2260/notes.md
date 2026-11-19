# Q2260 – width of the book (cm)

Lab video, 1280x720, 24 fps (same as question_fps). f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
Scale: depth_info distance_book_camera = 1.6650 m at t = 0 (the book does not move; it is static in every frame).
The prior (ball acceleration) is not needed for a size.

## Object
The "book" is the light-blue notebook on the right of the table (centre about (653, 410) px). It lies flat. Its short
side runs almost left-right in the image (the back edge goes from about (626, 390) to (663.5, 384.5)). Its long side
recedes from the camera (the left side goes from about (626, 390) to (640, 434)). Width = the short side.
scene.json's corners (627,388)/(660,384)/(682,432)/(643,437) agree to within 2-3 px.

## Measurements
- measure_book4.py: mask of the bright cover (blue > 175 or 190); line fits to both long sides and the back edge.
  Frames 0, 20, 40 and 48. The horizontal row width is 40.6-41.1 px. The short side's image length is 39.0-40.1 px.
  Treating the cover as a rectangle on the table plane and correcting for its in-plane rotation (theta about 9-13°)
  gives 39.8-40.5 px, i.e. 8.68-8.84 cm (mean 8.73 cm).
- Corners read by eye on a 10x crop (crop.py, frames/book_raw.png), including the light page edge:
  - back edge 37.7 px, front edge 42.7 px; the midline between the side midpoints is 40.25 px, which gives 8.79 cm.
  - The parallelogram analysis (view about 46° down, rotation about 15°) gives a true short side of about 41 px,
    i.e. 8.94 cm.
- The R−B<50 mask (measure_book2/3) also takes in the dark outline and shadow, and gives 45-50 px. Rejected: on the
  zoomed frame, those pixels lie outside the book.
- Size = 1.665 m x px / 762.8: 40 px gives 8.73 cm, 41 px gives 8.95 cm.

## Answer
8.8 cm (range 8.7-8.95). The long side comes out at about 13-14 cm, so the notebook is pocket-sized (about 9 x 14
cm), which is plausible. Confidence: moderate-good; the uncertainty is about ±1 px of edge (±2.5%).
