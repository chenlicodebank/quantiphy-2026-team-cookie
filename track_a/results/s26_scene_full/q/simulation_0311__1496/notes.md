# Q1496 – width (wheel to wheel) of the red car (simulation_0311)

Answer: **2.04 m**. Scale comes from the prior (car height = 1.15 m). The depth_info could not be used (see below).
File fps = question fps = 24.

## Camera calibration (poles.py, track_feats.py)
- Vertical vanishing point from the edges of both utility poles (fit rms < 2 px): V = (1284, 12062).
- Road-direction vanishing point from 150 LK feature tracks on the car, frames 29–71 (straight-line fit residual 0.45 px).
  The two halves of the clip agree: R = (−1106, −855). The motion is a pure translation.
- With the principal point at the image centre, f² = −(V−c)·(R−c), so **f ≈ 4228 px** (HFOV ≈ 34°, pitch ≈ 20° down).
  Check: the lateral vanishing point (9814, −859) lies on the tail-light line and on the mirror-to-mirror line.

## The depth_info is inconsistent with the video
For any point fixed to the car, the image law z ∝ 1/|u−R| gives d(t=1)/d(t=2) ≈ 0.83 (ratio_check.py). This
barely depends on f (f_explore.py). The given depths imply 17.83/23.20 = 0.768. No rigid origin offset can satisfy
both values. The depth-based scale (≈0.212 m/unit) would also make the car ≈0.95–1.0 m tall instead of 1.15 m.
So I took the scale from the exact height prior instead.

## Motion-stereo reconstruction (sfm.py, sfm2.py, cloud.py)
The car translates by one constant step D per frame. Each LK-tracked feature (frames 29–71, reprojection rms ≈ 0.6 px)
is triangulated in step units, giving along/lateral/up coordinates in the frame-48 position.
- Roof top: highest features (canopy at the centreline, al ≈ 89.8): up ≈ −36.43…−36.52. I take −36.40 ± 0.1.
- Ground: the bottoms of the rear and front left tyres, read in frames 40–71 against ticks drawn below the
  triangulated hubs (tyre_ticks2.py, hub_track.py): rear −41.1, front −41.0, so ground ≈ −41.07 ± 0.07.
- H_u ≈ 4.67 units, so the scale = 1.15/4.67 = 0.2463 m/unit.
- Centre plane (lateral): mirror-ring midpoint 44.18 (both mirrors triangulated by template tracking:
  same along and up, mirror_track.py), tail-light midpoint 44.27, central rear fin ≈ 44.3. I use **44.22**.
- Left wheels' outer faces: hub centres at lateral 40.33 (front) and 40.50 (rear); tyre and body features reach 40.07–40.2.
  Outer edge ≈ 40.15, so W_wheels ≈ 2 × (44.22 − 40.15) = 8.14 units = **2.00 m**.
- Mirror outer span (direct measurement, both mirrors): 48.43 − 40.03 = 8.40 units = **2.07 m** (an AABB that
  includes the mirrors).

## Second-route checks
- Proportions: mirrors 0.96 m high, tail lights 0.72 m, rear haunch top 0.91 m, wheelbase 10.49 units = 2.58 m.
  All are plausible for this LaFerrari-like model.
- Real-world check: LaFerrari is 1.992 m wide × 1.116 m tall; scaled to 1.15 m that gives 2.05 m.
- The wheel-to-wheel reading (2.00) and the AABB-with-mirrors reading (2.07) bracket the answer. I answer 2.04.

## Confidence
Moderate. The main uncertainty is the roof-top height in reconstruction units (±3%) and whether the reference
AABB includes the mirrors (±2%). Expected error is about 4%.
