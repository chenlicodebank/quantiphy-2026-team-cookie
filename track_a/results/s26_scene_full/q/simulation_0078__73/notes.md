# q73 – speed of the black-shirt person at 1.0 s

Overhead 2D view, 24 fps (file fps = question_fps, no re-timing). Both walkers move along the same image row
(y≈550–563), so one metres-per-pixel scale applies to both; the perspective height factor (pelvis vs feet vs head)
is the same for both and cancels in the ratio.

Scale from prior: white shirt (B) walks at 1.3 m/s steadily.
Pixel speeds (linear fits, `speeds.py`, full-body frames A 6–71, B 17–71):
- pelvis_est: A 11.14, B 14.50 px/frame -> ratio 0.769
- head:       A 11.82, B 15.38 -> 0.769
- shirt cx:   A 11.22, B 14.78 -> 0.759
- mask cx:    A 11.08, B 14.33 -> 0.773
Second route (planted feet, from scene notes): A 10.34, B 13.53 px/frame -> 0.764; step lengths 178 vs ~225 px with
equal cadence -> ~0.79.

Speed of A = 1.3 × 0.769 ≈ 1.00 m/s. Both walk at steady pace (no start/stop); frame-24 per-frame values of the
head-based pelvis estimate fluctuate with gait bob (±15 %) and are not used for the instantaneous value — the
rig root is assumed to move at the steady walking speed.

Answer: 1.0 m/s. Confidence: good (routes agree within ~3 %).
