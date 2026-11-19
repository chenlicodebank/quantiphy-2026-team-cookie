# Q84 – speed of the walking person at 0.5 s (m/s)

Prior: bike length = 1.7 m. 2D top-down render. The file and the question both run at 24 fps. t = 0.5 s → frame 12, so the speed is the step from frame 11 to frame 12, times 24.

## Scale
- Bike length (cyan pixel x-extent, `measure.py`) at frame 12 is 381 px; the SAM 3 "bicycle" mask at frame 12 gives 380 px horizontally. The two agree within 0.3 %.
- Scale: 1.7 / 381 = 0.004462 m/px. The bike reads 376–386 px across the frame, a slight perspective effect.

## Walker motion near frame 12 (px/frame)
| proxy | step at f12 | mean of steps over f10–14 |
|---|---|---|
| head (dark hair blob, my script) | 12.5 | 12.6 |
| white shirt centroid | 11.4 | 12.3 |
| shirt bbox centre | 12.5 | 12.2 |
| SAM mask centroid (limbs included) | 10.7 | – |
| SAM mask eroded core (15 px) | 14.3 | – |

- The pelvis can't be seen from above; the torso and head are the best proxies.
- The SAM centroid is pulled around by the swinging legs and arms, and the eroded core keeps parts of the thighs. Both differ from the torso proxies by more than 3 %, so I set them aside as noisier.
- I checked the SAM overlay (frames/seg_03_f12.jpg). The person mask is clean and the bike mask matches mine.
- Adopted pelvis step: about 12.4 px/frame.

## Speed
- Planar single scale: 12.4 × 24 × 0.004462 = 1.33 m/s.
- Perspective correction:
  - Parallax shows a camera distance of about 33 m: the rider's head shifts 0.04 px per px of x.
  - The pelvis (about 1 m high) and the head (about 1.7 m) therefore move about 2–4 % more pixels per metre than the bike, whose extremes are at axle height.
  - Corrected: from the head, 12.5 × 24 / (223.1 × 1.043) = 1.29 m/s; from the torso, about 1.27–1.30 m/s.
- **Answer: 1.29 m/s.**

## Second route
- Mean walk speed over frames 1–28 from the head is 12.95 px/frame, which gives 1.39 m/s planar or about 1.33 m/s after the perspective correction. Frame 12 is in a slightly slower part of the gait, which agrees.

## Confidence
Moderate, about ±7 %. The main uncertainty is the gait-phase speed of the hidden pelvis at this frame.
