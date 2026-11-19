# Q1191: speed of the walking person at t = 1.0 s (m/s)

The file rate and question_fps are both 33 fps, so t=1 s is frame 33 and t=2 s is frame 66.
The question gives the human's camera distance at both times: 11.9259 m at t=1 s and 10.8165 m at t=2 s.

## Method (measure.py)
- **Pelvis pixel.** I used the walker track from scene/ (`ref_x`, `ref_y`, the belt-line pelvis proxy). I checked it
  on crops at frames 33 and 66 (frames/w_1.0.png and frames/w_2.0.png), and the belt line sits at about y=344 and y=374.
- **Back-projection.** Each pelvis pixel is back-projected onto a ray, assuming the principal point is the image centre
  (960, 383), and placed at the given depth along that ray. The speed is the 3D distance between the two points over 1 s.
- **Focal length.** I estimated it from the 1.8 m height prior: height_px x D / 1.8 gives 1313 px at f33 and 1276 px
  at f66. Correcting for the downward camera pitch (vanishing point at y≈−177, so a vertical person is foreshortened by
  about 0.92) gives about 1390–1430 px.
- **Why the result is robust.** The radial depth change of 1.109 m/s is most of the speed. The lateral part is only
  about 3%, so the result hardly depends on f: f=1150 gives 1.146 m/s, f=1300 gives 1.140, f=1400 gives 1.136 and
  f=1550 gives 1.132. Moving the pelvis point 10 px lower changes the result by less than 0.001.

## Checks
- The walker moves steadily toward the camera, with no stops. Image-plane speed rises smoothly: 0.84, 0.92, 1.00 and
  1.18 px/frame over successive windows, as expected for a constant world speed as he gets closer. So the 1–2 s
  average stands for the speed at 1 s.
- Second route: the height-based scale implies a depth ratio of 198.2/212.3 = 1.071. The given depths give a ratio of
  1.103, which is consistent within the ±2 px height reading plus the changing foreshortening. The depth-based route
  above is the more reliable one.

## Answer
About 1.14 m/s. The one-frame speed of the origin may carry a few % of gait oscillation, which cannot be resolved here.
Confidence: about ±5%.
