# q1626: average speed of the rabbit (m/s)

File fps = question_fps = 24. 3D render, static camera.

## Method (measure.py)
- Tracks from scene/tracks (torso centroid; checked on frame 24 that tracks are on the right animals). Brown horse
  frame 49 is a loop reset, so only frames 0-48 are used for it.
- Pinhole camera, principal point at the image centre (960, 540). 3D position = d(t) * unit ray(u, v, f), with d(t)
  linearly interpolated/extrapolated from the depth_info values at t=0 and t=1.
- f is solved so that the brown horse's 3D speed equals the prior (0.874 m/s): f = 2638 px (frames 0-48, torso),
  2602-2674 in other windows/reference points.
- Rabbit: 3D positions for frames 0-49 with the same f; mean of per-frame speeds = 1.447 m/s, net displacement / time =
  1.439 m/s (motion is monotonic in +x, so the two agree).

## Checks
- Windows 0-24, 12-36, 24-48 and reference points torso / mask centroid / ground contact give 1.42-1.54; the
  full-window torso values cluster at 1.43-1.47. Mask centroid includes swinging head/legs (less reliable).
- Sanity: brown horse bbox ~330 px -> ~2.0 m nose-to-tail; cream horse speed ~1.46 m/s similar to the rabbit.

Answer: 1.44 m/s. Confidence: moderate-good (~±4 %).
