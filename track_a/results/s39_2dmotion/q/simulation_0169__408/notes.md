# q408 — acceleration of the astronaut at t = 3 s

The file is 24 fps and the question is 24 fps, so t = 3 s is frame 72. The scene is a 2D render with a static camera.

## Scale
- Prior: the astronaut is 2.2 m tall. Its upright pixel height at frames 0-3 is 90-91 px (my threshold mask, `measure.py`, mean 90.7 px).
- SAM 3 mask at frame 0: vert_px 90 and length 90.8 px. This is within 1 % of my mask. The zoomed frame (frames/f0z.png) shows the head top at y≈477 and the feet at y≈567, so it agrees.
- Scale = 2.2 / 90.67 = 0.02426 m/px.

## Motion
- I tracked the astronaut myself in `measure.py`, using a threshold mask centroid and an intensity-weighted centroid.
- The SAM 3 track jumped to the wrong object (net displacement 1216 px), so I didn't use it.
- The SAM 3 centroid at frame 72 is (1311.5, 247.9). My mask gives (1311.0, 249.7), the same as the scene record. That is a difference of about 2 px out of 275 px of travel. It is a constant offset and does not affect the acceleration.
- The path is almost straight, about 275 px upward. The motion is a Blender ease-in/ease-out. A smoothstep fit d = D·(3s² − 2s³), with s = (f − f0)/T, matches the data with an rms of 0.22-0.25 px. The fit gives D = 274.5 px, f0 ≈ −0.3 and T ≈ 78.5 frames.
- Acceleration is the backward difference of the speed at frame 72, as the convention requires:
  - smoothstep fit: −125.8 / −125.1 px/s² (plain / weighted centroid) → **3.04 m/s²** magnitude (decelerating)
  - local cubic fit over frames 60-79: −117 / −119 px/s² → 2.85 / 2.88 m/s²
  - mean of the raw per-frame accelerations over frames 69-75: −126 / −133 px/s² → 3.06 / 3.23 m/s²
  - the single raw value at frame 72 is noisy (−71 / −90 px/s²) because of about 0.3 px of centroid jitter, so I didn't use it.

## Answer
About 3.0 m/s². The astronaut is slowing down; the question asks for a positive number, so I give the magnitude.

Confidence: moderate to good. The routes span 2.85-3.06 m/s², and the scale is good to about 1 %.
