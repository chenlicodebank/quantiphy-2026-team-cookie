# Q422: diameter of the rear (main) landing-gear wheels

The prior is the airplane speed, 153.582 m/s. There is no depth_info. fps = question_fps = 24, so no re-timing.

## Scale
- The plane flies side-on at constant depth: its length stays constant in the scene record, so I used one m/px scale.
- Pixel speed (speed.py):
  - cross-correlation of the background-subtracted plane band over frames 10–31 gives 61.45 ± 0.19 px/frame;
  - linear fits of the nose and tail edges give 61.5 and 62.0 px/frame;
  - the scene record says 61.5.
- I used 61.5 px/frame = 1476 px/s, so the scale is 153.582 / 1476 = **0.1041 m/px**.

## Wheel size (wheel.py, wheel2.py, wheel3.py)
- The main gear sits about 20 px behind the plane's centre. It shows two wheels (left and right gear), offset by about 9 px
  vertically, and both are rings with a dark tyre and a hub.
- Their horizontal separation grows away from frame 20, which is a perspective effect. I therefore measured near frames
  18–22, where the plane passes the image centre.
- I measured the horizontal diameter through each wheel centre at the 50% crossing between sky and tyre levels, with
  sub-pixel interpolation:
  - upper wheel: 11.4–11.7 px;
  - lower wheel: 11.4–11.9 px.
- Result: D ≈ 11.6 ± 0.3 px.
- Second check (vertical): the two stacked wheels span 20.1 px in total. With the hub centres about 8.5–9 px apart, each
  wheel is about 11–11.5 px tall, which agrees with the horizontal value (the vertical one is slightly foreshortened).

## Answer
11.6 px × 0.1041 m/px ≈ **1.21 m**.

As a sanity check, the plane is 466 px ≈ 48.5 m long, and a 1.2 m main wheel fits an aircraft of that size.

Confidence: moderate-to-good. The main error is the wheel's pixel size, about ±3–5%, because the wheels are only about
12 px across.
