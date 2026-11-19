# q_2288: soccer ball displacement between 1.0 s and 1.5 s (cm)

The file and the question both run at 24 fps. t = 1.0 s is frame 24 and t = 1.5 s is frame 36. The camera is a lab camera
with f = 0.5959 x 1280 = 762.8 px and principal point (640, 360). The prior (gravity) is not needed for this question.

## Measurements
- **Frame 36** (free flight, motion blur): the scene record's auto-mask centre is (811.8, 77.6). I checked it on a 3x crop
  (frames/f36.png): the streak spans x 752-870 and y 27-126. The width across the blur is 98.3 px, and frames 35-38
  (103.6 / 98.3 / 98.0 / 94.7) are consistent with it. Depth is 1.402 m (depth_info). That gives a ball diameter of
  1.402 x 98.3 / 763 = 0.181 m.
- **Frame 24** (wind-up): the ball's left part is **hidden behind the thrower's hip/trousers** (frames/f24w.png), so the
  scene record's Hough diameter of 126.4 px and centre of (270.5, 602.5) are biased. I read 10 edge points on the
  visible top/right arc on a 5x crop (frames/f24z.png) and fitted two models:
  - circle (fit_manual.py): centre (276.1, 605.7), diameter 113.0 px, rms 0.75 px;
  - off-axis sphere ellipse (fit_ellipse.py): centre (266.3, 612.3), tangential diameter 118.5 px, rms 0.67 px.
- Depth at frame 24 comes from the apparent size: Z24 = 1.402 x d36 / d24, which is 1.14 to 1.22 m depending on the model.

## Result (displacement.py)
I back-projected both centres as ((u-cx)/f, (v-cy)/f, 1) x depth, following the method card, and took the 3D
distance between them:
- circle model: 129.3 cm;
- ellipse model: 128.0 to 128.8 cm;
- circle model with the tangential-corrected d36: 128.3 cm.

The answer is **128.6 cm**.

## Second-route check
The circle and ellipse models move the frame-24 centre and depth in opposite directions, but the displacement
stays within ±0.7 cm. If I use the record's biased Hough values (diameter 126.4), the displacement is 124.9 cm.
If depth_info is read as Euclidean distance rather than Z, the result is about 116 cm. I followed the method card's
Z convention.

## Confidence
Moderate. The main uncertainty is the depth at frame 24: no depth is given there, and the ball is partly hidden.
I expect the answer to be within about 5 to 8 percent.
