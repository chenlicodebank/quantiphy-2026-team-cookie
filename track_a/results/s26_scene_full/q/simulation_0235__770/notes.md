# Q770: height of each small window pane (m)

The video is a 2D, fronto-parallel Blender render with a static camera, at 24 fps (the file rate and question_fps agree).
The prior gives the basketball diameter as 0.282 m. depth_info is null, so I used a single metres-per-pixel scale.

## Ball (scale), from ball.py
- I built an HSV mask and took the largest blob. On frames 0, 10, 40 and 49 the bbox is 108 x 108 px, the area-equivalent diameter is 107.2–107.7 px and the hull-equivalent diameter is 107.5–107.9 px. The scene record's circle fit gives 106.1 px.
- I used 107.5 px, so the scale is 0.282 / 107.5 = 0.002623 m/px.
- The ball touches the floor at y ≈ 920, which is the wall-foot line. So the ball is close to the wall plane where the windows are, and one scale fits both.

## Pane height, from measure_pane.py and profile.py
I took vertical intensity profiles through 7 panes in each of the two rows. All panes in a row are the same.
- **Top row:** the frame band is at y 37–45, then a shadowed reveal strip at y 46–52, then black glass from y 53 to 199. That gives 147 px of black, or about 154 px with the reveal.
- **Bottom row:** the frame band is at y 239–246, the reveal at 247–251, and black from 252 to 400. That gives 149 px of black, or about 154 px with the reveal.
- I took the pane height as about 150.5 px, between the black-only and reveal-included values. The record's figure of about 150 px agrees.

## Answer
150.5 px x 0.002623 m/px = **0.395 m**.

Bounds: 147 px of black-only glass with a 108 px ball gives 0.384 m. 154 px with the reveal and a 106 px ball gives 0.410 m. So the answer is good to about ±3–4 %.

## Second-route check
- The bottom-row and top-row panes, measured separately, agree to within 1.5 %.
- The width-to-height ratio is consistent: panes are about 196–205 px wide.

## Caveat
The ball's fall acceleration is about 1.35 px/frame², which at this scale is only about 2 m/s². So the render is not at real-world scale, and I followed the prior, as instructed.

## Confidence
Moderate to high. The main uncertainty is whether the shadowed reveal strip counts as part of the pane (about 4 %).
