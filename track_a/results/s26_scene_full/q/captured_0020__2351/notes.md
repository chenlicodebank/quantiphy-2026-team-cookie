# q_2351 – height of the white jar (cm)

The "white jar" is the scene record's `white_ball`: a small white jar with a lid. The near (left) person throws it to the far person.
The "carrot" in depth_info is the record's `yellow_fruit`. The video and the question both run at 24 fps, so t = 0.60 s is frame 14.
Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Scale at frame 14
The jar centre is at (405, 238). The ray norm is 1.0585, so z = 1.9735 / 1.0585 = 1.864 m, which gives 0.2443 cm per px.

## 3D throw fit (fit3d.py)
I fitted both free-flight paths as ballistic in 3D with |g| = 9.8 (the prior). The gravity direction in camera coordinates was left free and shared by both objects.
Each path was pinned to its depth_info distance at frame 14. Inputs: jar frames 12-25 and fruit frames 12-17 and 19-24.
- Residuals are about 1-3 px. The fitted camera tilt is about 56 deg downward.
- The fitted jar distance runs 2.05 m (release) -> 1.97 (frame 14) -> 2.62 (frame 25).
- The fruit runs 2.95 -> 1.78 m. Both are consistent with the people at 1.58 and 3.24 m with their arms extended.
- The fit gives the depth at the sharp frames (20-24), where the jar is barely motion-blurred.

## Pixel extents (size.py, profile.py; masks in frames/masks.png)
Masks were thresholded at 50 % contrast. Sharp-edge steps were read from intensity profiles.
- Frame 14: width across the motion is 30 px, i.e. 7.35 cm. The vertical extent of 46-51 px is motion-blurred.
  - Blur model: length = s + k·speed, fitted over frames 14-15 and 21-24, gives k ≈ 0.57 and s ≈ 23 px, i.e. 5.7 cm.
- Frames 15-17, across the motion: 5.9, 7.0 and 7.7 cm.
- Sharp frames, extent between the edge steps, converted with the fitted z:
  - frame 21: about 27 px, 7.3 cm
  - frame 22: 25 px vertical, 6.95 cm
  - frame 23 (side view, lid plus body): 32 px vertical, 9.2 cm (probably a diagonal)
  - frame 24: 24 px, 7.3 cm
- The jar tumbles, so its projected extent ranges from about 6 to 9 cm. The median of all routes is about 7.3 cm.
- The jar looks about as tall as it is wide (the frame 5 lid view and the frame 23 side view).

## Answer
Height ≈ 7.2 cm.
- Route 1: frame 14 at the given depth gives 5.7-7.4 cm.
- Route 2: the sharp frames at the fitted depths give 6.9-7.3 cm, with one 9.2 cm diagonal.
- Confidence is moderate, about ±15 %. The main uncertainties are the SAM halo around the mask edge, the tumbling orientation (height versus diameter), and the motion blur near t = 0.6 s.
