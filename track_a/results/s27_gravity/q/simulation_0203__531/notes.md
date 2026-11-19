# q_531 – length of the table (simulation_0203)

Question: length of the table (m). Prior: magnifying glass acceleration before 0.5 s = 9.8 m/s^2. No depth_info.
File fps = question_fps = 24.

## Scale (from the prior)
- Glass falls straight down, frames 0-10 (contact at frame 11, t=0.458 s). Quadratic fit of the bbox-centre y
  (scene/tracks, rms residual 0.6 px) -> a = 7440 px/s^2 (7421-7444 depending on start frame; accel.py).
- Scale at the glass's depth = 9.8 / 7440 = 1.317 mm/px. Check: glass overall length 162 px -> 0.21 m, lens
  ring 104 px -> 0.14 m: plausible for a (large) magnifying glass.

## Table length
- The desk top is a perspective trapezoid; its side edges were found per image row against the wall colour
  (edges.py, frame 29). Width grows linearly ~3.75 px/row: 1520 px at y=946 (back edge), 1727 at y=1000,
  1771 at y=1012, 1794 at y=1018, 1953 at y=1060.
- The glass falls without any change of apparent size and comes to rest on the desk with its lens-ring ellipse
  centred at y~1010 (ring y 992-1028); the desk point under its origin is at y~1012-1015. The desk width at
  that row (same depth as the falling glass, so same m/px) = ~1775-1782 px.
- Length = 1780 px x 1.317 mm/px = 2.34 m.

## Uncertainty / second check
- Row choice 1000-1028 gives 2.27-2.41 m; acceleration fit variations <0.5 %. Using the back edge (1520 px)
  would give 2.0 m but that edge is farther than the glass, so it is not used.
- A ~2.3 m desk is large but realistic (partners' desk); glass size check is consistent. Confidence: moderate (~5 %).
