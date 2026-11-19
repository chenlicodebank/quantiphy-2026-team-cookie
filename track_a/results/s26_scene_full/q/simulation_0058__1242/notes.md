# q1242 – bicycle speed from beginning to end (m/s)

File fps = question_fps = 24, 72 frames. t=0.58 s -> frame 14, t=1.58 s -> frame 38.
The video frame 1 is a duplicate of frame 0, so the bike's speed for frame 1 is 0.

## Method (3D pinhole, principal point at the image centre (1080, 540))
- Tracks come from scene/tracks: cyclist ref_x/ref_y (the box centre, checked on frames 14 and 38: box 1154-1289 x 513-650
  matches the bike+rider) and van ref_x (also rear edge + constant) with ref_y.
- For a trial f, I put the two depth_info points of each object (frames 14 and 38) in 3D and took the straight line
  through them. For every frame I placed the object at the point of that line nearest to the pixel ray.
- Focal length from the prior (white car = the white van, a = 4 m/s^2): I fitted a quadratic to the van's position
  along its line over frames 2-36 (the cleanest window, rms 4 mm). Both van position definitions give f = 2209-2210 px
  (HFOV about 52 deg). The van starts from rest at t of about 0, and its acceleration stays at about 4 in other windows
  (3.95-4.13 for ref_x).
- Bike at f = 2210: the per-frame speeds are constant at 5.15-5.33 m/s (no trend). Results:
  - mean over frames 2-71: **5.19 m/s** (answer: constant cruising speed)
  - mean over frames 1-71, including the zero step from the duplicate frame: 5.11
  - chord distance between the frame 14 and 38 positions over 1 s: 5.25 (second route)

## Checks
- The bike's 3D direction is perpendicular to the main road (vanishing point 1253, 422.5) at f of about 2000, and the van's at
  about 2220. Both are within ~2 deg, so this is consistent but weak.
- The vertical parts of all four objects' depth-based displacements are about 0 for f between 1600 and 2600, so they don't constrain f.
- Sensitivity: the speed scales about as 1/f. A ±3% error in f gives about ±3% in the answer.

Confidence: good (about ±4%).
