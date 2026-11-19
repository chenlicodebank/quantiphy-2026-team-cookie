# captured_0010s — measurement record

Lab video, 3D, 24 fps, 49 frames (t = 0 … 2.000 s), 1280×720. Background is a uniform green (it looks replaced;
there is an SAM2 watermark at the bottom right). Benchmark intrinsics for this camera: fx = fy ≈ 763 px, principal point ≈ (640, 360).

## Scene
One pendulum: a **red/orange ball** (the only coloured object) on a thin **light-grey string** hanging from a
**pivot** at about (637, 229) px. The support itself is not visible. There are no other objects, no ground plane and no horizon.
The ball swings mostly **toward and away from the camera** (along the line of sight), with a small sideways (+x) part:
- far end of the swing: the ball is high in the image (cy ≈ 301), small (≈ 27.5 px diameter) and the string is strongly foreshortened (30–45 px visible);
- near end: the ball is lower (cy ≈ 378–392), large (≈ 37.5 px) and the string is ≈ 135–145 px long, tilted ≈ 15° from the image vertical.
The image-y of the ball is therefore **not** monotonic in the swing phase: it reaches its maximum (≈ 392) at frames 12 and 22 and
has a local minimum (≈ 378) at the near turning point (frame 17). Use the size (depth) together with the image position to get 3D positions.
The apparent-size ratio near/far ≈ 37.5/27.5 ≈ 1.37 ≈ the ratio of far depth to near depth.

## Files
- `scene.json`: inventory, camera, events (turning points), pivot position.
- `tracks/ball.csv`: every frame: centroid (cx, cy) of the red mask (= visible centre, the convention for lab clicks), bbox,
  mask area, equivalent diameter `equiv_diam` = 2√(area/π) (the best size measure), PCA major/minor extents, enclosing-circle diameter,
  occlusion flag (always 0), and bg_dx/bg_dy (phase-correlation shift of a background patch vs frame 0; ≈ 0, so the camera is static).
- `tracks/string.csv`: line fit to the string pixels above the ball: top (≈ pivot) and bottom endpoints, visible (projected) length,
  angle from the image vertical (negative = bottom toward +x), pixel count.
- `scripts/track.py`: HSV red threshold → largest component → closed and filled contour; string = low-saturation bright pixels above the ball, robust line fit.
  Overlays written to frames/ov_XX.png were checked by eye: the mask covers the full ball and the line follows the string.

## Events (frame / t)
Start f0 (the ball is already moving away); far turning point f3 (0.125 s); max image-y f12; near turning point f17 (0.708 s, largest ball, max tilt);
max image-y f22; far turning point f32–33 (1.333–1.375 s); near turning point f46–47 (≈ 1.92–1.96 s). Period ≈ 29.5 frames ≈ 1.23 s.
There are no releases, impacts or bounces.

## Reliability
- Ball centroid: ±0.5–1 px. Diameter: ±1 px (≈ 3 %). Specular highlights and compression slightly erode the mask; equiv_diam is more stable than the bbox, which is quantised to 2 px.
  Frame 0 shows some motion blur.
- Motion blur near mid-swing (frames 7–10, 25–28, 35–38) is small (a few px).
- String: not detected at frame 0 (blurred). At the far end (f1–8, f29–37) the upper string is faint and foreshortened, so top_y reads 234–262 instead of ≈ 229 there; use pivot ≈ (637, 229).
  The string top x is ≈ 639–641 in frames 1–28 and ≈ 633–636 in frames 29–48: either a small pivot drift or a detection bias; this is uncertain.
- Camera: static. There is no background texture to confirm this with, but the pivot point is fixed.
- No metric scale is assumed. Use the given depth_info with f = 763 px to back-project: X = (u−640)·Z/763, Y = (v−360)·Z/763 (approximately, with Z along the optical axis;
  depth_info is the Euclidean distance, so Z = d / √(1 + ((u−640)² + (v−360)²)/763²)). A ball of diameter D at distance d appears ≈ 763·D/d px wide.
