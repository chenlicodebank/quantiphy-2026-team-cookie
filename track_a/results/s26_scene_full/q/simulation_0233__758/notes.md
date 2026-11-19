# q_758 — length of black cat incl. tail (m)

Prior: cat speed = 0.714 m/s. 2D top-down render, 24 fps (file fps = question_fps, no re-timing). The cat walks along +x at constant speed on the table top.

## Scale (pixel speed from the prior)
- Head front (robust column, >=15 mask px) is very linear: slope 13.41 px/frame over frames 0-44 (13.38 over 10-44, 13.41 over 22-44). Frames 45-49 are left out because of the grey-head render artifact. Script: `scale.py`.
- 13.42 px/frame x 24 = 322 px/s, so the scale is 0.714 / 322 = 0.002217 m/px.
- The tail-tip slope (13.95 px/frame) is less reliable because the tail swings.

## Pixel length
- Full mask extent, nose to tail tip, in frames 22-49 while the cat is fully in view: median 330.5 px, mean 331 px (scene record). My own re-segmentation in `measure.py` gives 321-341 px over frames 22-44.
- The white muzzle is not in the black mask. At frame 36 it reaches about x 538, against a mask edge of 534, so add about 4-5 px. That gives about 335 px.
- Checked on a zoomed frame at t = 1.5 s: tail tip ≈ 205, nose ≈ 538, so about 333 px.

## Answer
335 px x 0.002217 = 0.743 m, rounded to 0.74 m.
- Second route: using the tail-tip slope as the speed gives 0.714 m. Without the muzzle correction the answer is 0.733 m.
- Confidence: about ±3-4 %. The main uncertainties are the curl of the tail (the extent varies by ±10 px between frames) and which reference point carries the prior's speed.
