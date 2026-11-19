# q_3270: average velocity of the toilet paper roll from 0.50 s to 1.50 s (cm/s)

**Answer: 11.0 cm/s**

## Scale
- Prior: the roll's width is 10 cm. For a toilet roll, "width" means its length along the axis. Here the axis is horizontal, so this is its horizontal pixel extent, end to end.
- At rest (frames 56–59) the extent is 584.5 px. The diameter is about 698 px, which gives a diameter of 11.9 cm. That is a plausible real roll, so this reading of "width" makes sense.
- While the roll moves (frames 14–45) the extent is 603 px on average. It reads longer there because the roll is slightly turned and a sliver of its end face shows.
- I used 585 px, so the scale is 0.01709 cm/px. Using 595 px would lower the result by about 1.7%.

## Time base
- The file is 24.098 fps with 60 frames. That odd rate suggests the clip was re-timed. The question states 30 fps.
- Both rates give a plausible hand speed (about 10 cm/s), so physical plausibility cannot settle which rate is right.
- I used question_fps = 30, taking it to be the original footage's rate. That means frames 15 to 45.
- With 24.1 fps (frames 12 to 36) the result would be 9.85 cm/s.

## Track
- I used `scene/tracks/toilet_roll.csv`. The camera is static.
- I checked the track against frames 15, 45 and 56 (`frames/`). The boxes match the roll: left edge at 2414, 1778 and 1616 px.
- Reference point: the centre of the bounding box.

## Results (`speed.py`)
| Method (30 fps, 585 px) | cm/s |
|---|---|
| Mean of per-frame centre speeds, frames 15–45 | 11.16 |
| Net displacement of the centre ÷ 1.0 s | 10.98 |
| Second route: left-top corner of the box | 11.12 (mean speed) / 10.93 (net displacement) |

The two routes agree to within 2%. The answer is 11.0 cm/s.

## Confidence
- Moderate.
- The main uncertainty is the frame rate: 30 fps gives 11.0 cm/s, 24.1 fps gives 9.9 cm/s.
- The pixel length used for the scale adds about 2–3%.
