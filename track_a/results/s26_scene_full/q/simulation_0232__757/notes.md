# Q757 – clock diameter (m)

Prior: black cat speed = 0.714 m/s. No depth_info. fps 24 (= question_fps). Static camera, frontal view of the wall.

## Scale from the cat (measure.py)
Cat torso-centroid track (scene/tracks/cat.csv, frames 0–49; checked on a frame that it is the cat on the desk):
- linear fit of x: 8.96 px/frame = 215.0 px/s (mask centroid 214.8, nose 216.4, torso ends 213.5 / 218.1)
- end to end: (702.1 − 255.9)/49 = 9.11 px/frame = 218.5 px/s
- mean of per-frame steps: 220.6 px/s. This one is pushed up by ±3 px gait jitter of the centroid, so I didn't use it.
Value used: 216 px/s, giving 0.714/216 = 0.003306 m/px.

## Clock (measure.py)
Averaged 10 frames. I fitted a circle to the outer edge of the dark rim along 72 radial profiles: R = 56.3 px,
diameter = 112.7 px. Thresholded extents: 112.7 px horizontal, 111.2 px vertical. Value used: 112.5 px (the outer diameter).

## Depth check
The desk's back edge (y≈738) and the cat's paws (y≈740) put the cat on the desk top close to the wall. Using the
wall/floor line (950), the ceiling line (175) and the desk-top edges, I estimate Z_cat/Z_wall ≈ 0.97–0.99 for horizon
rows between 450 and 540. That makes the clock about 1–2 % larger than a single 2D scale gives, so I applied a +1 % correction.

Diameter = 112.5 × 0.003306 × 1.01 ≈ 0.375 m. Range across methods: 0.364 (per-frame-step speed, no correction)
to 0.382 (linear-fit speed, +2 %).

## Confidence
Moderate to high, about ±4 %. The main uncertainty is which convention gives the cat's pixel speed.
