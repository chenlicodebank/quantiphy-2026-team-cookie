# q_1762: average speed of the yellow car (taxi), in m/s

**Answer: 4.1 m/s.** The likely range is 3.9 to 4.25 m/s.

- The video is a 3D Blender render (segmentation version).
- The file rate and question_fps are both 24, so frame i is at t = i/24.
- The depth_info times map to frames: t = 0.58 s is frame 14 and t = 1.58 s is frame 38.
- The yellow car is the taxi (`scene/tracks/taxi.csv`). I checked that the record's mask follows the taxi in all 72 frames.
- The taxi is stationary from frame 0 to frame 1. It then moves at roughly 4 m/s, first toward the camera, then turning left, ending side-on.
- Average speed means the mean of the 71 per-frame speeds (frames 1 to 71), which equals the path length divided by 71/24 s.

## Focal length (unknown; estimated three ways)
1. **Van acceleration.** The prior says the white van accelerates at 4 m/s².
   - The van's image track shows it starting from rest at about frame 1.
   - So its displacement from frame 14 to 38 should be 2·((37/24)² − (13/24)²) = 4.167 m.
   - Back-projecting the van's centroid at the given depths reproduces this when f ≈ 978 px.
   - This depends on the start frame: a start at frame 0.5 to 1.5 gives f between 905 and 1068 (`focal.py`, `focal2.py`).
2. **Perpendicular roads (vanishing points).**
   - The van's road vanishes at about (575, 55) px. The van and cyclist tracks, the van's wheel line at frame 71, and the 3D direction from the given depths all agree on this; that last one barely depends on f.
   - The cross direction comes from the wheel-centre lines of the parked purple sedan, the taxi at frame 71 and the green sedan.
   - Assuming the two roads are at right angles, f is between 890 and 990 px (`vp.py`, `vpcheck.py`).
3. **Box-model fit.** Fitting the taxi as a 3D box with a free ground plane gives a horizon tilt of about 136 → 42 px across the frame. This matches the line through the two vanishing points.

I used **f ≈ 970 px** (horizontal field of view about 96°).

## Taxi trajectory
- **Route A: depth points only.** I back-projected the taxi's centroid at frames 14 and 38 using the given depths, which are exact. The straight-line distance between them is 4.21 m (f = 930: 4.28 m; f = 1000: 4.16 m). The taxi turns about 40° in this window, so the arc is roughly 4.30 m. At constant speed from frame 1 that gives an average of about 4.24 m/s.
- **Route B: ground plane.** I intersected the centroid ray in every frame with a plane through the taxi's two depth points. This gives an average of 3.87 m/s, but only 3.78 m between frames 14 and 38, which disagrees with the given depths.
  - This method is sensitive to vertical pixel errors: about 0.07 m of range per pixel. The same method puts the van at 4.44 m instead of the 4.167 m the prior implies.
  - So this route has errors of roughly ±10% per object, and I gave it less weight.
- **Route C: 3D box fit.** I fitted a box (length, width, height) for the taxi with its ground position and heading in every frame. The ground plane was free, and the fit was forced to reproduce both given depths exactly. The bounding-box error is 0.67 px (`boxfit2.py`).
  - The fitted car length is 5.0 m. The width is degenerate at 0.75 m, so the box shape is unreliable, but the positions fit well.
  - Results by focal length:

    | f (px) | Average speed (smoothed / raw), m/s | Frames 14→38 distance, m |
    |---|---|---|
    | 930 | 4.12 / 4.19 | 4.18 |
    | 970 | 4.03 / 4.09 | 4.11 |
    | 1000 | 3.97 / 4.03 | 4.07 |

## Conclusion
Route C (about 4.06 at f = 970) is the main estimate. Route A suggests about 4.24 and route B about 3.87.

**Answer: 4.1 m/s.** Confidence is moderate, about ±6%. The main uncertainties are the focal length and how far the mask centroid sits from the taxi's true centre point.
