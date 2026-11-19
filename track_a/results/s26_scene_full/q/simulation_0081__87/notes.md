# Q87: distance between the walking person and the bike at t = 1.0 s (frame 24, 24 fps, fps = question_fps)

The video is a top-down render (labelled 2D), so I report the in-plane (ground) distance between the pedestrian's pelvis and the bike's root.

## Scale
- I measured the bike's cyan mask at frame 24 (measure.py): x 480–855, so the bike is 376 px long.
- Correcting for parallax, because the wheel tip and rack sit above the ground, the ground-equivalent length is about 372–376 px.
- Scale: 1.7 m / ~374 px = 0.00455 m/px.

## Bike root
- Bike bbox centre: (668.5, 639.5). This is also about the midpoint between the wheel axles.
- Ground-equivalent position: about (670, 639).

## Pedestrian pelvis (hidden under the torso)
- In the image at frame 24, the head is at x = 371.5 and the shirt/torso centre is at about (389, 440).
- Perspective pushes elevated points outward from the image centre. The rider-head parallax (0.04 px/px) gives a camera height of roughly 26 m.
- Route A, gait footprints (pedsheet.py, bbox extremes): the left toe stays planted near x ≈ 355 from frame 9 to frame 25. The right toe lands near x ≈ 560 at frames 26–28. At mid-stance (legs together, frames 17–18) and at double support (frame ~25.5), the pelvis sits about 25–33 px ahead of the head's image x. That puts the pelvis's ground x at frame 24 at about 400.
- Route B, torso centre plus parallax correction: about 412 (with H ≈ 26 m), or 390 with no correction.
- Adopted pelvis position: (402 ± 10, 442).

## Distance
- dx = 268, dy = 197, giving 333 px, or 1.51 m.
- Without any perspective correction (pelvis at 390, raw scale 376 px): 342 px, or 1.55 m.
- Using the head instead of the pelvis: 1.63 m. I rejected this because the pelvis is the origin.
- Answer: **1.52 m**. Confidence: moderate, about ±4%; the main uncertainty is the hidden pelvis position.
