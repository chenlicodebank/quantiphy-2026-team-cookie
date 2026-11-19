# q3139: height of the sign on the ground (internet_0053)

The "sign on the ground" is the free-standing A-frame "QUIET HOURS" board to the right of the court gate (x ~1063-1129).
Time base: 30 fps (file rate = question rate). The clip shows nothing that suggests it was re-timed.

## Scale (prior: rider's average speed = 4.46 m/s)
The scene/ track has the rider and scooter moving right in a near-straight line, and the camera is static (drift < 2 px).
- Rear-wheel centre, frames 0-80: 406.5 -> 1855.5 px = 543.4 px/s
- Scooter centre (midpoint of the wheels), frames 0-73: 547.3 px/s
- Upper-body template track, frames 0-80: 538.2 px/s
- Adopted value: 543 px/s (±1%). Because the path is straight, the mean of the per-frame speeds is about the net speed.
- Scale: 4.46 / 543 = 0.00821 m/px

## Sign pixel height (sign_measure.py: column profiles at x = 1070-1125; zooms frames/sign2.png and frames/signbot.png)
- Top of the handle tabs: y ~575.5 at frame 0 (~572.5 at frame 78; the camera drifts in y by about 3 px)
- Bottom of the board and base rail, where it meets the mulch: y ~683.5 at frame 0. A dark shadow band below it, down to ~688, is not counted.
- Height: ~108 px at frame 0 and at frame 78. The scene record gives 109 px. Adopted value: 108.5 ± 2 px.

## Answer
108.5 px x 0.00821 m/px = 0.89 m.
Check: a sidewalk sandwich board is typically 0.9-1.0 m tall, so the answer is plausible. The sign stands farther back (at the fence line) than the rider. A true perspective correction would make the sign somewhat larger, but the benchmark convention uses a single planar scale, so no correction is applied.
Confidence: moderate-high. The main uncertainty is whether the shadow or base at the bottom should count (±4%).
