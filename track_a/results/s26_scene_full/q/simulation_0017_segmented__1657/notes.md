# q_1657 — width of the freestanding art display panel (m)

The file rate and question_fps are both 33 fps. The camera is static and level: the pedestal block's edges are exactly vertical (x=405 and x=654 over 80 rows, see edges.py), so the horizon is at the image centre row (cy=540).

## Camera scale from the person (prior plus depth_info)
- Pelvis track (scene/tracks/person.csv, pelvis_x_smooth): mean 7.646 px/frame = 252.3 px/s. With a speed of 1.3 m/s, Z_person/f = 0.00515 m/px.
- From depth_info, d(t=0)=5.424 at u≈-1.5 and d(t=1)=4.886 at u≈252 (frame 33). Assuming constant Z, solving for f gives f ≈ 905 px and Z ≈ 4.65 m. This predicts the lateral speed as 1.30 m/s and reproduces d0 as 5.429 m (given 5.424). The three constraints agree with each other.
- The person's soles are at row 731 in frames 0-17. Camera height is h = 191 px × 0.00515 = 0.98 m. Consistency checks: the pelvis sits at about the horizon. At the pedestal's depth (5.93 m) the floor projects to row ≈690, which is hidden behind the bench top (697) as observed. The bench front floor edge is roughly consistent.

## The panel
- There are two identical framed panels on stands, either side of the sculpture.
  - Left panel: base x 293-404 (≈112 px), frame face 308-392 (84 px).
  - Right panel: base 666-781 (≈116 px), frame face 680-768.
  - Both: frame top at row 465 and base floor contact at rows 608-614 (front edge 613.5). The top edges are flat, so the panels face the camera with no yaw. (panels.py, bases.py, yaw.py)
- **Conflict:** depth_info gives 4.223 m to the panel, so Z_panel ≤ 4.22 m. But the person (Z ≈ 4.65 m) clearly walks *in front of* both panels (frames 28-61 and 78-100; occlusion checked visually at frames 45 and 95). The panel geometry therefore cannot be at 4.22 m. The 4.223 m value must refer to an origin that is offset from the mesh.
- **Floor-contact depth (used):** the panels stand on the floor with their front base edge at row 613.5, so Z = h·f/(613.5-540) ≈ 12.1 m. Width = w_px·h/(v-540):
  - left: 112 × 0.98 / 73.5 = 1.50 m
  - right: 116 × 0.98 / 73.5 = 1.55 m
  - answer: 1.52 m (mean)
- Sanity check: panel height = 148 px at about 12 m ≈ 2.0 m, and the camera sits at the panel's mid-height. A 1.5 × 2 m freestanding panel is realistic, and so is the rest of the scene at this scale (person 1.85 m, pedestal about 1 m high, bench about 2.5 m long).
- **Alternative reading (not used):** taking depth_info at face value gives Z ≈ 4.13 m and width ≈ 112·4.13/905 ≈ 0.51 m (0.53 m for the right panel). Even placing the panel just behind the person (Z ≥ 4.65 m) would give at least 0.58 m, and the panel would then have to float about 0.6 m above the floor.

## Confidence
Moderate. The geometry (occlusion, floor contact and a level camera) strongly supports about 1.5 m, but it contradicts the stated panel distance. There is also some ambiguity about which of the two panels is meant (1.50 vs 1.55 m).
