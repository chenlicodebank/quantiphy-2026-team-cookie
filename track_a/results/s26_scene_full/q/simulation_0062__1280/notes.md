# Q1280 – speed of the yellow car (taxi) at t = 2.5 s (frame 60, question_fps 24 = file fps)

Answer: **4.3 m/s**. The question says "average speed at 2.5s"; I read it as the speed at frame 60, using the backward difference smoothed over nearby frames. The speed is nearly constant here.

## Camera
- Focal length from the van (constant depth, moving parallel to the image plane). Its two given distances (30.065 m at f14, 29.307 m at f38) together with its image positions give f = 2256 px and Z = 29.17 m (`focal.py`).
  - Check against the prior: the van's pixel acceleration (307 px/s², quadratic fit) × Z/f = 3.97 m/s², against the prior's 4 m/s² (0.7 % off).
- Pedestrian check with f = 2250: Z = 16.26 m and 15.06 m at the two times. His height comes out as 1.821 m and 1.820 m (consistent). Feet rows give a camera height H = 0.997 m at both times, so fH = 2243.5 px·m (`ground.py`).
- Cyclist distances barely change between the two times, so they constrain f poorly; not used.

## Taxi at f60 (head-on, approaching)
1. **Ground-contact route** (`tyres2.py`): the bottom row of the right front tyre was measured to sub-pixel accuracy at its central columns for f51–71. That tyre is at front-axle depth, Z = fH / (y − 540).
   - Z60 ≈ 16.05–16.2 m.
   - Speed along depth vz = 4.16–4.46 m/s, depending on the edge definition and the fit window.
2. **Image-scale route** (`scale.py`, `speed.py`): a masked template of the whole taxi, taken at f60, was matched over scale and translation in f44–71, and Z ∝ 1/scale.
   - With the effective depth ≈ axle depth 16.1 m: 4.2–4.4 m/s from window fits; the raw f59→60 backward difference gives 4.56 m/s.
3. The record's integer `ground_y` (which includes the contact shadow) gives 4.17–4.34 m/s.
4. Lateral component: about 0.18 m/s (image x drifts by −2.3 px/frame). It adds less than 0.5 % to the speed.
5. Consistency check on the earlier side-view phase: the given distances at f14 and f38 give a 3.9 m chord in 1 s, so the speed was about 4 m/s there. The taxi drives at a roughly constant ~4–4.3 m/s.

## Corrections to the record
The record's taxi `ground_y` includes the soft contact shadow and sits about 10 px below the tyre bottom (691 vs about 680 at f60), so it should not be used for absolute depth.

## Confidence
About ±5 %. The main uncertainties are the camera height (the taxi's tyres at f14 suggest H could be up to about 2 % lower) and noise in the tyre edge.
