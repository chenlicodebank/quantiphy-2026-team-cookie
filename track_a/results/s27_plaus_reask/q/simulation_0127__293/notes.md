# Q293: width of the dark green car (m)

Prior: bike speed = 24 m/s. No depth_info. The video is a 2D top-down render with a static camera, 24 fps (the file and
question_fps match).

## Object
The dark green car is the parked coupe at the lower right curb, centred near (1800, 767). The scene record calls it the
"dark_sports_car (dark grey)". It is static, its front points left, and it is visible in all frames.

## Scale (from the prior)
- Cyclist step, from my own NCC template matching over 10-frame gaps (frames 10→20→30→40→50, `speed.py`):
  31.73, 31.82, 31.79 and 31.78 px/frame. The scene csv gives 31.5–31.7 (mean 31.64). I used **31.7 px/frame**,
  which is 760.8 px/s.
- Scale = 24 / 760.8 = **0.03155 m/px**.
- Plausibility: 24 m/s is not a realistic bike speed, so the scene is scaled about 1.6x. With this scale the bike is
  2.7 m long, the blue car 7.45 m and the red car 7.7 m. All of them are consistently about 1.6x real size, so the
  prior's scale is applied as given.

## Car width (y extent, across the body)
- Edge profiles per 10-px column (`edges.py`, `width2.py`), plus a contrast-stretched zoom (`view.py`,
  frames/dark_cs.png):
  - Top body edge: y = 719 ±1.
  - Bottom body silhouette: y ≈ 813 ±2. A highlight line at about 808 sits inside the body, and the darker band at
    814–820 is shadow next to the curb, which starts at y = 821.
  - Mirror tips: y 716.5 to 819.5.
- Body width ≈ **94 px** (range 91–97) → 2.97 m. Mirror to mirror 103 px → 3.25 m. The scene record's 90 px body width
  would give 2.84 m.
- The reference (a Blender bounding box) may or may not include the mirrors, so I answered with a value between the
  two readings: about 96.7 px → **3.05 m**. That is within about 3–6 % of both readings.

## Second-route check
- The cyclist speed from two independent trackers agrees within 0.5 %.
- The width is the same on frames 20, 41 and 56, as expected for a static car.
- The width-to-length ratio (about 94/228 = 0.41) is plausible for a sports car.

Confidence: moderate-high. The main uncertainty is whether the mirrors count, about ±5 %.
