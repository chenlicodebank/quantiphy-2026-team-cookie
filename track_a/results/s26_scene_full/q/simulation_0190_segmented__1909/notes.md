# q1909 — width of the truck (prior: box width = 1.33 m)

2D scene (straight-on rear view of a truck, static camera), single metres-per-pixel scale from the prior.
fps 120 = question_fps; time not needed.

Measurements (measure.py, box.py; non-white mask, same threshold for both objects), frames 0/200/400:
- Box (brown carton on top) horizontal extent: median row width 282 / 281 / 281 px (record: 279 px with a
  tighter mask). Width constant over clip.
- Truck widest part = container rear body: median row width 568 / 567 / 568 px; full silhouette bbox
  569–572 px (chassis/bumper below is narrower, ~548 px).
- Scale: 1.33 / 281.5 = 0.004725 m/px.
- Truck width = 568.5 px x 0.004725 = 2.686 m. Route 2 (record values, 567.5 / 279): 2.705 m.
  Same-threshold ratio is preferred (edge blur cancels): ~2.68 m.

Caveat: the box sits on the roof and may be slightly farther from the camera than the rear face,
which would make the true truck width a little smaller; no depth info, so the planar convention is used.
Sanity: 2.7 m is a realistic box-truck width.
Answer: 2.68 m. Confidence: moderate-high (±3% from measurement; perspective is the main unknown).
