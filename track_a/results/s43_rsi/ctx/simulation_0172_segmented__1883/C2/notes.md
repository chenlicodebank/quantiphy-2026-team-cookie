# q_1883: acceleration of the astronaut at t = 0.5 s (frame 12 at 24 fps; the file is also 24 fps)

## Scale
- Prior: astronaut height 2.2 m. depth_info: Z = 18.147 m at t = 1 s (f24), where bbox_h = 380 px.
- Focal length: f = h_px * Z / H. f24 gives 380*18.147/2.2 = 3134 px. f0 gives 342*20.3/2.2 = 3150 px (Z0 taken from the backpack scale).
  The walking pose is a little shorter than rest height, so f is probably about 3140-3300 px. I ran both values
  (HFOV about 39 deg). At Z ≈ 19.4-20.1 m around f12 this is about 0.0061 m/px.

## Measurements (scripts in this folder)
- `measure.py`: soft-mask centroid, bbox and upper-body centroid for every frame (meas.json).
- `regpack.py`: affine ECC registration of a rigid patch (backpack, helmet and upper torso, arms excluded;
  f12 region x700-790, y665-850) to frames 0-30, cc 0.95-0.99. Output: a body-fixed point track plus scale.
  The vertical scale sy is the depth cue. sx falls while the figure turns (yaw).
- Body-point image velocity over f1-f14 is very smooth: dx goes 9.1 → 10.8 px/f and dy 7.5 → 1.5 px/f.
  Image speed is 11.8-12.8 px/f early, falling to a plateau of 10.8 px/f at f10-f14.
- f14→f15 shows a sharp kink: image speed doubles to about 20 px/f. Later kinks follow at f30 and f60. f12 lies in
  the first smooth segment, so every fit uses f0-f14 only.
- `accel.py`: 3D points from back-projection ((u-cx)/f, (v-cy)/f, 1)*Z, with Z from several depth models. Results
  for the scalar speed derivative at f12:
  - Constant depth, linear depth from bbox_h, or linear depth from backpack sy: raw (s12-s11)*24 = -0.26 to -0.28;
    quadratic speed fit -0.27 to -0.31; cubic position fit -0.34 to -0.41; linear fit over the segment -0.53 to -0.61 m/s^2.
  - Quadratic depth from sy: -1.1 m/s^2.
  - Raw per-frame depth from bbox_h or sy: depth noise of ±0.3 % per frame swamps the result (±20 m/s^2), so I
    rejected those values. A quadratic depth fit to bbox_h gives +5. That is not credible: h rises after f9 because
    the legs close, not because the figure gets nearer.
- Speed at f12 is about 1.6-2.4 m/s; the range depends on how fast the figure approaches the camera.

## Answer
The scalar speed is nearly flat and falling slightly at f12: a ≈ -0.3 m/s^2 (a slight deceleration). The question
asks for a positive number, so I answer with the magnitude, 0.35 m/s^2.
Second route: the raw one-frame difference of the image-plane speed (10.85 → 10.77 px/f) gives -0.27 m/s^2. This
agrees with the smooth fits.
Confidence: low. The value is small, and the depth rate (approach towards the camera) is poorly constrained.
Depending on the depth model, the magnitude runs from 0.27 to about 1.1 m/s^2.
