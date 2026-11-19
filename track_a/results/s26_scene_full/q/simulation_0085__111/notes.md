# q111 — length of the car (m); prior: car acceleration = 4.03 m/s^2

2D top-down render, static camera, fps 24 (= question_fps). The cyclist moves at a constant 26.65 px/frame
across the whole width (quadratic term ~0), so the pixel mapping is linear: one m/px scale applies.

## Car pixel acceleration (track.py, ana.py, ana2.py)
Sub-pixel template tracking (front, mid and rear templates taken from frame 50) plus the record's integer edges.
- The car starts from rest at about frame 0–1. It then accelerates **uniformly**: front template frames 10–30 give a = 0.886 px/frame^2
  (rms 0.04 px). Integer front edge frames 2–30 give 0.879, and frames 3–46 give 0.890.
- After about frame 47 the acceleration rises to ~1.3–1.4 px/f^2 (frames 48–56) and then falls to 0 as the speed levels off
  at ~62.5 px/frame (frames 66–71). This looks like a transition to a cruise speed, not the nominal acceleration.
  A quadratic fit over the whole track would give ~0.96–1.0, which is biased by that transition, so I did not use it.
- Prior → a = 0.887 px/f^2 = 0.887·576 = 511 px/s^2 → scale = 4.03/511 = 0.00789 m/px.

## Car pixel length
Bumper-to-bumper x-extent with mirrors excluded along x (the record's bboxes for frames 40–63): 722–734 px. Perspective parallax makes
it smallest near the image centre (722–723 at frames 52–56) and larger off-centre (734 at frame 40). Representative value: 724 px.

## Answer
L = 724 × 0.00789 = **5.71 m** (range 5.69–5.79 over 722–734 px).

## Check
Real-world check: a Cybertruck-like pickup is about 5.68 m long. Running the prior the other way, 5.68 m / 726 px with a = 4.03 m/s^2 predicts
0.894 px/f^2. That matches the measured uniform-acceleration phase (0.886–0.890) to within 1 %. If I used the
whole-clip average acceleration (~1.0 px/f^2) instead, the length would be ~5.1 m.
Confidence: good (±3 %).
