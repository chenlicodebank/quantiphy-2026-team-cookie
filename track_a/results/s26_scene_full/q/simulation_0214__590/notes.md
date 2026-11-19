# q_590 — lampshade diameter (simulation_0214)

The prior is the black cat's speed, 0.94 m/s. fps = question_fps = 24, so there is no re-timing.

## Scale from the prior (measure.py)
- Black cat pixel speed, from linear fits over frames 0–49:
  - head-front bbox edge: 10.98 px/frame
  - body centroid: 10.94 / 10.96 px/frame (scene record and my own dark-pixel mask agree)
  - The tail edge (11.2) is excluded because the tail swings.
- Speed used: 10.97 px/frame = 263.3 px/s.
- Scale at the cat's level (about 0.2 m above the floor): 0.94 / 263.3 = 0.003570 m/px.

## Lampshade pixel size (lamp2.py, parallax.py; frames 0, 25 and 49 give the same result)
- Bounding box tip to tip of the pleats: 150 x 150 px.
- Least-squares circle through the zigzag outline: 146.8 px.
- Value used: 149 px. Projected at the cat's level this is 0.532 m.

## Perspective correction
The camera is a perspective camera looking straight down. The shade sits on a table lamp on the console, so it is much closer to the camera than the cats are. That makes it look bigger than the floor-level scale implies.
- **Parallax cue:** the centre of the shade's top opening sits 19.4 px further from the image centre than the centre of its bottom rim. The rim centre is 391 px from the image centre. This gives Δh / (H − h_top) ≈ 0.050. The vase shows the same outward shift (8.4 px at 367 px).
- **Assumed shade shape:** a pleated cone about 0.55 x diameter tall (Δh ≈ 0.27 m). That puts the camera about 5.5 m above the shade top, or H ≈ 6.6 m above the floor.
- **Assumed lamp height:** rim about 0.83 m above the floor. This is a guess for a lamp on a console.
- **Correction factor:** (6.6 − 0.2) / (6.6 − 0.83) ≈ 1.11. Diameter = 0.532 / 1.11 ≈ 0.48 m.

## Second route and confidence
- **Without correction:** pure 2D, one scale for everything, gives 0.53 m. This is an upper bound.
- **Stronger perspective:** if the camera were lower (H ≈ 5 m, using the vase cue), the answer would be about 0.46 m.
- **Answer:** 0.48 m, inside that 0.46–0.53 range. Medium confidence (about ±8%), mostly from the unknown camera height and lamp height.
- The scene record's lamp extent (146 px) and black-cat speed (11.0 px/frame) were confirmed by my own measurements.
