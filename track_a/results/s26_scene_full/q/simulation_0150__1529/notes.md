# q_1529: speed of the car at t = 0.5 s (m/s)

Video: 24 fps, which matches question_fps, so t = 0.5 s is frame 12. Speed = |p12 - p11| x 24.
Prior: the tyre diameter is 0.764 m. depth_info: camera to left-front tyre = 11.38 m at t = 0.5 s.

## Is the car still turning at frame 12?
The scene record calls frames 0-13 "turning out of bay". That label is wrong for frames 11-13. In those
frames the front-wheel rim fits as a circle (axes 121-122 px, aspect about 1.00), and the hub height in the
image stays at y = 791.5 (it is also 791.5-792.5 later, while the car is side-on). A circular rim means the
wheel plane, and so the car's side, is parallel to the image plane. The constant hub row means the depth is
not changing. The car's front shows in the image only because the car sits right of the image centre. So at
frames 11-12 the car is moving purely sideways, and every point of the car, including its origin, has the same
world speed as the wheel hub. The visible front tyre is the car's left front tyre (car heading to image-left).

## Pixel speed (wheel.py, wheel2.py, hub.py)
Rim-ellipse centre of the front wheel (from grey rim pixels; overlays in frames/wheels2.png):
f11 1721.1, f12 1656.8, f13 1588.4, f14 1516.2, f15 1440.3, f16 1360.7, f17 1277.9.
- Backward steps: 64.3, 68.4, 72.2, 75.9, 79.6, 82.8 px/frame. The car accelerates smoothly.
- A linear fit of the steps over f12-16 gives 64.4 at f12.
- Hub-hole centroid (second centre estimator): step 63.7 at f12 (linear fit 64.1).
- Value used: 64.3 px/frame (+/- 0.4).

## Scale (tyre3.py, zoomc.py)
I measured the tyre's outer radius by fitting edges along rays from the hub in frames 12-24, and checked it
visually on a contrast-stretched zoom of f21 (frames/zc21.png).
- Top: about 89-90 px. Bottom: 90-92 px, which includes some contact shadow.
- Horizontal diameter at f12-f16: 176-178 px. Vertical diameter: 180-183 px.
- Hub to ground contact: 882 - 792.5 = 89.5 px.
- Result: D = 179 +/- 3 px, so 0.764 / 179 = 0.004268 m/px at the tyre's depth.

Consistency with depth_info: f = D x Z / 0.764 with Z = 11.38 / sqrt(1 + (697^2 + 252^2) / f^2) gives
f ≈ 2560 px and Z ≈ 10.93 m. The far-wall base (y ≈ 700-703) compared with the tyre contact (y 882) gives
Z_car ≈ 23.44 x 160 / 342 ≈ 10.9-11.2 m. This is consistent within about 2%. For sideways motion,
m/px = Z/f = 0.764 / D_px, so the answer does not depend on f.

## Answer
speed = 64.3 px/frame x 24 x 0.004268 m/px = **6.59 m/s**

Second route: the hub-hole centre gives 63.7-64.1 px/frame, i.e. 6.53-6.57 m/s. The tyre-diameter range
177-182 px gives 6.48-6.66 m/s.

Confidence: fairly high, about +/- 3%. Most of the uncertainty is in the tyre's pixel diameter, because the
tyre edge is hard to separate from the dark wheel-arch liner.
