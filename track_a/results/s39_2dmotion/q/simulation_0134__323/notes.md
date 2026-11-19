# q323: acceleration of the bread slice at t = 1.75 s (m/s^2)

Prior: toaster height = 0.166 m. 2D video, 24 fps for both the file and question_fps, so t = 1.75 s is frame 42.
Convention: a = (speed(42) - speed(41)) x fps, where speed(i) = |p(i) - p(i-1)| x fps.

## Scale
- Toaster pixel height at frame 43, from the brightness profiles in `toaster_profile.py`: the top rim edge is at
  about y 1114.5 (x = 508) and the bottoms of the feet at about y 1398 (x = 300 and x = 715). Between the feet the
  base ends at 1389. That gives H = 283.5 px.
- SAM 3 "toaster" mask at frame 43 runs over y 1114-1399, which is 284-286 px. It agrees with my measurement.
- The scene record gave 276 px (1114-1390). That figure misses the feet. The feet are part of the bounding box,
  and the zoomed frame `frames/base.png` and the profiles show them going down to 1398. The record's 276 px is
  wrong by 3 pct, so I used 283.5 px.
- Frame 0 is not usable for SAM: there the mask includes the toast sticking out of the slot (top at 1059).
- Scale = 0.166 / 283.5 = 5.855e-4 m/px.

## Toast positions (y relative to frame 43, in px)
| route | f40 | f41 | f42 |
|---|---|---|---|
| template match on frame 43, vertical only, subpixel (`measure_toast.py`) | 80.41 | 31.83 | 7.85 |
| SAM box top | 80.2 | 31.3 | 7.4 |
| SAM centroid | - | 32.0 | 8.1 |
| SAM box bottom | - | 31.7 | 7.3 |
| top edge over the middle columns (integer px) | 81 | 32 | 9 |

- The scene record's top_y at frame 41 (866) is wrong: it caught a stray pixel or corner. Its top_flat_mid_y
  (874) agrees with my measurements, and with it the record's cy would be about 5 px too high at frame 41.
- Speeds: v41 is about 48.6 px/frame and v42 about 24.0 px/frame. So the scalar speed changes by about
  -24.7 px/frame^2, which is about -14200 px/s^2.
- The toast is rising and slowing down. The answer is the magnitude.

## Result
- Template match: -8.30 m/s^2. SAM box top: -8.43. SAM centroid: -8.27. SAM box bottom: -8.20. Integer top
  edge: -8.77 (limited by 1 px quantisation).
- Answer = 8.36 m/s^2, the mean of the template-match and SAM-box-top routes.
- The motion is not a constant-g parabola. The second differences are 87, 25 and 16 px/frame^2 while rising and
  about 41 and 44 after the apex, which looks like keyframed easing. So the per-frame convention is used directly,
  not a fit.
- Confidence: about ±4 pct. The position routes agree within 2 pct, and the scale is uncertain by about 1 pct.
