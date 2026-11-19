# q_1845 — ball diameter (m)

2D Blender clip (segmented, white background), 1920x1080, 24 fps file = question_fps 24, 38 frames.
Prior: gravity 9.8 m/s^2 -> the red ball falls freely from rest through the whole clip (no bounce), so it sets the scale.

## Scale (measure.py)
- Ball centre tracked per frame (red component, coverage-weighted centroid). Quadratic fit of y(t), all 38 frames:
  a = 609.2 px/s^2, rms residual 0.14 px. Frames 3-37: 609.0; frames 0-19: 612.1.
- m/px = 9.8 / 609.2 = 0.01609 m/px.

## Ball pixel diameter (diam.py, area.py, dump.py)
- Raw pixel dump (frame 3): the sphere has a dark rim (min-channel 60-130) and a lighter highlighted top (130-200);
  outside pixels 230-255. Edge-to-edge extent about 25 px vertically, 25.5 px horizontally.
- Area-equivalent diameter of the non-white blob: 25.1-25.3 px (threshold 220), 25.7 px (threshold 235, includes faint
  antialias/compression halo). Horizontal 50% profile width 25.5 px. The red-chroma mask (23.3 px) is too small because of
  4:2:0 chroma blocks and the highlight; not used.
- Adopted D = 25.4 px (+-0.4).

## Answer
D = 25.4 x 0.01609 = 0.409 m.

## Check / caveats
- Second route: threshold-235 bbox mean (27.1 x 25.7, like the scene record's 26 px) gives 0.41-0.43 m; area at 220 gives
  0.405 m. All within ~4 %.
- Forklift at this scale would be 4.7 m long and 3.9 m tall (larger than a real forklift); it may be at a different depth
  or scaled, but the ball's own fall gives the scale at the ball, so the answer uses gravity as the prior says.
- Confidence: good (~3 %).
