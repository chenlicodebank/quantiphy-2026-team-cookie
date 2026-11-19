# q_608 — width of the white sofa (m)

Prior: speed of the black cat = 0.94 m/s. (In scene/ the cat is called a "dog". It is the only moving black animal.)
This is a 2D top-down scene. fps = question_fps = 24, so no re-timing.

## Scale
- Cat pixel speed: linear-fit slopes of torso_cx / nose_x / mask_cx are 10.991 / 10.995 / 10.997 px/frame. The
  mean per-frame dx is 11.02–11.09. I used 11.0 px/frame × 24 = 264 px/s.
- Scale = 0.94 / 264 = 0.003561 m/px.

## Sofa (measure.py, frame 49, blurred-grey edge profiles)
- Left edge x = 565.5, right edge x = 1451.5, so the x-extent is 886 px.
- Top edge of the arm ends y = 518.5, bottom edge y = 995.5, so the y-extent is 477 px.
- These match the scene/ record (888 × 484 px, ±6 px).
- Width = the shorter horizontal extent (front-to-back depth of the curved sofa) = 477 px × 0.003561 = **1.70 m**.
  The length would be 886 px, which is 3.15 m.

## Checks
- Second route: using the scene/ box (484 px) and the mean per-frame dx (11.05 px/frame) gives 484 × 0.94 / (11.05 × 24) = 1.72 m.
  That is within 1% of the main answer.
- Sanity: a 3.15 m × 1.70 m curved sofa is plausible.
- Caveat: the sofa's top outline is above the floor and closer to the camera than the cat's origin. I could not
  correct for that perspective, because the camera height is unknown. It may make the pixel size a few percent too large.

Confidence: moderate to high (about ±5%).
