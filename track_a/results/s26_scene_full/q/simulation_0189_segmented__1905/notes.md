# q1905 truck length
2D scene (side view, vertical lift), 120 fps both file and question; camera static.
Prior: box speed 0.094 m/s. The cardboard box rises with the cargo body, slowly accelerating (px speed ~15 -> 23 px/s on box track,
~6 -> 29 px/s on body/marker tracks). The prior gives no time, so it is read as the clip-average speed (mean of per-frame speeds = net rise / 3.333 s).
- Box ref_y rise 64.1 px -> 19.23 px/s; box bottom edge 65.9 px; roof top edge / marker lights 67.2 px -> 20.16 px/s
  (box rides rigidly on roof; box top edge slightly affected by flap/shrink). Adopted 20.0 px/s.
- Scale = 0.094/20.0 = 0.0047 m/px.
- Truck length (bumper to bumper, non-white mask x extent, frames 0/200/400): 124..1839 = 1716 px (stable).
- Length = 1716 x 0.0047 = 8.07 m. Range by speed choice: 8.00 (20.16 px/s) to 8.39 (19.23 px/s).
Check: wheelbase ~879 px -> 4.1 m, wheel diameter ~165 px -> 0.78 m; plausible for a catering truck.
Confidence: moderate (depends on which speed the prior refers to, since the lift accelerates).
