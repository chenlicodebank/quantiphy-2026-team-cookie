# Q1606 — height of the black cat including its tail (m)

File fps = question_fps = 24 (no conversion issue). 3D Blender render, static camera, 1920x1080, principal point assumed at centre.

## Focal length (focal.py, height.py)
- Prior: cat speed 0.94 m/s; depth_info: cat origin 4.199 m at t=0 (frame 0), 4.481 m at t=1 s (frame 24).
- Origin proxy = torso-core centroid from scene/tracks/cat.csv: f0 (408.5, 842.7), f24 (869.4, 805.3) (f24 just
  starts to touch the dog; matches the f23 value + one step).
- Solved |P(f24) - P(f0)| = 0.94 m with P = depth * unit ray -> f = 2155 px (hFOV 48 deg).
  Sensitivity: origin offset +-60 px horizontally -> f 2135-2173 (+-1 %).
- Check (check_path.py): a constant-velocity straight path between the two 3D points reprojects onto the core track for
  frames 0-23 within +-11 px (gait wobble); speed 0.940 m/s reproduced.

## Height
- Tail tip (top of mask) per frame from my own background-subtracted mask (seg_cat.py -> cat_extents.json); masks checked
  on overlays. Frame 0: tail tip at (228, 696).
- Paw contacts read on zoomed gridded crops (the white paws over carpet are missed by the masks): f0 hind paw (218, 968),
  front paw (390, 956); f11 (573, 935), (660, 931); f22 (767, 920).
- 3D points from intersecting pixel rays with the cat's sagittal plane (vertical plane through the origin path).
  Height = vertical distance tail tip - floor contact. Floor contacts at different frames are coplanar within +-7 mm with
  zero camera pitch (pitch 0 fits best; 1.5-2.7 deg changes results by <1 %).
- Results: f0 0.490 (hind paw) / 0.495 (front paw); f11 0.454-0.460; f22 0.480; frames 0-23 mean 0.480
  (tail height varies with the walk cycle; range 0.457-0.491).
- Paw-bottom reading +-4 px -> +-0.007 m.

## Second route
Simple pinhole at frame 0: pixel height 968-696 = 272 px; tail/hind-paw region lies at Z ~3.88 m (sagittal plane),
272*3.88/2155 = 0.49 m. Using the origin's Z (4.03) instead would give 0.51 m (upper bound).

## Answer
0.49 m (frame 0 / t=0 value; whole-clip mean 0.48). Confidence: moderate, ~+-5 %; main uncertainty is which frame the
reference box is taken at (tail pose changes height by up to ~7 %).
