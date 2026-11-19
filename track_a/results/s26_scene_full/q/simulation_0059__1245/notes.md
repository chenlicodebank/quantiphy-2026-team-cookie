# Q1245: speed of the yellow car (the taxi) at t = 2.5 s (frame 60 at 24 fps; the file is also 24 fps)

The yellow car is the taxi in scene/. At f60 it has finished its right turn and is driving straight toward the camera
along the main road. Its image track f50-71 lies on a line through the road vanishing point, which fits that.

## Camera
- Principal point is taken as the image centre (1080, 540).
- Road vanishing point: I fitted lines to the curb edges on bg_full.png (vp.py, residual 0.5 px): **(1261, 707)**.
  That gives a horizon at y = 707 (no roll assumed) and the direction of the main road.
- Focal length from the van (white car), whose depths are given at f14 and f38:
  (a) The van's 3D displacement between f14 and f38 should run along the cross street, which is perpendicular to the
      main road. This gives **f ≈ 2240 px**.
  (b) Fitting a uniform acceleration to the van's track along its 3D line, with a = 4 m/s² (the prior), gives
      **f ≈ 2165 px**. The quadratic fits with 0.02 m rms.
  The two agree within 3.5%. The result does not depend on f within this range.
- Camera height above the road comes from the van tyre contact (y 799) and the bike wheel contact (y ~801), placed
  vertically below their origins at the given depths: H ≈ 1.75 m (horizon 707). The four estimates are 1.69–1.79 m.

## Route 1: ground contact (ground.py)
The taxi's lowest tyre pixel (y_max) in f50-71 is projected onto the road plane. A linear or quadratic fit of the 3D
position over f50-71 gives the speed at f60 (backward difference f59→f60):
- 4.07–4.08 m/s with horizon 707
- 4.00 m/s with horizon 702, 4.16 m/s with horizon 712
- no change between f = 2165 and 2240
The linear and quadratic fits agree, so the speed is constant over f50-71.

## Route 2: apparent size (scale_track.py, route2.py)
- A template of the taxi's front at f71 is matched across f46-71 at different scales (NCC 0.81–0.99 for f50-71).
  Depth is taken as proportional to 1/scale.
- The scale ratio f50→f71 is 1.136. The ground route gives 1.124 for the same frames, so the two are consistent.
- The absolute depth constant is fitted to route 1, and the 3D positions come from the template centre.
- Speed: 3.98–4.00 m/s (3.93–4.07 across horizon 712–702).
- Check: the taxi's height in pixels (88 px at f14, where the depth is 38.6 m; 119 px at f60) puts it about 28.5 m away
  at f60. Route 1 gives 28.7 m.

## Answer
The mean of the two routes is **4.04 m/s**. The routes differ by about 2%, and the horizon uncertainty (±5 px) adds
about ±2%.

## Caveats
- The two given taxi depths (f14 on the cross street, f38 mid-turn) do not agree on a constant-height origin plane
  (about 10% apart). This is because a turning car's bbox centre is not where its origin projects. So the scale came
  from the van and bike ground contacts instead.
- Confidence: good, about ±5%.
