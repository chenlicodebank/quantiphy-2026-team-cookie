# q_1910 — height of the box (prior: width of the box = 1.33 m)

"The box" = brown cardboard box on top of the truck container (seen straight-on from behind; 2D scene, static camera).
The scale is one metres-per-pixel value taken from the box's width.

## Method
- `measure_box.py`: HSV brown mask, keeping only the largest connected blob. This leaves out the container's yellow stripe
  and the dark lid flap. Width = mean mask fraction per column over the middle rows. Height = mean mask fraction per row over the middle columns.
  Mask overlay is in frames/mask_0.png.
- Width: 280.6–280.8 px at every frame (0–400). It is constant.
- Height: 170.0 px at f0 and f25, then shrinking steadily to 157.3 px at f400.
- `strip.py`: I compared brightness profiles down the box, aligned on its top edge (frames 0/100/200/300/400). The texture rows
  match exactly from the top down; the change is only at the bottom, where the box ends earlier in later frames. So the shrink is the
  bottom edge being hidden (the container rises 80 px, the box top only 66 px). It is not a rescale or a tilt. The full box shows at
  the start (f0–f25, before the motion; rounded corners visible at the bottom).

## Result
- Scale: 1.33 m / 280.8 px = 4.737 mm/px.
- Height = 170.0 px x 1.33 / 280.8 = **0.805 m** (f0). Check: f25 gives 170.0 / 280.6 x 1.33 = 0.806 m.
- If a late, partly hidden frame were used instead: 157.3 px gives 0.745 m. I rejected this because the bottom is hidden.
- Reading note: the prior's "width" is taken as the visible horizontal extent across the face (279–281 px). The box's
  front-to-back depth cannot be seen.
- Confidence: good (±1 px mask edges, about ±1 %). The main risk is how "width" is read.
