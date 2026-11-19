# q_2604 – total distance traveled by the right tennis ball (cm)

File fps = question_fps = 24, 49 frames, 1280x720. Lab method card: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Method
- Right ball (B, starts at the back-right corner) is at rest in frames 0–24, rolls left, hits the left ball at frame 38,
  then rolls down-right (toward the camera) until the end (frame 48). Path counted from frame 24 (frames 0–23 are static;
  their ±1 px centre jitter is not real motion).
- Centres: scene record (circle fit) checked against my own re-track (`track_b.py`, HSV mask + moments). The x values agree
  to within about 1 px. My mask sits about 2–3 px lower in y at a constant offset. At frame 38 my mask merges with the left
  ball, so I used the record there.
- Back-projection: X = ((u-cx)/f, (v-cy)/f, 1)·Z, with Z = 0.776 m (depth_info, t = 1.2 s). The depth change along the path
  is small: the apparent diameter has no trend (≈30–31 px). An affine model of the diameter on the table plane gives
  Z = 0.780 → 0.773 m.
- Total distance = sum of the frame-to-frame 3D displacements (frames 24→48). This includes the double step at 35→36,
  which looks like a dropped capture frame but is still real path.

## Results
- Pixel path length (24–48): 197.1 px
- Record centres: 20.05 cm (constant Z), 20.22 cm (modelled Z)
- Own re-track: 20.51 cm (constant Z), 20.68 cm (modelled Z)
- Including the static-frame jitter from frame 0: 21.2–21.7 cm
- Answer: **20.3 cm**

## Caveat (scale inconsistency)
At f = 763 px and Z = 0.776 m the ball's 30.6 px diameter corresponds to 3.1 cm, not the prior's 6.7 cm. The soccer ball shows
the same factor of about 2 (12 cm at the given depth). Using the prior's pixel scale instead (6.7 cm / 30.6 px) would give
about 43 cm. The answer follows the paper's lab convention: back-projection with the given depth and the card focal length.
Confidence: moderate. The route-to-route spread under the lab convention is about ±2%, but the depth vs. prior scale
conflict is unresolved.
