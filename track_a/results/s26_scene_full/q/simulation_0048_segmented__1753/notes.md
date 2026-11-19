# Q1753 – average speed of the walking person (m/s)

Prior: the walking person is 1.8 m tall. depth_info gives the human (pedestrian) at 11.9259 m at t=1 (frame 33) and 10.8165 m at t=2 (frame 66). The bike is at 16.49 m / 11.93 m.
question_fps = file fps = 33. The pedestrian is the man in the grey T-shirt, tracked in all 99 frames (scene/tracks/pedestrian.csv, mask centroid used as the pelvis).

## Method
- 3D pelvis position = depth × unit ray through the pelvis pixel. Principal point is the image centre and the focal length f is unknown.
- f comes from the vertical vanishing point (kiosk edges, about (1031, 6509), roughly 12° pitch) plus the condition that the pelvis stays at a constant height above the ground at t=1 and t=2. That gives f ≈ 1300–1390 px (model.py, traj2.py). The person's pixel height (1.8 m → ~200 px at 11.93 m) is consistent with f ≈ 1300.
- Displacement from t=1 to t=2 (|P66 − P33|): 1.12–1.14 m for every f from 1200 to 2500 px and every VP from 5000 to 10000. The result is insensitive to f because the motion is mostly radial (the depth change alone is 1.109 m).
- Extending the track to the whole clip (ray-plane intersection with a smoothed pixel track, traj2.py) gives a mean speed of 1.10–1.12 m/s. The 1-s segment speeds are 1.10 / 1.135 / 1.06–1.11, so the walk is roughly uniform. The end segments depend on how the track is smoothed, and the raw per-frame track is too noisy to use for the mean (gait wobble).

## Inconsistency found (check route)
- The image scale of the pedestrian (bbox height and sqrt of mask area, averaged over ±8 frames) grows only 1.063× from t=1 to t=2, but the given depth ratio is 1.1026.
- Mesh-only reasoning (depth ∝ 1/pixel height, lateral motion added) would give about 0.78 m/s.
- No pitch or focal length makes the two consistent with a flat pelvis height (pitchscan.py). The cyclist's growth does roughly match its own depth ratio.
- The reference answers come from the same object origins as depth_info, so I answer from depth_info: about 1.13 m/s (constant-speed walk).

Answer: 1.13 m/s. Confidence: moderate. The main risk is the depth/image disagreement; the image-only alternative is about 0.78 m/s.
