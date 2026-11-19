# Q1125 – length of the boat (m)

The file runs at 25 fps and question_fps is 24, so t=1 s is frame 24 and t=2 s is frame 48. The camera is static
(scene record). The 3D model is pinhole: principal point at the image centre, camera pitched down by δ, roll 0.

## Camera (solve.py)
- The prior (person 1.3 m/s) and the boat moving horizontally (depths 130.35→133.74 m, frames 24→48) both
  constrain f·δ only. They are nearly parallel constraints and do not fix f (ill-conditioned: they would give
  f≈9000 and a 1.2 m person).
- So f comes from the standard object. The walking person measures 76 px from head to lowest foot at about 140 m.
  A 1.72–1.75 m walking extent gives f≈6250 px (range 6000–6500 for a 1.70–1.82 m person, hfov about 8.7°).
  δ≈12–15° (boat-horizontal vs person-speed). With f=6250 and δ=14° the person walks at about 1.35 m/s, close to
  the prior.
- The boat moves at about 3.95 m/s, which is plausible.

## Length (length2.py)
- The boat's axis is the horizontal direction of its origin motion between frames 24 and 48. The origin is taken
  at the hull-box centre from scene/tracks/boat.csv, at the given depths.
- The vertical centre plane of the boat passes through the origin. The rays of the bow stem top and the transom
  top centre are intersected with this plane, and the length is their separation along the axis.
- I read the points myself on zoomed frames. In the scene record, "bow_tip" is actually the stern (transom). The
  boat travels bow-first, up-left.
  - frame 0: bow (187,704), stern (432,872)
  - frame 24: bow (100,666), stern (328,827)
  - frame 48: bow (19,629), stern (240,786)
- Results at f=6250: 10.28 m (frame 0), 10.09 m (frame 24), 10.26 m (frame 48).
  - f=6000 gives 10.20–10.39 m; f=6500 gives 9.98–10.17 m.
  - The result is insensitive to δ (±0.01 m), the stern point (5 px gives 0.02 m) and the origin height
    (40 px gives 0.03 m).
- Second route: frame-0 geometry mapped to frame 24 by the tracked scale and offset gives 10.3–10.5 m.

Answer: 10.2 m. Confidence is moderate, about ±5%; the main uncertainty is the person-height-based focal length.
