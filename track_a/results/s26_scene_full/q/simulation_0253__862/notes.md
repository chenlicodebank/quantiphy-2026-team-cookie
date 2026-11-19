# Q862 – acceleration of the box at t = 1.75 s (m/s²)

Prior: box width (side parallel to the slope) = 0.611 m. No depth_info. fps = question_fps = 24, so no re-timing.
t = 1.75 s → frame 42.

## Track
I used scene/tracks/box.csv (centroid projected on the path, `s_along_path_px`) for frames 15–44, the frames where
the box is fully in view. Frame 27 holds the frame-28 image (dropped frame then repeated: the 26→27 step is two
steps long), so I left frame 27 out and kept frame 28 at t = 28/24.

## Key finding: this is not a pure 2D view, because the slope recedes from the camera
- The pixel acceleration is not constant: about 935 px/s² over frames 15–26 and about 650 px/s² over frames 33–44.
  A quadratic leaves 2.0 px rms residuals.
- End-face visibility (rectified crops, `rectify.py`, `edges.py`): the downhill end face shows early and the uphill
  end face shows late. Both are edge-on at path s≈452 px, about 280 px uphill of the image-centre projection
  (s≈733). So the slope direction is tilted in depth, with the downhill end farther from the camera.
- Ramp band in frame 0 (`band.py`): the perpendicular width falls steadily from 49.7 px to 46.8 px going downhill,
  so the edges converge toward a vanishing point about 19,800 px down the path. The scene record's edge fit said the
  band widened; that came from its noisy upper-edge fit and is wrong.
- The front-face height (across the slope, `vert.py`, `vprof.py`) shrinks by about 7% from early frames to late
  frames.

## Model
A straight 3D line projects with a Möbius map: s(t) = α + X/(1+gX), with X(t) = v0·t + a·t²/2 (constant world
acceleration, as for sliding with friction). The metric scale is the local magnification ds/dX at frame 28. There
the end faces are edge-on, so the silhouette's along-slope extent equals the front-face edge: **92.0 px**
(b* 50% crossings 91.8–92.7 px over frames 26–31, `length28.py`). The box origin (its centre) sits half a box depth
behind the front face, so its magnification is 1/(1+k/2) = 1/1.0155 of the front face's. Here k = 0.031 is the
end-face width per pixel of offset, from a V-shaped fit of silhouette extent against position.

## Results
- Route 1 (`persp_fit.py`, VP free): rms 0.60 px, the same as a free cubic. The fit puts the box at rest at
  t = 0.026 s, i.e. released at the start of the clip, which is physically consistent. **A = 6.14 m/s²**.
  Its predicted 1/z size change (−7%) matches the measured shrink of the box height.
- Route 2 (`route2.py`, VP fixed from the ramp-band convergence): rms 0.65 px, at rest at t = 0.006 s.
  **A = 6.02 m/s²**.
- Taking the world acceleration as constant, the per-frame convention at frame 42 gives the same value
  (6.14 in route 1).
- For comparison, the naive 2D quadratic gives 5.12 m/s². It is rejected: its residuals are 2 px, it implies a
  nonzero speed at t = 0, and it contradicts the measured perspective.

Answer: **6.07 m/s²**, the mean of the two routes. Physically plausible: on an incline of about 44°, g·sin = 6.8,
which implies μ ≈ 0.1.

Confidence: moderate-good, about ±4%. The main uncertainties are the 92 px edge length (±1%), the vanishing point
(spread between routes ±1%), and the centroid-to-origin depth factor (about 1%).
