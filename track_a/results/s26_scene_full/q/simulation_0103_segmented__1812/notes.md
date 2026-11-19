# Q1812 – shark–boat distance at t = 0.5 s (frame 12)

2D side-view scene, 24 fps (file and question rates agree). Prior: shark acceleration = 1 m/s².

## Scale
Quadratic fits of the shark's x position over frames 1/2/5–53 (fit.py) for the bbox centre, mask centroid, nose and tail
all give |a| = 0.1477–0.1500 px/frame² = 84.8–86.4 px/s². The bbox centre gives 85.6 px/s², so the scale is
1/85.6 = 0.01168 m/px.
Checks: the boat is 856 px long, which is 10.0 m. Boat speed is 17.87 px/frame, which is 5.0 m/s. The shark's speed at
f2 is 7.5 px/frame, which is 2.1 m/s. These round, plausible values support the scale.

## Positions at frame 12
- Shark origin is the bbox centre (1575.5, 904).
- Boat origin is the hull midpoint (289.5, 440.5). The x value is the stern–bow midpoint (bow tip 717 − 427.5). The
  y value is the midpoint between the cabin roof and the keel.
- dx = 1286 px, dy = 463.5 px, so the distance is 1367 px, which is **15.97 m**.

## Uncertainty
The boat origin's height is unknown because the mast runs off the top edge of every frame:
- Origin at the keel: 1312 px, or 15.3 m.
- Origin at the full-bbox centre including the mast: about 16.3 m.
- Horizontal distance only: 15.0 m.

I used the hull-midpoint reading. Confidence is moderate: the scale is good to about 1%, and the vertical origin adds
about ±4%.
