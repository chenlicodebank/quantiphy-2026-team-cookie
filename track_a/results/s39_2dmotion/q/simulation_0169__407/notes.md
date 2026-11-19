# Q407 — speed of the astronaut at t = 3 s (m/s)

2D render, file fps = question_fps = 24, so t = 3 s → frame 72. Speed = |p(72) − p(71)| × 24 × (m/px).

## Scale (prior: astronaut height = 2.2 m)
- Frame 0, the astronaut is upright (axis ~95°). My threshold mask (gray > 25, `measure.py`): bbox height 91 px
  (y 477–567), width 44. SAM 3 mask at frame 0: vert_px 90, box 477.5–566.7 (89.2), length 90.8. Agrees within ~1–2 %;
  the scene record also gives 91 px. Using 91 px → 2.2/91 = 0.02418 m/px.
- The main-axis body length stays 91–92 px through the clip, so the depth doesn't change and one scale applies.

## Motion (mask centroid as the origin)
- `measure.py` gives the centroid each frame (binary and intensity-weighted). Steps in px/frame:
  frame 70: 1.88, 71: 1.92, 72: **1.76**, 73: 1.50, 74: 1.32 (ease-out deceleration). Weighted centroid at 72: 1.74.
- Smoothed: cubic/quadratic fits of the path over frames 62–79 give 1.69 / 1.64 for the step 71→72. The mean of
  steps 68–76 (a linear trend centred on 72) is 1.68. I adopt 1.71 ± 0.05 px/frame.
- Body rotation at this point is ~0.2°/frame, so centroid–origin offset effects are well under 0.1 px/frame.

## SAM 3 check (`sam_frames.py`)
- Text-prompted per-frame masks for frames 68–76 (area ~2140 px, overlay checked on f72: clean outline of the astronaut).
  The SAM centroids sit about 1 px lower and right of mine (the SAM mask leaves out the soft glow), and they jitter
  about ±1 px from frame to frame. Their raw steps are 0.99 / 2.58 / 0.34, which is too noisy to use directly.
  A linear fit over 68–76 gives 1.53 px/frame and a quadratic fit gives 1.64. These are 4–10 % below my value. My threshold
  centroid's steps fall smoothly from frame to frame, while SAM's jump around, so I trust mine. Even so, I moved my
  estimate slightly toward the smoothed values.
- SAM's video track latched onto the moon after frame 37, so I didn't use it. Box-prompted segments returned
  oversized masks (area 5000–8000), so I discarded those too.

## Answer
1.71 px/frame × 24 × 0.02418 m/px ≈ 0.99 m/s (raw single step 1.76 → 1.02; smoothed 1.64 → 0.95).
Confidence: moderate-high, ±4 %.
