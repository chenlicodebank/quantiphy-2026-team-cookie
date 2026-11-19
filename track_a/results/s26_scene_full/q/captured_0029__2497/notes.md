# q 2497 — distance travelled by the tennis ball until it hits the whiteboard (cm)

File fps = question_fps = 24. Hit at t=1.24 s -> frame 30 (matches the record: minimum size and reversal at 30).
Motion starts at release, frame 16-17 (ball held still in front of the table's front-right corner in frames 0-16).
Answer = 3D path of the centre from frame 16 to frame 30.

Camera: f = 0.5959*1280 = 763 px, c = (640,360). depth_info read as Euclidean camera-to-centre distance
(0.901 m at f24, 1.144 m at f30, 1.027 m at f38; the "0.901s" is a typo for m).

## Route 1 — table plane (plane.py)
Back-projected ball centres at f24, f30, f38 with the given distances; they define the plane of ball centres
(rolling on the table). Normal ~ camera -y (1 deg tilt), 0.138 m below the camera. Check: table corners from the
plane give a 0.74 x 0.58 m table top (plausible). Ray-plane intersection for every frame gives positions:
path 16->30 = 0.728 m, straight 16->30 = 0.710 m, path 17->30 = 0.712 m. (Assumes the ball at release is held at
about table height.)

## Route 2 — apparent size at release (ellfit.py, final.py)
Sphere off-axis is an ellipse elongated radially by 1/cos(theta); fitted that constrained ellipse to the upper
(unoccluded) contour: tangential diameter 88-91 px over frames 0-16 (rms 0.6 px). Same fit at far frames gives
38.7 px (f30), 44 px (f38); scale factor k = Z_given / (f*D/d) = 0.858 / 0.878 (0.816 at f24, blurred) — the
given depths are ~13 % smaller than raw size predicts, so the release depth is scaled the same way:
Z16 = 0.48-0.50 m -> straight-line 16->30 = 0.68-0.69 m; hybrid path (release point + plane points 18-30) = 0.69 m.

## Result
Routes give 0.68-0.73 m; path ≈ straight line (ball goes straight across the table). Answer 71 cm.
Confidence moderate (±5 %): main uncertainty is the release depth (0.455 vs 0.49 m) and the start frame.
The record's diam_px for frames 0-16 (110-116 px horizontal) is the radially stretched major axis plus halo; it is not
the size that gives depth.
