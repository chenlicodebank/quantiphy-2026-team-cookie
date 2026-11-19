# Q785 – height of the brown horse (m)

Prior: speed of "the horse at the back" = 0.874 m/s. Both horses walk to the right; the brown (chestnut) horse is the
trailing/rear one (left, behind the tan horse), so the prior is the brown horse's speed. 2D clip: both horses walk on
the same ground line in front of the wall, so one m/px scale is used. fps = question_fps = 24.

Speed (measure.py, frames 0-48; frame 49 is an animation loop reset):
- rump edge (leftmost chestnut pixel, median over rows y 925-965): very linear, fit slope 3.30 px/frame, net 3.26 px/frame
- scene record torso centroid: 151.4 px / 48 frames = 3.15 px/frame; torso_x0: 3.10 px/frame
- barrel template match: 3.08 slope (noisy, body deforms)
Adopted 3.25 px/frame = 78 px/s -> scale 0.874/78 = 0.01121 m/px.

Height: ear tip to hoof. Frame 0 zoomed read: ear y≈883, hooves y≈1042-1043 -> ~160 px; scene bbox heights 162-165
in frames 0-8 and 48 (clear frames), median over all frames 159.5 (some frames clip ears). Adopted 162 px.

Height = 162 x 0.01121 = 1.81 m. Route spread: speed 3.15-3.30 px/f and height 159.5-164 px give 1.76-1.88 m.
Confidence: moderate (main uncertainty: rig-root speed vs edge markers, ~±4%).
