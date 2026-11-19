# Q302: width of the car (m)

The video is a 2D top-down Blender render of an airport apron at 24 fps (question_fps is also 24). The only car is the small dark tug that tows the airliner up the image at x ≈ 475. Prior: the car's speed is 11.155 m/s.

## Scale (speed.py)
- I took a template of the tug, towbar and nose at frame 71 and matched it in frames 2, 10, …, 71 with sub-pixel peak fitting.
- The motion is a constant 5.2470 px/frame (residuals under 0.1 px), i.e. 125.93 px/s. This agrees with scene/tracks (5.247).
- Scale = 11.155 / 125.93 = **0.08858 m/px**.
- Sanity check: with this scale the airliner is 423 px = 37.5 m long and has a 386.5 px = 34.2 m wingspan, which matches an A320. So the scale is plausible.

## Width in pixels (rows.py, measure.py)
- I printed the raw grey-level rows across the tug at frame 71 and checked frames 20, 40 and 60.
- I found the edges per row at sub-pixel level from partial-pixel coverage, against the local background (the background is in shadow on the left, ~91–110, and bright on the right, ~163).
- Measured widths:
  - front section (rows 411–421): left edge ≈ 463.4–463.7, right edge ≈ 487.3–487.4, width ≈ 23.6–24.0 px;
  - rear section (rows 448–450): ≈ 462.7–487.3, width ≈ 24.6 px;
  - narrowest part, the mid body with its grey trim: ≈ 22 px.
- The width is the bounding-box extent, so I use the maximum extent: ≈ 24.4 px (±0.5). The record's value is 25 px.

## Answer
24.4 px × 0.08858 m/px = **2.16 m**. Other readings give: 25 px → 2.21 m; mid body only (22 px) → 1.95 m.

Second-route check: the speed from my own template matching and the speed in the record agree to 0.01 %. The front-section and rear-section widths agree within about 0.6 px.

Confidence: moderate to high. The main uncertainty is about ±0.5 px of edge softness, which is about ±2 %.
