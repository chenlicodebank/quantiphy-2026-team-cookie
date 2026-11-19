# q2882 – white ball diameter (cm)

The white ball is the record's `grey_object`, an off-white ball. The green ball is `yellow_object`, a yellow-green tennis ball. The two fly together.
- Depth at t = 1.0 s (frame 24, question_fps 24, same as the file rate): white 1.235 m, green 1.331 m.
- Focal length: f = 0.5959 × 1280 = 763 px (lab card).

## Method
- **Foreground:** difference from the median background (threshold 30), then split by colour. Green pixels are those with G−B > 40; white = the rest of the blob.
- **Width:** the minimum caliper width of each ball's mask (measure3.py). Motion blur only stretches a ball along its motion, so the width across the motion is close to the diameter.
- **Frames 21–34**, in px:

  | | f21 | f22 | f23 | f24 | f25 | f26 | f27 | f28 | f30 | f34 |
  |---|---|---|---|---|---|---|---|---|---|---|
  | white | 48.3 | 47.6 | 51.6 | 45.6 | 41.1 | 45.5 | 36.0 | 34.0 | 33.6 | 27.4 |
  | green | 44.6 | 43.1 | 41.3 | 41.5 | 37.4 | 34.0 | 34.0 | 32.0 | 30.1 | 24.7 |

  Both balls fly away from the camera, so they shrink. The blurred frames 23 and 26 are noisy for white, because the mask overlaps the green ball.

## White width at frame 24
| Route | Width (px) | Diameter |
|---|---|---|
| Direct, frame 24 | 45.6 | 1.235 × 45.6 / 763 = 7.38 cm |
| Smooth fit of 1/w vs frame (lin/quad) | 44.2–44.5 | 7.17 cm |
| White/green ratio (median 1.107, frames 21–34) × green width at f24 (39.2 fitted to 41.5 direct) | 43.4–45.9 | 7.0–7.4 cm |

## Check
The green ball at frame 24 is 39.2–41.5 px wide. That gives 1.331 × w / 763 = 6.8–7.2 cm, which fits a tennis ball (about 6.7 cm). This supports both the scale and the masks.

## Answer
7.3 cm (range 7.0–7.4). This is plausible for a baseball. Confidence: moderate, about ±5%.

No speed was needed, so the velocity prior was not used. The record's dropped-frame anomalies do not matter here.
