# q_2457 — width of the book (cm)

Lab video, 1280x720, 24 fps; question_fps 24, so the file rate and question rate match. f = 0.5959*1280 = 762.8 px, principal point (640,360).
Prior: book acceleration is 2.8 m/s^2 at t=1.0 (not needed for a size). depth_info: book 1.0685 m at t=1.0 and 0.977 m at t=1.2;
slope far 1.243 m, slope near 0.990 m; table left 1.035 m, table right 0.573 m.

The book is a light-blue cover with cream pages and a ribbon. It lies flat on the white ramp board. Its long side runs across the ramp (horizontal
in the image) and its short side runs down the slope. "Width" = the short side of the cover.

## Geometry (scripts: board.py, vp.py, vp2.py)
- I fitted the ramp board's 4 edge lines on frame 48 and took their vanishing points. With f = 763 the two board directions
  come out 89.1 deg apart, which confirms the focal length (600 px gives 80 deg, 1000 px gives 77 deg). Up-slope direction d = (0.739,-0.506,0.444),
  across direction u = (0.514,0,-0.858). The book's own left edge gives the same d to within 0.6 deg.
- Plane offset: the given far-slope depth (1.243 m, at the far/top-left board corner) and near-slope depth (0.990 m, at
  the middle of the bottom edge) give the same plane constant (-0.3934 vs -0.3936). The book centre at t=1.0 (depth 1.0685) is then
  1.2 cm above the board, which is consistent with a book about 1.5–2 cm thick. A depth-only slope direction disagreed by 12 deg, but that
  rests on guessed click points; the vanishing-point direction was used instead.
- The ramp is inclined 30 deg to the table. a = 2.8 implies mu ~ 0.25, which is plausible.

## Width measurement (width_ramp.py, width_ramp_check.py)
Frames 0–17 (book at rest on the ramp) were averaged. In code I found:
- the cover's far edge (top silhouette against the black background, half-level crossing, rms 0.11 px), and
- the cover's near edge (the dark shading line where the cover meets the page block, rms 0.14 px; the cover/rim
  boundary sits about 1 px above the line's centre).

I fitted lines to both, back-projected them onto the cover-top plane (board plane + book thickness T) and took the
in-plane perpendicular distance between the two 3D lines:
- near edge at the crease centre: 8.9 cm (T 1.5–2.0 cm: 8.98–8.86)
- near edge 1 px higher (cover boundary): 8.6–8.7 cm  <- adopted
- near edge at the rim top (2.5 px higher): 8.2–8.35 cm (lower bound)
- independent of the crease: top silhouette to the book's bottom contact line (on the board plane). This gives 8.0–8.9 cm
  depending on T; with T ~1.7 cm it gives 8.55 cm, plus ~0.3 cm cover overhang.
- If the plane is anchored on the book's own depth instead (centre exactly T/2 above the board), the result is about 1 % smaller (8.57).
Long side for reference: 19.3–20.0 cm.

## Second route: book at rest on the table (width_table2.py, rect_table.py)
- Table plane normal comes from the table-edge vanishing points (88.3 deg apart). The offset comes from the board's bottom edge.
- The top face's corners were found from 4 fitted edge lines. Short sides: 8.0 and 8.2 cm; long sides: 18.6 and 19.4 cm. W/L = 0.43, the same as on the ramp
  (8.7/19.5 = 0.44).
- This view is near-grazing (about 10 deg elevation) and ill-conditioned: a 3 deg tilt of the plane changes W/L from 0.43 to 0.58.
  The table depth_info values do not fit table corners (0.573 m cannot be the right corner), so I used this route only as a loose check:
  about 8.0–8.4 cm.

## Answer
Width ≈ 8.6 cm (ramp route, cover-edge definition). Estimated uncertainty ±4 %. Confidence: moderate. The main risks are which
image line counts as the cover's near edge (±1 px ≈ ±3 %) and the depth scale (±1–2 %).
