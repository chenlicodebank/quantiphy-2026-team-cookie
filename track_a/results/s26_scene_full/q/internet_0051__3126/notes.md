# q3126 — height of the green car (mint Fiat 500, rear view), internet video

Convention: an internet video, so I used one planar scale taken from the prior (the average speed of the scooter rider, 2.07 m/s).
fps is 30 and question_fps is 30, so there is no re-timing issue.

## Scale (speed.py)
- Rider track from scene/tracks/rider_scooter.csv (bbox centre, pan removed): net displacement is 863 px over 49 frames,
  which gives 528.4 px/s. The mean of 5-frame-smoothed forward differences is 528.4 px/s. The raw mean of per-frame
  speeds is 531.3 px/s (inflated by jitter). In raw image coordinates, without pan removal, it is 519.8 px/s.
- Check: I read the wheel edges by eye on zoomed frames 0 and 49. The front wheel's left edge moves 1320 -> 467 and the
  rear wheel's right edge moves 1512 -> 665 (raw). Adding the +14 px pan gives about 865 px relative to the background,
  which agrees with the 863 px from the track.
- Scale = 2.07 / 528.4 = 0.003918 m/px.

## Car height (carcrop.py; frames/car_ng.png)
- Roof top is at y ≈ 600–601 (the intensity profile changes at y = 599–600; the antenna is excluded). The tyre bottom and
  ground contact are at y ≈ 798–801, where the dark shadow under the car meets bright asphalt at y 801–804. The pixel
  height is about 200 px; the scene record says 198 px.
- Height = 200 × 0.003918 = 0.784 m. With 198 px it would be 0.776 m; with the raw-image speed (519.8 px/s) it would be 0.80 m.

## Caveat
The rider is nearer the camera than the parked car, so the single-scale planar convention gives a value well below the
real height of a Fiat 500 (~1.49 m). The rider's height comes out at 1.18 m on this scale as well. I followed the
annotators' one-scale convention.
Confidence: moderate. The result follows that convention; it is not the true physical height.
