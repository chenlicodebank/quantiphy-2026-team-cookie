# q_1861 – acceleration of the astronaut at t = 1 s

The video is a 2D segmentation render at 1920x1080 with 80 frames. The file and question_fps are both 24, so t = 1 s is frame 24.
The prior is: height of the astronaut = 2.2 m.

## Measurements (own scripts: measure.py -> track_own.csv, fit.py)
- **Mask.** Non-white pixels (min RGB < 225 or < 240), largest blob. I also computed a darkness-weighted centroid.
  The centroid tracks agree with scene/tracks/person.csv to within 0.1 px.
- **Scale.** At frames 0-2 the figure is upright (axis about 94 deg). There the bbox height is 90-92 px, mean 90.67 px.
  Scale = 2.2 / 90.67 = 0.02426 m/px.
- **SAM 3 check, frame 0.** Box height 89.8 px and vert_px 90, centroid (1294.4, 520.2). This matches my 90.7 px and (1295.2, 519.1) within 1 %.
- **SAM 3 check, frame 24.** vert_px is 87, but the SAM box spans 414.6-505.1 = 90.5 px. My mask gives 90 px, and the zoomed frame (frames/f24.png) shows a figure about 90 px tall.
  The vert_px figure therefore undercounts a little. Frame 24 is not used for the scale anyway.
  The SAM centroid (1299.0, 455.7) is within 1.1 px of mine (1298.8, 456.8).
- **Motion.** The figure moves along an almost straight line, up and slightly to the right: 275 px in total.
  It starts at rest at about frame 0 and stops at frame 78, with a smooth ease-in/ease-out profile (Blender Bezier).

## Acceleration
- **Smoothstep model.** I fitted s = L(3u^2 - 2u^3), u = (f - f0)/(f1 - f0), along a straight line to all 80 frames.
  Result: f0 = -0.4, f1 = 78.3, L = 275.1 px, rms 0.33 px (0.43 px with the weighted centroid).
- **Benchmark convention.** Acceleration = speed(24) - speed(23) with one-frame backward differences, i.e. s(24) - 2s(23) + s(22).
  From the fit this is 0.108 px/frame^2, which gives 1.511 m/s^2 (1.516 with the weighted centroid).
  With exact keyframes at frames 0 and 78, the result is 1.555 m/s^2.
- **Analytic second derivative at frame 24.** 0.1014 px/f^2, giving 1.42 m/s^2. The backward difference is centred on frame 23, which is why it is about 6 % higher.

## Second route
I fitted free local polynomials to the along-path distance, independent of the smoothstep model.
- Cubic fits over ±12 and ±15 frames give a second derivative at frame 24 of 0.1017-0.1036 px/f^2, i.e. 1.42-1.45 m/s^2.
- Adding the third-derivative shift to frame 23 gives about 0.109 px/f^2, i.e. 1.52 m/s^2.
- Both routes agree with the smoothstep model.

A constant-acceleration model (accelerate, then decelerate) fits much worse (rms 1.33 px), so I rejected it.

## Answer
The answer is 1.53 m/s^2: the backward-difference value (range 1.51-1.56). If the reference used the instantaneous derivative instead, the value would be about 1.42.
Confidence is moderate to high. The scale is good to about ±1 %, and the fitted keyframe timing is good to about ±3 %.
