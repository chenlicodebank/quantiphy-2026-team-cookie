# q_549 — width of the paper next to the typewriter (simulation_0207)

The file and the question both use 24 fps. Prior: the typewriter's acceleration before 0.45 s is 9.8 m/s^2 (free fall, frames 0-10). No depth_info.

## Object
The paper is the flat cream sheet lying on the desk directly left of where the typewriter lands. It touches
the typewriter's left side at rest. Image corners at frame 0 (sub-pixel half-threshold edges, card.py):
TL (743.5, 999.6), TR (884.6, 996.9), BL (730.6, 1042.6), BR (884.9, 1039.9). The sheet is slightly yawed.

## Scale
- Gravity: a quadratic fit to the typewriter bbox centre over frames 0-9 (measure.py) gives 7268 px/s^2, so
  s = 741.6 px/m at the typewriter's depth. The bbox top gives 6825 and the bottom 7711; they switch between
  near and far features, so the centre is used. This puts the typewriter's width at 291/741.6 = 0.39 m, which is realistic.
- Camera: the vanishing point of the desk side edges (horizon.py) is (1065, 544). That is about the image
  centre, so the camera has no pitch.
- Camera height above the desk, h: at frame 11 the typewriter sits flat on the desk. Its front-bottom edge
  is at v = 1027.5 (base.py), which is 483.5 px below the horizon. This edge is about 0.15 m in front of the
  origin's depth, so h = 483.5/741.6 - 483.5*0.15/f, which is about 0.623 m for f = 2000-3300. The f term
  changes h by only about 2%.
- On the desk plane, X = (u - cx) * h / (v - vh) does not depend on f.

## Measurement
Back-projecting the corners onto the desk gives these side lengths:
- Side running across the view: 0.3074 h in X, plus a small depth part. This is 0.309-0.310 h for both the
  front and back edges.
- Side running away from the camera: about 0.39 h at f = 2083, and longer for larger f. So it is the longer side.

The width (the shorter horizontal extent) is 0.309 * 0.623 = 0.192 m.
f comes from right-angle conditions, which are ill-conditioned: about 2083 px from the card and about
3240 px from the typewriter's footprint at rest. The width barely depends on f.

## Second route
Using the planar fall scale directly: the card's mean pixel width of about 146 px divided by 741.6 px/m gives 0.197 m.
The sheet is only about 0.1 m in front of the typewriter's origin, so the two routes agree within 3%.
The other papers give similar values: the standing letter by the books is 135 px wide at its desk line
(v ≈ 993), which is 135 * h / 449 = 0.187 m.

## Confidence
Moderate to good, about ±5%. The answer is a little smaller than US Letter (0.216 m), but no paper size was assumed.
