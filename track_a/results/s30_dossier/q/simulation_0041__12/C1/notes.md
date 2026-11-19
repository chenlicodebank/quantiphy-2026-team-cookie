# Q12: width of the boat (m). Prior: the person is 1.75 m tall. No depth_info.

**Answer: 3.32 m.** Estimated uncertainty is about ±6%.

## Time base
The file is 24 fps and question_fps is 24, so there is no re-timing. Time does not enter a size question anyway.

## Geometry: an oblique, narrow-angle pinhole camera (not a 2D scene)
The view is oblique, not top-down: the person stands upright and the boat's hull side is visible. I calibrated the camera from the video itself, with the principal point taken as the image centre.
- **Mast lean** (`mast.py`): the mast centreline was fitted in 16 frames as the boat crosses the image. Its lean changes linearly with x, which puts the vertical vanishing point at about (470, 4960).
- **Boat scale** (`scalechk2.py`): the boat's apparent scale relative to frame 30 shrinks smoothly, by 1.03e-4 per pixel as it moves up the image. That puts the horizon about 8760 px above the centre.
- **Joint fit** (`camfit.py`): f = 6223 px (horizontal field of view 9.9°), tilt θ = 54.6° (about ±1°), roll −0.9°. The residuals are at the noise level.
- **Independent check**: treating the cabin roof and aft wall as a box (conjugate directions) gives θ ≈ 54°.

## Scale from the person (`person_h.py`, `person_sub.py`)
- The head-top to lowest-toe extent was measured at the half-contrast edges.
- The extent is smallest at mid-stance, when the swing foot passes the planted foot (frames 17, 34, 51, 68): **38.8 ± 0.5 px**. The scene record's 45 px is the median over the whole gait, which includes the stride.
- Person model: the head top is at 1.75 m (a head sphere of radius 0.10 m centred at 1.65 m), above the ankle. The toe tip is 0.15–0.17 m ahead of the ankle, toward the camera.
- Solving the pinhole model for camera height gives H ≈ 156 m above the ground or water plane.

## Boat width (`topview.py`, `tvedges.py`)
- I rectified frame 30 to a metric top view on a horizontal plane at gunwale height. The boat axis comes from the boat's straight-line motion (track frames 2 to 60).
- **Near gunwale** (white/red boundary): maximum distance from the bow axis 2.03 m, at 4.0–5.2 m aft of the bow.
- **Far gunwale**: deck edge measured at 2.0–2.7 m and 5.0–6.0 m aft. The cabin hides the stretch in between, so a cubic fit fills it: maximum about 1.21 m.
- Perpendicular beam at the camera solution H = 151.9 m: 3.24 m. Rescaled to the half-contrast person extent (38.8 px) and a toe offset of 0.15–0.17 m, this gives **3.28–3.32 m**.
- The beam does not depend on the assumed gunwale-plane height (0 to 2 m changes it by less than 1.5%).
- The world-AABB width is taken as the beam, i.e. I assume the boat is axis-aligned in its scene.

## Second-route check
- An affine estimate uses the image width across the axis (98 px), the boat-local scale (person scale × the perspective ratio 1.06) and the foreshortening sin 58.4°. It gives 3.34 m.
- Plausibility: boat length ≈ 10.7 m (length/beam ≈ 3.2), boat speed ≈ 4.2 m/s, person walking speed ≈ 1.45 m/s. All are sensible.

## Sensitivity (`sens.py`)
- Tilt ±1° changes the width by about ∓2.5%.
- Toe offset 0.12–0.20 m: 3.21–3.39 m.
- Person extent ±0.5 px: about ±1.3%.
- Main residual risks: the person-model assumptions, and whether the hull is wider below the gunwale.
