# Q1515 – average speed of the rocket (m/s)

Prior: rocket length 2.9 m. depth_info: 43.064 m at t=0 (frame 0, rocket still in its tube), 41.127 m at t=0.5 s (frame 12).
question_fps = file fps = 24. 3D scene, static camera (see scene/notes.md).

## Data
I used the image origins from scene/tracks/missile.csv (frames 3-33): the nose/tail midpoint for frames 13-30, nose - L/2 for 3-12, and tail + L/2 for 31-33.
I checked frames 0 and 13 on zoomed gridded crops. At frame 13 the nose is at about (1170, 577) and the tail at about (1272, 690), which agrees with the record. The rocket comes out of the upper-right tube (mouth about (1285, 710)).

## Method (solve3d.py, grid.py, refine.py, final.py)
- Pinhole camera with the principal point at the image centre and focal length f unknown. The rocket moves on a straight 3D line along its own axis.
  That line must lie in the plane through the camera centre and the straight image flight line, so its direction is one angle th inside that plane.
- P12 = 41.127 m times the ray through the frame-12 origin. P0 is the point on the line with |P0| = 43.064 m.
  Each frame's origin pixel is mapped to the closest point on the 3D line, giving lambda(n), the metres travelled along the line.
- For each f, th is chosen so that the projected 2.9 m rocket matches the measured apparent length over frames 13-30.
  The apparent length grows from 145 to 213 px because the rocket comes toward the camera and turns more side-on.
- Best fit: f ≈ 2600-2700 px, length rms 4.1 px. The fitted model reproduces the growth (146 → 165 → 209 px at frames 13, 20, 30, against 145, 160, 213 observed).
  - Independent check 1: at f = 2600 the projected P0 falls at s = -521 px, exactly where the record puts the origin with the nose flush at the tube mouth (-522).
  - Independent check 2: the depth ratio of frames 13 to 30 is 1.19. The blur-free width ratio is 1.14-1.17, which points to f ≈ 2500.
  - So f is taken as 2600 ± 100.
- Average speed = mean of the per-frame speeds for frames 1-34 = (lambda(34) - lambda(0)) × 24/34, because the path is straight and monotonic.
  lambda(34) comes from a quadratic fit to frames 13-33 or 18-33, extrapolated by one frame; the rocket leaves the image at frame 34.

## Results
| f (px) | lambda0 (m) | lambda34 (m) | average speed (m/s) |
|---|---|---|---|
| 2500 | -3.21 | 16.44 | 13.87 |
| 2600 | -2.97 | 16.21-16.27 | 13.54-13.58 |
| 2700 | -2.79 | 16.06 | 13.31 |

Alternative interval: the mean over only frames 1-33 (the visible span) is 13.3 m/s at f = 2600.
The speed at the end is about 21 m/s, and the rocket accelerates throughout.

**Answer: 13.55 m/s.** Uncertainty is about ±3 %, driven by f. The choice of averaging interval adds about ±2 %.
