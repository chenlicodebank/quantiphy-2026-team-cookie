# q 2607 — height of the pencil bag (cm)

Answer: **5.5 cm** (vertical extent of the bag as it lies on the table). The file and the question both use 24 fps, so the time base is the same.

## Scale: why depth_info was not used directly
- Prior: the tennis ball is 6.7 cm across. Ball B's apparent diameter (half-max of RGB distance to the table, frames 5/15/46–48;
  `balldiam2.py`) is 29–31 px, so I used **30 ± 1 px**. With the lab focal length f = 0.5959·1280 = 762.8 px, the ball centre is about **1.70 m** away.
- depth_info gives 0.706/0.776 m for the tennis balls. At that distance a 30 px ball would be about 2.8 cm across, not 6.7. It also places the
  pencil bag (1.05 m) farther away than the soccer ball (0.894 m), but the image shows the bag nearer the camera.
  depth_info therefore contradicts the exact prior. The card formula (1.05 m × px / f) would also make the tennis ball about 2.4× too small. So I took the
  metric scale from the prior's ball plus pinhole geometry.
- Table plane (`geom.py`): the normal comes from the vanishing points of the table edges, and the plane offset puts it one ball radius below ball B's centre (frame 46–48).
  Consistency checks (`length.py`): the near and far table edges both come out at 79 cm (a rectangle, 79 × 64 cm). The soccer-ball radius consistent with
  sitting on the plane is about 9.4–10 cm (a size-4/5 ball). Pencil-bag length is 20.3 cm. All of these are plausible, so the geometry is consistent.
- Bag base distance ≈ 1.58 m and the camera tilts about 40° down. Across the bag axis (image angle −27°), each cm of height shifts the image by
  3.17 px, and each cm toward the back of the table shifts it by 3.65 px.

## Bag cross-section measurements (static average of frames 0, 6, 12, 18; `profile_avg.py`, `bagmask2.py`)
Profiles perpendicular to the axis, averaged over three segments of the bag:
- contact/bottom edge (dark crease) at q ≈ −16.5 px; top-back silhouette at q ≈ +15.5 → total extent ≈ 32 px
- saturated flat front face from −16 to about −3; a rounded top-front edge from −3 to about +7; the striped zipper top from +7 to +15.
Models (`geom.py`, `endcheck.py`):
- sharp box, front/top edge at the transition midpoint (q 0…+2): h = 5.0–5.7 cm, w = 3.7–4.2 cm
- rounded-rectangle model fitted to all three transitions: h ≈ 5.8, w ≈ 4.6, corner radius ≈ 1.5 cm
- h = 5.3 with corner radius 1.0 also fits the front-face end and the silhouette (w ≈ 4.7)
- If the front face leaned back by 15–20°, h would be 4.5–5.0. However, the right-end front edge is vertical in the image
  (x ≈ 737–738 from y 346 to 326; a leaning face would lean about 4 px left). This argues for a vertical front face.
- Second route (`rightedge.py`): the right end's vertical front edge spans about 20 px straight up before it curves (3.78 px per cm vertical there),
  which puts the flat part at ≥ 5.3 cm plus the rounding.

## Confidence
The most likely value is 5.3–5.8 cm, and I answered 5.5. The main uncertainties are the cross-section shape (±10%) and the ball pixel diameter (±3%).
For reference only, the card formula with depth_info (1.05 m × about 18–32 px / 762.8) would give 2.5–4.4 cm. I rejected it as inconsistent with the prior.
