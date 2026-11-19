# Q813 – speed of the white horse at t = 1 s (frame 24, fps 24 = question_fps)

2D top-down scene, static camera. Prior: "horse at the back" = 0.874 m/s. There are two horses: the brown one (upper, trailing
behind on the left) and the white one (middle). The small animal is a dog/cat. So "the horse at the back" = the brown horse.

## Scale (brown horse)
- Centroid track (scene record), frames 0-48: 2.592 px/frame. Frame 49 is a loop reset, so it is left out.
- Long-baseline template matching of the body, no accumulated error (brown2.py), pairs (0,48), (8,40), (12,36), (4,44), (0,24), (24,48):
  2.52-2.70 px/frame, mostly 2.59-2.66. Frame-to-frame torso matching (brown.py) gives a mean of 2.69. No gait surge is visible.
- Adopted: 2.62 px/frame = 62.9 px/s, so the scale is 0.874 / 62.9 = 0.01390 m/px.

## White horse (measure.py, white_track.json)
- Background-difference mask centroid, plus frame-to-frame torso template matching. The torso sum is 225.8 px against a
  centroid net of 225.3 px, so the torso method has no bias.
- Mean speed over the clip: 4.60 px/frame (4.69 over two full gait cycles, frames 9-41).
- The torso surges with the gait (period about 16 frames, 3.6-5.9 px/frame). At frame 24 it is about 5.7 px/frame, close to its peak.
  Y sways ±4 px with a period of about 32 frames.

## Answer
- Origin moving at a steady speed (as the brown horse's does): 4.60 × 24 × 0.01390 = 1.53 m/s.
- If the origin follows the surging torso/pelvis: 5.67 × 24 × 0.01390 = 1.89 m/s.
- The brown horse's steady, looping motion suggests the rigs are moved at a constant speed, so the constant-speed reading is more
  likely. The answer is set slightly above it to hedge: **1.60 m/s**.
- Second check: the white/brown speed ratio is 4.60 / 2.62 = 1.76, so 0.874 × 1.76 = 1.53 m/s, consistent with the above.
- Confidence: medium. The scale is good to about ±3%. The main uncertainty is whether the reference includes the gait surge.
