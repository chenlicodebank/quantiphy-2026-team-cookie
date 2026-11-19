# q1197: speed of the walking person, 1.0 s to 2.0 s (frames 33 to 66 at 33 fps; the file is also 33 fps)

Answer: **1.23 m/s**

## Method
- On frames 33 and 66 (frames/p33.png, p66.png) the pedestrian (white T-shirt, right sidewalk) walks almost straight
  away from the static camera. The pelvis pixel moves only from (1160, 631) to (1142.5, 623).
- depth_info gives the human at 19.0411 m (t=1) and 20.2710 m (t=2), so the radial change is 1.2299 m in 1 s.
- The sideways and vertical motion is tiny. speed.py back-projects both pelvis points for f = 800 to 3000 px, which
  gives a 3D displacement of 1.236 to 1.307 m. That assumes the origin sits at the visible pelvis, but see below.

## Consistency check (check_offset.py)
- **Bike**: the tyre-contact rows (759 at f33, 699 at f66) agree with the bike depths for a level camera with the
  horizon at y=530. The fitted offset is 0.48 m, about the rear tyre's distance behind the bike's centre. So the bike
  depths match its pixels.
- **Pedestrian**: the shoe rows (771.4 at f33, 751.2 at f66) do NOT match 19.04 / 20.27 m as the distance to the
  body.
  - The bike's ground plane puts the pedestrian's body at Z of about 12.9 m at t=1 (an upper bound, since the
    sidewalk's height is ignored).
  - The shoe-row ratio implies a constant offset of about 5.6 m along the line of sight, which puts the body at about
    13.5 m.
  - So the human's origin is apparently offset from the mesh by a roughly constant vector and moves rigidly with the
    body. Speed is a difference of positions, so the offset cancels.
  - Because the origin is offset, the pelvis-pixel back-projection in speed.py does not apply. Its lateral terms do
    not change the answer.
- **Second route**: the body depth from the ground plane (12.9 m) times the depth-ratio growth from the image (1.091)
  gives 1.18 m/s. That is 4 % below 1.23, which fits since the sidewalk height makes 12.9 m an upper bound.
- The body moves almost purely along the line of sight. Its lateral and vertical 3D changes are under 1 cm from
  pixels, so the speed is about the depth difference: 1.23 m/s. The uncertainty is a few percent (path length if the
  origin bobs with the gait, and the unknown direction of the offset).
