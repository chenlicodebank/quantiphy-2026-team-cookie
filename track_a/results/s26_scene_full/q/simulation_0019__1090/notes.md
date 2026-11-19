# Q1090 — walking speed of the person at t = 0.5 s (m/s)

## Time base
- The file runs at 33.265 fps and the question gives 33 fps.
- t = 0.5 s is frame 17 at either rate (16.6 → 17, or 16.5 → 17).
- I used the file fps. With 33 fps the answer would be 0.8 % lower, which makes no practical difference.

## Scale (3D pinhole model, principal point at (540, 540))
The person walks parallel to the back wall and the image plane: the record shows no trend in apparent height. I estimated the focal length two ways:

1. **Depth consistency (solve.py).** The given depths are 6.84 m at t = 0 (frame 0) and 6.49 m at t = 1 s (frame 33). The pelvis is at image offset (115, −342) px at frame 0 and (114, −158) px at frame 33. Requiring the same depth along the optical axis (Z) at both frames gives f = 892 px and Z = 6.34 m.
2. **Height prior.** The straight-leg height is about 260 px (90th percentile near frames 0 and 33). With H = 1.87 m and the given depths, f = 880 px at frame 0 and 877 px at frame 33.

I used f ≈ 886 px and Z ≈ 6.335 m, which gives 0.00715 m/px at the person's depth. As a check, 1.87 m / 260 px = 0.00719 m/px.

## Motion near frame 17
- **Pelvis from the record** (mean y of the hip-band mask): the arm swing makes it noisy.
  - Local rate near frame 17 is 4.5–4.9 px/frame.
  - Mean over frames 0–50 is 5.5 px/frame (1.30 m/s), but the speed varies within each step.
- **Sub-pixel template matching between consecutive frames (tmatch.py).** Matches that locked onto the static background (shift ≈ 0.3) were thrown out.
  - Waist band (x 605–650), frames 13–21: 4.9–5.2 px/frame along the walk, plus about −0.5 px/frame along the body axis.
  - Upper torso, frames 13–17: 4.3–4.8 px/frame.
  - Head, frames 19–22: 5.0–5.6 px/frame.
  - Both the head and torso bands are faster at frames 3–10 and 22–25 (5.5–6.2 px/frame) and slower near frame 17. This is a gait ripple of roughly ±8 %.
- **Local pelvis rate taken:** about 5.05 px/frame along the walk and 0.5 px/frame across it, about 5.07 px/frame in total.

## Answer
- Speed = 5.07 px/frame × 0.00715 m/px × 33.265 fps ≈ **1.20 m/s**.
- Other routes:
  - Raw pelvis track at frame 17: 1.03–1.12 m/s.
  - Average over the whole cycle: 1.30 m/s.
  - So the answer could plausibly lie anywhere from 1.1 to 1.3 m/s.

**Confidence:** moderate.
- The scale is solid: the two focal-length routes agree within 1.5 %.
- The main uncertainty is the instantaneous pelvis speed within the gait ripple, about ±8 %.
