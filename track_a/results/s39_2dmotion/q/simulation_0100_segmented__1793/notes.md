# Q1793: average speed of the shark (m/s), prior: boat length = 10 m

2D video at 1920x1080 and 24 fps. The file fps and question_fps are both 24. The camera is static and the background is white.

## Scale
- Boat length runs stern hull (x=666) to bow tip (x=1521) at frame 57.
  - My threshold mask (`measure.py`): 856 px.
  - SAM 3 "boat" mask, frame 57: box 666.7–1521.3, which is 854.6 px.
  - Scene record: 856 px.
  - These agree to within 0.2%.
- Scale: 10 / 856 = 0.011682 m/px. Using 855 px would change it by 0.1%.

## Shark motion
- I tracked the threshold-mask centroid below y=740 in every frame (`measure.py`).
- The shark is at rest in frames 0–1. From frame 2 it moves at a constant speed to the left (no vertical motion):
  - mean of the per-frame displacements over frames 2–57: 10.75 px/frame;
  - net displacement over frames 1–57: 601.9 px / 56 frames = 10.748 px/frame;
  - linear fit: 10.758 px/frame.
- SAM 3 "shark" centroid: frame 2 at 1624.5, frame 57 at 1033.4. That gives 591.1 px over 55 frames = 10.75 px/frame, which matches my measurement. The SAM length (278–280 px) also matches mine (278 px).
- Speed: 10.75 × 24 × 0.011682 = **3.01 m/s**.
- If I include the single rest frame (frame 1, speed 0) in the mean, the result is 2.96 m/s. I treated the rest frame as a render start-up artifact and answered with the moving speed. The two values differ by 1.7%.

## Confidence
High. The scale and the pixel speed agree across three routes (threshold mask, SAM 3 and the scene record).
