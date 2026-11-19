# q768 — height of the trophy (simulation_0235)

Question: trophy height (m). Prior: basketball diameter = 0.282 m. No depth_info. fps 24 = question_fps (time base irrelevant for a size).

## Measurements (scripts in this folder)
- `balldiam.py`: ball at rest (frames 0/1/48/49), 50 % crossings of the R-G profile: width 107.5-107.8 px, height ~108 px
  -> d = 107.6 px. (The scene record's 106.1 px circle fit runs slightly inside the edge. The 108 px bbox agrees with 107.6.)
- `bounce.py` (scene track): the lowest ball centre is y = 865.6 at frame 24 (resting on the floor), so the floor contact is at y ≈ 919.4.
- `verticals.py`: the window mullion edges (x = 75, 1762, ...) are exactly vertical from y 60 to 350, so the camera has no pitch
  and the horizon is at y = 540 (image centre).
- `trophy.py` (temporal mean, gold hue mask): the trophy top (the ball in the figure's hand) is at y ≈ 505.5. The front bottom edge of the base
  is at y ≈ 935 (`measure.py`, zoom frames/bot.png). The floor under the trophy's centre is at y ≈ 927 ± 8: the base is 90 px deep,
  and its front edge lies below the ball's contact line, so the trophy stands slightly closer to the camera than the ball.

## Geometry (level pinhole camera, horizon y_h = 540)
- Camera height from the ball: (y_centre - y_h)/r_px = (H - r)/r -> 325.6/53.8 = 6.05 -> H_cam = 7.05 x 0.141 = 0.994 m.
- Trophy height = H_cam x (y_floor - y_top)/(y_floor - y_h) = 0.994 x 421.5/387 = 1.083 m.
  The result barely depends on y_floor: 920 gives 1.084 and 935 gives 1.081.

## Second route
Flat scale at the ball's depth: 0.282/107.6 = 0.002621 m/px. The trophy's pixel height above its floor point is 421.5 px, which gives 1.105 m.
Scaling by the depth ratio D_t/D_b = (919.4-540)/(927-540) = 0.980 gives 1.083 m, the same as the geometry route.
Using the naive full pixel height (505 to 935 = 430 px) at the ball's scale would give 1.13 m. That overestimates, because the base front edge
is closer to the camera than the ball and lies below the floor point under the trophy's centre.

## Answer
1.083 m. Confidence: moderate-high. The main uncertainties are the ball's pixel diameter (±1 %) and the contact height (±0.5 %).
