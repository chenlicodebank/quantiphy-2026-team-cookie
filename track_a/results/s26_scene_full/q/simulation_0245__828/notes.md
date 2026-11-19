# Q828 – speed of the rabbit at 1 s (m/s)

Prior: antelope (the large horned creature) speed = 1.277 m/s. No depth_info. 2D scene (side view, both animals
walk/hop left→right parallel to the image plane, apparent sizes constant, static camera). fps = question_fps = 30.

## Method
One m/px scale from the creature's pixel speed; answer = 1.277 × v_rabbit_px / v_creature_px.

Creature pixel speed (px/frame):
- **Period matching (main)**: gait period is 40 frames (hooves land/lift 40 frames apart). Template of the whole
  creature at frame i matched in frame i+40 (same pose) for i = 0..34: shift/40 = **6.558** (sd 0.004). P = 39/41 give
  6.56/6.54 with worse correlation, so P = 40 is right.
- Planted front hooves (`hooves.py`): same hoof, same phase, 40 frames apart: 470→736 gives 6.60–6.63, 603→868 gives
  6.55–6.57. Mean ≈ 6.59.
- Horn template tracking 6.60, torso tracking 6.53. The scene record's mask centroid fit, 6.47, is lower because the mask
  is not body-fixed (missing snout, leg poses).
- Used value: 6.558 px/frame → 196.7 px/s → scale 0.006491 m/px.

Rabbit pixel speed: hop period ≈ 12.5–13 frames. Period-matched template shift (frames 0–64, fully in frame) gives
6.733 (P = 13, sd 0.015), 6.728 (P = 25) and 6.728 (P = 38). The scene record's centroid linear fit, frames 0–64, gives 6.739.
→ 6.733 px/frame = 202.0 px/s. Centroid backward difference at frame 30 is 6.89 px/frame, so the instantaneous value is
close to the mean even if the origin follows the hop. The answer assumes the rabbit's origin moves at a steady speed.

## Answer
v = 1.277 × 6.733 / 6.558 = **1.311 m/s**. If the creature's hoof-stride speed of 6.59 is used instead, the result is 1.305.
Confidence: good on the steady-speed reading (±1–2%). If the reference uses a hop-modulated root, frame 30 is
near mid-cycle, where the speed is close to the mean.
