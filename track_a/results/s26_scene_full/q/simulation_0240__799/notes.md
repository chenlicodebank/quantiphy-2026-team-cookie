# q_799 — height of the horse at the back

- "Horse at the back" = the chestnut horse (trailing, on the left; its hooves are also slightly higher in the image,
  y≈1048 vs 1055, so it's a little farther away too). The scene is 2D with a static camera, so one m/px scale.
- fps = question_fps = 24, so no re-timing.
- Pixel speed (speed.py, scene/tracks/chestnut_horse.csv, frames 0-48; frame 49 is a loop reset and is left out):
  linear fit of mask_cx 3.241 px/frame; the phase-matched displacement over one gait period (lag 39) 3.242
  px/frame; bbox edges 3.22-3.28. Used 3.24 px/frame = 77.8 px/s.
  (The record's mean step 3.154 is an endpoint difference that depends on the gait phase, so I didn't use it.)
- Scale = 0.874 / 77.8 = 0.01123 m/px.
- Height in pixels: the bbox runs from the ear tip at y≈882-885 (checked visually at t=1.0; the head renders as
  faint grey-brown) to the hoof bottom at y≈1048. The median height_px over the clip is 166 (range 159-169).
- Height = 166 × 0.01123 = 1.865 m.
- Cross-check: using the bbox_cx slope (3.26) gives 1.85 m. Using the record's endpoint step gives 1.92 m.
  A horse 1.86 m tall to the ear tips with the head up is plausible.
- Confidence: moderate-high (±4%). The main uncertainty is the speed definition and gait noise.
