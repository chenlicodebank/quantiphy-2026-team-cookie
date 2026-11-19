# q80 – speed of walking person at 0.5 s (prior: bike length 1.7 m)

2D top-down Blender scene, 24 fps (file fps = question_fps = 24). t = 0.5 s -> frame 12; speed = |p12 - p11| x 24.

## Scale (measure.py)
- Bike length (cyan pixel mask, x extent): 378 px in frames 0-5 (376 ± 2 later, faint tyre tips lost to threshold).
- SAM 3 "bicycle": frame 0 box 739.0-1118.2 = 379 px (length_px 380); frame 12 373-376 px. Scene record: 378.
- Used 378 px -> 1.7/378 = 4.497e-3 m/px. (Within 1 pct of all estimates.)

## Walker displacement
- Template matching of the torso+head region (rows 405-485, ±24 px around torso centre), sub-pixel:
  11->12: 13.07 px; 10->11 12.76; 12->13 13.25; 13->14 13.08; 10->14 average 13.05 px/frame.
- Scene record torso-bbox centre (pelvis proxy): 1077.0 -> 1090.0 = 13.0 px. Agrees.
- SAM 3 "walking person" centroid 1077.9 -> 1088.9 = 11.0 px: differs >3 pct, because the SAM mask includes the
  swinging legs/arms (overlay seg_02_f12.jpg shows the trailing leg inside the mask), so its centroid is biased by
  limb motion. The torso (pelvis proxy) is the right reference; SAM's mask over the torso matches the torso position.

## Answer
v = 13.07 px x 24 /s x 4.497e-3 m/px = 1.41 m/s.
Second route: mean torso speed over frames 10-14 (13.05 px/frame) -> 1.41 m/s; whole-clip mean 12.87 px/frame -> 1.39 m/s.
Confidence: good (~3 pct).
