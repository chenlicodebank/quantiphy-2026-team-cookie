# Q632: speed of the dog at t = 1.5 s (m/s)

- The video is a 2D top-down render at 24 fps, with question_fps also 24. The camera is static. t = 1.5 s is frame 36.
- The dog is the tan animal on the lower line (y ≈ 447), walking −x. The black cat is on the upper line, walking +x.

## Scale (prior: black cat speed = 0.94 m/s)
- Cat pixel speed comes from linear fits over frames 0–49 of the scene/ tracks (`cat_speed.py`):
  - front edge bbox_x1: 10.977 px/frame
  - body_x1: 10.979 px/frame
  - centroid: 10.94 px/frame
- The speed is constant (quadratic term ≈ 0), so I used 10.97 px/frame = 263.3 px/s.
- Scale = 0.94 / 263.3 = 3.570e-3 m/px.

## Dog speed at frame 36
- Mask centroids in scene/ are noisy (±3 px per step from gait and legs), so I re-measured the dog with `track_dog.py`.
  It matches 48×48 fur-texture patches on the torso (front, mid, hip, rear hip) from frame i−1 to frame i, with
  sub-pixel peaks. All patches matched with correlation ≥ 0.95.
- The dog cruises at about 13–14 px/frame in frames 26–33, then decelerates smoothly.
- Steps 35→36:
  - front: 10.80
  - mid: 11.17
  - hip: 11.26
  - rear hip: 11.43 px
- The neighbouring steps (frames 35 and 37) give 12.1 and 10.8, so the deceleration is consistent.
- I used about 11.2–11.3 px/frame (torso/pelvis) for the dog at frame 36.
- Speed = 11.25 × 24 × 3.570e-3 ≈ 0.96 m/s. Equivalently, the dog/cat pixel-speed ratio 11.25 / 10.97 × 0.94 = 0.964.

## Checks
- The fur-mask centroid averaged over frames 34→38 gives 12.1 px/frame. That window is centred near 36 but extends
  into the faster phase, and mask deformation biases it. This gives an upper bound of ≈ 1.03 m/s.
- The template route is preferred.
- Confidence: moderate-high, ±5%.
