# Q1108 – width (beam) of the boat, simulation_0024

Prior: boat speed 4 m/s. depth_info: D(t=1 s)=90.1103 m, D(t=2 s)=90.4360 m. question_fps 24 (file is 25 fps; frames are
used as Blender frames, t=1 s -> frame 24, t=2 s -> frame 48). Width = shorter horizontal extent = beam (side to side).

## Camera from prior + depths (geom.py, track.py, pitch.py)
- Image motion of the boat (template tracking of wheelhouse / rail / bow patches, frames 2-74, subpixel): du = -6.40..-6.50 px/frame,
  dv = -0.25..-0.27 px/frame; hull-bbox centre at frame 37 = (527.5, 590.5) (scene/ track, checked).
- Origin assumed at hull centre (u 527.5, v ~600 at frame 37). Back-projecting frames 24 and 48 with the given depths and requiring
  |P48-P24| = 4 m (24 frames at 24 fps) gives f = 3504 px (HFOV 15.6 deg). Requiring the 3D motion to be horizontal with zero camera roll
  gives camera pitch 20.4 deg down (range 19.3-21.7 for origin +-20 px / dv +-0.01), heading yawed 5.6 deg away from the image plane.

## Beam (prof.py, prof2.py, beam2.py)
- Column profiles across the deck between wheelhouse and stern rail: far gunwale top edge (sand -> far cap) and near gunwale top edge
  (deck -> white sheer band). Frame 24: x 615/625/650 -> 553.5/554.5/557.5 vs 593.5/593.5/596.0 (39-40 px).
  Frame 48: x 462/472/496 -> 547.5/548/551 vs 587.5/587.5/589.5 (38.5-40 px).
- Rays of both edges intersected with the horizontal plane through the near gunwale (range ~D-1.3 m); component perpendicular
  to the heading = beam. Six measurements (two frames, two depths): 2.63-2.76 m, mean 2.70 m.
- Second route/consistency: frames 24 and 48 (different depths, different image positions) agree (2.68 vs 2.71).
  Sensitivity: pitch +-1 deg -> beam -+0.1 m; origin vertical at waterline (v 640) -> 2.78 m.
- Sanity: hull length ~392 px -> ~10.2 m, L/B ~3.8 (plausible small fishing boat).

## Answer
2.7 m. Confidence moderate (~+-6 %, dominated by the pitch angle inferred from the small depth change).
