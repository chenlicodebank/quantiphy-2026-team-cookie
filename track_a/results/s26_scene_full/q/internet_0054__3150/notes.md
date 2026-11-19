# q 3150 – wheel-to-wheel width of the scooter (internet_0054)

Prior: average speed of rider = 4.9 m/s. fps = question_fps = 30 (no re-timing issue).
Convention (internet): one scale = 4.9 m/s / rider's mean pixel speed; apply to the scooter's pixel extent.

Reading of "wheel-to-wheel width": the scooter is seen exactly side-on, so the across-width is not
observable; the annotator's measurable "wheel to wheel" extent is front tyre front edge -> rear tyre rear edge
(the scooter's visible extent). Alternative reading (axle to axle, wheelbase) given below.

## Measurements (measure.py, using scene/tracks/rider_scooter.csv; checked on zoomed frame 0, view.py)
- Frame 0 crop: front tyre left edge ≈ x 2803, rear tyre right edge ≈ x 2980 -> ≈ 178–181 px, matches track (181).
- Scooter tyre-to-tyre length: 181 px (f0) -> 193.5 px (f93), mean 185.4 px (slight approach to camera).
- Wheelbase mean 144.2 px.
- Rider mean per-frame speed: 487–489 px/s raw image coords (box centre, torso, front axle agree);
  497–499 px/s after removing the slow camera drift (+0.34 px/frame).
- Scale: 0.00985 (stabilised) … 0.01005 (raw) m/px.

## Result
- tyre-to-tyre extent: 1.83 m (stabilised) / 1.86 m (raw) -> answer 1.85 m.
- Second route: split clip in halves (matching length and speed per half): 1.820 m and 1.837 m – consistent.
- Alternative reading (wheelbase, axle to axle): ≈1.42–1.45 m.
Note: the prior makes the rider ~2.8 m tall, so the scale is inflated vs reality; the reference follows the prior.
Confidence: moderate (main uncertainty is which "wheel-to-wheel" extent the annotator took).
