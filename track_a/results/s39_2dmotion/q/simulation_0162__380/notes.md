# q_380: acceleration of the ball at t = 2 s (m/s^2)

Prior: ball diameter = 0.21 m. 2D simulation, 1920x1080. The file fps and question_fps are both 24, so t = 2 s is frame 48.
Acceleration follows the convention (speed(48) - speed(47)) x fps, which is the second backward difference of x over
frames 46, 47 and 48.

## Track (measure.py -> own_track.json)
- For every row 642-683 I took the subpixel left and right silhouette edges of the difference mask against frame 0,
  which is empty. Centre x = median chord midpoint.
- My track agrees with scene/tracks/ball.csv to within about 0.5 px. The motion is purely horizontal and the camera is static.
- The centre wobbles with a period of about 10 frames (amplitude about 0.8 px). That period is one rotation of the ball
  (pi x 78 px / ~25 px per frame).
- wobble.py: the left and right edges move together (corr 0.89) while the width stays steady, and the top edge wobbles
  about a quarter period out of phase. So the visible sphere is slightly offset from its rotation centre (the origin).
  The origin itself follows the smooth trend, so I fit the trend and model the wobble separately rather than
  differentiating raw frames.

## Acceleration in pixels
- fit_accel.py: I fit x(f) = x0 + v_inf f + D tau exp(-f/tau), with and without a sinusoid. The 10-frame mean speeds
  show the acceleration decaying by a factor of about 0.72 every 10 frames, and this model matches that.
  - Fit values: v_inf = 30.5 px/frame, tau = 30.8 frames.
  - a48 = 0.2155 px/frame^2, the same for both tracks (own and scene) and for windows 20-92 and 19-96 (30-80 gives 0.213).
- Second route (fit_check.py): polynomial trend of degree 2-5 plus a free sinusoid over windows 28-68, 25-75, 33-63
  and 20-92. Results: 0.2146, 0.2257, 0.2199, 0.2174 and 0.2153.
- Local quadratic fits over +-10 and +-15 frames give 0.222 and 0.211.
- Adopted value: a = 0.2165 px/frame^2 (+-2%), which is 124.7 px/s^2.

## Scale (diameter in pixels)
- Equator chord (width_vs_x.py): 50% crossings of the lane-to-rim luminance edge on rows 645-649, frames 20-91.
  - The width grows off-axis, from 82.3 px at x = 86 to 77.1 px at x = 1000. That is sphere elongation in perspective.
  - Fit of w = w0 sqrt(1 + ((x - x0)/f)^2): w0 = 77.3 px, x0 = 947 (close to the image centre), f about 2400 px, rms 0.39 px.
  - The plane-of-motion scale Z/f equals D / w0, so 0.21 / 77.3 = 2.717e-3 m/px.
  - The local width at frame 48 is about 78.2 px, which would give 0.335 m/s^2.
- SAM 3 ("blue ball", sam_diam.py; frames 40-68) disagrees with this:
  - Box about 79.9 x 80.0 px, area-equivalent diameter 79.6. Centroid at frame 48 is (647.0, 646.8), which matches my 646.9.
  - The scene record gives about 80.5-81.5 px.
- They differ from my 77.3-78.2 by about 3-4%, so I checked the raw edge profiles at frames 48 and 60 (profile48.py).
  The edge ramps are 2-3 px wide. At 50% coverage:
  - Frame 48: the edges sit at 607.5 and 686.1 (78.6 px).
  - Frame 60: the edges sit at 909.5 and 987.7 (78.2 px).
- So the SAM mask and the record's diff > 40 mask both include the partially covered rim pixels, which adds about 1.5 px.
  The 50% edge is right, and I used it. SAM's box also does not show the off-axis elongation that the careful
  edges show clearly.

## Answer
a = 124.7 px/s^2 x 0.21 / 77.3 = **0.339 m/s^2**.

Sensitivity to the scale: local frame-48 width gives 0.335, SAM's 80 px gives 0.327, so the spread is within about 3%.
Confidence: good, about +-3%. The main uncertainty is the trend model, since the true acceleration varies in time.
