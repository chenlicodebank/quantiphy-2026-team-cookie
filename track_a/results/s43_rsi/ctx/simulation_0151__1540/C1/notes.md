# Q1540 – acceleration of the blue car (light-blue cart) at t = 1 s

The file rate and question_fps are both 24, so t = 1 s is frame 24. The acceleration is (speed(24) - speed(23)) x fps, which is the
second difference x22 - 2 x23 + x24 times fps².

## Motion (pixels)
- The cart moves parallel to the image plane at constant depth, and the camera is static. At frame 24 it is mostly hidden by the
  yellow car, so the acceleration has to come from a model fitted over the visible frames.
- I re-tracked the cart myself with masked colour SSD template matching against frame 36, ignoring yellow (car) pixels
  (`track.py`, `track2.py`). The patches were the rear light panel (frames 22-41), the rear box + handle, the roof, and the lower
  body/wheels (frames 27-41).
- The lights track fits a Blender ease-in/out (smoothstep: x = x0 - Δ(3u² - 2u³), u = (i - i0)/T) with rms 0.04 px. The fit
  gives i0 ≈ 0 and T ≈ 59 frames. This agrees with the record's early track: the motion starts from rest at frame 0, with
  about 2.2 px/f² at the start. In the fit, acceleration falls linearly to zero around frame 29.
- Pixel acceleration at frame 24 (`fit3.py`, `joint.py`):
  - lights-only fits starting at frames 22-25: 0.508-0.520 px/f²
  - joint fit with the early record (frames 0-13): 0.500
  - rear-box track: 0.48-0.52
  - joint fit of body + roof + record with polynomials of degree 3-5: 0.49
  - the record's own track (roof plane): 0.46-0.49
- Scaled to the wheel/side plane (body track = 1.0054 x lights track, 1.014 x roof track), the adopted value is **0.51 px/frame²**.

## Scale
- The cart's front tyre diameter was measured in code on frames 32, 36, 39 and 41 (vertical dark extent, `tire2.py`):
  75.0 ± 0.5 px. The rear wheel is merged with its dark wheel well, so I didn't use it.
- That gives 0.369 / 75.0 = 0.00492 m/px in the tyre/side plane. Because the motion is parallel to the image plane, every point
  of the rigid body (including the origin) has the same world acceleration.
- Check with depth_info and the ground-contact rows: the pixel tyre sizes give Z_cart/Z_car = 0.00492 / (0.764/192) = 1.236. The
  ground-contact rows (884 vs 817, horizon at 540) give 1.24 independently, so the two agree.
  - The focal length from the yellow tyre at 11.38 m is about 2860 px, which gives a cart depth of about 14.1 m.

## Answer
a = 0.51 px/f² x 24² x 0.00492 m/px ≈ **1.44 m/s²** (the cart is speeding up).
- The spread of the routes is 0.48-0.52 px/f², i.e. 1.37-1.48 m/s².
- Confidence: moderate-good. The value sits on the falling part of an ease curve and depends on the fitted model, but every
  independent track agrees within ±4 %.
