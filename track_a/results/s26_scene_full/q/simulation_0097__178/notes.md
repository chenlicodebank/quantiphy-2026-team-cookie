# q178: height of the plane (m); prior: car acceleration = 10 m/s^2
2D scene (side-on, static camera), one m/px scale from the car's pixel acceleration.
- Car x (centroid and bbox centre, scene/tracks/car.csv; re-checked by re-segmenting frames 20/28/35 in measure.py):
  quadratic fits over frames 1-40, 5-40, 10-40 give |a| = 211.6-213.5 px/s^2 (2c*24^2); per-frame dx grows ~0.37 px/frame each frame.
  Use 213.3 px/s^2 -> scale = 10/213.3 = 0.04688 m/px.
- Plane height (world AABB vertical extent = tail-fin top to engine bottom): 239 px (y 269-507) in all full-view frames 18-40,
  independent re-segmentation thresholds 6 and 10 both give 239 px (240 in a few frames); use 239.3 px.
- Height = 239.3 x 0.04688 = 11.22 m.
Check: car length 121 px -> 5.67 m (Cybertruck ~5.7 m); plane length 800 px -> 37.5 m, height 11.2 m (A320/737-class ~11.8-12.5 m): consistent.
Confidence: good (~2-3%).
