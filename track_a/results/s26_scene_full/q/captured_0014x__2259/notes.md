# q_2259 – length of the book (cm)  → **17.0 cm**

Lab video, 24 fps (file and question_fps are both 24), 1280x720, f = 0.5959*1280 = 762.8 px, principal point (640,360).
The book is the light-blue notebook (scene record calls it "notebook") lying flat on the table, right of the board;
it is static in all frames. Its depth is 1.6650 m (depth_info, t=0). The ball prior (4.6 m/s²) is not needed for this size.

## Why the plain "pixel extent × depth / f" is not enough
The book's long side runs from the front of the table to the back, so it is strongly foreshortened (the camera looks
down at only ~35° above the table plane at the book). Naive: 48.5 px × 1.665 / 762.8 = 10.6 cm (whole outline, incl.
the front page block) – not a physical length. So the book outline was back-projected onto the table plane.

## Method
1. `book_mask.py`: colour mask of the book (frames 0, 5, 40, 45 identical) → outline quad
   (627,391) (664,385) (681,430) (645,436); short side ≈ 37 px, long side ≈ 48.4 px.
2. `book_profile.py`, `book_top.py`: intensity profiles along the long axis at 3 positions separate the top cover
   (s≈-2 to 43 px) from the front page-block face (≈5-6 px, which belongs to the thickness, not the length).
   Top-surface quad: (626.1,388.9) (663.2,382.8) (679.4,425.7) (643.4,431.9); top surface ≈ 46 px along the axis.
3. Table plane normal from the vanishing points of the table-top edges (scene-record corners). Check: the two table
   axes come out orthogonal (cos = -0.012) with f = 762.8; table size 58 × 63 cm; heights of the other depth_info
   objects above the plane through the book centre are sensible (pen -0.6 cm, cookie +3.4, cup +8.5, slope_near -1.5,
   slope_far +12.8 cm) (`geom.py`, `plane_check.py`).
4. Book top-surface corners intersected with the plane through the book centre (1.665 m) → length 16.92-17.02 cm
   (left/right sides equal), width ≈ 8.2 cm (`book_top.py`, `book_len2.py`).

## Second route / checks
- Independent tilt check from the cup rim (circle parallel to the table): fitted lid-boundary ellipse ratio 0.477,
  orientation 84.2° (`cup_fit2.py`, `cup_pred.py`) → best match at tilt offset ≈ -0.5°, roll ≈ +4° from the
  record-based normal; with those the length is 16.9-17.1 cm (`final_len.py`).
- Alternative normal from silhouette line fits of the table edges (`table_edges.py`) gives 18.0-18.4 cm, but its table
  axes are not orthogonal (82°) and it disagrees with the cup ellipse (it needs dt≈-3°, ratio 0.43 vs measured 0.477),
  so it was rejected (rounded corners / segmentation fringe bias the silhouette).
- Sensitivity: 1° of tilt ≈ 0.4 cm (2.4%); ±1 px on the front cover edge ≈ 0.37 cm.

Other readings: whole outline incl. front page block on the plane ≈ 17.6 cm (counts thickness as length – rejected);
width (short side) ≈ 8.2 cm.

Confidence: moderate; estimated uncertainty ±0.8 cm (~5%).
