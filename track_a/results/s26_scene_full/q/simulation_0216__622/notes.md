# q_622 — height of the TV stand (m)

Prior: the black cat's speed is 0.94 m/s. fps 24 = question_fps, so no re-timing.

## Cat scale
- From scene/tracks/cat.csv `body_x_matched` (the camera is static): mean 17.735 px/frame, and a linear fit gives the
  same 17.735, so the walk is steady. That is 425.6 px/s.
- s_cat = 0.94 / 425.6 = 0.0022085 m/px at the cat's depth.

## Stand in pixels (measure.py, top.py, geom.py, rail.py)
- Front-top edge of the cabinet: y = 794.5. Back-top edge: y = 776.5. The top surface is visible, so the camera is above
  the stand.
- The front floor rail touches the floor at y ≈ 990. The rear leg loop's bottom is at y ≈ 958.
- The cabinet's side edges are vertical (x = 650/651 and 1423 for rows 800–860). So the camera is level and the
  horizon is at y = 540.

## Perspective correction
On a level camera, a ground point's scale ∝ 1/(y_floor − 540).
- Depth check: the top edges give Z_back/Z_front = (794.5−540)/(776.5−540) = 1.076. That predicts the rear floor line
  at y = 958.2, and the rear leg loop is measured at about 958. The two agree, so the geometry holds.
- The cat's floor line (midway between its near and far paws) is at y ≈ 1016 (near paws 1020, far paws about 1010).
- Stand-front scale = 0.0022085 × (1016−540)/(990−540) = 0.0023361 m/px.
- Height = (990 − 794.5) × 0.0023361 = **0.457 m**.
- Second route, using the back plane: (958.2 − 776.5) px × 0.0022085 × 476/418.2 = 0.457 m.

## Sensitivity
- If the cat's floor line is anywhere from y = 1012 to 1020, the answer is 0.453–0.461 m.
- With no perspective correction (one cat scale applied to 196–214 px), the answer would be 0.43–0.47 m.
- The camera height implied by the scale is about 1.06 m. A 0.46 m stand and a 0.54 m nose-to-rump cat are both
  plausible sizes.

Confidence: good, about ±3%.
