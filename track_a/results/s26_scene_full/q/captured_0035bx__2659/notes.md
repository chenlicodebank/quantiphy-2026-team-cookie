# q_2659 — soccer ball speed at t = 1.4 s (frame 34, question_fps = file fps = 24)

## Inputs
- depth_info lists "soccer_ball" twice at t=1.4 s (2.6020 and 2.3730). Read as soccer = 2.6020, basketball = 2.3730:
  at frame 34 the soccer ball is ~64-67 px wide and the basketball ~72 px. The labels are swapped vs. the image otherwise
  (with soccer = 2.602 the soccer diameter comes out at 21.8 cm, plausible; basketball 72 px x 2.373 / 763 = 22.4 cm, close to
  the 23.2 cm prior).
- t=0.9 s -> frame 22: soccer 2.4770 m, basketball 2.7777 m.

## Method (measure.py)
- f = 0.5959 x 1280 = 763 px, principal point (640, 360).
- Ball centres: scene/tracks circle_cx/cy (checked on a 3x crop of frame 34: centre ≈ (689, 496), correct). My own
  re-segmentation (threshold 246) was noisier (lost white panels, e.g. frame 33 height 44 px), so the record was kept.
- Back-projected the 4 given 3D ball centres (soccer & basketball at frames 22 and 34, depth = Euclidean distance).
  They lie on one plane to within 2 mm (after a 6 mm radius correction for the basketball) -> plane of the
  rolling ball centres. Every frame's soccer centre = ray ∩ plane. Reproduces the given distances: 2.4748 (2.477) and
  2.6033 (2.602).
- Per-frame forward speeds around frame 34 are noisy (13-125 cm/s; a likely dropped capture frame at 35→36).
  Smoothed estimates: mean fwd speed frames 32-37: 56.9; 31-37: 59.3; 30-38: 57.9; 29-39: 59.7 cm/s;
  linear fit of positions 29-40: 56.1, 30-38: 56.3 cm/s; net displacement/time 56-59 cm/s.

## Second route
- Fixed-depth pixel route: pixel velocity ≈ 6.6 px/frame over frames 30-38 x 2.60 m / 763 x 24 ≈ 54 cm/s lateral,
  plus a small depth component -> ~56-57 cm/s. Agrees.

## Answer
57 cm/s. Confidence: moderate (±5-8 %, dominated by the smoothing window and the dropped frame near 35→36).
