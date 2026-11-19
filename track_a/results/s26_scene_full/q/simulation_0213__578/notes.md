# q_578 — height of the vase (m)

Prior: black cat speed = 0.94 m/s. No depth_info. fps = question_fps = 24, so no re-timing.

## Scale from the cat
- Fitted the cat track (scene/tracks/cat.csv, visible frames 0-22 and 44-49; catspeed.py): nose bbox_x1 moves at 17.76-17.80 px/frame
  (rms 0.7 px); centroid_x gives 17.81 and bbox_cx 17.71. I used 17.78 px/frame = 426.7 px/s.
- That gives 0.94 / 426.7 = 0.002203 m/px **in the cat's walking lane** (paws at y≈1020).

## Vase pixel height (profile.py, vase_bottom.py, frame 48; the vase does not move)
- Top: the rim highlight starts at y≈573.5. Bottom: where the vase meets the orange tabletop, y≈791.5 at the centre and ≈789-790 at the sides.
- Pixel extent ≈ 218. Subtracting about 2-3 px for the near half of the base ellipse leaves **≈216 px** (the scene record says 214).

## Depth correction (the vase is behind the cat's lane)
- The floor lines are horizontal, so the camera has no roll or yaw. The lamp-shade bottom rim curves down by about 3.5 px over a 108 px half-width,
  so the camera is a little above the rim. That fits a level camera with the horizon at y≈540-555.
- With the horizon at y≈540, a floor point's depth is ∝ 1/(y - y_h):
  - Table front feet y≈992, front edge of the tabletop y≈808, back edge y≈782. The centre of the vase base is at y≈789, in the back part of the top.
  - Z_front/Z_cat = (1020-540)/(992-540) = 1.06. Z_vase/Z_front = (808-540)/(789-540) = 1.076. So **Z_vase/Z_cat ≈ 1.14**.
  - This ratio barely depends on the horizon (1.12 at y_h=500, 1.15 at y_h=555).
  - Check: the table height comes out at 0.41 × the camera height. With the camera height from the cat scale (≈1.06 m), the table is ≈0.43 m tall, a plausible side table.
  - The record's 2D label ignores this, but the cat and the vase are visibly at different depths.

## Result
- Uncorrected (single 2D scale): 216 × 0.002203 = 0.476 m.
- Depth-corrected: 0.476 × 1.14 = 0.54 m.
- Answer: **0.535 m**, the corrected value shaded slightly toward the 2D value because the horizon row is uncertain.
- Second route: the pixel height (216 vs 214 in the record) and the scale (nose, centroid, box-centre fits) agree within ~1%.
  The main uncertainty is the depth ratio, 1.12-1.15 for any plausible horizon.

Confidence: moderate. ±4% if the perspective model is right; if the reference used the flat 2D scale, the answer is ~12% high.
