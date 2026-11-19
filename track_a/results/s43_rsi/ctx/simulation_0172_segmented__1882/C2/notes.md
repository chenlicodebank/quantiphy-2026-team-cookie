# Q1882: speed of the astronaut at t = 0.5 s (m/s)

The file runs at 24 fps and question_fps is also 24, so t = 0.5 s is frame 12 and the speed is |p12 − p11| × 24 (pelvis).
I assume a fixed pinhole camera with depth_info D(f24) = 18.147 m.

## Where the candidates part ways
The answers split on the **depth (approach) rate at frame 11→12**. Both candidates have similar lateral components (about 1.5–1.9 m/s).
- C1 (3.2) took dZ/dt from bbox height, helmet width and sqrt of the upper-body area, which gave −2.0 to −3.1 m/s. These are mask-extent measures that change with pose. C1 also assumed a constant size over f0–9 followed by a sudden growth.
- C2 (1.9) took dZ/dt from the rigid-body LK scale, which gave about −1.0 m/s.

## My measurements (scripts in this folder)
- `rigid_scale.py`: LK + RANSAC similarity on the upper body (helmet, backpack, chest) between consecutive frames.
  - The scale grows steadily from f0, about 0.0025 per frame over f0–14. It is not constant until f9.
  - The image motion is smooth over f0–14 (du ≈ 10–11 px/frame, dv falling from 8 to 2) and changes abruptly at f14→15. That is the push-off into a long hop, which lasts until about f60.
- `gap_scale.py`: least-squares per-step scale from all frame pairs with gaps 1–5 in f0–14, using three rigid regions. The rate at 11→12 is 0.0014–0.0035 per frame (mean over f6–14: 0.0015–0.0020). I took r = 0.0022 ± 0.0007, i.e. dD/dt ≈ −1.0 m/s (range −0.7 to −1.4).
- `pair_scale.py` (long-baseline LK) agrees: 0.0013–0.0021 per frame. `tmpl_scale.py` (template matching with a scale search) was too noisy to use.
- `bands.py`: LK translation of body bands at 11→12. The hip/pelvis band moves du ≈ 10.0 ± 0.4 px and dv ≈ 3.7 px per frame. The upper body moves 10.6 / 3.2.
- Depth at f12: D12 = 18.147 × cum(24)/cum(12) = 18.147 × 1.1096/1.0283 = 19.58 m.
- Focal length: f = 380 px (bbox height at f24, a nearly upright pose) × 18.147 / (2.2 × k), with k = 0.95–1.0. That gives f = 3134–3300 px.
- `speed.py`: back-projects the f11 and f12 pelvis positions. The result is 1.82–1.93 m/s for the central rate (full range 1.63–2.13 over all f, rate and du combinations). Central value: about 1.88.

## Checks
- **Second route:** consecutive-frame chained LK scale (0.0026 per frame) gives about 2.0 m/s.
- **Plausibility:** 1.9 m/s is a realistic walking/lope speed, and the 2.2 m suit height gives f ≈ 3200 px (HFOV ≈ 40°).
- **Why C1 is too high:** C1's 3.2 m/s needs a depth rate of 2–3 m/s, i.e. a scale rate of about 0.005–0.007 per frame. The rigid-body scale shows that rate only after the f14/15 push-off, not at f12.

I agree with C2. Answer: **1.9 m/s**. Confidence: moderate (about ±10%). The depth rate is the dominant uncertainty.
