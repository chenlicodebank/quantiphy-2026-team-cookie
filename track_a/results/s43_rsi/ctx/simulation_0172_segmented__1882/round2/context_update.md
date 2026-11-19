# Context update for Q1882 (round 2)

## Established (verified independently of round 1)
- **The C1 fault is real.** The depth rate at f12 comes from the rigid upper-body scale, not from bbox height.
  - `sift_scale.py`: SIFT plus RANSAC similarity and affine fits over all frame pairs up to 12 frames apart, solved by least squares for log s. This is a different method from round 1's ECC, C2's LK and C3's template search. The local rate at 11.5:
    - Similarity: 1.4–1.7e-3 per frame.
    - Vertical scale: 1.4–2.3e-3 per frame.
    - Adopted: 1.7e-3, so dZ/dt ≈ −0.79 m/s.
  - The bbox-height rate is about 6.4e-3 because the legs straighten (337→348 px over f9–14). Putting it into the same geometry reproduces C1's 3.29.
- **Scale and depth at f12.** s12 relative to f24 = 0.937–0.946, so Z12 ≈ 19.2 m. Round 1 had 0.954, i.e. 19.0 m. The difference is small.
- **In-plane motion 11→12.** Hip band, SIFT and template routes give du 9.1–10.6 px and dv 3.0–4.0 px. Adopted: (9.9, 3.5) px, the same as before.
- **Focal length and closure.** The maximum normalised height is 394.5 px, which gives f ≈ 3233 px. Closure: 2.21 m against the 2.2 m prior.
- **Speed at f12.** **1.75 m/s.** The 10–90 % range is 1.62–1.91 and the full range 1.54–2.01. Round 1's 1.68 is confirmed within 4 %.

## Ruled out
- **3.2 and the 2.65 blend:** they rest on the bbox-height depth rate.
- **2.0–2.05 (C4, C6):** clip-mean depth rate, dominated by the hop. The scale rate is about 5e-3 per frame over f16–24.

## Open
- The exact local rate lies between 1.4 and 2.2e-3 per frame, about ±8 % on the speed.
- C2 (1.9) sits at the top edge of the range and has no proven fault. C3 and C7 (1.60–1.63) sit at the bottom edge.
