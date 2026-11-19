# Q797 – speed of the horse in the front at 1 s (m/s)

Prior: the horse at the back moves at 0.874 m/s. No depth_info. fps = question_fps = 24, so 1 s is frame 24.

Identification: there are two horses on the lawn below the house, seen from overhead, and both walk toward +x. The white/cream horse
(y≈865) is ahead in the walking direction (x≈1080 at frame 24, while the brown one is at ≈810), and it is also the lower one in the image.
So the **front horse is the white one** and the **back horse is the brown one**. On a flat ground plane with a static overhead camera
(per the scene record), one m/px scale applies to both horses.

## Pixel speeds (horizontal motion dominates; y sway is about ±3 px)
- Main method (`pairmatch.py`): masked template matching of the whole horse between every pair of frames (i, j) with
  sub-pixel peaks. At long lags, and for pose-matched pairs (lowest residual), the gait phase cancels out:
  - brown: 2.62–2.64 px/frame (lags 25–48); pose-matched pairs at lags 41–48 give 2.63–2.64, so I use **2.633**.
    Frames 0–48 only, because the brown horse loops back at frame 49.
  - white: the gait period is about 32 frames. Pose-matched pairs at lags 31–32 give 4.62–4.64, and long lags give 4.61–4.65. I use **4.625**.
- Second route: linear fits to the scene-record mask tracks give brown 2.51–2.69 (cx 2.69, torso 2.51, bbox ends 2.57/2.67)
  and white 4.59–4.63. These agree within their gait noise.
- The per-frame mask/template speed of the white horse wobbles between about 4.0 and 5.6 px/frame with the gait. I take the rig
  root as moving steadily, so the speed at 1 s is the mean speed. The local fit over frames 16–32 gives about 4.7 px/frame, about 1.5 % higher.

## Answer
v_front = 0.874 × 4.625 / 2.633 = **1.535 m/s** (scale 0.874 / (2.633 × 24) = 0.01383 m/px).
Confidence: good (about ±3 %). The main uncertainties are the brown horse's pixel speed and whether the reference's per-frame root speed
at frame 24 follows the gait.
