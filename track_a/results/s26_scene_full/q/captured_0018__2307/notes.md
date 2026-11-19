# q_2307 — distance box ↔ pineapple toy at 3.0 s (captured_0018, lab, 24 fps = question_fps)

## Key issue
The clip has only 49 frames (0–48, ends at 2.04 s). 3.0 s (frame 72) does not exist, so I used the last frame (48).
By then both objects are on the floor and nearly still: the box is lying on its side (it moved 6 px left from frame 47 to 48),
and the pineapple (called `lemon_plush` in scene/, a yellow plush with green leaves) has been tumbling in place at
x≈836–848, y≈596–613 since frame 40. Any further motion before 3.0 s should change the distance by about a centimetre or less.

## Method (floor-plane geometry; f = 0.5959·1280 = 763 px, principal point (640,360))
- Horizon y = 342 (left-wall baseboard and top edge meet at (1037,342); the back-wall baseboard vanishing point is
  also at y 342, so roll ≈ 0). That gives a downward pitch of 1.35°.
- Camera height h from the references in depth_info (geom.py, dist2.py):
  * Soccer ball (2.80 m, constant depth because its pixel size stays at 44–46 px). Its true floor impact falls between
    frames 39 and 40. I intersected the pre-bounce and post-bounce parabolas (bounce.py): impact at frame 39.27 with the
    centre at y 553.7, which is lower than the blurred frame-39 bbox. With radius 0.082 m this gives **h = 0.828 m**.
    (Using the naive bbox bottom at 565 would give 0.78 m.)
  * Near person (2.002 m, pelvis about (985,420), feet at y≈693): h = 0.844 m.
  * Far person (3.13 m, pelvis about (385,360), feet at y≈569): h = 0.889 m. This one is an outlier at +7%.
  I used h ≈ 0.836 m, the mean of the ball and near-person values; they agree within 2%.
- Object centres at frame 48, placed by intersecting each centre's pixel ray with a plane at the centre's height above the floor:
  * box centre pixel (423, 593.5), centre 0.037 m above the floor → camera distance 2.63 m
  * pineapple centre pixel (847, 600), centre 0.045 m above the floor → camera distance 2.53 m
- 3D distance = **132.7 cm**. Using floor-contact points (box bottom y 606, pineapple bottom y 619) gives 131.7 cm instead.

## Sensitivity / checks
- Horizon ±5 px: ±0.4 cm.
- h from the ball alone: 131.4 cm. Mean of all three references: 135.7 cm. Bbox-bottom ball calibration (not used): ~124 cm.
- Plausibility of the sizes this scale implies: box long axis 57.7 px → 19.9 cm, width 23 px → 7.9 cm; pineapple body 26 px → 8.6 cm.
- The record in scene/ covers the right objects (white_box, lemon_plush = pineapple); I re-checked frames 36–48 on zoomed crops.

Answer: 133 cm. Confidence: moderate (±5–8%). The main uncertainties are that the depth_info references disagree with
each other and that 3.0 s lies beyond the end of the clip.
