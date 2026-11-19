# Q800 – length of the horse at the back (simulation_0240)

- "Horse at the back" = chestnut horse: it trails on the left, and its hooves sit slightly higher (y≈1048 vs 1055), so it is also slightly farther away. Prior: its speed = 0.874 m/s. 2D scene, static camera; fps = question_fps = 24.
- Track: scene/tracks/chestnut_horse.csv, frames 0-48 (frame 49 is an animation-loop reset back to the start position, so it is excluded). I checked it on frames 0, 18 and 30: the box runs from rump/hind hoof to muzzle.
- Pixel speed (measure.py): linear fits of x against frame give 3.24 px/frame for the mask centroid, 3.26 for the box centre, and 3.24 / 3.28 for the box edges. The endpoint route (first to last frame) gives 3.15 px/frame. I used 78.0 px/s, so the scale is 0.874 / 78.0 = 0.01120 m/px.
- Length: horizontal nose-to-tail extent. Median 187 px, mean 188 px; it varies from 166 to 213 px over the gait. By eye: frame 0 ≈ 153→337 (184 px), frame 18 ≈ 213→390.
- Answer: about 188 px × 0.0112 = 2.11 m. The endpoint speed would give 2.17 m, so I answer 2.12 m.
- Confidence: moderate, about ±5%. The main uncertainties are the gait-induced length variation and the fact that the length convention (pose and frame used for the box) is unknown.
