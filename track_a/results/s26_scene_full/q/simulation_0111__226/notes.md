# q_226 – width of the bridge (prior: boat speed = 2 m/s)

Scene: a top-down 2D render at 24 fps (question_fps is also 24, so there is no re-timing). The boat moves straight down at constant speed. A footbridge crosses the canal at a tilt of about 5.6° and runs off both image edges, so its length is not visible. Width means the bridge's extent across its own axis (along the canal).

## Scale (boat speed)
- Record (`scene/tracks/boat.csv`): bow tip / centre slope 5.49 px/frame (5.49 for frames 2–40, 5.48 for frames 40–76, 5.42 for frames 203–210 after the bridge).
- Independent template match of the boat patch (`speed3.py`):
  - frames 10→70: 5.450 px/frame;
  - frames 10→75: 5.446 px/frame;
  - frames 205→210: 5.43 px/frame.
- Adopted value: 5.47 ± 0.03 px/frame = 131.3 px/s, so the scale is 2/131.3 = 0.01523 m/px.

## Bridge width (`bridge.py`, frame 144, boat hidden)
- Method: fitted lines to the orange outer edge strips on both sides of the deck, giving a tilt of 5.65°.
- Outer edge to outer edge, perpendicular to the bridge axis: 453 px. It varies 452–454 px across x = 400–900. The vertical extent is 455 px.
- Inner edges of the orange strips: 444 px perpendicular.
- The record's value is 437 px, from a cruder gray threshold.

## Answer
Width = 453 px × 0.01523 m/px = **6.90 m**.

Other readings:
- Inner edges: 444 px → 6.76 m.
- Vertical image extent: 455 px → 6.93 m.
- A world-AABB reading that includes the 5.6° tilt times the unseen bridge length would be larger, but it cannot be measured here and is not the natural meaning of the bridge's width.

## Second-route check
The record's speed (5.49 px/frame) gives 6.87 m and the template speed (5.45 px/frame) gives 6.92 m.

**Confidence:** moderate–good. The main uncertainty is whether the bridge, which is raised above the water, is at a slightly different depth from the boat. I ignored this because the scene is treated as 2D.
