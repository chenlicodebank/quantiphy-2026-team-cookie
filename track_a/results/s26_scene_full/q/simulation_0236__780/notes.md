# Q780: height of each glass window (m)

The video is a 2D-style scene: one horse walks left to right right in front of the brick ground floor of a house, and the camera is static. The prior refers to "the horse at the back", which is the only horse, walking near the facade. fps = question_fps = 24.

## Scale (from the prior)
- Horse x displacement over frames 0→49 is 154.2 px on the torso template track (scene record) and 155.2 px on the buttock-edge track. That is 3.146 px/frame, or 75.5 px/s. Vertical motion is negligible.
- Scale = 0.874 / 75.5 = 0.01158 m/px. A linear fit to the rump track gives 3.123 px/frame, or 0.01166 m/px.
- Depth: the hooves are at y ≈ 1042–1045 and the house base is at y ≈ 1037–1040, so the horse walks right by the wall. I treated them as being at the same depth.
- Sanity check: the horse comes out at 2.1 m long and 1.9 m to the ear tips, and the upper door at 1.83 m. All plausible.

## Window pixel height (win_measure.py, frame 49, brightness profiles)
- Middle window: the arch top edge is at y ≈ 844.5 (dark overhang shadow → frame/glass). The bottom of the frame/sill is at y ≈ 951.5, with brick starting at 952. Height ≈ 107 px. Width is 507.5–572.5, about 65 px.
- Right window: the same edges, 844.7 and 951.5, about 107 px.
- The scene record's 105 px figure was a ±5 px manual read.

## Answer
- 107 px × 0.01158 = **1.24 m**.
- Second route: the rump-edge linear-fit scale gives 1.25 m. The glass alone (about 105 px) would give 1.22 m.
- Confidence: about ±3–5%. The main uncertainties are the horse's root-motion speed and whether the frame is included in the height.
