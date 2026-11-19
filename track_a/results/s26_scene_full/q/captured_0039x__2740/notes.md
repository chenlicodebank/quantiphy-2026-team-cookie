# q_2740 — height of the pink bottle (cm)

Lab video, 1280x720, 24 fps (the file rate is the same as question_fps). Camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).
Given distance from the camera to the pink bottle = 0.9998 m (the bottle is static).

## Pixel measurement (measure.py, edges.py; frames 0, 24, 48 all identical)
- Top edge of the silhouette: the first bright pixel is y = 330 for x = 655–679, so the edge is at about 329.5. Its corners
  are rounded, and that rounding comes from the cap's shape, not perspective (the top is almost at eye level).
- Base: the bottle's bottom outline curves from 475 (x = 643) to 477 (x = 655–658), and a dark contact shadow sits at
  y 477–479. The centre column is hidden by the leaning card. Extrapolating along the ellipse puts the base edge at the
  centre at about 477.5.
- Vertical silhouette extent ≈ 148 px (the scene record gave 146, using the visible base at the left side).
- Width ≈ 48 px (x 642–690), so the radius is about 3.1 cm.

## Scale check with the prior
- The credit card (dark blue card) is about 100 px long at distance 0.6867 m. Using Z (the distance projected onto the
  optical axis), 100*0.668/762.8 = 8.76 cm, against the prior's 8.56 cm (+2%). This confirms the focal length.

## Height
- Simple method card: 0.9998 * 148 / 762.8 = 19.4 cm (19.36 cm using Z instead of the Euclidean distance).
- Cylinder model (geom.py): the bottom silhouette edge is the front point of the base ellipse, which lies about
  4–5 px below the axis's foot at this viewing angle (the cup's rim ellipse suggests a camera pitch of a few degrees).
  The axial height that reproduces the 329.5–477.5 silhouette is 18.6–18.8 cm for pitches of 0–6°.
- The answer lies between these two routes: **18.9 cm**. This is within about 3% of both. The true value depends on how
  rounded the base edge is.

Confidence: moderate-high (±4%).
