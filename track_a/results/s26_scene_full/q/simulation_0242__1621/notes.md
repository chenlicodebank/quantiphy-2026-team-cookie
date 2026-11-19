# q1621: length of the brown horse (m)

The file rate and question_fps are both 24 fps. The camera is static. The brown horse walks side-on, almost exactly along image +x.

## Scale
- Pixel motion: torso_cx goes 414.1 → 556.4 px over frames 0-24. A linear fit gives 5.94-5.99 px/frame.
- The question gives depths 16.288 m at t=0 and 16.112 m at t=1, and the prior speed is 0.874 m/s.
  `solve_f.py` back-projects both points with principal point (960, 540) and solves for the focal length that makes
  the 3D displacement over 1 s equal 0.874 m. This gives **f ≈ 2600 px**, camera Z ≈ 15.9 m and **0.00612 m/px**.
  The result hardly depends on which image row is taken as the origin (390 to 560 px).
- Check (`check_f.py`): if each animal moves parallel to the image x axis at constant camera Z, the depth change from
  t=0 to t=1 alone implies f. This gives 2444 px for the brown horse and 2560 px for the rabbit, which agrees with
  2600. The cream horse gives 4241 px, but it is ill-conditioned because it is near the image centre and its depth
  barely changes. So the depth drop of 0.176 m/s is explained by the horse moving along x while it is about 12° off
  the optical axis.

## Pixel length (nose to tail, along the motion)
- Frame 0: tail at about x 263, head disc at about 590, so about 327 px. The scene bbox of 336 px includes a few grass specks.
- Frame 24: about 405 to 732, so about 325 px.
- Frame 30: the hind leg is stretched back, so the bbox is 360 px. Without the leg, the tail is at about 437, so about 331 px.
- Over the clip, bbox_w has a median of about 326 px and a mean of 330 px (range 315-360).
- Using 330 px: 330 × 0.00612 = **2.02 m**. With the minimum or maximum gait extents the range is 1.93-2.20 m.

## Confidence
Moderate to good. The scale is solid because it comes from the exact prior and is cross-checked against the depths.
The main uncertainty is which pose or frame the reference bounding box uses (about ±5%), plus about ±10 px on the
right edge of the head disc.
