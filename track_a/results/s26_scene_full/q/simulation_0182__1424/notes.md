# Q1424 – acceleration of the box at 0.2 s (frame 5 at 24 fps; file fps = question fps = 24)

## What happens at t = 0.2 s
The box starts at rest in the air at frame 0 and falls freely, without rotating, until it first touches the ramp at frame ~7.6–8.
Frame 5 lies in the middle of this free fall.

## Measurement (fall.py)
- Sub-pixel template matching of the box (frame-0 template; several interior patches) over frames 0–8.
- The best patch (450–700 × 330–420, correlation >0.99) gives vertical steps of 2.23, 6.41, 10.40, 14.55, 18.42, 22.45 and 26.59 px.
- Its second differences are 4.18, 3.99, 4.15, 3.87, 4.04 and 4.14 px/frame², so the fall is uniform acceleration.
- A quadratic fit gives a = 4.05 px/frame² (≈2333 px/s²), with the vertex at frame −0.07, i.e. released from rest at frame 0.
- Other patches give 3.7–4.25 px/frame², but they include background or flap pixels and score lower.
- Result: the acceleration is constant through frame 5, so the asked value is the free-fall gravity of the simulation.

## Scale
- In a Blender rigid-body simulation, gravity is 9.81 world units/s².
- Consistency check: if a = 9.81 m/s², the pixel scale is 237.8 px/m. With the box at Z ≈ 9.34 m along the optical axis (from the 9.522 m distance at t = 0), that gives f ≈ 2220 px, i.e. a horizontal FOV of ≈ 47°. This is plausible.

## Second route: the prior (ramp acceleration 2.338 m/s² at 0.75 s)
- I tracked the slide over frames 13–35 with ramp.py (template matching with a scale search).
- The mean in-image acceleration is 1.14–1.42 px/frame², rising as the box nears the camera.
- The one-frame value at frame 18 is ≈2.0 px/frame². The per-frame values jump around between 0.1 and 3.4 px/frame² because of the rollers and tracking noise.
- Scaling the mean ramp acceleration with the free-fall scale gives ≈2.8–3.0 m/s², about 20 % above the prior.
- I conclude the prior is a noisy one-frame value from the roller conveyor and is not a reliable scale. A one-frame scale from it would give "g" anywhere between 5 and 8, which does not fit physically. The free-fall phase (smooth and uniform) fits standard gravity.

## Answer
9.81 m/s². Confidence: moderate-high; the main risk is a non-default scene gravity or scale.
