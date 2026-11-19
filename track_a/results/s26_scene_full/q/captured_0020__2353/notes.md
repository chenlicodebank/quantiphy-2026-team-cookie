# q_2353 – distance between the two people (cm)

Lab video, 1280x720, 24 fps (file fps = question_fps = 24). The camera is static and both people stand with their feet fixed,
so the distance does not depend on time.
Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
depth_info: near (left) person 1.580 m, far (right) person 3.237 m. The jar/carrot depths belong to other objects and are not used.
The gravity prior gives no scale for a static distance, so the scale comes only from depth_info.

## Method (dist.py)
Back-project each person's centre: P = d * unit((u-cx)/f, (v-cy)/f, 1), then take the 3D distance |P_near - P_far|.
I picked the centre pixels on gridded frames 0 and 14 (frames/f00.png, frames/f06.png):
- Far person (head cut off at the top border, soles at y about 267): torso/hip centre about (710, 100); visible-bbox centre (705, 135).
- Near person (cut off at the left and bottom borders): mid-torso about (150, 430); visible-bbox centre (195, 418);
  hips (shirt hem) about (170, 570).

## Results (cm)
| near centre / far centre | result |
|---|---|
| mid-torso / torso | 236.9 |
| mid-torso / bbox | 233.3 |
| bbox / bbox | 227.0 |
| hips / hips | 247.0 |
| chest / chest | 237.8 |

Across the plausible "clicked centre" choices the spread is 227-254 cm, centred on about 237 cm.

## Second-route check
I tried to estimate the camera pitch from vertical lines (room corner, radiator edge, far person's legs), to check that both
centres sit at about the same height. The lines are too blurred and too close to parallel (there may be roll or lens distortion)
for a reliable vanishing point, so this check was not conclusive. I also tried assuming a pitch from the hip-to-hip pair
(about 38 deg). With that pitch, the far person's hip would be about 0.7 m above the floor, which is roughly plausible.

**Answer: 237 cm.** Confidence is moderate: about ±5 % from the choice of centre pixel. The near person is only partly in the frame.
