# Q1195: speed of the moving bicycle at 1.0 s (m/s)

The video and the question both use 33 fps, so t=1 s is frame 33 and t=2 s is frame 66. The camera is static.

## Method
- **Focal length from the walker.** The prior gives the walker's height as 1.8 m. His pixel height is 198.2 px at f33
  and 212.3 px at f66 (scene record, which I checked on a 4x crop). His depth is 11.926 m at f33 and 10.8165 m at f66.
  I converted each Euclidean depth to optical-axis z with the pixel ray (principal point at the image centre) and then
  used f = h_px * z / 1.8. This gives f = 1182 px at f33 and 1148 px at f66, so I used f ≈ 1165 px (range 1150–1180).
  `focal.py`
- **Where the bike's origin is.** The bike's apparent scale grows between f33 and f66 by a factor of 1.35–1.44
  (width, height and head-to-handlebar measures). The given depth ratio is 16.49/11.93 = 1.38, with a z ratio of about
  1.41. These agree, so the bike origin is on the visible bike and not offset from it. On this measure the bike and
  rider asset is large (about 2.7 m tall), but the given depths set the scale anyway.
- **Constant velocity.** A projective trajectory fit to the chest, hip and ground-contact tracks finds an acceleration
  term of about 0 (`trajfit.py`). So the speed at 1.0 s equals the mean speed over 1–2 s.
- **Speed from two rays.** P1 = 16.4919 · ray(p33) and P2 = 11.9277 · ray(p66), and the speed is |P2 − P1| / 1 s.
  - p33 and p66 come from the tracked chest point, which I checked on frames 33 and 66: (1726, 396.4) and
    (1712.5, 592.1).
  - Each candidate origin point is offset below the chest. The offset is scaled by k = 1.38–1.44 at f66.
  - Results (`speed2.py`):

    | Origin point | Speed (m/s) |
    |---|---|
    | handlebar / hip | 5.01 |
    | wheel hub / bike centre | 5.15 |
    | ground contact | 5.22 |

  - Changing f across 1150–1180 or k across 1.38–1.44 moves these by less than ±0.5%.
- **Answer: 5.15 m/s.** This takes the bike centre (wheel-hub height) as the origin, which is the middle of the range.

## Second route
- **Street vanishing point.** I used the street-direction vanishing point from the scene record, (1771, −177), as
  the motion direction and solved |P1 + sD| = d2. This gives 5.1–5.6 m/s. The vanishing point is extrapolated about
  600 px above the image, so it is less reliable.
- **Chest-track fit.** The constant-velocity projective fit of the chest track gives 4.89 m/s. This fit constrains the
  depth rate only weakly.
- Both routes are consistent with the main result to within about 5–8%.

## Confidence
Moderate. The main uncertainty is where the bike's origin sits on its height, which gives ±2%. The two-ray result is
insensitive to the focal length.
