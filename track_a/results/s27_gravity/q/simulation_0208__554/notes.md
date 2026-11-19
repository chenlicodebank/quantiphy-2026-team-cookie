# q_554: length of the table (m)

Prior: the typewriter's acceleration before 0.45 s is 9.8 m/s^2 (free fall, frames 0-10). No depth_info. File fps = question fps = 24.

## Scale from the fall (fit.py, tmpl.py, track_lin.py)
I fitted a quadratic to the vertical position over frames 0-6/0-9, where motion blur is small:
- bbox centre (scene track), frames 0-6: 6981 px/s^2. Mask centroid: 6926. Top edge y0: about 6770 for every window.
- Template match of the frame-0 typewriter with a vertical blur, frames 0-6: 6720 (it degrades after frame 6 as the appearance changes).
- Fits over the full window (0-9/0-10) give 7200-7360, but those are inflated by the blur growing the bbox non-linearly.
- I adopted a = 6850 px/s^2 (+-3 pct), so s = 9.8/6850 = 0.001431 m/px at the depth of the fall plane.
- Check: the typewriter's airborne length of 292 px gives 0.42 m, which is plausible for a vintage typewriter.

## Table geometry (table.py)
- The back edge of the table top is at y ~ 947. The side edges were found per row against the wall colour:
  left x = 261 - 1.942(y-952), right x = 1808 + 1.808(y-952).
- The side edges converge at (1061, ~540), which is the image centre. So the camera is level, and the image row of a
  point on the table plane gives its depth: Z ∝ 1/(y-540).
- Table width in px = 3.750 (y-540). At the back edge that is 1528 px. Since 3.750 = (X_r - X_l)/H_cam, the
  **table length = 3.75 x H_cam**, where H_cam is the camera height above the table top.
- The typewriter falls at the depth where it lands. That gives H_cam = (y_f - 540) x s, where y_f is the image row of
  the table point under the typewriter's origin (the centre of its footprint).
- y_f: the front bottom edge of the base is at y ~ 1022-1028 at contact (frame 11) and at rest. The footprint centre
  lies some 25-45 px behind that, and its back must still lie on the table (behind it, back edge at 947). I took
  y_f = 990 +- 12.
- H_cam = 450 x 0.001431 = 0.644 m, so L = 3.75 x 0.644 = **2.42 m** (the left-right extent; the front edge is out of frame).

## Second route
Equivalently, the back-edge length is 1528 px at y = 947. Rescaled to the fall depth it is
1528 x (990-540)/(947-540) = 1690 px, and 1690 x 0.001431 = 2.42 m. Using the unscaled 2D convention
(1528 px x s) would give 2.19 m, but that ignores the clear perspective: the back edge is farther away than the fall plane.

## Confidence
The error is about +-5 pct. It comes mainly from y_f (+-12 px, +-2.7 pct) and the fitted acceleration (+-3 pct).
The table's depth is not visible, so I assumed its left-right extent is the length.
