# Q1624: average speed of the white (cream) horse, in m/s

The video is a 3D Blender render with a static camera. Both the file and the question run at 24 fps, and the clip has 50 frames. The white horse is the record's `cream_horse`. The prior gives the brown horse's speed as 0.874 m/s, and depth_info gives each object's camera distance at t = 0 and t = 1 s.

## Method (solve2.py)
- **Pinhole back-projection.** P = d · normalize((u - 960)/f, (v - 540)/f, 1). Depth is interpolated linearly in time from the depth_info values. The pixel tracks are linear fits of u and v over frames 0-48 for the brown horse, whose rig loops back to its start at frame 49, so that step is excluded. For the cream horse the fit covers frames 0-49.
- **Focal length.** I chose f so that the brown horse's mean per-frame 3D speed equals 0.874. This gives f = 2558-2613 px (horizontal FOV about 41 degrees), depending on the reference point (torso_cx, mask_cx or bbox_cx).
- **Cream-horse speed with that f.** Torso centroid: 1.468 m/s. Mask centroid: 1.516. Bbox centre: 1.518. The velocity is almost entirely along camera X; its Z component is about 0.1 m/s, which matches the slight change in depth.

## Checks
- **Pixel speeds by template matching** of the torso (tmatch.py): brown 140.4 px/s and cream 263.8 px/s, a ratio of 1.879. The mask centroids give 1.872 and the torso centroids 1.818. Scaling the torso-centroid result by the template speeds gives 1.517 m/s.
- **Focal length check** (check_plane.py). I placed the six origin points (three animals at two times, using the ground-contact pixel y) on a single plane. The plane fits best for f between about 2600 and 3000, and it implies a vertical vanishing point at y ≈ 4000-5200. The record measured that vanishing point at about 5500 ± 1500, so the two agree with f ≈ 2600.

## Answer
1.51 m/s. The main uncertainty comes from gait jitter in the pixel speeds (about 3 %).
