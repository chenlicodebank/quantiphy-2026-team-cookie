# Q1702: average speed of the boat (m/s)

File rate is 25 fps, but question_fps is 24, so t=1 s is frame 24 and t=2 s is frame 48 (I used the frame columns from scene/tracks).

## Method (solve.py)
- Pixel positions come from scene/tracks: the boat's hull centre (body_cx, centroid_y) and the bird's mask centroid (cx_best, cy_best; interpolated at the mast crossing in frames 48-49). Each value is taken from a linear fit over ±3, ±6 or ±10 frames around frames 24 and 48, which smooths the bird's wingbeat jitter.
- Back-projection: P = d · unit ray((u-480)/f, (v-480)/f, 1), with d from depth_info.
- Focal length: I solved for f so that the eagle's 3D displacement between t=1 and t=2 equals 12 m (the prior speed of 12 m/s over 1 s). Result: f ≈ 2650 px (horizontal FOV 20.5°). It is stable across the three fit windows (2650-2654).
- Boat: the 3D displacement between t=1 (133.96 m) and t=2 (131.26 m) is 4.122-4.128 m over 1 s, so the speed is 4.12 m/s. That splits into about 3.1 m of lateral motion and 2.7 m of range change.
- Constant motion: in the image the boat moves smoothly with no events. Its pixel speed rises from 2.53 to 2.69 px/frame, which fits a boat moving at constant velocity while it approaches the camera. Under constant velocity, the clip's average speed equals this 1-second speed.

## Checks
- The bird's pixel speed drops from 7.9 to 6.7 px/frame, which fits a bird flying at constant speed while it recedes (139.7 → 147.2 m). This supports the constant-speed reading of the prior.
- The boat's apparent length grows 3.8 % between frames 24 and 48, while its range shrinks by 2.0 %. Part of the growth is probably the boat's changing viewing angle. The answer depends on the given depths, not on the length.
- I had no independent second reference for f; the eagle prior is the only metric anchor besides the depths.

Confidence: moderate-good, roughly ±5 %.
