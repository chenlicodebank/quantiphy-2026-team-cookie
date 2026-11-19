# Q1412: acceleration of the astronaut at t = 2 s (m/s^2)

**Answer: 0.65 m/s^2. Confidence is low; the plausible range is about 0.3-0.8.**

## Time base
The file and the question both run at 24 fps, so t = 2 s is frame 48. The astronaut is in the air from frame 19 (take-off) to frame 58 (landing), with the apex at about frame 36. A flight of 1.6 s and an apex of about 0.56 m above the ground fit lunar gravity. The vertical fit of the mask centroid gives 1.62 m/s^2 at f = 3050 px, so 24 fps is consistent.

## Scale and depth
- Depth at frame 24 is 18.147 m.
- **Relative depth** comes from the torso scale. ECC affine registration of the helmet, backpack-top and chest region (`ecc_scale.py`) gives s(i). Chaining 24→30→48 gives s24/s48 = 0.951, so Z48 = 17.26 m.
- **Depth trend.** Between frames 48 and 60 the scale grows 5.4%, so the astronaut approaches at about -1 to -1.4 m/s.
- **Ground check.** The torso-scale depth ratio between the stance at frame 17 and the landing at frame 60 (1.163), together with the foot rows (1023 → 1053), implies a horizon at row ~838. That would put the camera about 1.1 m high, which is plausible.
- **Focal length.** About 3050 px, from the most upright frames 76-79: 438 px tall at Z ≈ 15.1-15.3 m (from the scale chain and the sqrt-area ratio) for 2.2 m. As a check, the lunar-g fit of the centroid matches at f = 3050.
- Positions are back-projected with the principal point at the image centre.

## Reference point
The origin is the pelvis, which I tracked three ways:
- the torso template centre (`track_torso.py`);
- a pelvis point (1500, 805) at frame 48, carried to other frames through the per-frame torso affine (this accounts for torso rotation);
- the mask centroid from scene/.

## Acceleration
The definition is d|v|/dt at frame 48, using backward differences of fitted positions. Raw one-frame differences are noise (±2-3 m/s^2), so I used fits:
- **(A) Local quadratic fits, ±6/±8 frames** (`local_fit.py`, `final_est.py`):
  - depth linear in t: -0.2 to +0.2;
  - depth quadratic (the approach speeds up in the torso-scale data): 0.33-0.95.
- **(B) Ballistic flight model, frames 31-56** (vertical quadratic, horizontal X and Z linear; `final_est.py`):
  - torso 0.74, pelvis 0.75-0.81, centroid 0.58-0.62;
  - fitted g is 1.54-1.95 m/s^2, close to lunar g.

  This equals g·v_vert/|v|: at frame 48 the astronaut is about 0.5 s past the apex, falling at about 1 m/s, with horizontal speed about 2.1 m/s.
- **Answer.** I took about 0.65, the centre of the ballistic estimates (0.58-0.81) and the quadratic-depth local fits (0.33-0.95).

## Caveats
- The image-plane x speed of the pelvis is nearly constant around frame 48. Whether the speed change is about 0 or about 0.7 therefore depends on the depth model (how fast the approach toward the camera changes) and on the pelvis vs. centre-of-mass motion.
- The torso-scale depth cue is affected by out-of-plane rotation: its vertical and horizontal scales differ.
- Speed segments change abruptly at frames 29/30 and 60/61, which suggests composited animation clips. No fit window crosses them.
