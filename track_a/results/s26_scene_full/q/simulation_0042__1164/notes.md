# q1164 – width (beam) of the boat, simulation_0042

Answer: **3.26 m** (boat width = beam, the shorter horizontal extent, rim to rim at the widest station).
File fps = question_fps = 24, so the frame numbers in scene/ are used as they are.

## Camera (geom.py, mast_vp.py)
- Focal length from the eagle: the eagle's positions are back-projected with its depths (t=1 s 179.2691 m, t=2 s 177.1009 m,
  interpolated linearly) and f is solved so that speed = 11.84 m/s. Net displacement over frames 24-48 gives f = 6220;
  frames 6-60 / 5-54 / 3-65 give 6177-6185; the mean of per-frame speeds gives 6235-6269 (inflated by centroid wobble
  from wing flapping). Used **f = 6200 px** (HFOV 9.9°), principal point at the image centre.
- Camera tilt: the vertical vanishing point comes from the mast line fitted in 61 frames (frames 2-62); the mast's slope changes
  with x, so the lines converge. VP = (428, 5089) ± (3, 88) px, so tilt = **36.3°** from nadir with a small roll.
  Check: with this vertical, the boat's 3D displacement over t=1→2 s (from the boat depths 177.2077/177.9993 m) is
  horizontal to within 0.3° (the same constraint alone gives 37.4°). The eagle's displacement gives 39.4°, but the eagle may
  descend a little. Eagle and boat move almost antiparallel, so their cross product cannot be used.
- The boat moves along its own axis: the deck rims are parallel to the motion direction (15° in the image) and the
  rectified hull is symmetric about the motion axis.

## Beam (rectify.py, beam.py, runall.py)
- Each frame is rectified onto the horizontal plane through the boat origin (0.01 m/px; a along the axis, b across it).
  Points at the same height are measured correctly; a common height only shifts them.
- Near rim = the boundary where the red hull side meets the white deck. Far rim: in the stern section (a = -3.5…-1.75 m) it is the
  outer gunwale edge (first dark row, i.e. water between the rail posts, past the pink deck line). In the bow section
  (a = 2.5…4.5 m) it is the deck edge against the water. Midships the far rim is hidden by the cabin and its shadow.
- The apparent centreline (near+far)/2 is flat at 3.53 m in the stern section and rises toward the bow as the sheer rises:
  3.78 at a=2.5, 4.03 at a=4.5. It is fitted as flat + quadratic (rms 0.01 m). Beam = 2·max(centre − near rim),
  which falls at a ≈ 1.1-1.4 m.
- Results: frame 24 gives 3.27, frame 12 3.25, frame 36 3.21, frame 48 3.22, frame 6 3.24, frame 56 3.25 (mean 3.24). With the
  tilt from the boat-displacement constraint: 3.29. With zero roll: 3.24. With the eagle tilt (least trusted): 3.37.
- Direct checks without the model: the widest measured stations are 2.90 m (a=2.5, bow section) and 2.59 m (a=-1.75, stern).
  The hull keeps widening toward a≈1.2 along the near rim, which is consistent with about 3.25 m.
- Sanity check: the boat is about 10.3 m long (transom to bow tip), so length/beam ≈ 3.2, which is plausible for a fishing boat.

## Confidence
Moderate, about ±4%. The main uncertainties are the centreline interpolation midships (far rim hidden), the
tilt (36-37.5°) and f (±0.7%). The answer assumes the boat's axes line up with the world axes, so the bounding-box width equals the beam.
