# q_2297 — width of the white box (cm)

File fps 24 = question_fps 24. Lab camera, f = 0.5959 x 1280 = 763 px, principal point (640,360).

## What "width" is
The box is a white rectangular product box held upright by the left (far) person's right hand, face to the camera.
Width = horizontal extent across its face (the long side ~57 px is its length). Thickness is not visible clearly.

## Pixel width (width_px.py, profile.py)
Luminance-gradient edges (sub-pixel) on rows 258-290 below the fingers, frames 0-28 (box held still, sharp):
left edge 471.5, right edge 490.3 -> 19.7 px (per-frame medians 19.6-20.1). The averaged profile and a 10x crop
(frames/box_zoom10.png) agree: ~20 px (the scene record's bbox 23 px includes blur/fingers). Used 20 px.

## Box depth (not given in depth_info — the main uncertainty)
Converted the given Euclidean distances to Z: far person pelvis 3.13 -> Z 2.97; near person 2.002 -> Z 1.81;
soccer ball 2.80 -> Z 2.76.
1. Ball ratio on the floor: box rests lower in the image than the ball (box bottom upright ~595, lying 607; ball
   contact bottom ~577 after correcting for contact between frames 39/40). Z_box = Z_ball (v_ball-vh)/(v_box-vh)
   with horizon 342-378 -> 2.39-2.56 m.
2. Floor plane calibrated by the far person's soles (y 575 at Z 2.97): box -> 2.61-2.78 m; this model puts the
   ball at 2.94 vs given 2.76 (+7%), corrected -> 2.45-2.6 m.
3. Body geometry: far person faces the near person (~32 deg towards the camera), so her right hand (box) is on the
   camera side and the left (ball) further; arm 0.55 m, shoulder half-width 0.18 m -> box Z ~2.53, ball Z ~2.83,
   predicted image x 453 / 527 (observed 481 / 541) — consistent.
Gravity prior: fitting the box/ball fall gives inconsistent depths because of a timing glitch (probable dropped
frame 35->36; ball with one dropped frame -> 3.1 m, box fit unstable), so it was not used for scale.
Adopted Z_box = 2.52 m.

## Result
width = 2.52 x 20 / 763 = 0.066 m = **6.6 cm** (range 6.3-7.2 cm across routes). Box length for sanity:
57 px -> 18.8 cm. Confidence: moderate (depth of the box inferred, ±7%).
