# q1358 — average speed of the bicycle over the whole clip (m/s)

Answer: **5.12 m/s**

Video and question fps are both 24, 72 frames. Frames 0 and 1 are identical (duplicate first frame).
Objects: white car = van, yellow car = taxi, bike = cyclist, human = pedestrian.

## Camera (3D scene, static camera)
- The horizon is at y ≈ -47, from the east-west and diagonal road vanishing points (2697,-43) and (110,-47); it is horizontal.
  Pitch = atan(587/f).
- Focal length:
  - Vertical VP from the long left-foreground pole (slope dx/dy ≈ 0.32-0.35), assuming a centred principal point:
    f ≈ 1090-1125.
  - Orthogonality of the two road VPs: f ≈ 1107.
  - Camera height above ground checked across objects (`hcheck.py`, using bike and pedestrian depths plus ground
    contact pixels): f ≈ 1000-1100.
  - Van prior (`vanacc.py`): the van track is the ray–plane intersection at the van's height, which is calibrated from its
    depths. A quadratic fit gives a = 4.2-4.4 at f = 1100, with v(0) ≈ 0.2-0.5 m/s, so the van is not starting
    from rest at frame 1. At f = 1100 the depth-based van displacement over frames 14→38 is 4.74 m. This matches a = 4
    with t0 ≈ -0.1 s, which agrees with the fit.
  - Adopted f ≈ 1100-1130 px.

## Bicycle track
- I used the head-top track from scene/tracks/cyclist.csv (all 72 frames; a few interpolated frames). Each head ray is
  intersected with a horizontal plane. I then fitted a quadratic in t per coordinate over frames 1-71, so pixel jitter
  does not inflate the path length. The motion is nearly uniform: about 5.23 m/s at the start falling to 5.12 m/s at
  the end (f = 1100).
- Route A (`bike.py`): metric scale from the bike-origin pixels (centre between the wheel hubs) at frames 14 and 38
  (t = 0.58 s and 1.58 s) with the given depths 14.1413 and 17.8223 m. This gives 5.20 m between those frames
  and a whole-clip mean of 5.11 m/s at f = 1100.
- Route B (`bike2.py`): no choice of origin pixel. I solved for the plane scale and the vertical head-to-origin offset
  so that both given bike depths are reproduced. This gives a camera height above the head plane of 5.28 m and a
  head 1.64 m above the origin, which is plausible. Whole-clip mean 5.15 m/s at f = 1100 (5.11-5.20 for a ±0.2 m
  fore-aft offset).
- How the mean speed depends on f: f = 1000 → 5.39, 1100 → 5.15, 1200 → 4.96, 1300 → 4.80.
- The mean of per-frame speeds over frames 1..71 includes the zero step from the duplicate frame. Excluding it
  (path / 70 frames) gives +1.4 % (5.22).

## Confidence
About ±4 %, mainly from the uncertainty in f (±100 px gives ±4 %).
