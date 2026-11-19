# Q1851: rocket speed at t = 1 s (m/s)

- 2D side view, static camera. fps = question_fps = 24, so t = 1 s is frame 24, and the speed is the backward difference p(24) − p(23).
- **Scale:** prior rocket length = 2.9 m. The rocket's nose-to-tail length is 221.9 px (median over frames 15-20, where it is fully visible; the per-frame values of 220-227 agree). That gives 0.013069 m/px.
- At frame 24 the nose is out of the image (the rocket crosses the top edge from frame 22), so only the tail is usable.
- **Re-measurement** (measure.py): a difference mask against frame 28, taken along the launch axis. The tail positions match the scene record: 140.9, 204.9, 262.4 and 327.0 px for frames 22-25.
- The raw steps are 64.0 (22→23), 57.5 (23→24) and 64.6 (24→25). This jitter of ±3-4 px comes from the bluish nozzle/plume at the tail, whose shape changes from frame to frame (frames/tails*.png). It is not real motion: the nose and tail steps disagree by up to 13 px in frame 21.
- The rocket accelerates steadily, with steps rising from 46 to 62 px/frame. So the speed was taken from smooth quadratic fits evaluated as p(24) − p(23):
  - Tail, frames 15-25: 62.5 px/frame. Tail, frames 18-25: 61.8.
  - Centre track, frames 15-25: 61.6. Frames 18-25: 60.7.
  - Second route: template-matching shifts of the tail profile (xcorr.py), cumulated and quadratic-fitted: 62.2 (frames 18-24) and 63.8 (frames 15-24).
  - Mean step over frames 21-25: 61.7.
- **Adopted:** 61.8 px/frame × 24 × 0.013069 = **19.4 m/s**. The spread across the methods is about ±1 m/s (±5%).
- **Confidence:** moderate-good. The main risks are tail-end noise and whether the "length" prior is the rocket's own long dimension (assumed here).
