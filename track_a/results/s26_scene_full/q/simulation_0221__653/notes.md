# Q653: lampshade diameter of the table lamp (m)

Prior: the vacuum's diameter is 0.438 m. No depth_info. fps 24 = question_fps, so no re-timing.

Scene: a top-down render. The camera is a perspective camera, because the wall faces are visible on the left, top and right. The table lamp is
the white pleated shade at the right end of the console, centred at about (1190, 225) px. It is static.

## Measurements (frame 77; scripts lamp_measure.py and vac_check.py)
- Lampshade: I made a white low-saturation mask (S<50, V>160) and took its minimum enclosing circle, which hugs the pleat-tip rim (overlay
  frames/lamp_mask_50.png). The diameter is **149.5 px** (bbox 150 x 144; parts of the top and right edges are lost to shading).
  The scene record's ~150 px agrees.
- Vacuum: the same method at frame 77 gives 119.6-121.4 px depending on threshold. The record's circle fit gives 120.9 px at x 650-1160.
  I used **120.8 px**. Near the dock it reads 122.9 px, which is probably merged with the dock or its side wall.

## Scale
- Planar, one m/px scale (0.438/120.8 = 3.626 mm/px): 149.5 px gives **0.542 m**.
- Perspective: the shade's rim is well above the floor (console height plus lamp base, roughly 0.8-0.9 m) and the camera is not very high.
  The brass top of the shade is shifted 10.4 px exactly along the radial direction from the image centre relative to the rim circle's
  centre (shift / radius = 0.027). The walls give a camera height of at most about 6 times the wall height (about 15 m). Together these
  suggest the rim is magnified about 4-8% relative to the vacuum's top, which puts the true diameter at about 0.50-0.52 m.

## Answer
0.52 m. This hedges between the planar-scale value (0.542) and the perspective-corrected range (0.50-0.52); it is within 5% of both
0.50 and 0.545. Confidence: moderate. The main uncertainty is the unknown camera height and lamp height.
