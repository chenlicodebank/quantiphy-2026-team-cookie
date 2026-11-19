# q_1585 – length of the typewriter (m)

Answer: **0.325 m**

The file rate and question_fps are both 24. The scene/ track (typewriter, frames 0-29) is correct: free fall in frames 0-9,
impact at about frame 10.3, rocking until about frame 23, then at rest.

## Scale: focal length from the gravity prior and the depths
- `fit3d.py` and `fit3d_h.py`: a 3D free-fall model, P(t) = A + ½·g·d·(t−t0)² with g = 9.8 and d = world-down in camera
  coordinates. It is fitted to the bbox-centre track (frames 2-9), with |P(0)| = 4.32 m.
- Fit with no other constraint: f = 2860 and tilt 25°. The tilt is poorly constrained this way, and the depth at landing
  comes out as 4.65 m, against the given 4.501 m.
- Fit with the camera tilt tied to the horizon (from the desk vanishing points, v ≈ −200 to −280): f = 2577-2613. This fit
  reproduces the given t = 0.5 s depth (4.51-4.53 m against 4.501 m).
- Adding the 4.501 m depth as a constraint instead gives f = 2564-2601 and tilt about 16°, which matches the horizon.
- Adopted f ≈ 2595 px (HFOV about 44°). Using the top or bottom edge of the box instead of its centre gives 2390 to 2800,
  because the box's apparent height grows during the fall. The centre is the right proxy for the origin.
- Corner-orthogonality cross-checks suggest a larger f (about 3000). They rely on rough vanishing points and
  hand-picked corners, so I used them only as an uncertainty bound.

## Size
- Route 1, rest pose, frame 26 (`rest_geom.py`): I intersected the base-corner rays with the desk-top plane. The
  plane's height comes from the revolver, at 4.704 m depth plus 1.5 cm. The base front edge (side to side) is
  W = 0.321 m and the side (front to back) is D = 0.309 m (f = 2595, horizon −240). Over f = 2400-2800 the range is
  W 0.30-0.34. As a check, the frame-12 origin lies 0.095 m above the desk, which is plausible.
- Route 2, in air, frame 4 (`air_geom.py`): the front base edge is almost parallel to the image plane, so it is a
  robust measurement. It is 195 px at about 4.27 m, giving W = 0.321 m. This agrees with route 1. The in-air pose is
  slightly tilted, so D from that frame is unreliable.
- The carriage, platen knobs and lever span about 197 px but sit further back, which gives about 0.33-0.34 m. So the
  whole side-to-side extent is about 0.32-0.34 m. The front-to-back extent is about 0.31 m, slightly shorter, so the
  length is the side-to-side extent.
- A typewriter about 32 cm wide is a realistic portable size.

## Caveats
- The answer is the object's own longest horizontal extent. If the reference used a world-axis bounding box with the
  typewriter yawed about 25° to the desk axes, it could be larger (about 0.4 m). I did not assume that.
- Confidence: about ±8%. The main uncertainty is f.
