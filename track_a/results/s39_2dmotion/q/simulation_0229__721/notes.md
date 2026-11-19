# q_721: acceleration of the paper airplane at t = 1 s (m/s^2)

Prior: the chalkboard is 5 m long. 2D video. question_fps = file fps = 24, so t = 1 s is frame 24.
Convention: a(24) = (speed(24) - speed(23)) x fps, where speed is the backward difference of the origin.

## Plane position (my_track.py -> my_track.json)
- Background = per-pixel median of frames 0-5 and 44-49. Mask = max RGB difference above a threshold
  (12/20/30); the plane's position is the centre of the mask's bounding box. The plane flies in a constant-depth
  plane (its length stays about 135-141 px).
- The scene record's ref point matches mine to about 1 px, except at **frame 22**: the record has x = 953.3,
  I measured 958.5. A zoomed crop of frame 22 shows the plane spans x ≈ 893-1023, which puts the centre at 958, so
  the record is wrong there. Its raw acceleration at frame 24 (74.0 -> 69.0 px/f) is therefore noise.
- SAM 3 "paper airplane" mask at frame 24: box centre (1098.2, 343.0), length 139 px. My bbox centre is
  (1097.5, 342.0), length 138 px. They agree to well under 3%.

## Speed and acceleration (accel.py)
- Per-frame speeds in px/frame (thr 20): f20 75.8, f21 74.1, f22 73.0, f23 69.6, f24 69.5, f25 67.2,
  f26 66.6, f27 66.1, f28 63.2. The speed is flat at about 76 up to frame 20, then falls.
- The raw one-frame difference is noisy (-1.6 to +0.9 px/f^2 depending on threshold), so I used the local slope
  of the speed:
  - Linear fits of speed over windows ±3 to ±5 frames around frame 24: -1.40 to -1.54 px/f^2.
  - A second route, polynomial fits of x(t) and y(t) (degree 4-5, frames 15-32) differenced by the convention:
    -1.57 to -1.72 px/f^2.
  - A wider window (±8): -1.24 px/f^2. The deceleration is strongest around frames 21-25.
- Adopted value: -1.45 ± 0.15 px/f^2 = -835 px/s^2.

## Scale (board_edges.py, SAM)
- Measured with row gradients at frame 24: the green surface runs x = 341.5 to 1670.5 (1329 px), and the outer
  wooden frame from about 321 to 1690 (about 1370 px). The record says 1372.
- The SAM "chalkboard" mask box is 325-1690 (1365 px), within 0.4% of mine. Its left side is eaten by the light
  beam (I checked the overlay), so I used my own gradient edges.
- I took the whole object, including the frame: 1370 px = 5 m, so 0.00365 m/px. If the green surface alone is
  5 m (1329 px), the result would be 3% higher, about 3.15-3.2.

## Result
a ≈ -835 px/s^2 x 0.00365 m/px = -3.05 m/s^2. The plane is decelerating; I give the magnitude, **3.1 m/s^2**.
Confidence: moderate. The speed slope has about ±10% uncertainty, and the motion is not uniformly accelerated.
