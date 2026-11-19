# Q804 — width of each glass window (m)

Prior: speed of the horse at the back = 0.874 m/s. No depth_info. The scene is 2D (side view, camera static), so I used
one metres-per-pixel scale. fps = question_fps = 24.

## The horse at the back
This is the chestnut horse on the left, trailing the pale horse. Its hooves are also slightly higher in the image
(y≈1048 vs 1055), so it is the rear horse under both readings of "back".

## Horse pixel speed (scripts: speed.py, torso.py, cycle.py, loopchk.py)
- Scene track, frames 0-48 (frame 48->49 is an animation-loop reset, so I excluded it):
  - mask centroid: net (x48 - x0)/48 = 3.154 px/frame; linear-fit slope 3.241 px/frame
  - bbox centre: net 3.125 px/frame; linear-fit slope 3.261 px/frame
- Whole-horse foreground template shift f0->f48: 149.6 px, i.e. 3.12 px/frame (low match score, so it only
  supports the other numbers).
- Torso template tracking was too noisy to use: it gave 2.8 px/frame typical steps with jumps.
- Adopted 3.18 ± 0.06 px/frame = 76.3 px/s, so the scale is 0.874 / 76.3 = 0.01145 m/px.
- Sanity check: horse body about 187 px = 2.14 m nose to tail, and 166 px = 1.90 m to the ear tips. Both are plausible.

## Window width (window.py, frames/win.png)
The three arched ground-floor windows are identical. Measured in code from rows y 870-930 of frames 0, 24 and 49:
- left 272-335 (64 px)
- centre 508-573 (66 px)
- right 744-809 (66 px)

The outer frame width is therefore 65 ± 1 px, which gives 65 × 0.01145 = 0.744 m.

Range across the speed estimates: 0.73 m (3.24 px/frame) to 0.75 m (3.154 px/frame).

Second-route check: the brick ground floor is 203 px high, which is 2.33 m, a plausible storey height. This shows the
single scale is reasonable for the house as well.

**Answer: 0.745 m.** Confidence is moderate. The main uncertainties are whether the house's depth differs from the
horse's (ignored, per the 2D convention) and the ±3% spread in the gait-averaged speed.
