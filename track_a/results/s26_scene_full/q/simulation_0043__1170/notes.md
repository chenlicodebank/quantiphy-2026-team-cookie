# q1170: width of the rock (m)

Prior: boat length = 10 m. Depths: boat to camera 173.7093 m at t=1 s (frame 24) and 174.5515 m at t=2 s (frame 48).
The file rate and question_fps are both 24.

## Camera geometry (geom.py, sens.py)
- Boat track from scene/tracks/boat.csv. I used a linear fit over frames 2-71, because the boat moves straight
  at a constant speed. The image positions are (358.35, 924.72) at frame 24 and (273.26, 899.73) at frame 48:
  89.0 px apart.
- Boat body length is 215.1 px at mid-interval, so its speed is 10 × 89.0 / 215.1 = 4.12 m/s.
- I solved for the focal length f such that the two back-projected boat positions (each ray scaled to its given
  depth) are 4.12 m apart. Result: **f = 3799 px** (HFOV 16.2°). The principal point is assumed at the image centre.
- Ground normal: it is perpendicular to the boat's 3D motion. The vertical direction comes from the mast lines,
  hand-read at frames 0, 24, 48 and 71 (nadir vanishing point near (457, 3411)). The four mast lines on their own
  give (470, 3609), which agrees.
  - Camera tilt is 37° from straight down. Camera height above the boat-origin plane is 148.4 m.

## Rock footprint (rockseg.py, footprint.py, extremes.py)
- Rock mask on frame 24 (the rock is static):
  - brightness/texture segmentation, minus water;
  - a hand-placed cut along the rock's right flank, to exclude the beach strip.
  - Overlay: frames/rock_auto_24.png. Image bbox x 390-885, y 8-447.
- I back-projected the outline onto the ground plane and measured extents in plane axes:
  - along the boat heading (e1): **24.57 m**;
  - across it (e2): 34.43 m;
  - minimum-area rectangle: 23.6 × 35.2 m. Its principal axes are within about 6-16° of the boat axes, so the
    rock looks roughly aligned with the boat's (likely world) axes.
- The e1 extremes are the left and right side silhouettes, at (402, 127) and (879, 153). Any height bias of these
  silhouette points shifts the two sides in opposite e1 senses, so it nearly cancels.
- "Width" means the shorter horizontal extent, which is the e1 extent.

## Sensitivity (sens.py)
| Change | Width along e1 |
|---|---|
| boat length in px ±1% | 24.3-24.9 m |
| mast lines ±1 px | 24.4-24.7 m |
| ground plane ±1-2 m | 24.2-24.7 m |
| minimum over all rotations (lower bound for any world-AABB width) | 23.6 m |

## Answer
**24.5 m.** This is the boat-aligned extent of about 24.6 m, shaded slightly towards the rotation-minimum of 23.6.
Confidence: moderate, about ±5%. The main uncertainties are the world-axis orientation and the boat's pixel length
standing in for its 10 m length.
