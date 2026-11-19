# q_2261 – height of the book (cm)

Video: lab capture, 24 fps (file and question rates agree), 1280x720, f = 0.5959*1280 = 762.75 px, c = (640, 360).
The prior (ball acceleration 4.6 m/s^2 at t=0.6) is not directly about the book; scale comes from the depth_info
(book centre at 1.665 m at t=0) and the lab focal length.

## What "height" means here
The light-blue notebook lies flat on the right of the table, so its height is its vertical extent, i.e. its thickness.
It is seen as the thin front face (cream page block under a dark cyan cover-edge line) below the top cover.

## Measurements (median of frames 30-48, when the ball is gone; the book is static)
- `edge_profile.py`: per-column sub-pixel minima of the two dark lines bounding the front face (cols 646-675).
  Top line (top-cover edge): y = -0.1763x + 545.49. Bottom line (bottom edge/contact shadow): y = -0.1738x + 550.02.
  Separation 6.18 px (6.14-6.22 across the columns).
- `face_zoom.py`: colour profile across the face. Cyan top face -> dark cyan cover edge (centre 0) -> cream pages
  (B/R about 0.97) -> wood hue from about +5.2, darkest contact shadow at +6.1. Face extent: about 6.0-6.9 px depending
  on where the edges are put. Used 6.3 ± 0.4 px.
- Foreshortening of a vertical segment depends on the camera's elevation seen from the book:
  - `table_sil.py`: the table outline fitted in code against the white background (left/right sides plus front edge,
    rectangle assumption) gives table normal (-0.065, -0.884, -0.462) and elevation 33.0° (stable 32.5-33.2° over
    row windows). That is 4.06 px per cm of vertical extent at the front face (depth there is about 1.60 m: a ray hits
    the plane through the book centre at 1.665 m).
  - Table corners read by eye in scene.json give 37° (3.85 px/cm). The code fit is preferred.
  - Ramp check (`ball.csv` + depths at t=0 and 0.6): with the 33° normal the board slopes 31°, which allows up to
    5.05 m/s^2. A steeper camera (≥ 40°) makes the ramp too shallow to reach the prior's 4.6 m/s^2, so it is ruled
    out. The pen and book depths (book centre about 0.4 cm above the pen centre) also fit 33-35°. The cookie and cup
    depths point steeper, but those are surface depths of tall objects and are unreliable.
- `book_dims.py`: the book's top face at 33-37° is about 9 x 17-18 cm, a plausible slim notebook.

## Result
height = 6.3 px / (3.85 to 4.06 px/cm) = 1.55-1.64 cm. With the pixel-extent range (6.0-6.9 px) the band is 1.48-1.79 cm.
Answer: **1.6 cm**.

Second route: min-to-min dark-line separation 6.18 px with the 33° normal gives 1.52 cm; the 37° normal gives 1.60 cm.
The naive lab-card formula without tilt correction (1.665 m * 6.3 / 763) gives 1.37 cm. It ignores that the face is
seen obliquely from about 33° above, so it was not used.
Confidence: moderate (±10-15%). The face is only about 6 px tall, so where its edges are placed dominates the error.
