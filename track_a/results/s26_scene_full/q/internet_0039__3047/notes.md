# Q3047: speed of the swimming man from 1 s to 2.33 s (m/s)

## Setup
- Overhead view with a static camera (checked in scene/notes.md: the rope strips move less than 1 px per frame). The swimmer moves in -y. I treated the scene as 2D and used one scale.
- Scale from the prior (height 1.68 m). I measured head-to-toe pixel length from the cap top to the feet: the track's median is 1040.7 px (IQR 1017–1062). I checked it by eye on frames 20 and 51 using gridded crops (look.py → frames/c20.png, c51.png), which gave about 990 and 1040 px. That gives 1.68 / 1040 = 1.615e-3 m/px.

## Time base
- The file runs at 18.54 fps and has 8 duplicated frames, so it was frame-rate converted. The question states 25 fps.
- At 25 fps one stroke cycle (56 frames) takes 2.24 s and the speed is about 0.76 m/s, which is a believable leisurely front crawl. At 18.54 fps the cycle would be 3.0 s and the speed about 0.56 m/s, which is very slow.
- I used question_fps = 25: t = 1 s is frame 25 and t = 2.33 s is frame 58.

## Measurement (speed.py, on scene/tracks/swimmer.csv)
| Reference point | Net displacement, frames 25→58 | Average speed (net) | Path length | Linear-fit speed |
|---|---|---|---|---|
| Head (cap) | 622.1 px | 0.761 m/s | 0.794 m/s | 0.736 m/s |
| Hip (trunks) | 619.0 px | 0.758 m/s | 0.778 m/s | 0.726 m/s |

The head and the hip, two independent routes, agree within 0.5%. Path length comes out a bit higher because of tracking jitter.

**Answer: 0.76 m/s.** For reference, using the file's own 18.54 fps would give about 0.52–0.58 m/s.

Confidence: moderate. The main uncertainties are the pixel height (about ±4%) and which time base the reference answer used.
