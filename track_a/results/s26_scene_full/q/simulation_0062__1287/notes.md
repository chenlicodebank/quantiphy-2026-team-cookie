# q1287 – bicycle wheel diameter (m)

The file and the question both run at 24 fps. t=0.58 s is frame 14 and t=1.58 s is frame 38.

## Scale / focal length
- The white van (prior: a = 4 m/s²) moves parallel to the image plane at constant image size. A quadratic fit to the van x track (scene/tracks/van.csv, `fitvan.py`) gives a = 0.5333 px/frame² from f1, f10 and f22 onward (rms 0.5 px), which is 307.2 px/s². So Z_van/f = 4/307.2 = 0.013021 m/px.
- With the van depths D(f14)=30.065 and D(f38)=29.3069: f² = (D/k)² − r². This gives f = 2239.0 and 2239.8 px, so the two times agree. I used f = 2240 px, giving Z_van = 29.17 m (van about 5.9 m long and 2.1 m high, which is plausible).
- Bike depth: D = 27.1687 / 27.0656 at f14/f38. Taking the box-centre x as the origin gives Z = 27.04 / 26.95. If the origin sits about 38 px behind the box centre (the offset that makes Z constant), Z = 26.99 at both times. I used Z_bike = 26.99 m.

## Wheel pixel size (`wheel3.py`)
I fitted a circle to the white rim/tyre ring with a radial-profile fit over 120 angles, in every second frame from f28 to f64 (both wheels, ignoring the frames where the ring is occluded or crops into another wheel):
- outer half-max edge diameter: 51.0–52.4 px, median about 51.9 px
- ring centreline 49.3 px; inner edge 47.0 px
- The hub centre is at y = 595, so the bottom of the wheel is at about 621, which matches the track's ground_y of about 620.

Diameter (outer tyre) = 51.9 × 26.99 / 2240 = **0.625 m** (range 0.619–0.631). Measured at the ring centreline it would be 0.594 m.

## Check
- The pedestrian's height from its own depths is 1.828 m at f14 and 1.827 m at f38. This is consistent and plausible.
- Wheelbase: 83 px, about 1.0 m. Bike length: 134 px, about 1.6 m. Both are plausible.

Confidence: good (about ±3%). The main uncertainty is whether to measure the tyre's outer edge or the ring's centreline.
