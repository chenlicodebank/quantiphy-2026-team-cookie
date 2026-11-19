# simulation_0117 – measurement record

2D simulation (Blender render), 1920x1920 px, 19 frames at 24.020228 fps (t = frame/fps, 0 to 0.749 s).
Pixel coordinates are full resolution, x to the right, y DOWN.

## Scene
A small yellow-green ball (tennis-ball-like, seam visible) **falls straight down** in front of a
dark wall with a brown wood-grain door that is lit by a white spotlight. A grey floor strip is at the bottom.
The camera is **static**: phase correlation of the background against frame 0 gives shifts under 0.11 px in every frame.
The view is frontal (no visible perspective). The ball falls in the wall plane facing the camera, so one
metres-per-pixel scale applies.

## Files
- `scene.json`: inventory (ball, door, door_handle, floor, wall), static pixel extents, camera, events.
- `tracks/ball.csv`: one row per frame (0-18). The reference point (`ref_cx_px`, `ref_cy_px`) is the
  centroid of the ball's mask. Frames 0-1 are clipped by the top image edge (`clipped_at_edge=1`). For those frames
  `ref_cy` = bbox bottom − 22 px (half of the 45 px diameter), and the raw centroid is biased downward.
  The file also has the raw centroid, the min-enclosing-circle centre, the bbox, the bbox width/height, the
  min-enclosing diameter and the mask area. `n_blobs` is the number of difference blobs; only the largest one,
  which is the ball, is used. The rest are tiny compression-noise specks.
- `scripts/track_ball.py`: subtracts a per-pixel median background (|ΔRGB| sum > 30, 3x3 opening) and takes the largest component.
- `scripts/check_overlay.py`: draws the bbox/circle crops and the whole trajectory (I checked these visually: the masks
  cover the whole ball).
- `scripts/static_and_camera.py`: camera-shift check, door edges from gradient profiles, handle bbox.

## Ball (only moving object)
- Diameter: **45 px** (median bbox width/height over the unclipped frames; range 44-47 px). Frames 12-16 read
  1-2 px larger because of motion blur and the bright background. Use 45 px as the size.
- The path is vertical: x = 1017.1 ± 0.2 px throughout. y runs from ≈9 (frame 0, estimated) to 1774.8 (frame 18).
- Per-frame Δy (px): 5, 16, 27.7, 38.0, 49.0, 59.8, 70.7, 81.5, 93.0, 103.4, 114.6, 125.7, 135.8, 147.7,
  158.1, 168.7, 180.2, 190.9. The increments grow almost linearly (about 10.9 px/frame per frame), which is
  consistent with free fall from near rest at about frame 0. The first two values depend on the clipped-frame
  estimates (±1-2 px).
- Events: falling from the first frame, starting from near rest at the top edge. Fully in view from frame 2. It
  passes the top of the door (y≈372) between frames 7 and 8. In the last frame (18) it is still falling, with its
  bottom at y=1797, about 49 px above the floor line (y≈1846-1848). **There is no bounce, impact or contact in the clip.**
- Reliability: the centre is good to about ±0.5 px in frames 2-18. Frames 0-1 are good to ±1.5 px (clipped).

## Static objects (frame 18; the camera is static, so this holds for every frame)
- Door with frame: outer bbox x 697-1412, y 372-1846 → **715 px wide, 1474 px tall**. The right edge and top edge
  have low contrast (±3 px). The left jamb inner edge is at x≈714. A vertical seam/groove at x≈821 separates a narrow left
  strip from the main leaf.
- Door handle (black smart lock): bbox x 826-862, y 1036-1224 → 37 x 189 px, centre (844, 1130).
- Floor: the wall/floor boundary is at y≈1848, and the floor strip fills y 1848-1919.

## Ambiguities
- The ball's colour changes (dark olive in shadow, bright yellow-green in the spotlight). This is lighting only.
- Only one ball; there are no similar objects. There is no visible shadow of the ball.
- The release happened at or just before frame 0. The ball's start position is partly outside the image.
