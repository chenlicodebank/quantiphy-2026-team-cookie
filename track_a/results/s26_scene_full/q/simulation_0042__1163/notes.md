# q_1163 – length of the boat (m)

Prior: eagle speed 11.84 m/s. depth_info: eagle 179.2691 m (t=1 s, frame 24), 177.1009 m (t=2 s, frame 48);
boat 177.2077 m (frame 24), 177.9993 m (frame 48). question_fps = file fps = 24.

## Focal length (focal.py)
Bird (eagle) centroids from scene/tracks/bird.csv (checked: smooth ~17 px/frame, the dark bird on the sand):
f24 (368.2, 460.6), f48 (761.5, 563.6). Back-projecting both with their depths (principal point = image centre)
and requiring the 1 s displacement = 11.84 m (constant speed; mean per-frame pixel speed 17.01 px vs chord
16.94 px/frame) gives f = 6220 px (HFOV 9.9 deg). 3-frame-averaged centroids give the same.

## Boat length (boatpts.py, length3d.py)
Camera is oblique (hull sides visible, mast leans up-image). Boat mask (red hull + white/grey deck, overlay
frames/boatmask_24.png) -> deck-level bow tip (217.4, 886.9) and stern transom/rail edge centre (545.5, 984) at
frame 24; (83.0, 849.3) and (408.5, 946) at frame 48. Lower hull points are not aft of the deck edge (x ≤ 541 < 546).
Ground (water) plane normal from: the boat's 3D displacement f24->f48 (horizontal; uses the given boat depths, gives
the depth gradient along the boat axis ≈ motion direction) + the mast's vertical vanishing direction. Tilt ≈ 36-42 deg
from nadir. Intersecting the bow/stern rays with that plane through the boat origin:
length = 9.930 m (f24), 9.938 m (f48). Varying mast lean ±0.03 changes it by <0.1 %; f ±1 % -> ±1 %.
Check: bird velocity is nearly in that plane (horizontal flight), consistent.

## Second route
Simple scale: hull PCA length 345.5 px × 177.6 m / 6220 px = 9.87 m, times foreshortening along the axis
(3D boat speed 4.09 m/s vs image-plane 4.01 m/s ≈ 1.02) ≈ 10.0 m. Agrees within ~1 %.

Answer: 9.93 m. Confidence: good (main uncertainty is f from the eagle speed, ~1-2 %).
