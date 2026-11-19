# q_2013: acceleration of the yellow car at t = 1 s (frame 24 at question_fps 24; the file is also 24 fps)

## Method
- The yellow car translates right to left at a constant depth (its apparent size is constant), so its image is a pure
  translation. I measured that translation from the **axle centres**: a circle fit to the silver rim edge of each wheel
  (`axle_track.py`). This is rotation invariant and sub-pixel. The fit residual sd is ~0.1 px per frame.
  - Front wheel: frames 17-26. Rear wheel: frames 23-33. The constant offset between them is 709.5 px (the wheelbase).
- Per-frame pixel speeds (px/frame) from the front axle: 18:85.65 19:88.24 20:90.81 21:93.10 22:94.94 23:96.84 24:98.24 25:99.60 26:100.68.
  From the rear axle: 24:98.39 25:99.62 26:100.78 27:101.64 28:102.09 29:102.54 30:102.54 31:102.54 32:102.11 33:101.59.
- The motion matches Blender's default 2-key Bezier ease (smoothstep in time) almost exactly:
  x = A + D(3u²-2u³), u = (f - 0.03)/58.99, D = -4036.6 px. The rms is 0.06 px, and the keys sit at video frames 0 and 59.
- Acceleration by the benchmark convention, (speed(24) - speed(23)) × fps: from the fitted curve this is 1.540 px/frame², i.e. **886.8 px/s²**.
- **Scale:** tyre diameter in pixels, measured from the axle centre to the tyre silhouette against the white
  background along rays in the lower arc, with a half-level threshold (`tyre_radius.py`).
  - Mean radius: front 91.89 px, rear 92.14 px. D ≈ 184.0 px (±1 px).
  - The scene record said ~175-186; a full-circle fit gives ~200 because it picks up the wheel-arch shadow, so I rejected it.
  - Scale = 0.764 / 184.0 = 0.004152 m/px. This holds at the tyre plane, which is the car's depth; all rigid points share the same world velocity.
- **Result:** a = 886.8 × 0.004152 = **3.68 m/s²**. The speed at frame 24 is ≈ 2360 px/s ≈ 9.8 m/s.

## Checks
- Second route, free polynomial fits to the axle track:
  - deg 3 over frames 14-34 and 16-32: 886.7-886.8 px/s².
  - deg 4 over frames 12-36: 890.1 px/s².
  - The raw discrete second differences near frame 24 (1.90, 1.40, 1.36 px/frame²) average 1.55, i.e. ≈ 893 px/s².
  - Quadratic fits give ~750 px/s², but they are biased: the acceleration changes linearly, and their rms is 0.5-1.5 px against 0.06 for the smoothstep fit.
- Depth consistency: f ≈ 184 × Z/0.764 ≈ 2650-2740 px (HFOV ≈ 39-40°). This is plausible for depth_info 11.38 m to the left front tyre at t = 0.5 s.
- The scene/ cx track (edge based) gives similar speeds but is noisier (±3 px). I did not use it for the answer.

## Confidence
High for the pixel acceleration (<1%). The scale depends on the tyre pixel diameter (±1%), so the overall uncertainty is about ±3%.
