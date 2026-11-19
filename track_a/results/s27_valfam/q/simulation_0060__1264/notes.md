# q_1264: average speed of the walking pedestrian over the clip (m/s)

The file fps and question_fps are both 24, so t=0.58 s is frame 14 and t=1.58 s is frame 38.
Tracks come from scene/tracks (pedestrian pelvis estimate, van wheel midpoint). I checked the pedestrian's position on frame 14 (frames/p14.png).

## Focal length (focal.py)
- The van starts from rest (frames 0 and 1 are identical) with a = 4 m/s^2.
- I back-projected the van at frames 14 and 38 using the given depths (22.7254 m and 21.5370 m) to get a 3D line, then projected every frame's ray onto that line to get a path length s(t).
- I fitted s = 0.5 a (t - t0)^2 and solved for a = 4. This gives f ≈ 2290 px with a very good fit (RMS 5 mm). The f1–27 and f28–71 fits give the same f within 1%, and the reference-point height doesn't matter.
- If t0 is fixed at frame 1 instead of left free, f ≈ 2520.
- Check: the vanishing point at y = -41.7 implies a pitch of atan(582/2290) = 14.3°. The pedestrian's 3D walking direction has a y-component of -0.254 (sin 14.7°), which agrees.

## Pedestrian (ped.py, ped2.py)
- The two given depths (34.48 m and 35.65 m) plus the image positions give a 3D displacement of 1.198 m over 1.0 s between t=0.58 and t=1.58. Most of this comes from the 1.17 m change in depth.
- The result barely depends on f: 1.205 at f=2000, 1.194 at f=2500.
- Over the whole clip, I projected each frame's ray onto the 3D walking line:
  - constant-velocity fit, frames 2–71: 1.246 m/s
  - endpoints, frames 1–71: 1.225 m/s
  - mean per-frame speed over frames 1–71, counting the zero at the duplicated frame 1: 1.21 m/s
  - 1-s segments: 1.20, 1.30, 1.22 m/s
  - using the head point or the feet point gives the same result within 0.5%.
- Check on depth: apparent height × depth is constant (4286 vs 4292), so the depths are consistent with the track.

## Answer
1.22 m/s: the whole-clip average, within about 2% of the routes above (range 1.20–1.25). Confidence: good, about ±4%.
