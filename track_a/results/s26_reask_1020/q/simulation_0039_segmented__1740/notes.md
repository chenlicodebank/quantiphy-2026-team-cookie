# q_1740: width of the boat (m)

The file is 25 fps and is a 24 fps render with duplicate frames at 1, 26 and 51. The question uses question_fps = 24, so
t = 1 s and t = 2 s are render steps 24 and 48.

## Camera (camera.py)
- Boat image track from scene/tracks/boat.csv, with the duplicates removed: (-8.086, -2.269) px per render step,
  straight line, residual 0.6 px.
- The boat origin at t=1 and t=2 is back-projected with the given depths (177.2077 m and 177.9993 m). I then solved
  for the focal length that gives |P2 - P1| = 4 m (the prior):
  - f = 9106 px (horizontal FOV 9.6 deg).
  - Shifting the origin by ±20 px changes f by less than 0.02 %.
- Pitch, assuming the boat velocity is horizontal and the camera has no roll: 54.4 deg down (±0.3 deg under the same
  shifts). The boat sits off-axis, so its local depression angle is about 58 deg.

## Beam (rectify.py, beam_multi.py, profile.py)
- I rectified the boat onto a horizontal plane through its origin, at 0.02 m/px. The rectified axes are along the
  motion and across it.
- Checks of the rectified view: the deck hatches come out rectangular, and the deck length (bow tip to stern) is
  about 10 m, a realistic fishing boat.
- The beam is the distance between:
  - the far gunwale edge (the deck silhouette), and
  - the near gunwale edge (where the white cap meets the red hull side).
  Both edges are at about the same height, so a plane-height error cancels.
- Profile along the hull, frame 30:
  - Far edge: y ≈ 132 near the stern cockpit, rising to ≈ 123 beside the wheelhouse, both aft and forward of it.
  - Near sheer: 269 at the stern, up to 275 at midship (x 360-410).
  - Maximum beam = (275 - 123) × 0.02 ≈ 3.04 m. The aft cockpit section reads 2.75-2.8 m; the bow tapers.
- Second route, frames 0, 15, 30, 45 and 60: the same columns give the same edges to ±1 px, so the result is stable
  across the clip.
- Sanity check: the beam-to-length ratio is about 0.3. The person's mask length (54-71 px at about 0.020 m/px) fits
  an adult seen from above at about 53 deg.

## Answer
The width (beam, the largest horizontal extent across the hull) is about **3.0 m**. Uncertainty is about ±5 %: edge
fringes of about 1 px, the choice of section, and ±1 deg of pitch (about 1 %).
