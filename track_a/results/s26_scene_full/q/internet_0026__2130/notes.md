# Q2130 – sitting height of the baby (cm); prior: sofa total height = 90 cm

Internet video, so I used the annotators' convention: one scale = 90 cm / sofa pixel height, applied to the child's
pixel sitting height (planar, no perspective correction). Time does not matter here (static sizes), so the
19.68 vs 24 fps question does not apply.

## Measurements (frame 0, checked at frames 10, 20, 28; scripts measure.py, child.py, child2.py, prof.py)
- Sofa (red, back facing camera, directly behind the child): the top edge is flat at y = 156-160 for x 60-500
  (r-g column profiles). The bottom of the body is at y≈530 (x 150-250) to ≈539 (near corner x≈500-520), with a dark
  gap/foot band of about 8 px below it before the floor (y≈540 at the child's x, ≈548 at the corner foot).
  Sofa height at the child's position: 540 - 157 ≈ **383 px** (range 374 for the body only, up to 391 at the near-corner foot).
  The rolled arm top at y≈130 (x≈600-650) is the far end of the arm: it looks higher only because of perspective, since the
  camera is above the sofa. So I did not use it (using it would give 418 px).
- Child: head top y≈375-376 (column profile minimum over x 320-340; the same at frames 10, 20, 28 within 2 px). Bottom
  where the shorts meet the floor is y≈660-664 (the dark shadow below excluded; overlay checked in
  frames/child_ov_0.png). Sitting height ≈ **286 px** (scene record said 293 px by eye; 315 px from the automatic dark mask is wrong because it included the shadow).

## Result
286 / 383 x 90 = **67.2 cm** -> answer 67.
Alternative sofa readings: 374 px -> 68.8 cm; 391 px -> 65.8 cm; 418 px (arm top) -> 61.6 cm.
Check: the result is stable across frames 0-28 (child height 284-288 px, sofa top 156-160).
Sanity: real toddler sitting height is ~50-55 cm. The child sits in front of the sofa, closer to the camera, so the
single-scale convention overestimates; the convention is followed on purpose.
Confidence: moderate (about ±4% from the choice of sofa bottom/top).
