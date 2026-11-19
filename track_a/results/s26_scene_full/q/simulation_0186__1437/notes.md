# q_1437 — length of the gift box (m)

The file rate and question_fps are both 24 fps. The box falls from frame 0 to frame 8, lands on a blue roller ramp at frame 9, then slides down it.

## Scale (focal length)
Script: `scale.py`.
- **Gravity route.** A parabola fitted to the free fall (frames 0–8, body centroid) gives 3.744 px/frame² (residual 0.12 px). Z0 comes from d(t=0) = 9.859 m. Setting f·g/Z = a_px with g = 9.81 gives **f = 2124 px**.
- **Prior route.** I back-projected the slide (frames 9–38). Z is set by d(t=0.5 s) = 9.741 m at frame 12 and follows the change in apparent size (sqrt of hull area) at other frames. I then solved for the f that makes the slide acceleration equal 3.18 m/s², using both a linear fit of speed and a quadratic fit evaluated at t = 1 s. This gives **f = 2214–2218 px**.
- The two routes agree within 4%. I used **f = 2169 px**, their mean. The prior route depends on the area-based Z and on a single-frame acceleration; the gravity route is cleaner.
- The camera is static and level: the fall track stays at u = 554 within 0.4 px over 121 px of fall.

## Box geometry
Scripts: `fitbox2.py` (single frame) and `fitjoint.py` (joint fit).
- I fitted a 3D cuboid to the background-difference silhouette, leaving out the bow, plus the ribbon lines, which run through the centre of each side face. The box centre sits on the ray at the given depth.
- The joint fit uses frames 0, 3, 6, 8 and 12 with shared dimensions and orientation. Frames 0–8 share Z (free fall), and frame 12 uses d = 9.741.
- The orientation is constant through the whole clip. The box sits flat on the ramp; its long axis runs along the downslope direction (0.82, 0.49, −0.29) in camera coordinates, so the **slope is 29°**. This matches the 3D direction of the box's own track.
- Box edges at f = 2169:

| Edge | Joint fit | Frame-12-only fit |
|---|---|---|
| Along the slope | 0.393 m | 0.391 m |
| Across the slope (horizontal) | 0.349 m | 0.380 m |
| Normal to the ramp (box "height") | 0.362 m | 0.335 m |

  The cross edge and the height trade against each other; the edge along the slope is stable.

## Value of "length" under each reading
1. **Box edge, local dimensions:** longest roughly horizontal edge = **0.39 m**.
2. **World AABB with axes along the ramp heading:** a·cos29° + c·sin29° = **0.505–0.52 m**. The width is the cross edge, about 0.35–0.38 m.
3. **World AABB with axes along the wall.** The wall faces the camera within about 3°, and the ramp is yawed about 17° relative to it, so this reading gives an x-extent of about **0.60 m**.

## Answer
**0.50 m.** This follows the stated world-AABB convention, using the ramp-aligned extent. It also sits between the other two readings: about 28% from the edge length and 17% from the wall-aligned AABB.

## Confidence
- The pixel geometry and scale are good to about ±4%.
- The main uncertainty is which size convention the reference uses (0.39, 0.51 or 0.60).
