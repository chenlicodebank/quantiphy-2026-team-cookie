# Q403 — astronaut speed at t = 1 s (m/s)

2D video, 24 fps file = question_fps 24 → t = 1 s is frame 24. Static camera.

## Scale (prior: astronaut height 2.2 m)
- Own mask (gray > 40, `measure.py`), frame 0, upright figure: bbox height 90 px (y 477–566).
- SAM 3 segment frame 0: box y 477.5–566.7 (89.2 px), vert_px 90, length 90.8 px. scene/ record: 91 px (threshold 25).
- All within ~1 pct; I used 90 px → 0.02444 m/px. (91 px would give 2.58 m/s, 1 pct lower.)

## Speed (one-frame backward difference at frame 24, lightly smoothed)
- Own intensity-weighted centroid track (`measure.py`, `speed.py`): the raw step at frame 24 is 4.61 px (noisy; steps 22–26 run 4.30–4.61).
  Local polynomial fits (±6..±12 frames, deg 2–3) give a backward difference of 4.43–4.47 px/frame. Mean of steps 22–26 is 4.43; the binary-mask centroid gives 4.44–4.47.
- Second route: the SAM 3 box-prompted track (tracks/astronaut_0.csv; correct near frame 24, the summary's large net displacement comes from later frames) gives a
  centre (471.2→435.8)/8 = 4.43 px/frame over frames 20–28. Its box-top edge gives 4.5 px/frame. The two routes agree.
- I used 4.45 px/frame × 24 = 106.8 px/s × 0.02444 m/px = **2.61 m/s**.

The motion has an ease-in profile, so speed is still rising slowly at frame 24 (about +0.1 px/frame per frame). Smoothing is symmetric about frame 24, so the bias is small.
Confidence: good, about ±4 pct (centroid jitter, plus a 1 pct ambiguity in the pixel height).
