# Q1413: speed of the astronaut at t = 3 s (frame 72 at 24 fps; the file is also 24 fps)

Speed = |p(72) - p(71)| x 24, where p is the pelvis/root.

## Image motion of the pelvis at 71->72
- `torso_track.py` tracks the rigid helmet-back + backpack region from frame to frame. It searches rotation and refines translation to subpixel; match scores are about 0.99. A hip point is attached rigidly to that region.
- Hip displacement 71->72 = (8.59, -2.69) px, so |d| = 9.00 px. Neighbouring frames give 9.19 (70->71) and 8.70 (72->73), so the motion is smooth.
- Second route: the mask-centroid dx in scene/ is 8.2 px. Its dy is noisy because the limbs swing.

## Scale
- Rigid size cue L = helmet top to backpack bottom, measured on the silhouette's left edge (`leftedge.py`, `backpack.py`):
  - about 181 px in frames 0-19
  - grows to about 213 px during hop 2 (the astronaut comes toward the camera)
  - stays at about 207-214 px in frames 60-79
- Most upright walking frames (76-79): bbox height is 438-439 px against L = 213-214, a ratio of 2.054. Extended in-air frames (26-29) give about 2.12 (pointed toes). I took the rest standing height as 2.08 x L.
- At frame 72, L is about 210, so the standing height is 437 px and the scale is 2.2 / 437 = 0.00504 m/px.
- Check with depth_info: Z72 = 18.147 x 183/210 = 15.8 m, so f is about 3150 px (horizontal FOV about 40 deg). At frame 24 this predicts a standing height of 382 px; the measured bbox there is 385 px in a nearly extended pose. Consistent.
- Lateral speed: 9.00 px x 0.00504 m/px x 24 = 1.09 m/s.

## Depth component
- L/cos(tilt) rises 1.8% from frame 60 to 79; raw L rises 0.5%. That gives dZ of about 0.005-0.02 m/frame; I took 0.012 m/frame, which is about 0.29 m/s.
- Template-scale matching was rejected: the torso's out-of-plane rotation biases it.
- Foot rows were rejected: the feet skate.
- Total: sqrt(1.09^2 + 0.29^2) = 1.13 m/s. With no depth component it is 1.09 m/s. Answer: 1.11 m/s.

## Confidence
Moderate, about ±10%. The main uncertainties are:
- the rest-height-to-L ratio (±2%)
- the depth-rate component (+0.5% to +9%)
