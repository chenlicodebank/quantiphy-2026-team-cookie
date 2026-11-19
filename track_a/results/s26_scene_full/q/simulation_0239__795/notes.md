# Q795 – width of the house (m)

Prior: the horse at the back moves at 0.874 m/s. I took this to be the **brown horse**. It is behind the white
horse in the walking direction and it is the upper horse, nearer the house. With its scale both horses come out at
realistic lengths (2.0 and 2.4 m). With the white horse's scale they would be 1.1 to 1.4 m long, which is too small
for horses. fps = question_fps = 24.

## Scale (ground / horse level)
- tm.py tracks the brown horse's back texture by template matching over frames 0–48, using two templates (from
  frames 0 and 24). Both give 2.617 px/frame = 62.8 px/s. This is steadier than the scene record's mask centroids,
  which give 2.46–2.69 px/frame.
- s = 0.874 / 62.8 = 0.01392 m/px at the height of the horse's back (about 1.4 m).

## House geometry (frame 0, zoomed crops via crop.py)
- Overhead camera looking straight down. The principal point is near (960, 544), and the gable ends are consistent
  with a vertical optical axis. The house covers the nadir, so no walls are visible; only the roof can be seen.
- The main block runs N–S (up–down in the image) and has gable ends at the top and bottom:
  - Top gable: eave corners at y ≈ 96 (x 661 / 1361), apex at y = 21.
  - Bottom gable: eave corners at y ≈ 717, apex at y = 746.
  - From these, the ridge-to-eave magnification is k = 1.1675.
- The cross gable runs E–W. Its eave corners are at x 647 / 1379, its apexes at 616 / 1426, and k = 1.107.
- Footprint at eave level:
  - N–S extent (gable-end planes): 717 − 96 = **621 px**.
  - E–W extent: 700 px for the main block and 732 px for the cross gable.
  - So the shorter horizontal extent, the width, is N–S = 621 eave-level px.
- The roof sits above the ground, so its pixels are magnified relative to the horse plane. The conversion is
  width = 621 · s · (D − h_eave) / (D − 1.4), with D = s·f + 1.4.
- The focal length can only be estimated roughly from the horses (leg/side parallax): f ≈ 1500–2700 px, which gives
  a camera height D ≈ 22–38 m. A main-roof pitch of 31–47° is plausible across that range.
- The eave height cannot be measured because the walls are hidden. I assumed a single-storey eave of about 3 m.

## Result
- Width ≈ 7.98 m at f = 1500, 8.14 m at f = 2000 and 8.27 m at f = 2667, all with h_eave = 3 m.
- **Answer: 8.0 m.**
- Sensitivity:
  - Ignoring perspective (planar) gives 8.64 m.
  - A higher eave lowers the answer: about 7.6 m for a 4 m eave and about 6.7–7.2 m for a 6 m eave.
- The length (E–W) under the same assumptions would be about 9.0–9.4 m.

## Confidence
Moderate. The pixel speed and pixel extents are good to about 1–2 %. The main uncertainty is the eave height and
focal length used for the perspective correction, worth roughly ±8 %.
