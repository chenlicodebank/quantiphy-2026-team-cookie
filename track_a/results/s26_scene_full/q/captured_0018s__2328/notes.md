# q2328 – distance tennis ball ↔ soccer ball at 3.0 s (cm)

**Main issue:** the clip has 49 frames (0–2.0 s at 24 fps; the question also uses 24 fps). The question asks about
3.0 s, which is frame 72 and is not in the file, so I extrapolated the positions from the motion in frames 37–48.
This makes the answer much less certain.

Camera: f = 0.5959·1280 = 763 px, principal point (640, 360).

## Depths
- Soccer ball: depth_info gives 2.80 m (Euclidean), so Z ≈ 2.71 m.
- Tennis (green) ball: no depth was given. I estimated it three ways:
  1. Size: a standard 6.7 cm ball spans 21–23 px, which gives Z ≈ 2.22–2.40 m.
  2. Floor row: I fitted a ground plane through the far person's feet (v≈570, Z≈2.97 from 3.13 m), the near person's
     feet (v≈690, Z≈1.82 from 2.00 m) and the soccer ball's floor contact (bottom 577 at Z 2.71). This puts the
     horizon at v≈380 and the camera ≈0.72 m above the floor. The tennis ball's floor contact (bottom ≈616–620) then
     gives Z ≈ 2.29–2.33 m.
  3. Gravity, using the ratio of pixel accelerations against the soccer ball: about 2.1–2.6 m. This is noisy.
  - I used Z_t = 2.3 m.

## Motion and extrapolation to frame 72 (fit_g.py, bounce.py)
- Tennis ball: first floor impact at about f35.8, apex at f44.9, restitution about 0.67. Later impacts at about f66
  and f74, so at f72 it is in a small hop (≤0.14 m). Its x drifts by −0.2 px/frame, so x ≈ 742 at f72.
- Soccer ball: first floor impact at about f39.7, apex at f48.7, restitution about 0.6–0.7. At f72 it is near the
  floor (≤0.1 m). After the bounce its x drifts by **+2.1 px/frame** (spin/roll toward the tennis ball). I assumed
  this mostly continues, giving x ≈ 580–603 at f72.
- Vertical positions: the centres are near the floor plus about half a hop. The vertical gap matters little
  (about 3 cm).

## Result (final.py)
| Soccer x at f72 | Distance (Z_t = 2.3 m) |
|---|---|
| 597 px | 62 cm |
| 580 px | 67 cm |
| 551 px (no drift) | 74 cm |

Changing Z_t by ±0.1 m shifts the result by about ±5 cm.

**Answer: 64 cm.**

Confidence: low to moderate. The uncertainty comes from extrapolating beyond the end of the clip (soccer ball
drift) and from the tennis ball's depth, which was not given.
