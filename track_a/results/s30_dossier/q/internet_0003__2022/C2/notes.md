Pizza mask (SAM3, frames 30/36, complete outline) gives an unforeshortened horizontal diameter of 1006 px (vertical 945 px). The prior object is the flat Monopoly 500-bill (SAM3 'banknote' k=3), a clean rectangle 304-332 px along its long/main axis (148-159 px across, aspect 2.06). Using the benchmark's one-scale-factor convention with the note's main-axis extent: 7.5 cm / ~315 px = 0.0238 cm/px, so the pizza = 1006 x 0.0238 = 24.0 cm. A perspective-aware homography of the table plane (from the Monopoly board's grid vanishing points, f~1311 px) gives the same ratio (pizza/bill-long = 3.1 -> 23.3 cm), and it makes the pepperoni 2.8-3.1 cm, the wine-glass foot 5.7 cm and the fist 8.8 cm, all plausible; the alternative reading (7.5 cm = the note's short side) would give a 48 cm pizza with 6 cm pepperoni and an 18 cm fist, i.e. >40% implausible, so it was rejected.

Final message:
I measured the pizza and the prior object directly from the video.

**Method**
- **Pizza:** SAM 3 masks on frames 30 and 36 (frame 0's right edge is occluded by the arm). The complete outline gives a horizontal (unforeshortened) diameter of **1006 px** (vertical 945 px).
- **Prior (Monopoly money):** SAM 3 "banknote" on frame 0 isolates the flat 500-bill as a clean rectangle, 304–332 px along its long/main axis and 148–159 px across (aspect 2.06). The $1 bill is partly hidden behind the sleeve, so it wasn't used.
- **Scale:** following the benchmark's one-scale-factor convention (prior world value / prior pixel extent along the object's main axis): 7.5 cm / ~315 px ≈ 0.0238 cm/px → pizza ≈ **24 cm**.

**Second route / checks**
- A perspective-aware homography of the table plane (built from the Monopoly board's grid vanishing points, f ≈ 1311 px) gives the same ratio: pizza / bill-long-side = 3.1 → 23.3 cm.
- Standard-object sanity check in the same plane units: pepperoni 2.8–3.1 cm, wine-glass foot 5.7 cm, fist 8.8 cm — all plausible. The alternative reading (7.5 cm = the note's short side) would imply a 48 cm pizza with 6 cm pepperoni and an 18 cm fist, i.e. >40 % implausible, so it was rejected.

Notes written to `notes.md`; answer submitted: **24 cm**.
