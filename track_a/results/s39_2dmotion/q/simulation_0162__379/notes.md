# q_379: speed of the ball at t = 2 s (m/s)

Prior: ball diameter = 0.21 m. 2D video; the camera is static. question_fps = file fps = 24, so t = 2 s is frame 48.
Speed = |x(48) - x(47)| x 24 x (m per px). The motion is horizontal, and cy changes by less than 0.1 px between 47 and 48.

## Scale (ball diameter in px near frame 48)
- measure4.py: profiles of |frame - background frame 0| across the ball centre. From the partial-pixel coverage at
  frame 48, the left edge is at 607.8 and the right edge at 686.8, so the width is about 79.0 px. With thresholds 40/60/100/150
  the width is 80.4/79.9/79.3/78.5 px. The top edge is at about 607.6. The bottom is contaminated by the contact shadow.
- SAM 3 ("blue ball"), frame 48: box 607.5–687.3 x 607.8–688.4, so horiz 79.8 and vert 80.6. Frame 47: horiz 80.2, vert 80.5.
- Scene record: circle-fit diameter at frame 48 is 80.6 px (81.5 is the whole-video median; early frames are larger).
- My first blue-chroma contour fit (measure.py) gave r = 37.3. That is too small: the rim is light and less blue, and the overlay
  frames/my_fit48.png shows the circle inside the rim. I used it only for centres, not for size.
- All the size routes agree within about 2 pct (79.0–80.6). I adopted **D = 80.0 px**, so the scale is 0.21/80 = 0.002625 m/px.

## Pixel step 47 -> 48
- Edge-profile centre (measure2.py, thresholds 60 and 100): 24.57 and 24.58 px.
- Contour-fit centre: 24.67 px. Scene track: 647.34 - 622.76 = 24.58 px. SAM centroids: 647.0 - 622.6 = 24.4 px.
- Smoothed (quadratic fit of x over frames 44–52, evaluated at 47.5): 24.2 px. The mean of the 5 steps centred on 47.5 is 24.35 px.
- I adopted **24.4 px/frame**, between the raw step (24.6) and the smoothed value (24.2).

## Answer
v = 24.4 x 24 x 0.002625 = **1.54 m/s**.
Range of the routes: raw step 24.6 px with D 79.0–80.6 gives 1.54–1.57; smoothed 24.2 px gives 1.51–1.54.
Confidence: about ±3 pct. The main uncertainty is the ball's pixel diameter, because the edge is soft and the shadow sits at the bottom.
