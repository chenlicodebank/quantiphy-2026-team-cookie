# q_708: height of the swimming ring (pink flamingo float), in m

Prior: the black cat's speed is 1.041 m/s. There is no depth_info. The file runs at 24 fps and question_fps is also 24, so there is no re-timing.

## Scale from the cat
- The cat's body centroid (scene/tracks/cat.csv, body_cx) moves 5.378 px/frame net over frames 0–49. The mean of the per-frame steps is 5.51, which includes gait jitter.
- s_cat = 5.378 × 24 / 1.041 = **124.0 px/m** at the cat's depth. The paws touch the deck at y ≈ 918.5.

## Perspective correction (the float is closer than the cat)
- The camera is level. The deck tile joints converge at about (930–960, 540 ± 30), so the horizon is at v_h ≈ 540, the image centre (my read of three joints on deckR.png; vp.py found only two segments). The house verticals are vertical.
- On a ground plane, the pixel scale is s = (v − v_h) / H, where H is the camera's height above that plane:
  - At the cat: s = 378.5 / H_c.
- The pool water sits below the deck by δ:
  - The deck edge is at y ≈ 926, the dark joint line in profile.py.
  - The water meets the wall at y ≈ 960–965, where frame-to-frame change starts (texture.py).
  - δ / H_c = 32–37 / 388 ≈ 0.08–0.095, which is about 0.25 m.
- The float's water-level centre is at y ≈ 1005. This comes from a torus model: the front waterline is at 1016, the hole/tube contours give sinθ ≈ 0.15, R ≈ 57 px and r ≈ 20 px, and the tube is about 4 px submerged.
- s_float = s_cat × (1005 − 540) / (378.5 × (1 + δ/H_c)) ≈ 124.0 × 1.13 ≈ **140.7 px/m**. The ratio varies by only about ±1% for v_h between 510 and 570.

## Float's pixel height
- Head top: y = 887 (frame 0, clean ref box; it stays the same in every frame, checked at frame 49).
- Visible waterline: about 1016–1018. That gives 130–132 px above the water.
- Vertical extent of the 3D bounding box:
  - Head height above the water-level centre: (1005.7 − 887) / cos 8.6° ≈ 120 px.
  - Plus the submerged tube bottom, about 4 px.
  - Total ≈ **124 px**, with a range of about 118–130.

## Answer
Height = 124 / 140.7 ≈ **0.88 m**.

## Second-route check
Using the naive single 2D scale (no depth correction), the height would be 132 / 124 = 1.065 m. The perspective evidence makes this an overestimate:
- The horizon is at about 540.
- The float's waterline is about 87 px lower in the image than the cat's paws.
- The water is only slightly below the deck.

The model is self-consistent:
- Ring width: 159 px / 140.7 = 1.13 m.
- The cat stands about 0.5 m behind the coping edge, and the float centre is about 1.2 m in front of the wall.

Without the water drop (δ = 0) the height would be about 0.82 m, and with a larger drop about 0.90 m.

Confidence: moderate, about ±8%. The main uncertainties are the water-drop estimate and the head's depth offset.
