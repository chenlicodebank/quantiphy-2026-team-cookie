# Q808: rabbit speed at t = 1 s (frame 24), in m/s

Prior: speed of the horse at the back = 0.874 m/s. The horse at the back is the chestnut horse: it trails the
other horse, and its hooves touch the ground highest in the image, so it is also the farthest from the camera.
fps = question_fps = 24, so frame 24 is t = 1 s.

## Pixel speeds (scene/tracks mask centroids, checked against bbox centres; measure.py)
- Chestnut horse, frames 0-48 (the frame 48->49 jump is an animation loop reset and is left out):
  3.15-3.26 px/frame depending on the method (end-to-end 3.154, linear fit 3.241, bbox-centre fit 3.261).
  I used about 3.2.
- Rabbit: the hop makes the centroid steps vary (3-10 px). Fits around frame 24: frames 19-29 give 6.35,
  18-30 give 6.28, 22-25 give 6.55, 23->24 gives 6.51, and the whole clip gives 6.23. I used about 6.3 px/frame.

## Perspective / depth correction
The camera is level: the house's vertical edges are vertical in the image, so the horizon is at cy = 960.
Ground-contact rows measured on zoomed crops (crops.py): chestnut hooves about 1046, pale horse about 1052,
rabbit about 1063 (feet in the grass, ±2-3 px).
Depth goes as 1/(y_contact - 960), so Z_rabbit / Z_horse = 86/103 = 0.835 (0.81-0.85 over the error range).
Cross-check: the ratio of the two horses' heights (166/177.5 = 0.935) matches their contact-row depth ratio
(86/92 = 0.935). So the horizon model is right and the different contact rows are real depth differences.
The rabbit is nearer the camera, so its metres per pixel are 0.835 times the horse's.

## Answer
v_rabbit = 0.874 x (6.3 / 3.2) x 0.835 ≈ 1.44 m/s, reported as 1.43.
Without the perspective correction (a single planar scale) it would be about 1.72 m/s.
Confidence: moderate. The main uncertainties are the ±4 % hop-phase variation of the rabbit's local speed,
how the reference treats the depth difference, and the contact rows.
