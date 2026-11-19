# q_1699: length of the eagle (m)

The file runs at 25 fps and question_fps is 24. Frames are indexed with question_fps: t=1 s is frame 24 and t=2 s is frame 48 (scene/ frame column).

## Scale (focal.py, geom.py)
- Eagle image positions come from scene/tracks/bird.csv (cx_best/cy_best). Frame 24 is at (236.5, 522.3) and frame 48 at (411.0, 528.4); local quadratic smoothing gives the same values. The principal point is taken at (480, 480).
- The depths are 139.70 m and 147.16 m. Requiring |P2-P1| = 12 m (the prior, over 1 s) gives f = 2652 px (hfov 20.5 deg), stable between 2647 and 2655 for every smoothing window.
- 3D velocity (camera frame) = (8.95, 0.47, 7.98) m/s. The eagle flies right and away, and its motion makes 51.6 deg with the line of sight.
- Boat check: 160-176 px at about 132-134 m gives 7.9-8.9 m, a plausible fishing boat. So the scale is realistic.

## Eagle length
- The body projects almost horizontally, at 14.5 px per metre of body length at 143.4 m (this includes sin 51.6 = 0.78). That is 14.9 px/m at frame 24, 14.1 at frame 50, 13.5 at frame 73, 13.9 at frame 56 and 13.7 at frame 65 (scaled by depth).
- Wings-up frames (V silhouette, rows.py): the body and wing roots form the bottom of the V, about 10-11 px at half-coverage and 11-12 px counting faint pixels. That gives L = 0.70-0.82 m (frames 24, 50, 72-74).
- Wings-level frames: the dark body core is 8-11 px, giving 0.70-0.79 m (frames 6, 56, 65).
- The visible silhouette therefore gives about 0.75 m. Thin ends lose contrast through blur and threshold: the beak tip and the tail, which is seen nearly edge-on from a camera about 1 deg above it. These add roughly 1 px at each end, about +0.1 m.
- Cross-check via the wingspan: the maximum horizontal extent with wings level is 25-30 px. The wing axis is foreshortened by sin 38.4 = 0.62, so W is about 2.2-2.5 m. A typical eagle length/wingspan ratio of about 0.35-0.43 gives L of about 0.8-1.0 m.
- Answer: 0.85 m.

## Confidence
Moderate. The bird is only about 10-30 px and is seen obliquely from behind. The foreshortening assumes the body points along the 3D velocity and the camera is roughly level. Plausible range 0.7-1.0 m.
