# q2119 — average velocity of the swimmer (m/s)

Prior: swimmer height = 1.8 m. Internet video in 2D, top-down drone shot. The file runs at 26.64 fps, but question_fps = 30 is used for all times (frames 0–129 → T = 129/30 = 4.30 s).

## Scale
Frame 0, body flat at the surface, read on a 3× zoom with a 20 px grid: toe tips at x≈579, top of head at x≈785 → height = 206 px (scene record: 205 px). Arms stretched forward reach x≈835, but they are not part of the height.
Scale = 1.8/206 = 0.00874 m/px.

## Displacement (measure.py)
Camera drift at frame 129 (scene/camera.csv): dx = +11.3, dy = −0.95 px, so it is compensated.
- Head centre: (774, 697) at f0 → (1430.7, 680.5) at f129 (the head/upper-body patch, checked on zooms). That is 645.6 px bg-compensated (656.9 raw) → **1.31 m/s** (1.335 raw).
- Second route, leading tip (fingertips → front of the head patch): 628.7 px → 1.28 m/s.
- Mid-body: 669 px → 1.36 m/s. This one is less reliable because the legs are bent at f129.
Average velocity = net displacement / T, using the head reference with background compensation.

## Answer
1.31 m/s. The routes spread over 1.28–1.36 m/s. I'd expect the error to be within about ±5 % if the annotator used feet-to-head height. If they used the 256 px fingertip length instead, the answer would be about 20 % lower (1.06).
