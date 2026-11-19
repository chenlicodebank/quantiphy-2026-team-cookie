# q_1519: width of the yellow car (simulation_0149)

Prior: tyre diameter 0.764 m. depth_info: at t=0 the right-front tyre is 14.244 m from the camera. Rate: 24 fps (the file and the question agree).
This is a 3D render with a static camera. The car is an RX-7 style coupe.

## Camera
- I took the horizon at y≈829 (vanishing point of the ceiling tubes) and the principal point x at 960. The hubs sit at y≈827-833 in every frame,
  so the camera is at hub height (0.382 m).
- At frame 0 the right-front tyre is about 137-138 px tall (2 x (bottom 898 - hub 829); the visual read gives 760-897).
  The vertical size gives f/Z, and the off-axis distance gives Z, so f ≈ 2400 px (HFOV ≈ 44°). Then Z0 = 13.35 m and X0 = -4.97 m.
- Check: the red ceiling pipe vanishes near x≈-770. If that pipe runs perpendicular to the tubes, f ≈ 2313 (about 4% lower). Using that f
  would change the answer by about +2%.
- Rim ellipses fitted in frames 23-29 (rim2.py, overlays in frames/rims.png). Tyre/rim height ratio ≈ 1.47-1.50, from the tyre bottoms
  at frames 0 and 23. That gives a rim diameter of 0.516 m, so each wheel's Z = f x 0.516 / rim_h px.

## Heading
- From the right-front and right-rear rim sizes and positions (frames 23-28): wheelbase 3.00-3.04 m, heading 37.2°.
- From the aspect of the rear rim ellipse (frames 23, 26, 28): 38.6-38.9°. From the right-front rim aspect at frame 0: about 39°.

## Track and width
- Left-front tyre contact x is the centre of the lowest dark band of the tyre: 950 at f23, 1008 at f24, 1073 at f25, 1145 at f26 and 1302 at f28.
  Combined with the heading this places the left wheel along the car's lateral axis from the right-front rim face.
  T(rim face of RF → centre plane of LF) = 1.95-1.97 (frames 23-28, heading 37°) or about 2.0 (heading 38.5°).
- Second route, frame 0, using depth_info directly: RF at (-4.97, 13.35); the left tyre's bottom band is centred at x≈390;
  with heading 39° this gives T = 1.94. Using f = 2313 instead gives 1.99.
- The ground rows of the left tyre sit about 3 px too low for this model. That is the contact shadow/reflection, which spreads toward
  the camera on a tyre seen from the front, so I did not use those rows.
- Tyre width ≈ 0.27-0.28 m (rough, from the left tyre's projected bottom width at frame 0; the real RX-7 ratio gives 0.273).
- Wheel-to-wheel width (outer face to outer face) ≈ T (1.96) + half a tyre width (0.14) + rim face to sidewall bulge (0.02) ≈ **2.12 m**.
- Body width: on a real RX-7 the body is about 4% wider than the outer track, which would give ≈2.2 m. I can't measure the body edge
  directly, because the front corners are rounded. Mirrors are not included. I answer with the wheel-to-wheel reading, as the
  naming rules ask.

Confidence: moderate, about ±7%. The main uncertainties are heading (±2° ⇒ ±4%), the tyre/rim ratio (±2%) and f (±2%).
