# Q1357 — height of the walking pedestrian (simulation_0067, 3D)

File fps = question_fps = 24. t=0.58 s -> frame 14, t=1.58 s -> frame 38.

## Focal length (principal point assumed at the image centre, 1080,540)
- `poles.py`: centre lines of two traffic-light poles fitted in code (right pole dx/dy=-0.251, left foreground pole
  +0.329, residuals <0.7 px). They meet at vertical VP (1088, 2640); its x is about cx, so the principal point is
  centred.
- With the horizon y=-47 (road VP (2697,-43) from scene/): f^2=(2640-540)*(540+47) gives f=1110. The pole VP is
  orthogonal to the road VP, which gives f=1101. Treating the two roads as perpendicular (VPs (2697,-43) and
  (110,-47)) gives f=1107. **f ≈ 1105 px** (HFOV ≈ 89°).
- Check with the prior (`vanfit.py`, `vanprof2.py`): I back-projected the white van (bbox centre) with its given
  depths at frames 14 and 38, put its track on that 3D line and fitted a quadratic over frames 14-38. This gives
  acceleration 3.8 m/s² at f=1100 (prior 4) and 3.1 m/s² at f=1340. The van's profile is not cleanly uniform (the
  bbox centre is biased, and the van is clipped by the frame edge up to frame 14). So the van cross-check is loose,
  but it agrees with f≈1100.
  A "starts from rest at frame 1" assumption would give f≈1340. I rejected it because it conflicts with three
  vanishing-point estimates and with the fitted acceleration.

## Height (`pedmeas.py`, `height2.py`)
- I re-measured the pedestrian's outline in code against scene/bg.png, using half-max edges with |diff| summed over
  RGB > 100. The record's bot_y cut the feet 2-7 px short, so I replaced it. Pixel height is 112 px at frame 0,
  110 at frame 14, 107 at frame 38 and 104 at frame 71.
- Pelvis 3D position = bbox centre back-projected with the given depths (21.677 m at frame 14, 22.7825 m at frame
  38), interpolated linearly in time. Walking speed comes out at about 1.2 m/s, which is plausible.
- I placed the head top and the stance foot on the world-vertical line through the pelvis (up direction from the
  vertical VP). This corrects for the camera pitching down about 28°; a naive D*h/f gives 2.2 m, which is wrong.
- Mid-stance frames (feet at the same image row, stance foot under the pelvis): 18, 19, 20, 64, 65, 66 give
  1.85, 1.86, 1.87, 1.85, 1.85, 1.80, **mean 1.85 m**. Over all frames: median 1.86, range 1.80-1.94 (the
  rear-foot-lower bias inflates the stride frames). Pelvis sits 0.97-1.02 m above the foot, a ratio of about 0.53,
  which is anatomically consistent.
- Sensitivity: f=1340 would give 1.70 m.

Answer: 1.85 m. Confidence is moderate to high, about ±5 %; the main uncertainty is f.
