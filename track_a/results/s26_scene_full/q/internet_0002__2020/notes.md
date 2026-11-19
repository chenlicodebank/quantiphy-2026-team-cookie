# Q2020 — width of the red car (red pickup), prior: lane width = 3.66 m

The view is a near-nadir drone shot from a static camera, so this is a planar, single-scale problem. Timing does not
matter for a size question, so the 19.6 vs 24 fps difference is irrelevant here.

## Scale (lane width in pixels)
The red pickup drives in the lane between the divider rows at y≈989 and y≈1310 (from scene/static_markings.json,
dash centre lines measured on the median background). Dash centre y values, upper row vs lower row:
- x≈600–900: 982.8 vs 1302.1 → 319.3 px
- x≈1750–2040: 991.2 vs 1308.6 → 317.4 px
- x≈2900–3200: 993.0 vs 1318.6 → 325.6 px

This gives a lane width of about 320 px for the car's own lane. The mean over all five lanes is 318.1 px.
Scale: 3.66 / 320 = 0.01144 m/px.

## Car width in pixels
Scripts: measure2.py and measure3.py. Each takes a redness profile (R − (G+B)/2) down image columns of the body,
finds the half-max edges with sub-pixel interpolation, and checks them on overlays (frames/ov*.png).
- Front fenders/hood, side to side: 178–183 px in frames 3, 9, 15 and 21. Mirrors are excluded (they read ≈210–220 px).
- In the cab region, the red-mask top edge snaps to the window strip and gives ≈165 px. On the overlay, the outer
  red body line there spans ≈185 px.
- The truck is tilted ≈2° (lane change), so the column-wise extent ≈ true width (cos error <0.1%). The full bounding-box
  height would wrongly add ≈16 px.
- Width taken: 181 px (±4). The scene record gives 180 px, which agrees.

## Answer
3.66 × 181 / 320 = **2.07 m**

Range: 178–185 px gives 2.04–2.12 m. Using the all-lane mean spacing (318 px) gives 2.08 m.

## Checks
- The same scale gives a bumper-to-bumper length of 532 px → 6.1 m, which is plausible for a crew-cab pickup.
- A width of 2.07 m is plausible for a full-size pickup.

Confidence: good, about ±4%.
