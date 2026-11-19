# Q1193: distance between the near door's left pillar and the far door's right pillar

**Answer: 7.5 m** (plausible range 7.25 to 7.8 m).

The file rate and question_fps are both 33. The camera is static, so frame 0 was used for all the static geometry.

## Which objects
The scene/ record does not cover the doors, so I measured them from scratch.

The doors are on the building row at the left of the street, at image x ≈ 1160–1395 and y ≈ 0–330. The row is seen at a grazing angle behind the kiosk.

- **Near building (light clapboard).** Its first entrance has two round dark columns with capitals under a shared hood. On frame 0, at y=250:
  - left column: x 1169–1196, axis at x≈1182.5;
  - right column: x 1224–1250.

  Next to it is a second, white-framed glass door (x≈1257–1312) with thin pilasters.
- **Far building (dark).** Its entrance has two ornate Corinthian columns at the top of the black-railed stoop:
  - left column: x≈1322–1345;
  - right column: x≈1365–1388, axis at x≈1376.5.

I read "near door" as the first clapboard entrance and "far door" as the dark ornate entrance. If the far door were instead the white glass door, the distance would be about 3.9 m.

## Camera (from static scene geometry)
- **Vertical vanishing point:** about (952, 8300), from 7 clean vertical edges (pillars, door frames).
- **Facade-horizontal vanishing point:** (1782, −74). Three cornice lines meet there within about 1 px.
- **Cross-street direction:** the wooden-wall base line and the kiosk front edge meet at about (−3556, −72), on the same horizon.
- **Focal length.** Two independent orthogonality constraints give f = 1891 px (vertical vs facade-horizontal) and f = 1879 px (cross-street vs facade-horizontal). The orthocentre of the three vanishing points is about (952, 373), which is the image centre. I used **f = 1885 px**: pitch is 13.4°, the horizon is at y = −74, and the street rises about 2.9° (vanishing point (1771, −177)).
- **Inconsistency in the given data.** At this f, the walker's given depths (11.93 m and 10.82 m) would make him only 1.22 m tall. Scaling him to the 1.8 m prior needs his distances about 1.47× larger. With that 1.8 m scale, the cyclist's given depths (16.49 m and 11.93 m) put the road only 0.45–0.5 m below the walker's sidewalk, so they roughly agree. The walker's depth_info is therefore inconsistent with the image. **The metric scale comes from the walker-height prior** (walking extent 1.78 m, head top to lowest shoe, 15 keyframes; checked on a zoomed crop at frame 33: about 196 px).

## Sidewalk and facade planes
- **Sidewalk plane.** It is fitted through the walker's foot points and constrained to contain the street direction and the cross-street direction (residual 0.07 m).
- **Facade plane, two independent routes.** The plane normal is the cross-street direction n.
  1. Where the clapboard corner vertical (x≈1152 at y=200, traced toward the vertical vanishing point) meets the wooden-wall base line on the sidewalk, at pixel (1142.5, 585.4). Offset **3.89 m**.
  2. The far stoop's post base (1480, 387) lies on the sidewalk. The railing's top end (1335, 197.5), where it meets the far-left column, is placed in the vertical plane through the post along n. Offset **3.86 m**. The resulting stoop is 1.5 m long and the rail end is 1.8 m high, which is plausible.

  The two routes agree within 1%. A flat sidewalk instead of the 2.9° slope would make them disagree by 6%, so the sloped plane was kept.
- **Pillar positions.** Each pillar axis pixel is back-projected onto its plane:
  - far columns: the railing-route plane (3.86 m);
  - near-left column: the clapboard wall plane minus how far the column axis stands in front of the wall (0–0.15 m, central value 0.08 m). The column is round, about 0.21 m across in the image.

  The origins are taken at mid-shaft. Pillar tops are 3.3–3.5 m above the sidewalk, and the vertical offset changes the 3D distance by less than 0.02 m.

## Results (final2.py)
The central case is f=1885, walking height 1.78 m, column offset 0.08 m:

| Case | Distance |
|---|---|
| Central case (3D) | **7.53 m** |
| Column offset 0 / 0.15 m | 7.25 / 7.77 m |
| f 1850 / 1920 | 7.43 / 7.62 m |
| Walking height 1.75 / 1.80 m | 7.40 / 7.60 m |
| Corner x 1158 instead of 1152 | 7.67 m |

- **Size checks:** the far columns are 2.17 m apart (centre to centre), and the near-door columns about 1.6 m apart. Both are plausible.
- **Second-route check:** facade route 1 gives 7.42 m and route 2 gives 7.34 m (column offset 0, before the near-column correction).

## Confidence
Moderate. The view of the facade is grazing: a 0.1 m error in a pillar's distance from the wall moves it about 0.35–0.55 m along the facade. The main uncertainties are:
- how far the near column's axis stands in front of the wall (±3.5%);
- the scale from the walker's walking height (±2%);
- f (±1.5%).

If the cyclist's depths were taken as the scale (with a 0.15 m curb), the answer would be about 7% larger (about 8.1 m). I used the exact walker-height prior instead.

## Scripts
- `vvp.py`, `vvp_fit.py`: vertical vanishing point.
- `linefit.py` with `segs_*.json`, `hlines.py`: line fits for the vanishing points.
- `kiosk_vp.py`: kiosk-edge vanishing points.
- `calib.py`, `calib2.py`, `fcheck.py`, `fcheck2.py`: focal length and scale-consistency checks.
- `geom.py`, `facade.py`, `final.py`, `final2.py`: the 3D reconstruction.
- `jac.py`: pixel per metre along each axis at the pillars.
- `profiles.py`, `colprof.py`: intensity profiles for pillar and post edges.
