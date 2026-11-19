# q_2338 — height of the yellow toy (cm)

Object: yellow plush with dark-green leaves on top, held in the hand of the near (right) person and dropped at frame 28.
Its depth is taken as distance_near_person_camera = 2.002 m (from depth_info). Camera: f = 0.5959 x 1280 = 763 px.
File fps = question_fps = 24.

## Pixel height (measure_plush.py: yellow + green colour mask, bbox and PCA extents; crops.py for visual checks)
- Held upright, frames 0-27 (leaf tip to body bottom): bbox height 54-59 px, PCA major 56-59 px; visually f0 y 220 -> 277 = 57 px.
- Free and upright after the bounce, frames 41-42 (no hand, little blur): bbox height 53-55 px, PCA major 54-56 px.
- Fall frames 29-38 are motion-blurred (64-77 px), so I didn't use them.
- Adopted value: 56 px (range 54-58).

## Size
H = 2.002 m x 56 / 763 = 0.147 m = 14.7 cm (range 14.2-15.2 cm).

## Check (gravity_depth.py)
- I fitted a parabola to the plush's free fall over frames 29/30-35, before the dropped-frame jump at 35->36.
  It gives a_px of about 3510-3660 px/s^2, so Z = g f / a_px = 2.04-2.13 m. That matches the 2.002 m depth for the near person.
- The fall width (26-28 px) matches the width at frames 41-42, so the depth stays about the same. The 54-56 px heights after the bounce are therefore at about the same depth too.
- If I used the gravity-derived depth of about 2.08 m instead, the height would be 15.3 cm.

Confidence: moderate-high, within about 5 %.
