# Q427 – height of the small elephant (m)

Prior: big elephant speed 2.313 m/s. 2D side-view render, 24 fps (file fps = question_fps, no re-timing).
Both elephants walk on the same ground line (feet y≈690–697), so one m/px scale applies to both.

## Scale (m.py on scene/tracks)
Big elephant horizontal pixel speed (px/frame): centroid_x linear fit 6.88, net 6.97; body_centroid 6.85/6.93;
body_x0 7.02; body_x1 6.91. Adopted 6.90 px/frame = 165.6 px/s → 2.313/165.6 = 0.01397 m/px.

## Small elephant height
Mask height (top of back/head to feet) per frame 147–161 px, median 156 px. Frames 0–45 (top edge against sky,
reliable) 152–161; late frames (head against dark foliage / head lowered) drop to 147–151. Checked visually on
zoomed crops at f10 (top ≈541, feet ≈694 → ~153–155) and f30. Adopted 156 px.

Height = 156 × 0.01397 = 2.18 m.

## Checks
- Using the leading-edge speed (bbox_x1, 7.13 px/f) instead gives 2.11 m; body_x0 (7.02) gives 2.14 m; net-centroid
  gives 2.16 m – all within ~3%.
- Big elephant height 230 px → 3.21 m, small/big ratio 0.68: plausible adult + young elephant.
Confidence: moderate-high (~±4%).
