# q453 – truck tyre diameter (simulation_0187)

2D side-on render, static camera, 30 fps (file fps = question_fps = 30, so no re-timing). The truck translates
horizontally left to right with constant acceleration from rest at frame 0. Prior: a = 10.757 m/s^2.

## Pixel acceleration
- Record track (scene/tracks/truck.csv, side-plane features), quadratic fits (fit.py): 2.036-2.050 px/frame^2
  depending on the window; the cleanest window (frames 36-50) gives 2.042.
- Independent check (hubtrack.py): template-matched the bright front-wheel hub over frames 21-44 and got
  a = 2.0373 px/frame^2 (rms 0.08 px, vertex at frame -0.01, so it starts from rest at t=0). Matching the rear hub over
  frames 34-52 gives 2.0353.
- Used a = 2.037 px/frame^2 = 1833 px/s^2, so the scale is 10.757 / 1833 = 0.005868 m/px. The hubs lie at the same
  depth as the tyres, so this scale applies directly to the tyre.

## Tyre pixel diameter (prof.py, enh.py; measured with each wheel near the image centre to avoid perspective widening)
- Rear wheel, frame 44 (centre x ~954): width at row 867 is 886.1 -> 1020.5 = 134.4 px (half-intensity edges against
  the bright floor); height is about 800 -> 934 = ~134 px.
- Front wheel, frame 35 (centre x ~945): width is 878.1 -> 1011.1 = 133.0 px; height is 803 -> 934.5 = ~131.5 px.
- Mean is about 133.2 px. The record's "tyre_diameter 150 px" (centre 862 / bottom 939) is too large: the enhanced
  crops show the tyre outline clearly inside the fender at ~133 px. I corrected it here.

## Answer
133.2 px x 0.005868 m/px = 0.782 m (front-only reading 0.776, rear-only 0.789).
Confidence: good (~3 %). The main uncertainty is the tyre edge against the dark fender and chassis (±2 px).
