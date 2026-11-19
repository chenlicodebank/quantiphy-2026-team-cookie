# Q400 – width of the road the bike and car are on (m)

Prior: bike speed = 5.52 m/s. No depth_info. fps 24 = question_fps.

## Scale (2D top-down, static camera)
- Cyclist pixel speed: the scene track gives a mean per-frame speed of 14.44 px/f and a linear fit of 14.42 px/f.
  An independent whole-cyclist template match gave 14.40-14.46 px/f over frames 10→70, 20→60 and 20→70
  (`speed.py`). Used 14.43 px/f = 346.3 px/s, so 5.52/346.3 = 0.01594 m/px at the tracked point's height.
- Perspective correction: the tracked point (backpack, about 1.1 m up) sits closer to the camera than the road.
  I estimated the camera height at about 55 m from two cues: car roof features drift −0.22 px/f against bumper
  features while the car moves 18 px/f, and the lamp pole leans radially (top/base distance ratio 1.17).
  Ground scale ≈ 0.01594 × 55/53.9 ≈ 0.0163 m/px. This changes the result by about 2%.

## Road edges (`profile.py`, median row profile over x 500-1100 at frame 79, when the road is empty)
- Top kerb: bright kerb top at y 336-341; asphalt starts at y≈342. White edge line: y 359.5-368.5 (centre 364).
- Yellow centre lines: dashed at y 527.5-534.5, solid at y 541.5-548.5.
- Bottom white edge line: y 735-744.5 (centre 739.8). Gutter at y 746-751, then kerb top at y 752.5-758.5.
- The lamp posts stand beyond both kerbs, on the sidewalks.

| reading | px | m (0.01594) | m (0.0163, ground) |
|---|---|---|---|
| kerb to kerb (asphalt, 342→752.5) | 410.5 | 6.54 | 6.69 |
| white edge lines, outer edges | 386 | 6.15 | 6.29 |
| white edge lines, centres | 375.8 | 5.99 | 6.12 |
| one lane (yellow solid → white) | 194.5 | 3.10 | 3.17 |

Answer: kerb-to-kerb carriageway width ≈ **6.65 m**.

## Checks
- Car length with the same scale: 289 px × 0.0159-0.0163 = 4.6-4.7 m, a plausible police saloon.
- Car speed: 18.04 px/f gives about 6.9-7.1 m/s, and a lane of about 3.1 m is a realistic width.

Confidence: the scale is good to about 2%. The main uncertainty is which width the question means: kerb to kerb
(my answer) or edge line to edge line (about 6.1-6.3 m), roughly 7% apart.
