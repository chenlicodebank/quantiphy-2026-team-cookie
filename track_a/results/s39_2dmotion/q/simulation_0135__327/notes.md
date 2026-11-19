# Q327: speed of the cup at t = 2.25 s (m/s)

Prior: cup diameter = 0.087 m. 2D video; question_fps = file fps = 24, so t = 2.25 s is frame 54.

## Object
The only moving object is the navy-blue cup (scene record "blue_cylinder"). It lies on its side, slides left to right along the
counter at a constant depth (bottom edge y≈997 the whole time), and turns slowly about a vertical axis. It is a tapered cup:
the closed base is the smaller end, the open rim the wider one.

## Problem: frame 54 is off-screen
The cup leaves the right edge by frame 54. It is fully gone at frames 54-59 and cut by the edge at frames 47-53. Over frames
29-46 it moves at a constant speed with no trend:
- Linear fits of my colour-mask centroid (`measure.py` → `my_track.csv`, `speed.py`): 28.07, 28.07, 28.09 and 28.10 px/frame over
  windows 30-46, 35-46, 30-38 and 38-46. Vertical speed is about 0.07 px/frame.
- SAM 3 track (`tracks/blue_cup_0.csv`): 28.11, 28.05, 28.30 and 28.09 px/frame over the same windows.
- Second check (scene record `cx_edge_est`, the exit-edge estimate while the cup is cut, frames 46-53): steps of 24-29 px,
  mean of about 27 px/frame. This agrees within its noise; that estimate is biased slightly low because the cup's rotation
  changes where its edges sit relative to its centre.

So the speed at frame 54 (backward difference 53→54) is taken as the constant **28.1 px/frame**, extrapolated from that window.

## Scale
Diameter in pixels: I took the widest cross-section across the cup axis (the rim).
- Frame 20 (axis nearly towards the camera): row-by-row half-max edges of the blue signal (`edges.py`) give a maximum width of
  129.8 px at y≈890. The mask bbox width is 128 px.
- Frames 31-46 (axis at about 45°): the 95th percentile of the across-axis width profile is 128-130 px (`measure.py`).
- SAM 3 masks: frame 44 width_px = 133.9 (2.8 % above mine); frame 20 horiz_px = 135 and box width 134 (about 4 % above).
  On the zoomed frame 20 (`frames/f20.png`) the cup's edges are at x≈951 and x≈1081 at the widest row. SAM's box
  (949.4-1083.4) takes in the soft anti-aliased edge and shadow fringe on both sides. My half-max edges are right there.
- I used D = 129 px, so the scale is 0.087 / 129 = 6.744e-4 m/px.

(If "diameter" meant the smaller base, about 105-110 px, the answer would be about 20 % lower. The max/rim diameter is the
bounding-box reading, so I used it.)

## Answer
v = 28.1 px/frame × 24 fps × 6.744e-4 m/px = **0.455 m/s**

Confidence: moderate-high. The pixel speed is solid (±0.5 %). The main uncertainties are the extrapolation to the
off-screen frame, the pixel diameter (±2-3 %), and whether the Blender origin sits off the visual centre (with rotation
this could change the per-frame step by about 1 px).
