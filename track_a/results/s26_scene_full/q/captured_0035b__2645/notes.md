# q_2645: soccer ball diameter (cm)

The file rate and question_fps are both 24. So t=0.9 s is frame 22 and t=1.4 s is frame 34. The focal length is f = 0.5959 x 1280 = 763 px.

## depth_info labels
Both t=1.4 lines say "soccer_ball" (2.6020 and 2.3730). One of them must be the basketball's distance. I decided which by checking that the depths agree with the pixel sizes:
- The soccer ball's pixel diameter grows from 53.0 to 55.0 px. Then 2.477 x 53.0/55.0 = 2.387, which is close to 2.373.
- The basketball's pixel diameter grows from 62 to 66.5 px. Then 2.778 x 62/66.5 = 2.59, which is close to 2.602.

So I read soccer_ball = 2.373 m and basketball = 2.602 m at t=1.4 s.

## Measurement (measure.py)
I fitted a robust circle to the steepest radial luminance edge along 72 rays, seeded from the scene/ track, on frames 18-39. I used medians over ±2 frames:
- Soccer ball: about 53.0 px at frame 22 and about 55.0 px at frame 34. This agrees with the scene/ record (52.5 and 54.8).
- Basketball: about 62 px at frame 22 and about 66.5 px at frame 34.

## Results
| Route | t = 0.9 s | t = 1.4 s |
|---|---|---|
| Direct pinhole, soccer ball | 2.477 x 53.0 / 763 = 17.2 cm | 2.373 x 55.0 / 763 = 17.1 cm |
| Prior check, basketball | 2.778 x 62 / 763 = 22.6 cm (prior 23.2, -2.7 %) | 2.602 x 66.5 / 763 = 22.7 cm (-2.2 %) |
| Ratio to the basketball (scaled by the prior) | 17.7 cm | 17.5 cm |

The direct pinhole route reproduces the basketball prior to within about 2.5 %, but slightly low. The ratio route corrects for that small bias. I answer 17.4 cm, between the two routes. I expect it to be within about 3-4 %.

Under the literal labels (soccer ball = 2.602 m at t=1.4 s), the t=1.4 s value would be 18.8 cm. I rejected that reading because it disagrees with the t=0.9 s value and with the pixel-size trend.
