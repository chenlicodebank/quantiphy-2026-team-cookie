# q_2187 – basketball diameter (cm)

Lab video, 1280x720, file fps 24 = question_fps 24. f = 0.5959*1280 = 762.8 px, principal point (640,360).
Depth_info: t=0 (f0) Z=1.3210 m; t=1.8 s (f43) Z=1.5835 m; t=1.92 s (f46, rebound apex) Z=1.5795 m.
The prior (g = 9.8 m/s^2) is not needed for a size.

## Measurement (measure.py)
Mask: same as scene/scripts/track_ball.py (saturation/dark threshold). Points on the outer (convex-hull) silhouette,
pushed 0.5 px outward. This excludes the white notch left by the erased hand in frames 0-27. Two size models:
- Card (D = Z * pixel diameter / f): circle-fit diameter f0-3 = 137.2 px -> 23.8 cm; f43 107.9 px -> 22.4 cm;
  f46 111.1 px -> 23.0 cm.
- Exact pinhole sphere: silhouette rays fitted with a cone of half-angle a, so D = 2 Z sin a. Gives f0 22.15 cm,
  f43 21.44 cm, f46 22.18 cm. At f0 the ball is about 17 deg off-axis, so its image is stretched about 7 % by
  perspective. The card formula ignores this, which is why it reads high there.

## Consistency check (second route)
The apparent angular size should scale as 1/Z. Angular-size ratio f0/f46 (cone model) = 1.195. Depth ratio
1.5795/1.321 = 1.196, an excellent match. For card pixel diameters the ratio is 1.235, which does not match.
The f43 depth looks inconsistent: the ball's image grows 3.7 % between f43 and f46, but the given depths differ
by only 0.25 %. So f0 and f46 are the trusted references.

## Answer
Cone model: 22.2 cm (f0 and f46 agree to 0.1 %). Card method: 23.0-23.8 cm.
Answer 22.7 cm. This leans toward the geometrically consistent value but stays within about 5 % of the card reading.
Confidence: moderate (true value probably 22-24 cm).
