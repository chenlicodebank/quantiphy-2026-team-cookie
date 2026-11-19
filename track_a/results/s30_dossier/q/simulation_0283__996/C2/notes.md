Scale from the dragon's broadside nose-to-tail length (816 px, SAM3 mask at f37) = 0.75/816 = 9.19e-4 m/px. Displacement between frame 12 (t=0.5s) and frame 24 (t=1.0s) measured four ways on my own background-subtraction masks (mask centroid raw/smoothed, thick-torso centroid, bbox centre) averages 383 px, giving 0.352 m. Cross-check: ~825 px/s horizontal speed x 0.5 s = 0.38 m, consistent with the measured net displacement.

Final message:
I measured the dragon's displacement from 0.5 s to 1.0 s (frames 12→24) and answered **0.35 m**.

Method summary:
- **Scale:** The dragon yaws during the clip, so its projected nose-to-tail length varies (≈519–816 px). The broadside maximum (816 px, SAM3 mask at frame 37) is the best estimate of the true 3D length, giving 0.75 m / 816 px = 9.19×10⁻⁴ m/px.
- **Displacement:** Four independent pixel routes (raw mask centroid, smoothed centroid, thick-torso centroid, bbox centre) gave 371–400 px, averaging 383 px → 0.352 m.
- **Check:** The ~825 px/s horizontal speed over 0.5 s (≈0.38 m) is consistent with the measured net displacement including the vertical bob.

Notes written to `notes.md`; answer submitted via `finish_answers`.
