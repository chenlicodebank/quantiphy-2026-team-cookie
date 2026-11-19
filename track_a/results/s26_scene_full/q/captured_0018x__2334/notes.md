# q_2334 — length of the box (cm), captured_0018x (lab video, 24 fps; file fps = question fps = 24)

Prior (gravity 9.8) gives no scale. The scale comes from depth_info and the lab focal length f = 0.5959 x 1280 = 763 px.

## Depth of the box
depth_info has no entry for the box. The box (white carton) is held by the far (left) person in her left hand. It sits right
beside the soccer ball (ball at 2.80 m), at the same image height (box cy 266, ball cy 265) and with the same pose of both arms.
I therefore take Z_box = 2.80 m.
Check: I fitted a floor-contact row model to the left person's feet (row 577 at 3.13 m), using a level camera with cy = 360
(camera height about 0.89 m). In that model the box's floor contact row (about 602-609) gives Z of about 2.75-2.8 m, which is consistent.

## Pixel length (long axis of the box)
- Route 1, frame 0 (held still and upright, top edge visible, fingers only at the side). measure_box.py prints the
  row-by-row mask. The box spans rows 240-293, so it is **54 px** long (and about 21-22 px wide).
- Route 2, free fall, frames 32-38. Fitted L_obs = L0 + k*v (motion blur), leaving out the dropped-frame anomaly
  at 35->36. Result: k = 0.66 and **L0 = 55.6 px**.
- Route 3, lying on the floor, frame 48 (measure_lying.py, minAreaRect). It measures 61.3 px while sliding left at 9.5 px/frame.
  Removing the blur (61.3 - 0.66 x 9.5) gives **55.0 px**. The top face is also visible, so the foreshortening is small.

## Result
These routes give a pixel length of 54-55.6 px, about 55 px.
Length = 2.80 x 55 / 763 = 0.202 m. Route 1 alone gives 19.8 cm and route 2 gives 20.4 cm.
If I use the depth along the optical axis instead of the radial depth (factor 1.029 off-axis), the result is about 19.6 cm.
**Answer: 20.0 cm.**
Confidence: moderate, about ±5%. The main uncertainties are the assumed box depth (no depth is given for the box) and blur and edge softness.
