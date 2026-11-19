# Q1367 – height of the turning yellow car (taxi), metres

The file rate and question_fps are both 24, so t=0.58 s is frame 14 and t=1.58 s is frame 38.
The asked object is the yellow taxi (`taxi` in scene/). The prior's object is the white car, i.e. the van (length 6 m).

## Camera (independent of the record)
- Background = median of frames 0/20/40/71 (`bg.py`). Road–sidewalk kerb edges were found from the saturation gradient
  and fitted as lines (`vp.py`, rms 0.4–0.7 px). The two road directions give the vanishing points
  VA = (-1296, -258) and VB = (2689, -259). With the principal point at the image centre and the roads orthogonal,
  f = 1785 px (horizontal FOV 63°). The optical axis is tilted 24.1° down and there is essentially no roll (`cam.py`).
- Camera height h comes from the depth_info, treating each origin as the ground point under the object's centre
  (`solve_h.py`, `solve_van.py`, `check_bike.py`, `check_taxi14.py`):
  - taxi f38: 9.27–9.34
  - taxi f14 (sign-foot route): 9.37–9.43
  - van f14 / f38: 9.43 / 9.56
  - cyclist: 9.44–9.61
  - pedestrian (pelvis): 9.62–9.69
  - Adopted h = 9.40 ± 0.15. This leans on the taxi's own depths but sits close to the overall median.

## Taxi height
- Reads taken by hand from zoomed crops (`crop.py`): bottoms of the near-side tyres and the top of the roof sign at
  frames 38, 50, 60 and 71.
- The tyre contacts are back-projected onto the ground to get the car axis. The sign sits on the car's centre line,
  offset w across the car and a along it.
- Joint least-squares fit over the four frames (`joint.py`): w = 0.89 m, a = -0.47 m, H = 1.627 m at h = 9.295.
  - Residuals are at most 1.7 px.
  - The wheelbase comes out at 2.90–3.04 m, which matches a real Crown Victoria (2.91 m), so the scene is at about
    real scale.
- Frame subsets gave H = 1.61–1.66 at h ≈ 9.3. A taxi origin 0.7 m above the ground changes H by +0.01.
- H scales with h, so at the adopted h = 9.40, H ≈ 1.627 × 9.40 / 9.295 ≈ **1.65 m**. The bounding box runs from the
  ground (tyre bottoms) to the top of the roof sign.

## Checks
- Second route: frames 38+50, 38+60, 38+71 and 50+60+71 each give H between 1.61 and 1.66 at h ≈ 9.3.
- Sanity check: a real Crown Victoria is 1.47 m tall, plus a roof sign of about 0.2–0.3 m, giving roughly 1.7 m.
- I could not directly check the van's 6 m length: its bumper ends are not cleanly visible on the ground. Its
  depth-based h (9.43–9.56) agrees with the taxi's to within 2–3 %.

## Confidence
Moderate. The main uncertainty is the spread of h across objects (±2 %) and the sign's lateral offset (±0.05 m).
Estimated error is ±4 %, giving a range of about 1.60–1.70 m.
