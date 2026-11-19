# Q1378: diameter of the red blood cell (m)

Answer: **1.665 m**

## Scene
There are two identical red discs (red blood cells) seen nearly face-on. They rise and move away from the camera. The depth_info and the prior refer to the left one. The file runs at 24.008 fps; all times here use question_fps = 24, so t=1 s is frame 24 and t=2 s is frame 48.

Correction to scene/: frame 31 in both tracks is wrong. The halo switches on in that frame and the segmentation fails (diam 22.8 px and 68.5 px), so I left frame 31 out of every fit.

## Scale (focal length)
- `fit3d.py` fits a constant-velocity straight 3D line to the left cell's pixel track (frames 0-62, without 31). The unknowns are f, P0 and V; principal point (540, 540). The given distances at frames 24 and 48 fix the scale.
- **Free fit, speed prior not used:** f = 1507 px, |V| = 4.765 m/s. The prior is 4.7833 m/s, so the difference is 0.4%. Reprojection rms is 0.074 px.
- **Fit with the speed prior added:** f = 1500 px.
- **Two-frame check (`solve.py`):** solving |P48 - P24| = 4.7833 m alone also gives f = 1500.
- The fitted model reproduces both given distances: 22.0155 m and 24.0333 m.

## Size
- `edge.py` finds the outline at sub-pixel accuracy: radial G-channel profiles, 50% level between the background (204) and the rim (~70). It then fits an ellipse to the outline points.
- The outline is slightly elliptical (major/minor about 1.03), which points to a slightly tilted disc. I take the major axis as the true diameter.
- **Major axis:** 121.1 px at frame 2, 114.2 px at frame 24, 112.6 px at frame 30.
- **Conversion:** D = major_px × Z / f, with Z the fitted camera-axis depth at each frame.
  - The result is very stable: 1.659–1.668 over frames 2–30, mean 1.6626 (f = 1507) or 1.6701 (f = 1500).
  - Frames 40 and 48 give 1.666–1.683, but the halo slightly affects the background level there.
- **Other readings:**
  - Minor axis: about 1.61.
  - Horizontal / vertical edge extents: about 1.635 / 1.665.

## Second route and confidence
- **Second route:** f comes out the same whether it is found from the speed prior or only from the perspective shape of the trajectory plus the two depths (1500 vs 1507). The size is also consistent across 10 frames.
- **Remaining uncertainty:** mainly whether the reference takes the disc's full diameter (major axis, my answer) or a slightly smaller extent (minor axis, about 1.61, -3%). I am confident to about ±3%.
