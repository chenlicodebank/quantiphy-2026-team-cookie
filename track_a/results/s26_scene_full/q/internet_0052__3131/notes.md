# q_3131 — height of the no-parking sign (m)

Prior: average speed of the scooter rider = 2.91 m/s. Internet video, 30 fps (file and question_fps agree), 56 frames.
Annotator convention: one planar scale = prior world value / prior pixel value.

## Prior in pixels (speed.py)
Mean per-frame |dx| of the rider/scooter over frames 0–55, from scene/tracks/rider_scooter.csv:
- raw frame pixels: front wheel edge 18.50 px/frame (555 px/s); bbox centre 555; scooter centre 556; person centre 550
- background-stabilised: 560 px/s (the camera drifts ~+9 px over the clip, about 1%)
Visual check: front-wheel leading edge at x≈1262 in frame 0 and ≈245 in frame 55 (raw) → 1017 px / 55 frames = 18.5 px/frame.
Used 557 px/s → scale = 2.91 / 557 = 0.005224 m/px.

## Sign (sign.py)
The "NO PARKING FIRE LANE" plate is on the light pole, x≈948–998, y 535/536–604/606.
Measured by a bright-or-red pixel mask in frames 0, 15, 30, 45 and 55: height 71 px every time (70 px between
mid-edges), width 50 px (ratio 1.42, close to a standard 12x18 in plate).
Height = 70.5 px × 0.005224 = **0.368 m → 0.37 m**.

Other reading: the whole stack of three plates (y536–658, 123 px) would be 0.64 m. I answered with the main
no-parking plate.

## Checks / confidence
- Speed routes agree within ±1% (front edge, centres, raw vs stabilised): range 0.364–0.373 m.
- The sign is farther away than the rider (it stands behind the curb), so the real plate is probably bigger
  (~0.46 m for a 12x18 in plate). The benchmark convention uses a single planar scale, so I kept 0.37.
- Confidence: medium-high under that convention.
