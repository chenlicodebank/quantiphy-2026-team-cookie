# Q2364 — displacement of the yellow toy, 0.60 s -> 0.80 s (cm)

File fps = question_fps = 24, so the times map to frames round(0.60*24)=14 and round(0.80*24)=19.
Yellow toy = the "carrot" in depth_info (yellow with a green leafy end): 2.630 m at t=0.60 (frame 14).
White object = the "jar": 1.9735 m at frame 14. Camera: f = 0.5959*1280 = 763 px, c = (640,360).

## Problem
Depth is only given at frame 14, so the toy's depth at frame 19 has to be estimated. The toy is in free flight
from its release (frame 14) until the near person's hands touch it (~24-25).

## Method (fit3.py, fit4.py)
- Pixel centroids come from scene/tracks (I checked them on frames: tiles.png, tiles3.png). Frame 18 is
  wrong for the yellow toy (it is mostly hidden behind the white object, so only the green end shows) and is excluded.
  Frames 24-26 are excluded because of hand contact.
- Joint 3D ballistic fit: each object has X(t) = X0 + V t + 1/2 g d t^2, with g = 9.8 (prior) and a shared world-down
  direction d (camera pitch and roll fitted). X0 is the back-projection of the frame-14 centroid at the given depth
  (yellow 2.63 m, white 1.9735 m). Yellow frames 14-17 and 19-23; white frames 15-17 and 20-25. The white object's
  frames 18-19 are left out because the two objects overlap there.
- Result: pitch 58.0°, roll 9.0°, rms 0.9 px (yellow) and 1.5 px (white). The yellow toy's distance from the camera
  is 2.63 at frame 14 and 2.12 m at frame 19. The model's frame-19 point (448.1, 81.7) agrees with the tracked
  centroid (446.5, 83.8) to within about 3 px.
- **Displacement 14->19 = 68.7 cm.**

## Checks
- Yellow toy alone, over several frame subsets: 67.1-71.3 cm. Changing the white frame set or its start frame: 68.7-69.0 cm.
- Pitch scan (fit4.py): the joint rms is lowest at 58°. Under this solution the catch points are plausible: the
  yellow toy is caught at 1.74 m (near person 1.58 m) and the white object at 3.04 m (far person 3.237 m), so both
  are caught a little in front of the catcher. Pitch 46° (a rough estimate from the people's body-axis vanishing
  point, ±10°) gives 56 cm, but the rms is 2-2.5 times worse.
- D14 ±0.07 m changes the answer by about ±1 cm.

Confidence: moderate-good, about ±5-8% (driven mainly by the fitted gravity direction).
