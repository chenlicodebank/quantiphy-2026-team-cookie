# Q1541 – width of the blue car (light-blue utility cart), m

Answer: **0.755 m**. I agree with C1 (0.753). C2 (0.97) is too wide.

## Setup
- Blender 3D scene at 24 fps; the file and question_fps match. Static level camera, principal point ≈ (960, 540).
- The cart drives left to right, parallel to the image plane, at constant depth. Its right side faces the camera, so its
  width lies along the camera axis and must come from depth differences (parallax and perspective).
- Scale: depth_info gives 9.312 m to the near (right) front tyre centre at t = 1 s (frame 24). With f ≈ 2690 px (from the
  0.369 m tyre being ≈109-112 px across; Z hardly depends on f), Z_centre ≈ 9.16 m. The near tyre's outer face is ≈ 9.10 m.
- Checks of that scale: camera height ≈ 1.39 m. The cart is ≈1.8 m long, ≈1.6 m tall, with a wheelbase of ≈1.1 m. The
  yellow car is ≈4.7 m long. All are plausible.

## Where the candidates part ways
They part ways on how the depth difference across the cart is measured.
- C1 used motion parallax: tyre silhouette edges over many frames.
- C2 used the two front-face edges, read by eye in two frames. Those gave 0.86 and 1.10 m, and its answer of 0.97 m was
  partly a guess from proportions. The 2-3 px edge errors are large on a face only ~30-45 px wide.

## My measurement (faredge.py, prof.py)
- I took the far-side front tyre's right silhouette (its outer face) in frames 12-24 at row 898, sub-pixel
  half-level crossing. I regressed it on the near-front hub from the scene track (ref_x + 169.25).
- Result: slope Z_near/Z_far = 0.9244, rms 1.1 px over 13 frames. Rows 901/904 give 0.931/0.926, but they are noisier
  because the edge jumps in 2 frames.
- Width = Z_no·(1/0.9244 − 1) = 9.10 × 0.0818 ≈ 0.745-0.75 m. C1's independent near-edge route gave 0.923-0.924, which is
  0.749-0.756 m.
- Second route: the front face of the body, its near and far corners read on zoomed frames, assuming both corners share
  the same X:
  - frame 18: u 372 / 418 → Z ratio 1.085 → 0.77 m
  - frame 22: u 545 / 578 → Z ratio 1.086 → 0.78 m
  - Headlight spacing is ≈0.53-0.56 m, a lower bound.
- So the bounding box is ≈0.75-0.78 m wide. Answer 0.755 m.

Confidence: moderate-good, about ±5 %.
