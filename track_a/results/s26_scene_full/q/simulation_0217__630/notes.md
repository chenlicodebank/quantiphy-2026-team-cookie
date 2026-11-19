# q_630 — width of the floor mirror (m)

**Object.** The scene record calls the light-wood frame at the top right (x 1340–1615, y 85–218) an "A-frame /
ladder shelf". It is actually the floor mirror. It is a wooden-framed mirror leaning against the top wall, and the
glass reflects the carpet (frames/mirror3.png). The camera looks straight down with perspective. So the top bar,
which rests against the wall, is closer to the camera and looks magnified compared with the bottom edge on the floor.
Width = the horizontal extent across the mirror's face = its image-x extent.

**Time base.** fps = question_fps = 24, so no re-timing is needed.

**Scale (2D, from prior).** The black cat walks a straight horizontal line at a constant speed. Linear fits of
x(frame) over frames 0–49 (catspeed.py):
- front edge: 10.98 px/frame
- centroid: 10.94 px/frame
- body centroid: 10.95 px/frame
- steady across both halves of the clip.

Speed = 10.96 × 24 = 263 px/s, so 0.94 / 263 = 3.574 mm/px at the cat's origin height. The mirror's bottom edge is on
the floor, slightly farther from the camera than the cat's origin. I added about +1% for this; the camera is high,
since the mirror's top-to-bottom magnification is only about 1.15.

**Mirror pixel width** (profile.py wood-colour row profiles and zoom.py crops; frames 0 and 48 agree):
- Top bar outer width at the top end (x 1420 → 1613): 193 px. This edge is closer to the camera, so it is magnified.
- Bottom outer corners on the floor: left about 1350 (in shadow, ±3) and right about 1519 at y ≈ 211–216, giving
  169 px ± 4.
- Second route: the inner edges of the two side bars converge linearly in image y.
  - Inner gap: 159 px at y = 105 and 139 px at y = 207.
  - Extrapolated, that gives a top/bottom magnification of about 1.17, consistent with a principal point at the
    image centre.
  - Top width 193 / 1.17 = 165 px at floor level.
  - Bottom inner gap 138 px plus two bar widths (about 15 px each) = 168 px.
- Adopted width: 167 px at floor level.

**Answer.** W = 167 × 3.574 mm × 1.01 ≈ 0.60 m. Readings span 0.59–0.62 m (165–170 px).

**Confidence.** Moderate to good. The main uncertainties are:
- the shadowed lower-left corner (±2%);
- the perspective correction between the floor and the cat's origin height (about 1%);
- the side faces of the bars, which are excluded because the world bounding box spans the front-face outer edges.
