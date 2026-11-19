# Q760: length of the chair (m). Prior: black cat speed = 0.714 m/s

## Time base
fps = question_fps = 24, so no re-timing.

## Scale from the prior (the cat is on the table top)
`speed.py` fits a line to the record's cat track (`scene/tracks/cat.csv`).
- `head_front_robust_x`: 13.46 px/frame over frames 0-49, 13.56 over frames 22-49.
- `mask_cx`: 13.56 px/frame over frames 22-49.
- Pixel speed is therefore about 13.5 px/frame = 324 px/s.
- Scale at the table plane: s_c = 0.714 / 324 = 0.002204 m/px.

## Perspective: the scene is not a flat 2D layout
The camera looks straight down. The chair stands on the floor, well below the table top, and its parts are at different heights. Image offsets are measured from the image centre (960, 540).

- **Table legs** (`legs.py`, `legview.py`):
  - The leg feet show beside the table's right edge (x = 714), near (734-740, 403-408) and (730-740, 785-790).
  - Model: vertical legs inset d from the corners (714, 366) and (714, 848).
  - Fitting x and y together gives Z_table / Z_floor = r = 0.84-0.866 for both legs, with d of about 15-25 px. I used r = 0.855.
  - The leg lines point roughly at the image centre, so the principal point is near (960, 540).
- **Chair** (`chairview.py`, `chair_mask.py`): a seat (x 1584-1767, y 550-716) and a curved backrest bar (x 1597-1836, y 498-535).
  - Its two left legs show in perspective as short near-radial tube segments, with feet at x of about 1537-1547 and tops at the seat and backrest edges.
  - Front-left leg: offset from 587 to 626 gives h_seat / H of about 0.062.
  - Rear-left leg: offset from 577 to 637 at the backrest end gives h / H of about 0.094 at the bar's attachment. I took the backrest top as k of about 0.12 ± 0.02.
  - Sanity check: seat/table height ratio = 0.062 / 0.145 ≈ 0.43, which is plausible (a small classroom chair).
- **Floor-plane scale:** s_f = s_c / r = 0.002204 / 0.855 = 0.00258 m/px. Then world X = (u - 960) · s_f · (1 - h/H), and the same for Y.

## Chair bounding box, in floor-scale px units
- **X:** the minimum is the left-leg outer edge, 577 (equal to the backrest's left end, 637 · (1 - k)). The maximum is the backrest tip, 876 · (1 - k).
  - Extent ≈ 239 · (1 - k) = 210 ± 6.
- **Y:** from the backrest top edge, -42 · (1 - k) ≈ -37, to the seat front and front-leg foot, ≈ +165 to +170.
  - Extent ≈ 205.
- **Length** (the longer horizontal extent) ≈ 210 units × 0.00258 = **0.54 m**. The width is about 0.53 m, so the two readings give almost the same value.

## Second route / sensitivity
- Naive single table-plane scale (the record's 2D assumption): 300 px × 0.0022 = 0.66 m. I rejected this: the chair is on the floor (r ≈ 0.86), and its backrest is raised, which magnifies its image.
- Range over r = 0.84-0.866 and k = 0.10-0.14: 0.52-0.56 m.
- If the cat's origin is at its body (about 0.12 m above the table) rather than at its feet: +2-3%.

## Confidence
Moderate. The main uncertainties are the table-leg depth ratio and the backrest height (about ±5%).
