# q_3191 — distance pink box to floor at t=0 (m)

Prior: g = 9.8 m/s^2. Internet video, 2D, one scale factor. Clip is rotated 90 deg: image +x = physical down,
black strip/wood = floor side. fps 30 vs 30.0136 is negligible (0.05%); used 30.

Scale (fit.py, on scene/tracks/packet.csv, which I checked against frames 0, 60 and 81):
- Quadratic fits of x(t) in free fall (frames 53-64, other windows too):
  cx_bg 9835-10588, bbox_cx 9402-10401, edges 9150-10575 px/s^2. Taken: a ≈ 10100 px/s^2
  -> 9.8/10100 = 9.70e-4 m/px. The packet is ~100 px, so about 9.7 cm, which is plausible.
- Second differences of the background-corrected centroid have a median of about 11000 early and drop to about 9500 later (light packet, drag);
  the fit average is used.

Distance:
- t=0 (frame 0): bottom (right) edge of the held packet at x ≈ 140 px (zoomed crop; the mask bbox says 131 because the
  edge is partly washed out).
- Floor contact = where the packet comes to rest (frames 78-99): bottom edge x ≈ 1432 at frame 78-81, with camera
  drift about -15 px, so about 1447 in frame-0 coordinates.
- Centre-to-centre check: start centre ≈ 83-90, rest centre bg ≈ 1397, so about 1307-1314 px. Edge to edge: about 1307 px.
- 1308 px x 9.70e-4 = 1.27 m.

Confidence: moderate. The scale is uncertain by about ±5% (the acceleration estimate depends on the window and on drag). An
alternative reading measures to the black strip's far edge (the wall/floor junction, about 1465 px), which gives about 1.29 m.
Answer: 1.27 m.
