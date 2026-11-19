# Q1707: average speed of the boat (m/s). Answer: 4.03

The file runs at 25 fps, but the question uses 24 fps. All times use 24 fps: t = 1 s is frame 24 and t = 2 s is frame 48. Speeds are per-frame differences × 24.

## Boat motion (3D, camera fixed)
- Distance from the camera to the boat: 130.349 m at frame 24 and 133.743 m at frame 48. The boat moves straight away from the camera at 3.39 m/s.
- I checked that the boat's apparent size follows these distances. Its bbox height ratio between frames 24 and 48 is 0.9785, against a distance ratio of 0.9746, so the distances fit the boat.
- The boat's reference point in the image is the bbox centre (scene track, frames 0–53, before the boat is clipped by the frame edge). It moves linearly at u −3.78 and v −1.62 px/frame, with an rms residual of 1.6 px.
- 3D position = D(t) × the unit ray through ((u−cx)/f, (v−cy)/f, 1). D is linear in t, and u and v come from the linear fits. Speed = mean of the per-frame |ΔP| × 24 (`boatspeed.py`).
- Result: f = 5000 → 4.28, 5500 → 4.14, **6000 → 4.03**, 6500 → 3.94, 7000 → 3.87 m/s.
- Other reference points (bow, the edge-robust ref point, all frames) change the result by 0 to +2.5%.

## Focal length (the key quantity)
- **The prior taken literally gives an implausible scene.**
  - The person's image speed is 1.34 px/frame = 32.2 px/s at about 140 m.
  - If all of that motion were across the view, 1.3 m/s would give f ≈ 3470 px.
  - With f ≈ 3470, the person (74.6 px tall) would be 3.0 m, the wheelhouse 4.9 m and the eagle's wingspan more than 4 m. So that geometry is wrong.
- **The person walks partly toward the camera.**
  - The person's given distance barely changes (139.954 → 139.983 m). This is the case where the character's origin stays put while its body walks.
  - Crops of the person (`frames/hstrip.png`) show a 3/4 front view, so the person is walking diagonally toward the camera and to the left.
  - The body also moves down in the image, which fits approaching the camera.
  - Over the clip the expected size change is about +2.4%. The measured size change is within about ±1.3% (bbox height trend −0.2% ± 1.3%; same-phase template scale +1.2% over 72 frames, −1% over 36). That is too noisy to pin the direction.
- **Focal length from standard objects:**
  - Person: 74.6 px tall at 140 m. A 1.75 m adult (about 1.72 m bbox height while walking) gives f ≈ 6070.
  - Eagle: maximum image wingspan 70 px at about 136.6 m. Its 3D flight direction is about 56° toward the camera, so the wings are foreshortened by about 0.83. A wingspan of about 2.0 m gives f ≈ 5760.
  - Wheelhouse: about 130 px tall at 130 m. A height of about 2.3–2.9 m gives f ≈ 5800–7300.
  - I used f ≈ 6000.
- **Check against the prior.** With f = 6000, the person's movement across the view is 0.75 m/s. With a total of 1.3 m/s, the movement toward the camera is 1.06 m/s, a walking direction about 55° toward the camera. That matches the 3/4 front view, so the prior and the standard objects agree.

## Second route and confidence
- Taking only the boat's distance change and its image motion, the boat moves 3.39 m/s away from the camera and about 2.3 m/s across the view at f = 6000. That gives |v| ≈ 4.03 m/s.
- If f is wrong by ±10% (5400–6600), the boat speed is 4.17–3.93 m/s, a spread of about ±3%.
- The scale comes from the standard objects (adult person, eagle, wheelhouse), cross-checked against the 1.3 m/s prior. The literal across-the-view reading of the prior (f ≈ 3470, answer about 5.2 m/s) was rejected because it makes every object about 1.7× too large.
