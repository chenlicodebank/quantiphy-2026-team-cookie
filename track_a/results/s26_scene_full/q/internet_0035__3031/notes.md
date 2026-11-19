# q_3031: displacement of the toilet-paper core from the start to 0.83 s (cm)

## Scale
The prior says the toilet-paper core is 100 mm. That is the tube's length along its axis, which is also the direction it moves
(the diameter is about 260 px, or about 4.7 cm, which is reasonable for a tube). At frame 0 the length is 555–557 px: the left end
is at x≈1718 and the open right end, visible between thumb and index finger, is at x≈2273, with the axis tilted about 4°.
I checked this on the zoomed crop frames/f0.png. Scale = 10 cm / 556 px = 0.01799 cm/px.

## Time base
The file runs at 22.297 fps, which is not a standard rate, so the 36-frame clip looks re-timed. question_fps is 30, so I take
the original footage as 30 fps: 0.83 s → frame round(0.83×30) = 25. The camera is static (scene record: grout lines move less than 1.2 px).
Under the other reading (file fps), 0.83 s would be frame 19 and the answer about 6.8 cm (380 px).

## Measurement (measure.py: Lab-colour tube mask, overlays in frames/mask*.png)
- Left end of the tube: x 1720 → 2352 between frame 0 and frame 25. The median left boundary gives 1728 → 2358, so Δx ≈ 631 px.
- Centre y, from the top and bottom edges near the left end: 1362.5 → 1320.5, so Δy ≈ −42 px.
- Displacement ≈ 632 px → 632 × 0.01799 ≈ 11.4 cm.

## Second route
I read the position of the small dark mark on the tube by eye from the gridded crops (frames/f0.png, frames/f25.png): about (2010, 1430) at frame 0 and about (2640, 1405) at frame 25.
That gives Δ ≈ 630 px ≈ 11.3 cm, which agrees.

## Confidence
Good on the pixel measurement and the scale (about ±3 %). The main risk is the time base: if the reference used the file's
fps instead, the answer would be 6.8 cm.
