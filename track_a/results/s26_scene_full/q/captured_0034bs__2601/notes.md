# q 2601 – length of the pencil bag (cm)

The file is 24 fps and question_fps is also 24. The bag does not move (frames 0–48), so the time doesn't matter.

## Pixel measurement (profile.py)
I sampled saturation along the bag's image axis (−24°, rising to the right) and took the half-max edges, on frames 3, 10, 18, 29 and 45.
Every frame gives the same ends: (649.5, 376.4) and (737.2, 337.4), so the **silhouette length is 96–97 px** and the visible width is about 23 px.
The overlay frames/prof.png matches the ends of the bag. The scene record's ~99 px is close to this.

## Why I did not use the method card directly
- Card route: 97 px × 1.05 m / 763 = **13.3 cm**. But the same route gives the tennis ball 31 px × 0.706 / 763 = 3.0 cm, and the prior says 6.7 cm. Under the card's f, the prior is off by a factor of 2.2.
- depth_info does not match this view. It gives tennis balls (0.71/0.78 m) < soccer ball (0.894) < bag (1.05).
  In this view, though, the camera is in front of and above the table. The tennis balls are at the back corners, the soccer ball is in the middle and the bag is
  in front, so the order should be the reverse. The depths look like they come from a camera on the other side of the table.
- If I scale with the depth_info ratio bag/ball (1.05/0.74) anyway, I get about 29.5 cm. I rejected this because it uses the wrong view.
- So I took the metric scale from the prior (tennis ball = 6.7 cm, about 30.5 px; ball fits from the scene record), and the relative depth from this view's own perspective.

## Geometry used (length3d.py)
- On the table plane, 1/Z is linear in the image row. I calibrated this from the table's top edge (337 px wide at v≈245) and its front edge (419 px at v≈423).
- The scale constant comes from the two static tennis balls (A d=30.9 px at v=288, B d=30.0 px at v=257). Each gives Z = f·0.067/d, and they agree within 1%.
- I back-projected the bag's two ends onto that plane and took the 3D distance. The bag's axis is about as high above the table as the ball centres.
  - f = 763 (card): Z at the bag ≈ 1.51 m, ends at 1.48 and 1.55 m → **20.7 cm**
  - f = 345 (the f that makes depth_info match the ball sizes): **19.7 cm**
  - Same scale with no foreshortening: 19.0 cm.
- Check with the soccer ball: 105 px at Z≈1.5 m with f=763 gives a 20.6 cm diameter, which is a standard size-4/5 ball. So the scale model is consistent.
- Upper bound: if I ignore perspective and use the ball scale at the bag (0.067/30.5 m/px), I get 21.3 cm flat, about 23 cm after foreshortening.

## Answer
**20.5 cm.** The plausible range is about 19.5–23 cm.
Confidence is moderate. The main risk is that the reference follows the card convention (13.3 cm) instead of the ruler value.
