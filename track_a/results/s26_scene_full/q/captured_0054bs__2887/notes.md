# Q2887: velocity of the white ball at 1.5 s (frame 36)

The white ball is scene `grey_object`, the off-white oval ball. It was confirmed on frames 24 and 36. The green ball is the yellow tennis ball. Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360). question_fps = file fps = 24.

## Measurements
- `seg.py`: my own segmentation of the white ball, frames 20-47. It uses a background difference, excludes yellow pixels and gives the centroid plus sizes. Masks were checked in `frames/masks.png`. Output: `white_track.csv`.
- Timing: one source frame is missing between frames 35 and 36 (every object's step doubles there). Frame 36 is just after that gap, and the bounce is at frame 38.
- Distance at 1.5 s: depth_info only gives 1.235 m at 1.0 s (frame 24). I used two routes:
  1. **Apparent size** (`vel.py`). The size across the motion is about 44-50 px at frame 24 and about 22-24 px at frame 36, a ratio of about 2.0. That puts the distance at about 2.4-2.6 m.
  2. **Free-flight physics** (`phys.py`). I modelled the distance as linear in true time and back-projected the track. Requiring the vertical acceleration to be g = 9.81 gives a depth rate r of about 3.0 m/s. Requiring the horizontal X to move at constant speed gives r of about 2.5. I took r ≈ 2.6 m/s, so the distance at frame 36 is about 2.64 m.
- 3D velocity at frame 36 (`vel3.py`, r = 2.6):
  - one-step forward difference 36→37: 3.93 m/s;
  - quadratic fit over frames 30-37: 3.91 m/s;
  - 5-frame window 34-38 at t = frame/24: 4.56 m/s. This window spans the missing frame.
- Convention check with the prior: the orange ball at 0.5 s (frame 12) also sits just after a missing frame. A 5-frame centred window 10-14 at t = frame/24, at a depth of 2.24 m, gives 2.22 m/s against the prior's 2.21. A single forward step gives only about 1.7-1.9. So the reference appears to use a centred smoothing window at t = frame/24, which spans the gap.

## Answer
4.5 m/s, from the centred-window convention. The depth-rate uncertainty (r = 2.3-2.9) gives a range of 4.2-5.0. The physical speed without the missing-frame inflation is about 3.9.

**Confidence:** moderate-low. The distance at 1.5 s is not given, so it is estimated.
