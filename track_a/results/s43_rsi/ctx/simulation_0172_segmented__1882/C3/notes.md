# q_1882: astronaut speed at t = 0.5 s (m/s)

Prior: the astronaut is 2.2 m tall. Depth: D = 18.147 m at t = 1 s (frame 24). question_fps = file fps = 24, so t = 0.5 s is
frame 12, and the speed is |P(12) - P(11)| x 24.

## Observations
- The astronaut walks right in profile. In the image the motion is slow (about 10.5 px/frame) from f0 to f14, then
  jumps to 20-33 px/frame from f15 on. The speed asked is in the slow phase, which is steady from f3 to f14.
- The scene/ pelvis heuristic was not used. Instead I tracked image patches frame to frame with sub-pixel template
  matching (patch_track.py) on the waist/hip, the lower backpack and the helmet+backpack. Waist displacement
  f11->f12 = (9.9, 3.5) px, |d| = 10.50 px. Neighbouring frames (f10-f14) give 10.4-10.9 px.
- Depth change: the bbox height depends on the pose (crouched at f12: 343 px; 380 px at f24), so I did not use it
  for depth. Instead I matched rigid parts from f24 with a scale and rotation search (part_scale.py: helmet,
  backpack, and helmet+backpack). Relative scale at f12 is about 0.94 for all three parts. A linear fit of the
  backpack scale over f4-f15 gives a slope of +0.00096/frame, so the astronaut approaches slowly (radial speed
  about 0.5 m/s). This gives Z12 = 19.27 m.

## Focal length
- From the prior: the bbox height at f24 is 380 px at 18.147 m, which gives f = 3134 px. The pose is slightly bent,
  so this is a lower bound.
- The most extended poses (f35-f40) normalised by the part scale reach about 384-388 px in f24-equivalent pixels,
  which gives f = 388 x 18.147 / 2.2 = 3200 px. This equals a 50 mm lens on a 36 mm sensor (HFOV 39.6 deg).
- I used f = 3200. With f = 3134 / 3268 the answer is 1.66 / 1.60 m/s.

## Result (speed.py)
- 3D back-projection of the waist track with depth Z = Z24 / s(i): speed at f12 = 1.627 m/s (lateral 1.52,
  radial about 0.55). The mean over f10-f14 is 1.646.
- Second route, the lower-backpack track: 1.606 at f12 and 1.648 over f10-f14. The helmet patch gives 1.76, but
  it includes the torso straightening (rotation of about 1 deg/frame), so it does not track the origin.
- Answer: **1.63 m/s**. Confidence: moderate (about ±6%). The main uncertainties are f (±3%) and the
  radial component taken from the scale slope.
