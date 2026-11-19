# q_1758 – wheel diameter of the moving bicycle

Answer: **0.665 m** (front wheel; the bike comes head-on, so the wheel is seen edge-on).
Video 33 fps = question_fps (no time-base issue). Static camera, 3D render.

## Depth consistency check (sizefit.py)
- Cyclist: apparent size (sqrt of the mask area, bbox width) follows K/(d+c) with c ≈ 0 using the given bike depths, so the bike depths fit its body.
- Pedestrian: the size grows far more slowly than the given human depths imply (fitted offset c ≈ +5…+8 m). The pedestrian is also
  higher in the image than the cyclist and has a smaller head (19 px vs 25 px), yet its given depth is smaller (11.9 vs 16.5 m).
  So the "human" distance is to a character origin away from the body, and I did not use it for the body.

## Camera (camfit.py, sweep.py)
Pinhole with principal point at the image centre and no roll. Unknowns: f, pitch, camera height. Fitted to:
(1) the cyclist's front-wheel ground contact (mask bottom, frames 0-59) at the given bike distance minus 0.3 m (origin to front contact);
(2) the pedestrian's head row predicted from the foot ground point with a 1.78 m head-to-foot extent while walking (prior 1.8 m), frames 0-98.
Result: f = 2062 px (2022-2142 over HP 1.72-1.80 and offset 0-0.6 m), pitch 12.8°, camera height 4.6 m, cyclist slant rms 0.04 m.
Plausibility: pedestrian body at about 18.9 m, walking 1.23 m/s; bike 4.8 m/s; rider head width about 0.20 m and pedestrian's 0.17 m;
handlebar height about 1.0 m; seated rider's head about 1.6 m. The kiosk's vertical vanishing point (record: y ≈ 6500, flagged ±30 %)
is predicted at 9500 by the fit. That is a weak, rough check only.

## Wheel (wheel.py, rows.py, frames/wheelhi.png)
The bottom of the front tire is the mask bottom. Just above the tire is a tire-width (9-10 px) bluish patch: the upward-facing top
of the tire, lit by the sky. Above it is a wider grey part (fork crown / head-tube base; the frame is silver).
For a head-on wheel, the image-vertical silhouette extent is D·f/z_hub, whatever the pitch. z_hub comes from the camera model
(the hub is about 0.5 m nearer than the bike origin, which fits an origin at mid-wheelbase).
Frames 36-59 (24 frames), D from the tire bottom to the top of the blue patch: median 0.662 m (range 0.64-0.675, very stable).
Same with the blue middle: 0.61; with the blue bottom: 0.56 (this would be the reading if the blue were a frame part. It is rejected
because the frame/head tube is grey and the blue patch is exactly tire width).
Sensitivity to f (±3 %) puts the answer at 0.64-0.69. Final: 0.665 (0.662 plus a small allowance for the crown hiding the very top of the tire; HP = 1.80 gives 0.67).
Confidence: moderate. The main uncertainty is where the tire top is, under the crown or blue patch.
