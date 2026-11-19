# q_2436 – length of the book (cm)

Answer: **17.0 cm**

The "book" is the cyan notebook that slides down the white ramp. It is the only moving object, as tracked in scene/tracks/blue_notebook.csv.
Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360). The file fps and question_fps are both 24, so t = 1.0 is frame 24 and t = 1.2 is frame 29.

## Why the naive card formula is not enough
The book's long edge appears roughly horizontal in the image, but it lies across the inclined ramp. That direction points
strongly into depth (its z component is about -0.75), so the projected length is heavily foreshortened. At frame 24 the long edge is about 80–88 px.
Applying depth x px / f directly gives only about 12 cm. The short edge (about 45–55 px) runs down the slope.
On the table (frames 36–48) the book lies diagonally. Its cover corners are about (497,468), (548,462), (645,479) and (596,487): a long edge of about 100 px
and a short edge of about 50 px. The 150 px bbox in the scene record is the diagonal span, not the length.

## Method (3D plane back-projection)
- Book centre at frame 24: (750.6, 397.3) at 1.0685 m. At frame 29: (670.3, 451.9) at 0.977 m. Both back-projected.
  Their difference gives the slide direction D down the ramp. At frame 29 the centre is still on the ramp, about 30 px above its foot.
- Across-ramp direction A: perpendicular to D and lying in the viewing plane of the ramp's top edge, (757,360)-(858,361).
  The ramp normal is N = D x A.
- Cover corners were read on zoomed frames:
  - Frame 0 (sharp, at rest): (755,352.2), (843.3,352.5), (807.5,385), (720.3,380).
  - Frame 24: (722.9,374.3), (811.4,380), (770,412), (689.3,400.7).
- The corners were intersected with the cover plane. That plane is parallel to the ramp and passes through the book centre, offset by half the thickness (0–1 cm).
  The frame-0 centre lies on the slide line through P24 (depth 1.125 m).
- Results with D from the book depths (ramp-plane parameter about -39 deg):
  - Frame 0: L = 17.1 cm, W = 10.5 cm.
  - Frame 24: L about 16.9–17.6 cm, W about 9.2–9.6 cm.
  (scripts: rect_fit.py, f24_check.py)

## Cross-checks and spread
- If D comes instead from the slope far/near depths (1.243 m and 0.990 m, taken at the ramp edge midpoints): L = 15.6–15.9 cm.
- If the ramp board's own rectangle fixes the plane (vanishing points; ramp_rect.py): L = 17.6–19 cm.
  However, that plane predicts a frame-29 depth of 1.009 m against the given 0.977 m, so it disagrees with the given depths.
- The table distances (left 1.035 m, right 0.573 m) cannot be the table corners: they would put the camera about 8 cm above the table,
  which contradicts the view. So the table was not used (table_plane.py).
- The ramp acceleration measured with any D is about 2.0 m/s^2, against the 2.8 prior. It is insensitive to D, so it does not discriminate between the planes (accel_fit.py).
- Final value: 17.0 cm, the estimate tied to the question's own book depths. The other routes span about 15.8–18.5.
  Confidence: moderate, about ±8%.
