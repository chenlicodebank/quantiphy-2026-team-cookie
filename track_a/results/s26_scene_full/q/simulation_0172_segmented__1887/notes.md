# q_1887: acceleration of the astronaut at t = 2 s (m/s^2)

Time base: the file and the question both use 24 fps, so t = 2 s is frame 48. The convention is
acc = (speed(48) - speed(47)) x 24, with speed being the one-frame backward difference of the pelvis (origin) in 3D.

## Scene
There is one astronaut doing a bounding low-gravity stride:
- in the air or landing f0-16;
- a fast hop f16-35 (top of the hop at about f35);
- coming down f35-60, holding an almost fixed stride pose f36-56;
- landing at about f60, then walking on the ground.

Frame 48 falls in the descent, with no contact or bounce near it, so a smooth fit across f38-58 is allowed.

## Scale
- Upper-body template scale relative to f48 at f24 (the depth_info time) is 0.9265, so Z48 = 18.147 x 0.9265 = 16.8 m.
- The f48 pose is a stride (bbox_h 413 px). The tallest size-normalised poses (f37-41) reach about 421 px, so I
  took 2.2 m standing ≈ 423 px at f48 scale, giving 0.0052 m/px.
- This implies f ≈ 3230 px. Check: the crouched pose at f24 (380 px at 18.147 m) comes out at 2.13 m, plausible
  for bent knees.

## Motion near f48
Tracked by scale+translation template matching (`track_tm.py`, `track_multi.py`; whole body with references
f48/f56, and upper body). I excluded the f40 reference because its scale fit jumps between two peaks at f50.

| | Value |
|---|---|
| Image velocity at f48 | about 14.2 px/f in x, 7.9 px/f in y |
| 3D speed | about 2.0-2.1 m/s |
| Vertical image velocity | rises from 3.5 to 8 px/f over f40-47, then flat at about 8 px/f to f58 (not ballistic) |
| Horizontal image velocity | dips slightly around f48-50, then increases |

The depth trend (relative scale growth per frame) comes from the whole-body, upper-body and helmet+backpack
templates. Near f48 it is about 0 to 0.15 %/frame: the astronaut approaches the camera slowly. The body turning
makes the scale estimates uncertain.

## Result
`accel2.py` fits polynomials over several windows (f38-58, 40-56, 36-59, 42-54, 44-52), three tracks and three
depth trends, then applies the convention on the fitted path.
- Static depth: +0.12 to +0.56, typically 0.3-0.45.
- Approach at 0.15 %/f: about +0.05 to +0.40, typically about 0.2-0.3.
- Approach at 0.3 %/f (likely too fast): about -0.2 to +0.16.

`accel.py` (local quadratic smoothing) gives a similar spread.

Answer: **0.3 m/s^2**. The speed is nearly constant here (about 2.05 m/s), so the acceleration is small and its
estimate is dominated by tracking noise and the depth-trend assumption.

Confidence: low. The plausible range is about 0.1-0.5 m/s^2.
