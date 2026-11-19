# Q1538 – acceleration of the yellow car at t = 1 s (frame 24 at 24 fps; file fps = question fps = 24)

Definition used: a(24) = (speed(24) - speed(23)) * fps, speed = one-frame backward difference.

## Motion (hubs.py, accel.py)
- Re-tracked the car myself: centre of the white rim circle (least-squares circle fit to the rim contour) of the
  front wheel (frames 16-25) and rear wheel (frames 23-33). The rim is planar and parallel to the image plane, so
  its centre moves by pure translation; rim radius stays 60.6 / 61.3 px, hub row constant (791.5 / 789.0).
- Per-frame shifts are very smooth, e.g. front 96.73 (f23), 98.35 (f24), 99.57 (f25) px/frame; rear 98.24 (f24).
- Raw second difference at frame 24 (front wheel): 1.62 px/frame^2; neighbours 1.68 (f23), 1.22-1.43 (f25).
- Joint polynomial fit of both wheels (common curve + wheel offset), degree 3-5, windows 16-33 / 18-30 / 19-29 /
  16-28 / 20-33: accel at frame 24 = 1.54-1.57 px/frame^2 (fit rms 0.05 px). Used 1.552 px/frame^2.
- Matches the scene record's trend (its track is noisier: 0.43-1.1 px/frame^2 at f23-25, so it was not used).
- The car accelerates until about frame 30, then brakes. At frame 24 the acceleration is still decreasing, so it is not constant.

## Scale (tire2.py, tire4.py, cart_tire*.py)
- Yellow car front tyre: hub centre to the dark-to-floor crossing at the tyre bottom = 94.0 px (9 frames, sd 0.15)
  -> diameter 188 px. (Rear tyre gives 96.3 px; it may be a larger tyre. The depth_info names the front tyre.)
- Cross-check with the blue cart's tyre (0.369 m): horizontal outer diameter of its rear tyre = 72 px (frames 40-41).
  The depth ratio from the ground-contact rows relative to the horizon row 539.3 is (885-539.3)/(817-539.3) = 1.245.
  That predicts a car tyre diameter of 72*(0.764/0.369)*1.245 = 185.6 px, vs 188 measured, so they agree within 1.3%.
- Used D = 187 px -> 0.764/187 = 4.086 mm/px in the tyre/side plane (same plane as the tracked hubs; the car's
  motion is parallel to the image plane, so the origin's world motion equals this plane's).
- For reference: f/Z ~ 246 px/m, so with Z = 11.38 m, f ~ 2800 px (HFOV ~ 38 deg). Camera height ~ 1.4 m, which is plausible.

## Result
a = 1.552 px/frame^2 * 24^2 * 0.004086 m/px = 3.65 m/s^2 (3.63 with D = 188 px, 3.67 with 186 px).
Answer: 3.64 m/s^2. Confidence: about ±4% (the scale from the tyre-bottom edge, blurred by the glossy floor, is the main error).
