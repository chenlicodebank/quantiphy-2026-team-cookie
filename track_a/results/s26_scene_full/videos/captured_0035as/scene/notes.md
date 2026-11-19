# captured_0035as — measurement record

Lab video (real recording, 24 fps, 49 frames, 1280x720, 3D). People and balls were cut out with SAM2 and
pasted on a static synthetic blue-white gradient background (watermark bottom-right). All values are in
pixels / frames; t = frame/24. No metric scale is assumed.

## Scene
Two people kick balls toward each other. The **far person** (light-grey T-shirt, blue-grey jeans, white
sneakers; top-left, head cut off by the top border) kicks a **soccer ball** (white with black pentagons)
from her left (image-left) foot toward the camera / image right. The **near person** (dark-grey T-shirt,
black trousers, long dark hair; right edge, close to the camera, cut by right and bottom borders) holds an
orange **basketball** beside her thigh and kicks it toward the far person (up-left). The balls collide at
frame 19→20: the soccer ball bounces back to the far person, who stops it with her foot (frames 47-48);
the basketball slows sharply and rolls left. Nothing else is in the scene: floor, walls and furniture were
removed by the background replacement, so there are no static objects or ground markings.

## Files
- `scene.json`: inventory, camera, events, size summaries.
- `tracks/soccer_ball.csv`: frame, t, cx, cy (centre), bbox, mask area, major/minor axis length and angle,
  area-equivalent diameter, minimum-enclosing-circle centre/diameter, `manual` flag, occluded.
- `tracks/basketball.csv`: same columns plus `fit_cx, fit_cy, fit_diam` (circle fitted only to the edge
  bordering background) and `edge_bg_frac` (fraction of the outline bordering background).
- `tracks/far_person.csv`, `tracks/near_person.csv`: centroid of the visible mask, bbox, area, principal
  axes. Both persons are truncated by image borders, so the centroids are of the visible parts only.
- `scripts/`: bgcheck.py (median background), cleanbg.py (cleans person remnants from it), soccer.py
  (+ soccer_manual.py), track.py (basketball, persons), tracksheet.py / zoomsheet.py / viewframes.py
  (visual checks), steps.py (per-frame displacements), summarize.py.

## Method and reliability
- **Camera**: static. The background pixels are identical in every frame (std 0.7 grey levels). Following
  the benchmark convention, use f = 762.8 px, principal point (640, 360). Perspective: elevated view onto
  an invisible floor; image y increases toward the camera. The only depth cues are the ball sizes.
- **Soccer ball**: foreground = |frame − clean background| > 14 minus orange pixels, tracked backward from
  frame 48. Frames 12-46 are automatic; the ±1 px centre was checked on contact sheets.
  Frames 0-11 and 47-48 are manual circles read off 4x zooms because the ball touches a shoe there:
  0-4 at rest (±1 px; the top is hidden by the right shoe), 5-8 blurred and merged with the kicking shoe
  (centre = leading edge minus one radius, ±4 px), 9-11 blurred blob (±3 px), 47-48 clear (±1.5 px).
  Diameter: 46 px at rest, 43-46 px at the end (same depth, near the far person's feet), largest ~52-55 px
  around frames 15-22. Frames 5-19 have strong motion blur: the major axis (60-64) includes blur, so use
  `wid_minor` for the true diameter there.
- **Basketball**: HSV orange mask; `fit_*` is the circle fitted to the background-bordering edge. In frames
  0-11 the ball is partly hidden by the near person's thigh and hand, then by her kicking foot. There the
  fit is the better centre, though it jitters ±3 px in frames 0-7, when the ball is actually still at
  about (884, 616). The `occluded` column flags edge_bg_frac < 0.9. That threshold is conservative:
  values of 0.84-0.9 after frame 22 come from blurred edges, not occlusion. Genuine occlusion or contact is
  limited to frames 0-11 (leg, hand, foot) and 19-21 (touching the soccer ball). Diameter: 82-84 px while
  held (closest), 73-75 px at frames 12-16, 69-70 px from frame 17 on.
- **Persons**: foreground components minus the balls. The far person's white T-shirt and shoes are close to
  the background colour, so her mask misses some patches; her bbox is reliable to a few px and her feet are
  at bbox_y1 ≈ 311-333. The near person's mask is good, but she is cut at the right and bottom borders.
  Neither person has a measurable full height.

## Events (frame / t)
- Soccer ball at rest at the far person's foot: frames 0-4. It starts moving at frame 5 (0.208 s); the shoe
  is in contact until about frame 9.
- Basketball held still: frames 0-7. It starts moving at frame 8 (0.333 s); the foot is in contact during
  frames 8-11 and the ball is free from frame 12.
- Collision of the two balls between frames 19 and 20 (0.792→0.833 s), visibly touching in frames 19-21.
  Soccer ball per-frame step: ~19 px toward the lower right before, then reverses to ~16 px toward the upper
  left and decelerates to ~4 px/frame. Basketball: ~18 px/frame up-left before, ~5 px/frame leftward after.
- Far person's foot touches the returning soccer ball: frames 47-48 (end of clip).

## Ambiguities
- **Dropped frames**: between frames 11→12 and 35→36 both balls move about twice their normal step. One
  capture frame was probably lost at each point. The tracks keep the file's indices (t = i/24); any speed
  that uses these intervals is about doubled.
- Reference point: "visible centre" for the balls. Persons are truncated, so the person centroids are not
  body centres.
- The two balls are easy to tell apart (orange vs white). The white soccer ball resembles the far person's
  white sneakers when it touches them (frames 0-11, 47-48), which is why those frames were done by hand.
