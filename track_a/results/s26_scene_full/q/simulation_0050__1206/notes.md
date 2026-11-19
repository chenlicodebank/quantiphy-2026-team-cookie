# q1206: length of the moving bicycle (m). Answer: 1.69 m

File fps = question_fps = 33. t=1 s is frame 33, t=2 s is frame 66. The camera is static.

## Data used
- Bicycle pixel extents come from scene/tracks/cyclist.csv (bbox_x0 is the front-tyre leading edge, bbox_x1 is the
  rear-wheel/rack trailing edge). I overlaid them on frames 33, 45, 66 and 85 (frames/ext*.png). They hug the wheels
  to within about 3-5 px. Frame 33: x 900-1142 (241.7 px). Frame 66: x 341-520 (178.5 px).
- Bike origin ray: (hub_mid_x, middle of head-to-ground). Depths are 11.896 m at frame 33 and 14.642 m at frame 66.
- The bike is oblique to the image plane, so I don't use length = d * px / f. Instead the bike axis is taken to be its
  3D motion direction (P66 - P33, from back-projection), and I solve for the two points on that axis that project to
  the front and rear pixel edges (solve.py, consist.py).

## Focal length: the routes disagree
1. Walker speed prior (solve.py): the torso x (1370 -> 1194 px) and the two human depths give a net 3D displacement of
   1.236 m over 1 s at f ≈ 3010 px. That would make the bike 1.27-1.38 m.
2. Street vanishing point (street_vp.py): I traced the cornice/lintel lines of the green house and two curb lines.
   They meet at about (-2750, 575) ± 100 px. The bike's own image track runs through this point (y 575). For the
   bike's 3D motion (from its depths) to point at this vanishing point, f ≈ 1900 px (range about 1800-2050).
3. Rigid-length constancy over frames 6-92 (consist.py): each frame's bike position is placed on the 3D line through
   P33 and P66. The spread in length is smallest at f ≈ 1800-1900 (std 0.018 m), and the length shows no trend at
   f ≈ 1810. At f = 3000 the length drifts by +12 % (std 0.052 m).
4. Constant bike speed along that line: zero fitted acceleration at f ≈ 1980.
5. Plausibility: at f = 1900 the cyclist is 1.72 m from head to ground and the bike 1.69 m, both realistic. At f = 3000
   they would be 1.09 m and 1.31 m.
Routes 2-4 rely only on bike data and agree on f ≈ 1900. Route 1 doesn't fit the image geometry. For any f, the human's
two depths put his motion at a vanishing point of -2271 px or further right, never at the street's -2750. So the walker
would be cutting diagonally across the sidewalk, while his feet line in the image runs parallel to the street. I
couldn't find the cause (the torso x is checked to about 1 px). I trusted the three bike routes that agree.

## Result
f = 1900 px. Bike length: 1.677 m (frames 15-30), 1.678 m (31-60), 1.702 m (61-92), mean over 6-92 = 1.686 m.
Frames 33 and 66 alone give 1.669 and 1.734 m.
Sensitivity: f = 1800 gives 1.75 m, f = 2000 gives 1.63 m.
Answer: 1.69 m (length = the long horizontal extent, front tyre to rear wheel/rack).

Confidence: moderate, about ±5 %, as long as the bike-based f is right. If the walker-speed route were right instead,
the answer would be about 1.31 m.
