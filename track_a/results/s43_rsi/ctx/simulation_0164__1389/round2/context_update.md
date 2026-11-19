# Round 2 addendum, q1389

## Verified
- **Round 1's switch to 0.41 is confirmed.** It was reproduced with independent code (vp_mine.py, recon_mine.py).
- **Lane VP = (5648, 208) ± 3 px.** Three cyan floor lines were fitted at sub-pixel precision; they meet within 5 px.
- **Second route to the ball VP.** The camera roll is about 0: screen and pit edges near the centre column have a tilt of about 0. So the horizon is the row y = 208, and the ball path y = −0.0832x + 678.6 crosses it at x = 5656.
- **Line model anchored at 9.391 m at frame 12, frames 6–37:**
  - a = −0.412 at f = 3670;
  - a = −0.419 at f = 3573 (self-consistent with the late clean diameters, off-axis factor applied);
  - a cubic fit evaluated at 1 s gives −0.416;
  - v(1 s) = 3.6 m/s.
- **The answer is now 0.415.**

## New point settled
- **The vertical edges disagree with f, but this does not move the answer.** The "vertical" screen and pit edges tilt by up to 1.8°, and the pit top edge has slope 0.085. Together they imply f ≈ 2450 if the principal point is at the image centre. That is ruled out:
  - it makes the ball 0.30 m (prior 0.21, exact);
  - it makes the pins about 0.5 m tall.
- **A lens-shift explanation leaves a unchanged.** With the principal point at (950, 947), at f ≈ 3550, a = −0.422. Either way a is 0.41–0.42.
- **The diameter-trend VP is ruled out.** Taking the VP at 5300 gives a = −0.31, the low answers' value. That VP is off the lane lines and off the horizon crossing.

## Open
- Physics jitter in the ground-truth per-frame speed difference at frame 24 cannot be known from the video.
