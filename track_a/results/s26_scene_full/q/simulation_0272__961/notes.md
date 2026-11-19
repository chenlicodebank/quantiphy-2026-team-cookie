# q_961 – phoenix body length (m)

Prior: acceleration at 2.0 s = 2 m/s². This is a 2D top-down render at 24 fps (the file rate and question_fps agree).

## Scale from the acceleration
- Track: scene/tracks/bird.csv (the beak_x, body_cx and bbox_cx columns). I checked it on frames 0 and 48 (frames/f0.png, f48.png):
  the mask covers the bird, from the beak tip to the end of the tail shaft.
- The bird starts from rest (frames 0 and 1 are identical) and accelerates left. Its per-frame speed pulses with the wingbeat,
  but the position follows a constant-acceleration-from-rest curve x = x0 − ½a(n−n0)² very closely, with n0 ≈ 0–1.5.
  Script: fit.py.
  - Quadratic fits over frames 2–71, 1–71, 10–71, 20–71 and 26–71, on all three columns: 226–254 px/s².
  - From-rest fits: 245–250 px/s².
  - Adopted a = 244 px/s² (±3%).
- Why the smooth fit: the prior is a round 2 m/s², which suggests the rig root was keyframed with constant acceleration while the
  wingbeat makes the visible body surge. The one-frame difference at frame 48 (about 2870 px/s²) is a peak of that surge, not the root's acceleration.
- Scale: 2 / 244 = 0.00820 m/px.

## Length
- bbox_w is the horizontal mask extent from the beak tip to the tail-shaft tip, i.e. along the body axis, which points along the motion.
  - Median over the clip: 436 px; range 420–456 (the tail flexes).
  - Frame 0 (rest): 443 px. Frame 48: about 430 px.
  - Adopted 438 px.
- L = 438 × 0.00820 = 3.59 m.
- Other reading: the wingspan (618 px max, about 5.1 m) is sometimes the longer horizontal extent, but "body length" means beak to tail.

## Check
- The from-rest model alone gives a = 245.7 px/s² (n0 = 1), so L = 436/245.7 × 2 = 3.55 m. The general quadratic gives 241 px/s², so 3.62 m.
- Confidence: moderate-high on the measurements. The main risk is how the reference defines the root acceleration.
