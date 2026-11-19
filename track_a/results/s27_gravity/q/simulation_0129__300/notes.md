# q300 – forklift height (m), simulation_0129

The prior is the red ball's free fall at g = 9.8 m/s². The clip is a 2D-style render, so I used one metres-per-pixel scale. File fps = question_fps = 24.

## Scale (from the ball)
- I tracked the ball centroid in frames 2–38 and fitted a parabola. Frame 39 is left out because the ball is occluded there.
  - Own tracker (ball2.py): 515.6 px/s², rms 0.30 px. Split windows give 504 (frames 2–20) and 513 (frames 20–38).
  - Re-fit of the scene/ track (fit_ball.py): 519.3 px/s², rms 0.41 px.
  - Adopted value: 517 px/s². Scale = 9.8/517 = 0.01896 m/px.

## Forklift height in pixels (height.py)
- I took difference masks against a frame where the forklift is elsewhere, in frames 0, 20 and 39.
- The top of the overhead guard is at y 721–723, and the tyre contact is at y ≈ 926–927. Below that is the floor reflection.
- Height = 206 px (±2). The scene record gives 208 px.

## Answer
206 × 0.01896 = **3.9 m**. Using 208 px would give 3.94 m.

## Depth / plausibility check
- A real forklift is about 2.1–2.2 m tall, so this one is about 1.8× real size. The geometry rules out a depth difference that would explain this:
  - At frame 39 the ball is hidden behind the forklift's mast, so the ball is behind the forklift.
  - The ball is also in front of the opaque facade.
  - The forklift's tyres touch the floor at y 927, just below the wall base at y 910–925. Its shadow falls on the glass wall about 45 px ahead of it, so it stands next to the facade.
- So the ball and the forklift are at almost the same depth (within a few %), and the gravity scale applies to the forklift directly. The scene's assets are evidently scaled up: the forklift is taller than the 165 px doorway next to it.
- The scale of the other scene objects is consistent: storey about 4 m, doorway 2.9 × 3.1 m, ball diameter 0.38 m.

Confidence: moderate-high on the measurement (±2 %). The main risk is how the reference scaled the forklift asset.
