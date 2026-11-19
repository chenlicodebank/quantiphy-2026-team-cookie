# Q1216 – height of the curb along the road (simulation_0052)

Answer: **0.19 m**

The file rate is 30.0033 fps and question_fps is 30, so frames were converted with 30.

## Curb pixel height (curb_profile.py, joint.py; frame 90)
- The far curb, between the sidewalk and the road. I took column-averaged intensity profiles at 4 column ranges
  (x 420-1060). The sidewalk's top edge is a sharp drop at row 763.4. The dark, textured curb face runs to about
  row 782, then there is a dark crease at rows 782-783.
- Below the face, rows 783-788 are a gutter strip and the white line at rows 789-790 is on the road. The vertical
  joints between curb blocks (x = 709 and x = 905) run from row 759.5 (top surface) down to row 782 and stop
  there. That confirms the face ends at about 782, not at 790. The record's "curb face 763-790" includes the
  gutter and line.
- Face height: **18.5 ± 0.7 px**. The near curb at the bottom of the image is seen from above, so its face cannot
  be measured.

## Scale
- Orange car: a quadratic fit of the hub midpoint over the measured frames 6-84 (rms 0.25 px) gives 301.3 px/s².
  With a = 2.86 m/s², the scale is z/f = 0.00949 m/px at the car's near side. Using only the two depth_info
  distances gives 0.00964 m/px, which agrees to 1.5%.
- Vertical lines converge upward (lamp poles slope +0.016 / −0.008), so the camera is pitched up a few degrees.
- camera_fit.py fits a pitched pinhole camera (f, pitch, height H) to: the orange car's distances and
  acceleration, the green/black car's distances (u from its hubs, −69.84 px/frame), and the tyre-contact rows
  (794 and 900, half-track 0.8 m). Result: f ≈ 1540-1550 px, pitch ≈ 3.7°, H ≈ 1.45 m, horizon at row ≈ 638.
- The curb's base row (782) on the road plane gives a depth of Dc ≈ 15.8 m. The top row (763.4) then gives
  **h ≈ 0.187 m**. The result barely moves with half-track 0.7-0.9 m (0.187-0.188).

## Second route (lamps and hydrant depth_info)
- Lamps and hydrant: z ≈ d / sqrt(1 + r²/f²) ≈ 17.1-17.2 m. Their bases (row 757) sit on the sidewalk about
  6 px above the curb edge. The ground-plane ratio (757 − vh) / (763.4 − vh) puts the curb at about 16.0-16.3 m.
- This gives h ≈ 18.5 × 16.0-16.3 / (1550-1600) × 0.99 ≈ 0.185-0.193 m.
- The car-based model predicts lamp distances about 3% shorter than the given values, so there is some tension
  between the references. Both routes still land within 0.185-0.195 m.

## Ambiguity and confidence
- If the gutter strip is counted as part of the curb (rows 763-790, 27 px), the height would be about 0.27 m.
  I rejected this because the block joints end at row 782.
- Confidence is moderate: about ±5% from the scale, and more if the reference counts the curb's bounding box
  differently.
