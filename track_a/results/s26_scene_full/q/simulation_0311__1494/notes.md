# Q1494 – speed of the car at t = 2.0 s (frame 48), m/s  → **6.05 m/s**

The file and question frame rates are both 24 fps, so t = 2.0 s is frame 48. The camera is static, and the scene/ record's car track was checked and used only for rough pixel positions.

## Geometry (all measured in code)
- **Vertical vanishing point** from the centre lines of three poles (colour segmentation, robust line fits, `poles2.py`):
  (1271.7, 12242). The three pairwise intersections agree within 3 px.
- **The car moves as a pure translation in a straight line.** I tracked about 250–320 LK features on the car (`foe.py`). Every
  window (29–45, 34–62, 40–56, 50–71) gives the same focus of expansion, FOE ≈ (−1128, −869) ± 7 px, and the tracks
  are straight (rms < 1 px).
- Since 1/Z ∝ (pixel distance to the FOE), the per-frame depth growth is smooth and constant from about frame 20 to 71 (`zrate.py`),
  so the speed is **constant**. The speed at 2.0 s equals the steady speed.
- **Focal length**:
  - The FOE must be perpendicular to the vertical (car moving on level ground): f = 4286.
  - The car's tail-light pair must be perpendicular to the heading (symmetry test, `symtest.py`): f ≈ 4380.
  - The rim ellipse axis ratios (`rimfit.py`) favour f ≥ 4300; they clearly reject 3600.
  - The car's height/wheelbase ratio matches a LaFerrari's at f ≈ 4300–4450.
  - **Used f ≈ 4350 ± 100.**

## Scale and speed (motion stereo, `sfm2.py`, `speed_final.py`)
For a translating rigid body, each feature's depth is Z(k) = (1/D(k))/slope, in units of Tz (the per-frame z-step).
This gives a 3D model of the car in Tz units. The pieces:
- Rear-left hub: the rim ellipse centre, with depth from the features around it.
- Tyre radius: the tyre bottom edge sits 1.15–1.25 visible-rim radii below the hub along the image vertical (`tyre.py`), corrected
  for foreshortening.
- Roof top: the highest canopy features, 3.7–4.0 Tz above the hub.
- Height H = roof − ground = about 5.4–5.7 Tz. With the prior H = 1.15 m this gives Tz ≈ 0.205–0.213 m.
- Speed = Tz / m_z × 24, where m_z = 0.832 (heading z-component at f = 4350).

| f | height route (1.15 m prior) | wheelbase check (LaFerrari 2.65 / 2.73 m) |
|---|---|---|
| 4286 | 5.79–6.03 | 6.03 / 6.21 |
| 4350 | 5.90–6.14 | 6.03 / 6.21 |
| 4450 | 6.08–6.32 | 6.03 / 6.22 |

**Second route:** with the height-derived scale, the car's wheelbase comes out at 2.58–2.74 m, its rear half-track at about 0.95 m,
and its tail lights 1.56 m apart. All of these are consistent with a real LaFerrari scaled ×1.03 to the 1.15 m height. The wheelbase route
is almost independent of f and gives 6.0–6.2 m/s. The final answer is the centre of both routes: **6.05 m/s**.

## depth_info is inconsistent with the video (not used for the scale)
- The given values (17.83 m at frame 24, 23.20 m at frame 48) need a depth ratio of 1.30.
- The image gives Z48/Z24 = 1.22–1.24 for every point on the car. This does not depend on f. Two independent checks agree:
  - FOE distances.
  - The rear rim's major axis: 109.4 px at frame 24 and 87.3 px at frame 48, a ratio of 1.25.
- No time offset of 24 frames reaches a ratio of 1.30 either.
- So the depth_info origin cannot be a point on the car body in these frames. An offset object origin would explain it, and with pure
  translation the speed is unaffected. The scale therefore comes from the exact height prior, plus car-proportion checks.
- Had I trusted d48 = 23.2 with an on-car origin, the speed would be about 5.3 m/s. That contradicts the 1.15 m height prior unless
  f ≈ 3800, which the symmetry, rim and proportion tests reject.

Confidence: moderate. The estimate is likely within about ±5%. The main uncertainties are the roof-peak and tyre-bottom heights,
and f within ±2%.
