# q1324 – width of the turning yellow car (taxi), simulation_0065

Answer: **1.89 m** (body width across the car, without mirrors).

The file and the question are both at 24 fps, so frame = round(t*24): t=0.58 s is f14 and t=1.58 s is f38. 3D scene, static camera.

## Focal length (3D, pinhole; principal point at the image centre)
- Road vanishing point from the curbs: (800, -208) (scene record).
- Vertical vanishing point: `poles.py` fits 6 lamp and traffic-light poles (rms 0.1-0.2 px each), giving (1076, 6896).
  Its x equals cx, so roll is about 0. Orthogonality of the two vanishing directions gives **f = 2180 px**
  (2180-2187 across pole subsets).
- Check 1 (`focal.py`): with the given depths, the pedestrian's f14->f38 displacement is perpendicular to the road
  and parallel to the ground only for f ≈ 2000-2200.
- Check 2 (`geom.py`): at f=2180 the reference points of all four objects (van, cyclist, pedestrian, taxi), placed
  with the given depths at both times, lie at consistent heights (7.24-7.50 m below the camera). Ground ≈ 8.0-8.15 m
  below the camera. Origin heights are plausible: pedestrian pelvis 0.92 m, taxi origin 0.63 m.
- The prior (van acceleration 4 m/s^2) is a weak constraint. A quadratic fit to the bbox-centre track gives 3.4-3.5
  m/s^2 at f=2180, and 4 m/s^2 would need f ≈ 1000, which the vanishing-point geometry excludes. The bbox-centre
  track is a biased proxy for the origin, so I did not use the prior for scale. The scale comes from depth_info.

## Taxi width
- Taxi origin: exact depth at f14 (23.7441 m) and f38 (27.0055 m). At other frames, the bbox-centre ray is intersected
  with the origin plane (up·X = -7.448 m) defined by those two points.
- Heading (`rearwidth.py`): the two taillight centroids (red blobs, `taillights.py`) must be at the same height on a
  rear-face plane L/2 = 2.5 m behind the origin. Side-on box fit gives L ≈ 5.0 m (`boxfit.py`). Heading rises
  smoothly over the turn: 0.8° (f0) -> 12.5° (f14) -> 18.9° (f18) right of the road. Taillight separation is
  steady at 1.23-1.27 m.
- Widest body row just above the taillights (`maxwidth.py`, yellow silhouette): 205 px at f0 down to 187 px at f14.
  Its left and right pixels are intersected with a lateral plane s metres ahead of the rear face:
  - s = 0.3: W 1.81-1.85
  - s = 0.6: W 1.84-1.87
  - **s = 1.0: W 1.876-1.910**, mean ≈ 1.89
- Only at s ≈ 1.0 are the left and right half-widths equal (0.93-0.96 m each) in every frame from f0 to f14, while
  the heading changes 12°. This symmetry is the self-check that picks s, so W = 1.89 m.
- Rear face itself at the taillight row (`edges.py`): 1.66-1.70 m. That is the narrower, rounded tail, not the
  maximum width.
- Mirror-to-mirror (rough, f12, mirrors ~3 m ahead of the rear): ≈ 1.95 m. If the reference AABB includes the
  mirrors, the answer would be about 1.95.

## Sensitivity and confidence
- Width scales as 1/f: f = 2080 gives 1.95 m, f = 2280 gives 1.83 m.
- Moving the rear plane (Lr 2.3-2.7) changes W by less than 1%.
- Result: L ≈ 5.0 m, W ≈ 1.89 m, a plausible sedan taxi (Crown Victoria-like, slightly scaled).
- Confidence: about ±5%.
