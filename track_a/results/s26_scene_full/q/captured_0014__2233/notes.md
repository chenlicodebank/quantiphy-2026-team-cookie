# Q2233: cookie diameter (cm)

The file is 24 fps and question_fps is 24, so frame = t x 24. The cookie is static: it leans against the front of the white cup at the back-left of the table.

## Method (lab method card)
- f = 0.5959 x 1280 = 762.75 px, depth at t=0 = 1.7355 m (depth_info, distance from camera to the cookie centre).
- Pixel diameter measured in code (`edges.py`), on rows 384–400 and columns 478–495 of a crop at x 440–540, y 340–440:
  - left edge = where saturation rises from the white cup (S > 90), at x ≈ 469–470
  - right edge = the dark rim/shadow before the white board, at x ≈ 503
  - top edge = where saturation rises against the cup, at y ≈ 376
  - bottom edge = the dark rim against the table, at y ≈ 409–410
- Horizontal width: the 3 widest rows give 33.3 px (frame 0) and 34 px (frames 20/40/48). Vertical height: 33–34 px on the clean columns. The larger values at x > 491 are the dark band at the board edge, not cookie.
- The cookie looks round (same width and height), so the diameter is 33.8 ± 0.5 px.
- Diameter = 1.7355 x 33.8 / 762.75 = 0.0769 m = **7.69 cm**.

## Checks
- The second route is the vertical extent, which gives the same 34 px. The measurement is stable across frames 0, 20, 40 and 48. The scene/ record's 36 px bbox was read by eye and includes the edge blur, so I did not use it.
- Sanity check: a typical cookie is 7–8 cm across. The cup comes out at 41 px → 9.3 cm wide, which is plausible.
- The prior (ball acceleration) is not needed: the scale comes from depth_info plus the fixed focal length.

Confidence: good (about ±3%). The main uncertainty is ±0.5 px in the edge positions.
