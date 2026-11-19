# Q1562 – width of the paper next to the magnifying glass (simulation_0202)

The file and the question both run at 24 fps. The 3D render has a static camera.

## Object
"Paper next to the magnifying glass" means the cream sheet just left of the resting glass, on the right-front of the
typewriter. Its image corners at frame 29 are R (1258,720), B (1160,741) and T (1149,673); the fourth corner is hidden
under the typewriter. I found the corners from a brightness mask (`paper_mask.py`, overlay in frames/paper_mask.png)
by fitting a line to each edge and intersecting the lines (`solve.py`). The visible edges form a parallelogram in the
image. The fully visible short side is R–B (the lower front edge). R–T is the long side.

## Camera / scale
- Focal length and tilt come from the free fall: the glass falls from 4.2401 m at t=0, and I fitted the pixel track
  (frames 0–9, initial velocity along the vertical only) with g = 9.8 m/s². Result: f ≈ 2644 px (2630–2680 depending on
  frames and constraints), hfov ≈ 44°, pitch ≈ 14° down, roll ≈ 0. RMS error 0.2 px.
- Desk-top plane: I took "near corner" (3.593 m) to be the front-left desk corner at about (695,882), and "far right"
  (5.009 m) to be the front-right corner at (1992,645). Back-projected, the two heights agree within 3 cm at pitch 14°,
  and exactly at pitch 13°. The t=0.5 s glass depth (4.4097 m) puts the glass 4 cm above that plane while it bounces,
  which is consistent.
- I back-projected the paper corners onto the desk plane.

## Results (paper side lengths on the desk plane)
| camera solution | R–B (width) | R–T (length) | corner angle at R |
|---|---|---|---|
| fall only, frames 0–9 (f 2644, pitch 14.0°) | 0.193 | 0.306 | 90.5° |
| fall + equal corner heights (f 2630, pitch 13.1°) | 0.198 | 0.319 | 93.3° |
| fall only, frames 0–8 (f 2682, pitch 17°; poorly constrained, rejected) | 0.181 | 0.274 | 82° |

Checks:
- At pitch 14° the paper comes out a right-angled rectangle (90.5°).
- At pitch 13° the desk's front and right edges are perpendicular (the back-right corner pixel is only approximate),
  and the two given corner depths lie at the same height.
- Answer: width = 0.195 m, the midpoint of the two consistent solutions (0.193–0.198).

## Second-route check and plausibility
- The paper is 0.195 × ≈0.31 m, about A4/Letter size (A4 is 0.21 × 0.297). The scene is at roughly real scale:
  the glass is 0.29 m long and the desk 2.47 × 1.07 m (large, but fixed by the given depths).

## Confidence
Moderate to good: about ±4% from camera pitch, plus 1 px corner uncertainty.
