# Q1506 – total length of the bird's flight path (m)

The file is 24 fps and question_fps is also 24, so there is no time-base issue. The video has 100 frames (0–99).

## Scale (focal length)
- Prior: each window frame is 1.48 m wide. The windows lie on the backdrop facade around the neon sign, and the sign is
  34.5 m from the camera (depth_info). The sign centre is about 230 px off-axis, so the plane depth is Z ≈ 34.45 m.
- Window width in px:
  - Visual reading on zoomed crops (win3.png): 845–970 and 1025–1150, i.e. about 125 px.
  - Half-level edge crossings (winhalf.py): 128.8–129.6 px for the two central windows, and 120–127 px for the
    neighbouring windows.
  - The lit window is 126 px.
  - Adopted value: 127 px (range 125–129).
- f = 127 × 34.45 / 1.48 ≈ 2950 px, which gives a horizontal FOV of about 36°.

## Depth model
- Converting the given camera distances to optical-axis depth with the bird's pixel position:
  - t = 0: D = 25.328 → Z = 24.36
  - t = 0.5: D = 24.899 → Z = 24.30
- So almost all of the drop in distance comes from the bird moving toward the image centre. Z itself is nearly constant.
- A constant-Z model (the mean of the two values) reproduces both given distances to within 0.035 m.
- This agrees with two other observations:
  - the bird's pixel speed is constant (16–17.6 px/frame in every 8-frame window);
  - its apparent maximum wingspan per wingbeat cycle is about the same (50–56 px) all along the path.

## Path
- Track: `scene/tracks/bird.csv` centroids, checked with my own re-segmentation (seg.py, frames/segsheet.png).
- Frames 0–4 are unreliable (the bird is merged with its shadow or over a black pillar). They were replaced by a linear
  extrapolation of frames 5–14.
- Savitzky–Golay smoothing (window 9, order 2) removes wing-flap jitter. The image path is about 1680 px.
- Each frame is back-projected as P = ((u−cx)/f·Z, (v−cy)/f·Z, Z), and the frame-to-frame 3D steps are summed.
- Results (path3d_z.py):

  | Window width | f (px) | Path length |
  |---|---|---|
  | 125 px | 2905 | 14.00 m |
  | 127 px | ~2950 | ~13.8 m |
  | 128 px | 2975 | 13.69 m |

## Second-route checks
- Other depth models:
  - Z falling linearly with the measured rate: −0.9%.
  - Z constant after 0.5 s: same result.
  - The older model with distance falling linearly (not Z): 13.8–13.9.
- Other start-point handling (quadratic extrapolation, or the bird body on the ledge at (228, 870)): ±1%.
- Overall spread is 13.4–14.4 m. Most of it comes from the window-width pixel measurement.

**Answer: 13.8 m.** Confidence: moderate, about ±4%.
