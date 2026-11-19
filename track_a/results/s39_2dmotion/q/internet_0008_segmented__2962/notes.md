# q_2962: average speed of the speedboat (prior: sailboat length = 12 m)

## Objects
- Sailboat: the large maroon ketch, visible in all frames (prior object).
- Speedboat: the small dark blob at the bottom (scene/ "bottom_object"). It enters at the left edge at file frame 179, is fully in from frame 184 and is still moving right at frame 239.

## Time base
- The file is 24 fps with 240 frames (10.0 s). question_fps is 30.
- The speedboat's per-frame steps repeat every 4 file frames: ~7, 7, 7, then ~14 px. That is a duration-preserving 30 -> 24 fps resample, with 1 of every 5 original frames dropped. So 24 file frames = 1 real second, which is the same real time as 30 original frames.
- Speeds are therefore px per file frame x 24. This equals the original's px per frame x 30.
- Alternative reading (not used): px per file frame x 30 would give 32.3 m/s, 25 % higher. I rejected it because the frame-drop pattern shows the clip keeps real time.

## Scale
- `measure.py`: dark-pixel mask (min RGB < 200, watermark excluded) and connected components.
- Sailboat overall horizontal length: median 100 px over 240 frames. The hull alone is 99 px.
- Scale = 12 / 100 = 0.120 m/px.
- SAM 3 sailboat mask: horiz 100 px at f184 and 97 px (box 99.4) at f239. Both agree with 100 px to within 3 %.

## Speedboat motion (`speed.py`)
| Reference point and frames | Mean per-frame speed | Speed |
|---|---|---|
| Centroid, frames 184-239 (2D) | 215.6 px/s | 25.87 m/s |
| Right edge, frames 179-239 | 214.4 px/s | 25.73 m/s |
| Right edge, frames 184-239 | 216.0 px/s | 25.92 m/s |
| Left edge, frames 184-239 | 213.8 px/s | 25.66 m/s |

- The boat accelerates gently, from about 190 to 245 px/s (quadratic fit).
- Second route: the mean of the quadratic-fit velocity is 216.0 px/s, or 25.92 m/s. This matches the first route.
- SAM 3 check of the speedboat centroid: 29.9 at f184 and 522.7 at f239. My values are 29.8 and 523.4. The displacement is 492.8 px from SAM against 493.6 px from mine (0.2 % difference). Box widths are 37 / 42 px for both.
- A box-prompted SAM run ("boat") at f184 returned a mask that included the white background (66x45 px). The overlay showed this, so I rejected it. The text-prompted mask (37x19 px) matches mine.

## Answer
- 25.8 m/s, about 215 px/s x 0.12 m/px.
- Confidence: moderate-high for the measurement (the routes spread ±0.5 %).
- The main risk is the time-base convention: if the reference used 30 per file frame, its answer would be 32.3 m/s.
