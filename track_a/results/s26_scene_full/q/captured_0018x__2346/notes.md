# q_2346: distance between box and tennis ball at t = 3.0 s (cm)

**Caveat:** the clip has 49 frames (0-48) at 24 fps, so it ends at 2.0 s. Frame 72 (3.0 s) is not in the file,
so the answer is an extrapolation of where the two objects rest or move after 2.0 s. The file fps and question_fps are both 24.

## State at the end of the clip (scene/ tracks, checked on crops in frames/box_38_48.png)
- White box: by frames 47-48 it has tipped over to the image-left and lies flat. Centre u ≈ 415-418 and the
  front-bottom edge is at row 609. At 3.0 s I assume it is at rest at u ≈ 415.
- Tennis ball: it bounces almost straight up and down at u ≈ 746, drifting about -0.2 px/frame, so u ≈ 742 at frame 72.
  Restitution from the first bounce is e ≈ 0.70. Extrapolating, frame 72 falls in roughly the third small bounce,
  with the centre about 0.1 m above the floor.

## Depths (no depth_info for box or tennis ball; estimated)
I used a level-camera floor model, v - cy = f·H/Z, with f = 763 and cy = 360.
- From the soccer ball (2.8 m, contact row 577): H = 0.784 m.
- From the far person (3.13 m; feet at row 577, Z ≈ 2.97): H = 0.845 m.
- Tennis-ball depth checked independently:
  - its free-fall pixel acceleration on frames 28-35 with g = 9.8 gives Z = 2.45;
  - its 20.5 px diameter, assuming a 6.7 cm ball, gives 2.49;
  - its floor row 616 gives 2.34-2.52.
  - Overall Z ≈ 2.47, which corresponds to H ≈ 0.83.
- Box: front edge at row 609 gives Z_front ≈ 2.54, so the centre is at ≈ 2.58 (with H = 0.83).
- The jump between frames 35 and 36 is a dropped frame: a parabola fit fits well only if one extra frame is inserted there.

## Result
- Box centre ≈ (-0.76, 0.79, 2.58) m; tennis ball ≈ (0.33, 0.70, 2.47) m. Distance ≈ 110 cm.
- Range over the camera-height choices: 104 cm (H from the ball depth) to 112 cm (H from the far person).
- Answer: **108 cm**.

Confidence: moderate to low. The time asked is outside the clip, and the box and tennis-ball depths are estimates.
