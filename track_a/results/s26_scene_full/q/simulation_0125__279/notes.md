# q279 — house height (m)

Clip type: 2D, with a static camera and a frontal view. fps = question_fps = 24, so no re-timing.

## Scale from the prior (person's speed = 1.22 m/s)
- Source: scene/tracks/man.csv (pelvis_x_smooth, frames 0-70). The man walks horizontally the whole clip.
- Line fit of pelvis x gives 133.8 px/s. Line fit of centroid x gives 134.1 px/s. The mean of the per-frame smoothed steps is 136.2 px/s, which is inflated a little by jitter.
- I used 134 px/s, so the scale is 1.22 / 134 = 0.00910 m/px.
- Sanity check: the man is about 220 px tall, which comes to 2.0 m. That is plausible but tall. It suggests the person stands slightly behind the facade plane, since he walks inside the recessed porch.

## House pixel height (prof.py, column intensity profiles on frame 0)
- The roof apex edge is at y = 27.5, from the column at x = 536.
- The bottom of the house body (black frame/wall) is at y ≈ 910. It is the same at x = 165, 180, 540 and 900.
- Below that is the deck/platform: the top surface runs 910-950 and the front face 950-966.
- House body: 882.5 px, which gives **8.03 m**.
- If the deck counts as part of the house: 938 px, which gives 8.54 m.

## Answer
8.0 m (house body, from apex to the base of the wall). The deck is treated as a separate object.

## Check and confidence
- Using the mean per-frame speed (136 px/s) instead gives 7.9 m. Using the line fit gives 8.03 m.
- Confidence is moderate. The main uncertainties are whether the deck belongs to the house, and the small depth offset between the person and the facade.
