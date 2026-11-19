# q1063 – crow wingspan when spread (m) → 4.5

File fps = question fps = 24. Frame = round(t*24).

## Scale (focal length)
- The prior is gravity. The "nest" (distance 17.27 m at t=0/1) is the black fuzzy object that falls beside the trunk
  (frames ~30-49) and lands at frame 50. I re-tracked it with a mask of pixels darker than the median background
  (nest_track.py). Parabola fits of the centroid over frames 30-49 / 32-49 / 34-47 / 36-49 give a_px = 1306-1367 px/s².
  Camera depth Z ≈ 16.2 m (17.25 m Euclidean, ray 0.34 rad off-axis). That gives f = a·Z/g ≈ 2180 px (±7 %), hfov ≈ 48°.
- Independent check: vertical house edges converge upward (verticals2.py): lean ≈ 6.3e-5 per px of x offset, so the
  vertical vanishing point is near y ≈ -14700. Ground contacts with the given distances (nest landing 17 m, cart 33 m,
  house 64 m) put the horizon near y ≈ 1280. f² = (cy-yv)(yh-cy) gives f ≈ 2130. This agrees with the gravity route.
  A real-size reading (f ≈ 6000) would need the horizon below the image, so that reading is ruled out.
- Consequence: the scene is not at real-world scale. The door is ≈5.5 m, the cart wheel ≈2.6 m and the crow's body
  (beak to tail) ≈2.3 m. Gravity and the camera geometry agree, so I kept the prior's scale and did not rescale from
  "standard" objects.

## Crow geometry
- 3D positions from the depths at t=0 and t=1 (centroids (1029,1090) and (1220,1094)) give a velocity of about
  (3.7, -0.3 up, -3.0) m/s, a heading 38° toward the camera from +x (heading.py). The shadow path on the lawn
  (shadow.py) gives 44°. I take 41 ± 4°.
- Body length: frame 58 (wings edge-on), beak to tail ≈133 px, Z ≈ 36.5-37.3 m, foreshortening ≈1.0 → L ≈ 2.29 m
  (this barely depends on the heading).
- Wing tip-to-tip by eye on zoomed crops (crow_zoom.py, crow_mask.py; the background-difference masks are inflated by
  the crow's shadow on the wall):
  - frame 24: 117 px horizontal + 25 px vertical, f/Z ≈ 50 px/m → 3.8 m (heading 44°) to 4.4 m (heading 38°).
  - frame 42: 138 px, f/Z ≈ 54.7 px/m → 5.0-5.9 m. The wing foreshortening is larger here, which makes it less certain.
- Shadow route (shadow_span.py): the camera height comes from matching the shadow's displacement to the bird's (h ≈ 2 m).
  The widest wings-level shadow widths are 141-151 px, giving 4.2-5.4 m. Penumbra and body make this an upper-biased
  estimate.
- Proportion check: a crow's wingspan is about 2.0× its length → 2 × 2.29 ≈ 4.6 m.

## Answer
The routes cluster at 3.8-5.4 m, with a median of about 4.5 m. Answer: 4.5 m.
Confidence: moderate (±15 %). The main uncertainty is the heading-dependent foreshortening of the wings, which are
never seen face-on.
