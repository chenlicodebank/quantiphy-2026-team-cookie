# Q67: speed of the white-shirt man at 1.0 s

- **Scene.** A top-down camera over a flat floor. Both men walk toward -x on the same ground plane, so the two speeds can be compared directly in pixels. The file's fps and question_fps are both 24.
- **Prior.** The black-shirt man walks at 1 m/s. I read this as his steady walking speed and use it for the scale.
- **Method (`measure.py`, using the tracks in `scene/`).** I compared the mean per-frame step of the two men over frames 2–71, after walking starts.
  - Head point: 15.83 / 12.25 px/frame, ratio 1.292. Net-displacement ratio: 1.299.
  - Mask centroid (second route): ratio 1.296 per-step, 1.298 net.
  - Estimated pelvis point: ratio 1.292 per-step, 1.299 net.
- **Result.** White-shirt speed ≈ 1.30 × 1 m/s = **1.30 m/s**. Both men walk at a steady speed, with no stops. The centroid's per-frame step swings by about ±25% with the gait, and frame 24 lands near a low point of that swing. The answer assumes the reference uses the nominal steady speeds, consistent with the prior being exactly 1 m/s.
- **Confidence.** High for the ratio (±1%). The main risk is the reference using an instantaneous pelvis value that includes the gait swing.
