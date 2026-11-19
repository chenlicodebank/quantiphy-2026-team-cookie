# q_238 — height of the middle yellow door

The file's frame rate is 24.006 fps. All times use question_fps = 24.0, and the fit is done in frame units.

## Scale from gravity (fit.py)
- I fitted a quadratic to the football centroid track (scene/tracks/football.csv, frames 0–31, frame 17 left out).
- Result: a = 1799 px/s², with 0.43 px rms residual. Starting the fit at frame 0, 2 or 5 gives the same value, and using bbox_cy instead of the centroid gives 1795–1800 px/s².
- So the scale is 9.8 / 1799 = 0.005447 m/px.
- Sanity check: the ball is about 61 px long, which gives 0.33 m. A regulation football is about 0.28 m, so this is +18%: plausible.

## Door pixel height (door.py)
- I measured vertical runs of yellow pixels at frame 0 along the door-frame stiles.
- **Middle door:** the yellow frame, including the dark glass transom, runs from y = 825 to 1171. That is 347 px tall and 158 px wide (x 648–806).
- **Bottom door (same model):** about 1376 to 1724, i.e. 348 px. This agrees.
- **Height:** 347 × 0.005447 = **1.89 m**. The proportions also fit a door: 158 px gives 0.86 m wide.

## Alternative reading
The yellow leaf alone, below the transom, runs y = 891 to 1171, which is 280 px or 1.53 m. That is too short for a real door, so the answer uses the whole door object (frame plus transom).

## Confidence
Moderate to high. The scale is good to about 1%. The main risk is which parts count as "the door".
