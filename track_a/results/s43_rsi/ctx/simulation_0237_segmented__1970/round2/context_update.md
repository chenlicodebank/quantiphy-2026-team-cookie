# Round 2 addendum (q1970, house width)

## Verified (own code: measure.py, overlay.py)
- Horse pixel speed fits (px/s), giving 0.013699 m/px at the horse:
  - centroid 63.97;
  - muzzle tip 63.84;
  - brown-only centroid 63.84;
  - brown left edge 63.43.
- Closure on the prior: 0.3 pct.
- House Y extent at eave corners: 615 / 619 / 617 / 625 px (x = 664 / 670 / 1358 / 1350).
  - At the ridge it is 721 px. The ridge/eave ratio about the image centre is 1.164 (top) and 1.172 (bottom).
  - Width = 618 eave-px, so 8.47 m uncorrected.
- X extent: 700 px at eave level, 803 px at the gable peaks. So X is the length.
- The C2/C3 fault (longer axis at ridge level) is real. Round 1's switch to 8.1 is confirmed.
- New top-down cue: grey hooves peek out only on the horse's edge facing the image centre, and stay put while planted.
  This is consistent with a perspective view from above, with a ground depth of roughly 30-45 m (rough).

## Ruled out
- 10.95-11.0 m: this is the length at ridge level.
- 8.87 m (blend): above the 8.47 m upper bound.

## Still open
- Eave height above the horse cannot be observed.
  - Single storey: factor 0.93-0.96, giving 7.85-8.15 m.
  - Two storeys: about 7.2 m.
- The tile-period route (tiles.py) is inconclusive. The main-wing foreshortening is about 0.82, but the tile aspect is
  unknown and the cross-wing spectra are harmonic-dominated.
- Answer 8.1, medium confidence.
