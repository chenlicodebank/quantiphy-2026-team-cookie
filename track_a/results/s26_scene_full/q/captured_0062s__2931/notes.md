# q_2931: length of the whiteboard (cm)

The video and the question both run at 24 fps. t = 1.4 s is frame 34. The given depth to the whiteboard at that time is 2.815 m. Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## Method (measure_len.py)
- Board mask: V>185 & S<45, largest component, holes filled. Also checked with V>200 & S<35. A third threshold leaked into the
  background and was discarded.
- I fitted the outline with a quadrilateral, refining each side by a Huber line fit to the contour points on its middle 70%. That leaves out the
  two grey knobs on the far edge. The overlay is in frames/quad_34.png and the fit is good.
- Route A, rectangle back-projection: the 4 corner rays with the parallelogram constraint P1+P3 = P2+P4 give the 3D shape up to scale. I scaled it so the centre is
  2.815 m from the camera.
  - Frame 34: long sides 80.8 / 80.3 cm (two thresholds), short sides 60.4 / 59.3 cm, corner angle 87.8-89.7 deg.
    The angle being close to 90 deg is a self-consistency check that f and the corners are right.
- Route B, pinhole on the midline: the long-axis midline is 222.9 / 221.4 px. Z = 2.800 m (depth projected on the optical axis), so
  Z x px / f = 81.7 / 81.2 cm.
- Frame 33 gives 81.0-82.6 cm with the depth of frame 34; the board is ~1% nearer there, so this is consistent.
- Over frames 26-45 the length/width ratio is 1.30-1.37, consistent with an 80 x 60 cm board, a standard whiteboard size.

## Check against the velocity prior (vel_check.py)
- The shape-only reconstruction gives the board-centre track in units of the board length. Matching the prior
  (1.9339 m/s at 1.4 s) would need L ~ 1.0-1.05 m when the dropped frame 35->36 is counted as 2 intervals, or ~0.87 m when it is not counted.
- Per-frame steps are irregular (frame timing jitter or dropped frames, as the record notes), and the reference velocity comes from
  clicked centres plus sensor depth. So the velocity prior is a noisy scale.
- The depth_info route is direct, and it is self-consistent: with L = 0.80 m the reconstruction puts the board centre at 2.786 m, against 2.815 m given.
  I answer with the depth route.

## Answer
Length ~ 81 cm (range of routes 80.3-81.7). Width ~ 60 cm.

Confidence: moderate-high for the depth route. The main risk is that the reference instead follows the velocity prior,
which would give ~87-100 cm.
