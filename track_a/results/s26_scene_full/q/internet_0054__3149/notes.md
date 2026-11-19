# q_3149 – height of the scooter (m)

Prior: average speed of the rider = 4.9 m/s. 2D internet clip, rider moving side-on right to left. fps = question_fps = 30, so no re-timing.

## Scale (speed.py)
I used the per-frame track in scene/tracks/rider_scooter.csv. I checked the front-wheel x positions against my own crops at frames 0, 45 and 93, and they match.
Mean per-frame pixel speed over frames 0–93:
- stabilised (measured against the background; the camera drifts about +0.34 px/frame): 496.9–498.8 px/s (box centre, torso, front axle) → **497.5 px/s**
- raw: about 488 px/s

Scale = 4.9 / 497.5 = **0.009849 m/px**. With raw coordinates it would be 0.01007, about 2 % higher.

## Scooter height in pixels (zoom.py, view.py; 6x zoomed crops)
Height runs from the top of the handlebar to the bottom of the tyre (ground contact). The handlebar bar is hidden inside the rider's hands, so I put its top about 2 px below the top of the hands.
| frame | handlebar top y | tyre bottom y | height px |
|---|---|---|---|
| 0  | ~930 | 1122.5 | ~192.5 |
| 45 | ~935 | ~1129  | ~194 |
| 93 | ~936 | ~1135.5| ~199.5 |
The rider moves slowly toward the camera, so the apparent size grows about 6 % over the clip. I used the value at the middle of the clip, which is also the clip average: **~195 px** (±3 px).

Height = 195 × 0.009849 = **1.92 m**. With the raw-coordinate scale it would be 1.96 m.

## Check
The scooter length from the record (tyre to tyre) averages 185.4 px over the clip. My height/length ratio is about 1.04–1.05, and length × scale = 1.83 m, so the height comes out at about 1.91 m. That agrees with the direct reading. Both use the same scale, but the pixel measurements are independent.

## Caveat
The speed prior gives a scale that is large for real life: the person would be about 2.8 m tall. Because fps equals question_fps there is no re-timing to correct this, and the prior is defined as exact, so I applied it as given. Confidence: moderate. The handlebar top is hidden by the hands (about ±2 %), and the choice between stabilised and raw speed adds about ±2 %.
