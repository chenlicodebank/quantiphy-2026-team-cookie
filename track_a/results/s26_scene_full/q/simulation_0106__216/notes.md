# q216: distance between the two viruses at t = 1.0 s (frame 24)

Prior: the right virus moves at 1.5667 m/s. No depth_info. fps = question_fps = 24, so t = 1.0 s is frame 24.

## Data
I used the scene/ tracks (body-circle centre and radius per frame). They cover both viruses at frame 24
with the bodies fully visible: left at (712.7, 296.2), r = 129.3 px; right at (1235.2, 899.0), r = 135.5 px.
The tracks look clean (steps are smooth, about ±0.5 px).

## Perspective
The scene is called 2D, but it shows perspective. The left virus moves up and grows (its radius goes from
123.8 to 132 px), and the right virus moves down and shrinks (139 to 135 px). The likely cause is a camera tilted
downward with both viruses moving roughly vertically.

## Route 1: pinhole model in units of the body radius R (fit3d.py, fit3d_b.py)
- Camera-space position = ((u-cx)/r, (v-cy)/r, f/r)·R, with cx, cy at the image centre.
- I fitted the right virus linearly over frames 1–27 (its speed is constant: the linear and quadratic fits agree
  within 0.5 %). That gives about 2.05 R/s, so R = 1.5667 / that ≈ 0.765 m.
- The distance at frame 24 comes from the fitted positions; the raw frame-24 positions agree within 0.1 %.
- The focal length f is unknown. Scanning f from 1800 to 3200 px gives a distance of 4.70 to 4.60 m. At f ≈ 2200–2667
  px (2667 px is Blender's default 50 mm lens; 2200 px is where the two viruses start at equal height under the
  equal-size assumption) the distance is 4.64–4.67 m.
- I assumed the two viruses are the same physical size: it is the same model, with the same spike-to-body ratio.
  If instead the left one were 0.87× the size (the ratio that would give both the same world speed), the distance
  would be 4.50–4.53 m, about 3 % lower.

## Route 2: flat 2D scale
- The right virus's pixel speed over frames 2–27 averages 11.2 px/frame, i.e. 269 px/s, so the scale is 0.00583 m/px.
- The pixel separation at frame 24 is (522.5, 602.8), i.e. 797.7 px, which gives 4.65 m.

## Answer
4.65 m. Both routes agree; the remaining uncertainty is about ±3 % (from the size-ratio assumption and the
unknown focal length).
