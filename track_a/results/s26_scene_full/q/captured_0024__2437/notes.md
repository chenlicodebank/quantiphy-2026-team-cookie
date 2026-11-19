# q_2437 – width of the book (cm)

Object: the light-blue notebook (cyan cover) that slides down the white ramp. Width = shorter side of the cover
(about 10.7 cm). The longer side is about 17 cm. File fps = question fps = 24.

Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Method (scripts: book3d.py, sides.py, final_f0.py, cover.py, ramp.py, crops.py)
- The book lies on the ramp with its long edge running across the ramp (horizontal in the image) and its short edge
  running down the slope. The short side is foreshortened, so a naive pixel extent x depth / f would be wrong.
  I rebuilt the ramp plane in 3D instead:
  - Slope direction, two ways:
    (a) from the book's own given positions: centroid at frame 24 (750.6, 397.3) at 1.0685 m and at frame 29
        (670.3, 451.9) at 0.977 m, back-projected;
    (b) from the slope far/near depths (1.243 / 0.990 m) at the ramp's top-edge and bottom-edge centres.
    The two agree: incline about 24 deg to the camera's vertical.
  - Across-ramp direction: perpendicular to the slope direction and horizontal in the image, because the cover's top
    edge is image-horizontal at frame 0–18.
- Cover corners at rest on the ramp (frame 10, sharp, 6x zoom): TL (754.7, 352.5), TR (843.3, 352.5),
  BR (807.5, 385), BL (720, 380.3). I intersected these rays with the plane and measured the side lengths in 3D.
- Results:
  | plane anchor | width (short side) | length (long side) |
  |---|---|---|
  | through the given book depth P24, centre-to-cover offset 0 / 0.8 cm, track orientation | 10.76 / 10.53 cm | 17.5 / 17.1 cm |
  | through the given book depth P24, centre-to-cover offset 0 / 0.8 cm, slope orientation | 10.73 / 10.52 cm | 15.8 / 15.5 cm |
  | ramp-depth plane + book thickness | 11.1 cm | |
  - The width barely depends on the orientation choice. It mostly depends on the depth anchor.
  - The given book depths sit about 3 cm in front of the ramp plane built from the slope depths. I weight the book's
    own depths more.
  - Opposite sides agree to 2–3 %, so the quad is consistent with a rectangle.
- Answer: **10.7 cm**.

## Checks
- Frame 24 (where the depth is given), colour-mask quad on the plane through P24: short side about 10.0–10.2 cm.
  This frame is blurred and the book is rotated in-plane, so the quad is skewed and less reliable.
- Long side, naive check at t = 1.0: 125 px x 1.0685 / 762.8 = 17.5 cm. This matches the 3D long side of 17.1–17.5 cm.
- The ramp-plane fit in plane.py (parallelogram corners plus the slope depths) is not consistent with the book
  depths: 1.146 m vs the given 1.0685 m. I did not use it for the answer.
- On the table (frames 36–48) the cover is only about 17 px tall and its right end is hidden by the ramp, so I did not
  use it.

Confidence: moderate, about ±5 %.
