# q356 – displacement of the shark (simulation_0155)

Prior: shark speed = 7 m/s. 2D scene, 24 fps (file fps = question_fps, so no re-timing), 48 frames (0-47).
The shark swims straight in −x at constant height and constant apparent size, with no turns. That makes displacement = path length.

Measurements (scene/tracks/shark.csv origin_x_est, measure.py):
- origin x 2236.6 px (frame 0) → −392.2 px (frame 46): 2628.8 px over 46 frames = 57.1 px/frame on average.
  The shark is gone at frame 47. Extrapolating one more step (~56 px) gives ≈2685 px for frames 0-47.
- The mid-clip dorsal-apex speed is 58.5 px/frame (frames 7-38). The end steps are about 56, and the first snout steps are lower (37-56, partly snout-detection lag).

Answer: with the prior taken as the shark's (constant) speed, the displacement over the clip (frame 0 → frame 47 = 47/24 s) is
7 × 47/24 = **13.71 m**.
Second route: pixel displacement × m/px, with m/px taken from the clip-mean pixel speed, gives the same 13.71 m. If instead
m/px comes from the mid-clip pixel speed (58.5 px/frame ↔ 7 m/s), the result is 13.37 m (−2.4 %). The gap comes from the
slightly slower first and last steps, which are measured on the snout and tail tips and carry flex error.
I chose 13.71 (constant-speed reading). Using the 2.0 s duration would give 14.0.
Confidence: good (within about 3 %).
