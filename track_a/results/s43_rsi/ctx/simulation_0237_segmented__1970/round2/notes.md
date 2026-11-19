# q1970: width of the house (prior: brown horse speed 0.874 m/s). Round 2 investigation.

File fps 24 = question_fps 24. The clip has 50 frames. The camera is static and the background is segmented white.

## Task
Round 1 proposed a switch to 8.1 (follows C1). My first job was to verify it.

## Crux
The answers part on which dimension is measured, and where:
- C1 / round 1: shorter horizontal extent, the Y extent between the gable ends, 618 px at eave level, with a small
  eave-height depth correction.
- C2 / C3: the whole mask's horizontal X extent, 800 px, taken at the cross-wing gable peaks. That is the longer axis,
  at ridge level, with no correction.

## Scene (frames/f0.png, horse_*.png, overlay.png)
The camera looks straight down at a cross-gabled roof.

The horse is seen from its back. There are no legs along its far (bottom) edge. Grey hooves peek out only along the edge
facing the image centre (frames 0, 8, 24, 40, 48), which fits a top-down perspective: points at ground level project
closer to the principal point. The hooves stay put while planted: x about 795 in frame 0 and about 797 in frame 24.

## Measurements (measure.py → horse_track.csv; overlay.py → frames/overlay.png)
**Horse pixel speed (own threshold mask, 50 frames), linear-fit slopes:**

| reference point | slope (px/s) |
|---|---|
| centroid | 63.97 |
| muzzle tip x1 | 63.84 |
| brown-only centroid | 63.84 |
| brown 2-pct left edge | 63.43 |
| left edge x0 (gait-noisy) | 62.34 |

The endpoint displacement gives 61.5 px/s; it is affected by the gait phase. I take 63.8 px/s, so the scale at the
horse is 0.874 / 63.8 = 0.013699 m/px.

**House, frame-0 mask column extents:**
- At the eave corners: x=664 gives 615 px, x=670 gives 619, x=1358 gives 617, x=1350 gives 625.
- At the ridge, x=1018: y 24..744 = 721 px.
- About the image centre (540), the ridge/eave ratio is 517/444 = 1.164 at the top and 204/174 = 1.172 at the bottom.
  The two agree, so the gable ends are vertical and the principal point is at the centre.
- Eave-level width is therefore 618 ± 3 px; from the ridge, 721 / 1.167 = 618 px also.

**House, row extents:**
- Main wing: 699-700 px at y=100, 200, 600 and 700.
- Cross-wing eave corners: 711-735 px.
- Gable peaks at y=383: 803 px.

The X extent is longer than the Y extent at the same eave depth, so width = Y.

**Second route (tiles.py), inconclusive:** I measured the roof-tile periods on the main wing:
- along the ridge, about 20.3 px;
- along the slope, about 16.7 px;
- ratio about 0.82, which would mean a pitch of about 35° if the tiles were square.

The cross-wing spectra are dominated by harmonics, and the tile aspect is unknown. So this does not fix the focal length.

## Depth correction (the open point)
width = 618 × 0.013699 × Ze/Zb = 8.466 × Ze/Zb, where Ze is the eave depth and Zb the depth of the horse's back.

**Camera depth Zb:**
- From the roof, tan(main pitch) = f/2468 and Zb = 0.0137 f. A 30-45° pitch gives Zb = 19.5-34 m.
- The hooves peek out about 6-7 px on the near-centre side and never on the far side. The perspective shift is
  237 × hb/Zg, which gives Zg of roughly 30-45 m (rough).
- I take Zb at about 24-35 m.

**Eave height above the horse's reference features** (silhouette and muzzle, about 1.2-1.4 m above the ground):
- Single storey (eaves about 2.7-3 m): 1.3-1.8 m above them. Factor 0.93-0.96, width 7.85-8.15, central about 8.0.
- Two storeys (eaves about 5.5-6 m): factor about 0.85, width about 7.2.

Without walls or ground in view, the storey count cannot be observed. A single storey is the default for a building
this size with this roof.

My own central value is about 8.0 m. Round 1 / C1 gave 8.1. They differ by about 1 pct.

## Rechecks
a. **Closure:** at 0.013699 m/px:

| reference point | speed (m/s) | error vs prior |
|---|---|---|
| centroid fit | 0.876 | 0.3 pct |
| muzzle fit | 0.875 | 0.1 pct |
| left-edge fit | 0.854 | 2.3 pct |

b. **Plausibility:**
- The horse is 149.5 × 38 px, so 2.05 × 0.52 m (a realistic horse).
- The house footprint is about 8.0-8.5 m × 9.6-10 m, with a roof rise of about 3-4 m. Realistic.

c. **Units and time:** metres. File fps equals question fps (24); slopes are per second at 24 fps.

d. **Fault proof:**
- C2 (10.95) and C3 (11.0) used the image X extent of the whole mask: 799-800 px, reproduced at 803 px on row y=383.
  - That is the longer horizontal axis, 700 px at eave level, against 618 px for Y.
  - It was taken at the gable peaks, about 10 pct closer to the camera than the eaves.
  - With the "width = shorter extent" rule, it is the length, not the width.
- The submitted 8.87 is the blend with their 10.975. It is above the uncorrected upper bound of 618 × 0.013699 = 8.47 m.
  Any eave above the horse's back lowers the width further, so 8.87 is not reachable.

## Decision
Round 1's claimed fault is reproduced: 803 px at X/ridge level against 618 px at Y/eave level. My value of about 8.0
agrees with the proposed 8.1 within 2 pct. The change stands: switch to 8.1 (C1). Confidence is medium, because the
eave height is unobservable.
