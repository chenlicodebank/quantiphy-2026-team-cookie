# Q989 – speed of the whale at 1.0 s (m/s)

Prior: whale length = 19.17 m. No depth_info. fps = question_fps = 24, so t = 1.0 s is frame 24.
Top-down view with a static camera; the whale swims straight in the -x direction at a constant height, so I treat it as a 2D problem with one m/px scale.

## Pixel speed (edgetrack.py, fit.py)
- Head position: for every frame, the mean over rows y 1040-1270 of the leftmost whale-mask column (head left-edge profile).
  This is steadier than the single nose pixel.
- Motion is constant after frame 3. Linear fits of the head-edge position give 8.59 px/frame (frames 14-34),
  8.63 (frames 20-28) and 8.62 (frames 4-71). The head-mask centroid gives 8.50-8.59 and the nose pixel 8.46-8.62.
  I use 8.60 px/frame = 206.4 px/s. There is no acceleration, so the one-frame backward difference at frame 24 equals this slope.
- I also tried template matching on the head (headtrack.py). It gave 5-7 px/frame, but the template contains
  animated caustics on the background and the whale skin, which bias it. I rejected it because the silhouette
  measures all agree.

## Scale
- Whale x-extent from nose to fluke tip: 2355 px at rest (frames 0-1, before the swim starts). It changes with
  the fluke stroke: 2125 px minimum near frame 26, about 2390 px when straight (frames 56-63, slightly enlarged
  because the fluke is raised toward the camera). I take the rest/unbent length, about 2353 px, as the model's length:
  19.17 m / 2353 px = 0.00815 m/px.
- Speed = 206.4 × 0.00815 = **1.68 m/s**.
- Other readings of the length: 2133 px (the bent pose at frame 24) gives 1.86 m/s; 2393 px (straight, later) gives 1.65 m/s.

## Check
The three position measures (edge profile, head centroid, nose pixel) and the fit windows (local and whole clip)
agree within about 1 %. Most of the uncertainty is in which pixel length matches the 19.17 m prior: about ±2 %
if the rest pose is meant, up to +10 % if the bounding box was taken in the bent pose at t = 1 s.
Confidence: moderate to high.
