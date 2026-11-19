# Q2744 – diameter of the white ball (cm)

Lab video, 24 fps (file fps = question_fps = 24), 1280x720, so f = 0.5959*1280 = 762.8 px, principal point (640,360).
depth_info: ball at t=1.5 s (frame 36) d = 0.7045 m; t=2.0 s (frame 48) d = 0.627 m. (The prior, card length 85.6 mm,
isn't needed for this size; the lab camera f is fixed.)

## Pixel diameter at frame 36 (primary)
At t=1.5 s the ball is near the top of its 2nd arc and moves almost horizontally, so I measured its vertical extent
in diff-vs-median-background profiles through the centre column (diffprof.py, rawprof.py):
- top: sharp step (ball edge) at y≈338.6; above it is a ≈5 px low-contrast halo (SAM2 background-blur bleed),
  which shows up the same way at the frame 45 top edge and on the still ball in the hand.
- bottom: the ball's shaded underside covers the white cup rim (the rim is bright in the background but the
  ball's yellowish pixels sit in front of it), so the edge is at y≈379-380, with a few px of halo below.
- step-to-step extent ≈ 41 px. About 3 px of that is vertical smear (vy ≈ -7.5 px/frame, exposure ≈ 0.4 frame from
  the length of the horizontal streak), giving **D_px ≈ 38.5-41 px**. A low-threshold criterion (15 % of peak)
  minus halos gives ≈ 41.5 px. The record's mask_height_vertical (39, threshold 25) agrees.
- Size = d * px / f = 0.7045 * (38.5…41.5) / 762.8 = 3.56…3.83 cm (with Z = d*cos = 0.697 instead: 3.52…3.79).

## Second route: frame 48 (t=2.0 s, d=0.627, Z=0.507 since the ball is off-axis, cos 0.809)
Blurred streak along 56°. The extent across the motion (perp48.py) is ≈57 px at 15 % of peak and ≈52 px after
removing the halo. Tangential scale gives D ≈ 0.507*52/762.8 = 3.46 cm, about 6 % below the frame 36 estimate.
That's consistent given the heavy blur and that the frame is near the image edge.
The ratio of pixel sizes between the two frames (~40 vs ~52-55) matches the depth ratio Z48/Z36 = 0.727.

## Focal/depth consistency check
The vertical pixel acceleration on the 2nd arc (second differences of cy, f37-39 ≈ 18.5 px/frame²) with g = 9.81
gives Z ≈ f*g/a ≈ 0.70 m, which reproduces the given 0.7045 m at f36. So f = 762.8 and the depth are consistent.
(The full 3D ballistic fits in arc3d.py were poor, with rms 8-10 px, probably from drag/centroid bias, so I didn't use them.)

## Answer
D ≈ 3.7 cm (range 3.5-3.8). A table-tennis ball would be 4.0 cm; the measurement suggests a slightly smaller value.
Confidence: moderate (±7 %). The main uncertainty is where the edge of the shaded underside lies, plus the halo.
