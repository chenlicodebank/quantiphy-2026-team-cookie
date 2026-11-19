# Q324: length of the toaster (prior: cup diameter = 0.087 m)

Time base: fps 24 = question_fps. Only static geometry is needed, so the timing does not matter.

## What the scene really is (a correction to scene/notes.md)
The "blue cylinder" is a tapered tumbler/cup lying on its side. Its closed base faces the camera and its wider rim is
at the far end. It never turns. Its axis points straight away from the camera the whole time. The apparent tilt from
-40° to +45° is perspective: the axis converges on the vanishing point. A 3D cone fit gives yaw = -88° to -91° in
frames 10-44 (`conefit.py`, `yawscan.py`). The cup is at the front edge of the counter. The toaster stands further
back, on the same counter surface. So a single flat 2D scale is wrong; I used a ground-plane perspective model.

## Camera / ground plane
- Horizon: two receding counter lines intersect at (963.6, 520.5). These are the left edge of the cooktop
  (1180,891)->(1232,980) and the sink cut-out edge (0,934)->(70,904). The receding right side of the toaster base
  (front foot 475,925 -> back foot ~511,893) also points to this vanishing point. v_h = 520 and the principal x is
  about 962, so pitch is about 0.4°.
- Focal length, from the burner ellipses (circles on the counter; `burners.py`): about 2850-3060 px, so HFOV is
  about 36°. f only enters the cone fit; the direct route does not use it.
- For a ground point at image row v, depth z = f·h/(v - v_h), where h is the camera height above the counter. So a
  horizontal width = Δx_px · h / (v - v_h). Everything is expressed in units of h.

## Cup (the scale)
- Frame 19 (cup end-on, near the image centre), rim silhouette from sub-pixel luminance edges (`rimwidth2.py`,
  `rimwidth3.py`). The colour mask in scene/ misses the dark shaded right edge, so I did not use it:
  max width 131.9 px at rows 893-899, top edge y = 830.3. The rim circle faces the camera, so its centre is about
  896 and its ground contact row is about 830.3 + 131.9 = 962.2.
- D_rim / h = 131.9 / (962.2 - 520) = **0.2983**.
- Second route: a truncated-cone silhouette fit over 6-7 frames (IoU 0.93-0.97), with shared shape and per-frame
  pose. It gives D_rim = 0.2953 h (base 0.221 h, length 0.59 h). This is 1% smaller, as expected, because it fits
  the colour mask, which loses the dark edge.

## Toaster
Measured on frame 59 (the cup has gone; `feet.py`). The axis-aligned bounding box in x is set by the feet, which
stick out past the base and body:
- Left front foot: outermost x = 59 at ground row about 926. X = (59 - 962)/(926 - 520) = -2.224 h.
- Right front foot: outermost x = 475.5 at row about 926, giving X = -1.198 h.
- Right back foot: x = 511 at row about 893, giving X = -1.209 h.
- Length (left-right) = 1.015-1.026 h, about **1.020 h**.

The front-back depth is about 0.19 m and the height is smaller still, so the left-right extent is the length.

## Answer
L = 1.020 / 0.2983 × 0.087 = 0.2975 m from the direct rim route, or 0.3005 m using the cone-fit rim. **Answer
0.299 m.**

For comparison, a naive flat 2D scale (445 px toaster / 126 px mask width × 0.087) gives 0.307 m. The perspective
correction and the edge correction partly cancel.

Confidence: about ±3%. The main uncertainties are which ground row the feet sit on (about ±0.5%), the rim width
(about ±1%), and the toaster extent (feet against back body, about ±1%).
