# Q56: speed of the walking pedestrian at 1.0 s (m/s)

The question and the file are both 24 fps, so t = 1.0 s is frame 24. The video is 2D and top-down, with a static camera.
The prior is that the white car is 6 m long. The white car is the white van/minibus, the only white vehicle in the scene.

## Scale (van length)
- My own measurement (vanlen2.py, vanprof.py): a brightness profile along the van's long axis against the road. The body ends are taken at a +30 grey-level crossing.
  The length is 233.9 px at f0, 232.6 px at f24 and 234.4 px at f71. f48 reads 228.5 px, probably shortened by motion blur, so I left it out. **L = 234 px**, which gives 6/234 = 0.02564 m/px.
- The scene record's thr-25 body length is 236 px, which agrees within 1%.
- SAM 3 segment ("white van", f24) gives 243 px (y 717–959). That is 4% longer than my value. The zoomed crop (frames/van24.png) and the profile
  show why: rows 716–722 ahead of the hood are darker than the road (−30), so they are the van's shadow, and SAM includes them. My 234 px body length is the right one.
- Reading the length as 236 px would change the answer by 1%.

## Pedestrian motion
- The walker has a white top and walks right along the SE sidewalk (y ≈ 843) at constant velocity.
- Record torso-centroid track (look.py): linear fits give 2.045–2.062 px/frame over windows f2–28, f10–38, f12–36 and f2–71.
  The y drift is about 0.
- SAM 3 track (tracks/pedestrian_0.csv; I checked the overlay): 2.073 px/frame over f14–34 and 2.046 px/frame over f2–71. The SAM centre and the torso
  centroid at f24 agree within about 2 px.
- The one-frame difference is noisy (±1 px from the leg and shadow motion). The motion is uniform, so I used the fitted rate as the
  frame-24 backward difference: **2.05 px/frame**, which is 49.2 px/s.

## Answer
v = 2.05 × 24 × 6/234 = **1.26 m/s**. That is a plausible walking speed.
The second route (SAM track slope with the same scale) gives 1.26–1.28 m/s.
Confidence: high. The likely error is about 2%.
