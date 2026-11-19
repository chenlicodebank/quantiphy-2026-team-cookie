# q1724: average speed of the eagle (m/s)

The file rate and question_fps are both 24 fps. The clip has 72 frames, and the eagle starts moving at frame 1.

## Scale
- Prior: the person is 1.75 m tall. The person's pixel height is 40.5 px (median over frames 0-64, from scene/tracks/human.csv; I checked it on a zoomed crop at t=1). Depth is 139.10 m at t=1 and t=2.
- Focal length: f = Hpx × Z / 1.75, where Z is the depth component of the 139.1 m along the pelvis ray. This gives f ≈ 3190 px. For a ±1 px height error, f ranges from 3110 to 3270 px.

## Eagle
- The reference point is the eagle's body-core centroid (ref_x and ref_y in scene/tracks/bird.csv).
- 3D positions are the pixel ray × depth: 139.7035 m at frame 24 and 147.1583 m at frame 48. Between t=1 and t=2 this gives V = (8.73, 0.43, 7.91) m/s, so |V| = 11.78 m/s. The eagle is flying away from the camera as well as sideways.
- Check: the x pixel track over the whole clip fits this constant-velocity, receding 3D line to within 3 px. The pixel speed slows from 9.5 to 7.2 px/frame, which matches the depth growing. This supports a straight flight at constant speed. The y position bobs by about 10 px with the wing beats.
- Results:
  - Chord from frame 1 to frame 71: 11.78 m/s.
  - Mean of the per-frame speeds (raw, which includes the bob from the wing beats): 11.86 m/s.
  - The same mean after 5-frame smoothing: 11.64 m/s.
- Sensitivity to the person's pixel height (39.5 / 41.5 px): 11.96 / 11.61 m/s.

Answer: 11.8 m/s. Confidence is good, at about ±3 %; the main uncertainty is the person's pixel height.
