# Q855 – speed of the box at t = 0.5 s (frame 12), m/s

Prior: the box's side parallel to the slope is 0.611 m. fps = question_fps = 24, so t = 0.5 s is frame 12. The box is cut off by the top edge of the frame at frame 12, so its speed there comes from a model fitted to frames 14–44.

## Measurements (scripts in this folder)
- `track.py`: template tracking (normalised cross-correlation, sub-pixel) of the box face and of the tape patch over frames 9–44, using a template from frame 24. The tracks are in `tm_tracks.json`. The face and tape tracks agree within about 1 px.
- Duplicate frames: frame 27 shows the frame-28 position (one frame dropped, then repeated). Frame 27 is mapped to t = 28 and frame 28 is left out. The same glitch at frames 10/11 is in the clipped part, which is not used.
- The pixel acceleration is not constant: about 6.0 px/frame² early (frames 14–26) and 4.5 late (29–44). A quadratic fit in the image is therefore biased (it gives 3.0–4.0 m/s depending on the frame window). The cause is perspective: the ramp recedes from the camera going downhill. The box's end faces show the same thing: the downhill end face is visible early, the uphill one late, and both are edge-on near frame 28.
- `persp.py`: model = constant acceleration along a 3D line seen through a pinhole. The image coordinate along the path is w = (A·s + B)/(C·s + 1), with s = (t − tc)². This fits frames 14–44 with an RMS of 0.18 px (tape track). tc ≈ 0.95 frames, so the box starts from rest at the start of the clip, which is physically consistent.
- Scale: the box's along-slope length is 92 ± 1 px at frames 24–31 (`along.py`, half-max edge crossings on the b* difference image, 11 lines per frame). There the end faces are edge-on, so this is close to the true face length. The scale is set at frame 26.5 from 92 px = 0.611 m, then carried to frame 12 by the fitted model. The model says the image scale at frame 11.5 is 1.053× the scale at frame 26.5.
- Result: acceleration a ≈ 6.27 m/s² (the same as g·sin 40° on a frictionless slope, which is plausible). Speed at frame 12 (backward difference between frames 11 and 12) = 2.74–2.80 m/s across tracks and frame windows; the tape track over frames 14–44 gives 2.759.
- Small correction: the box edge I measured is closer to the camera than the box's centre. The camera is about 15 m away (`geom.py`: f ≈ 2200 px, from the vanishing point plus the frame where the end faces are edge-on). That makes the speed slightly too low. I added about +0.7% (the possible range is 0 to +1.5%).

## Check by a second route
- Four frame windows (14–44, 16–44, 14–30, 16–36) on two independent tracks (face, tape) give 2.68–2.80 m/s; most fall within 2.74–2.78.
- An image-space quadratic fit restricted to the early window (14–26), where the scale is closest to that at frame 12, gives 2.83–2.99. Those use the frame-24 scale and assume constant acceleration in pixels, so they are expected to read high. That is consistent with the perspective model.

## Answer
2.77 m/s. Confidence: moderate to good, about ±4%. The main uncertainties are the 92 px box length (±1.5%), the depth offset of the measured edge, and extrapolating the model to frames where the box is clipped.
