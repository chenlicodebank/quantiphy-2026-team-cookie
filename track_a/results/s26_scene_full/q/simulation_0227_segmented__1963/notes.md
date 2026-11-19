# q_1963: acceleration of the red general chess piece at t = 1 s

## Finding: the asked object is not visible
- I searched every frame for red pixels (`find_red.py`). The only red pixels are on the flamingo float's beak and
  they move with the float. All non-white content lies in x 512–1431, y 712–1018: the cat, the float, six lounge
  chairs and the round item.
- The round item (the only disc-like object) does not move. Its centroid stays at about (969.6, 830.0) ±0.3 px over
  all 50 frames (`round_item.py`).
- So no red Chinese-chess "general" piece can be seen in this segmented clip, and its motion cannot be measured
  directly.

## Fallback (low confidence)
- Scale (2D, from the prior): the cat's centroid moves 268.6 px in 49 frames, which is 5.48 px/frame or 131.6 px/s.
  1.041 m/s divided by that gives 0.00791 m/px. fps = question_fps = 24.
- Proxy: the flamingo float is the only object that accelerates. Its speed rises smoothly from about 0.8 to a peak
  of about 13.5 px/frame near frames 24–25, then falls to about 1 px/frame. This looks like Bezier ease-in/out
  keyframes.
- Float acceleration at frame 24:
  - Local cubic fits over windows of ±4, ±6, ±8 and ±10 frames give 0.00, 0.09, 0.16 and 0.17 m/s².
  - A global quintic fit gives 0.12 m/s².
  - At t = 1 s the float is at its turnover, so its acceleration there is close to zero.
- Answer given: 0.15 m/s². This is the float proxy and is very uncertain, because the asked object could not be
  identified in the video.
