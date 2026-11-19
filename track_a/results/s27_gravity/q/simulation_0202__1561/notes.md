# Q1561 – height of the typewriter (simulation_0202, 3D Blender, 24 fps = question_fps)

## Scale / camera (fitfall.py)
- Prior: magnifying glass falls with g = 9.8 m/s^2; depth 4.2401 m at f0, 4.4097 m at f12 (t=0.5 s).
- Fit of the scene track (bbox centre, frames 0-10) with a pinhole camera (principal point at image centre),
  glass at depth 4.2401 m at f0 moving straight down under g: unknowns f, camera pitch, release time.
  Result f = 2668 px, pitch 15.4 deg down, release t0 = -0.001 s, rms 0.38 px. (Lens-centre reference: f = 2628,
  pitch 12.7, rms 0.97 px - worse.) Predicted impact 0.461 s matches the observed contact at f10-f11.
- Checks (check.py): back-projected near desk corner (700,880 px, 3.593 m) lies at the same height as the glass on
  the desk (1.371 vs 1.367 m below camera along "down") -> desk plane consistent. The far-right corner (1990,650 px,
  5.009 m) is 7 cm off (corner point pick uncertain). Glass length ~0.29 m, lens ~0.14 m, typewriter footprint
  0.33 x 0.35 m -> realistic scale.

## Typewriter (typewriter.py, tw2.py)
- Desk plane: n = down, at 1.38 m (glass origin 1.367 + ~1 cm). Footprint corners of the typewriter base intersected
  with that plane: distance from camera ~4.0-4.4 m.
- Height = vertical segment above the ground point under the feature whose projection reaches the top pixel:
  - top of the inserted paper sheet (highest point y = 507 px): 0.31-0.33 m (paper leans back -> ~0.31)
  - machine without paper: type-bar lever tip y = 570 -> 0.21-0.22 m; roller top y = 600 -> ~0.17 m.
- Ambiguity: whether the sheet of paper is part of the typewriter object's bounding box. The sheet carries a
  handwritten texture unlike the blank loose papers, so it is probably part of the typewriter asset; answer with the
  paper included, rounded slightly down for the backward lean: 0.30 m. Without the paper: ~0.21 m.

Confidence: scale good (~3 pct); answer depends on the paper reading (0.30 vs 0.21).
