# Q13: speed of the boat at t = 1.0 s (m/s). Prior: person height = 1.75 m. No depth_info.

Answer: **4.15 m/s** (plausible range about 3.6–4.7).

## Time base
The file fps (24) and question_fps (24) match. t = 1.0 s is frame 24. Frame 1 duplicates frame 0, which does not matter at frame 24.

## Boat pixel velocity (scene/tracks/boat.csv template track, checked with speed.py)
- The boat moves in a straight line at constant speed. A linear fit over frames 24±5, 24±8 and 24±12 gives v = (−5.712, −1.600) px/frame, |v| = 5.93 px/frame.
- The raw backward difference at frame 24 is 5.98. The per-frame steps scatter by ±0.3 px of tracking noise, so I used the fitted value.

## Why I did not use a plain "2D" scale
The scene is labelled 2D, but the camera is clearly oblique. The person's whole body and the boat's hull side are visible.
- With one metres-per-pixel scale from the person's height (45 px = 1.75 m), the speed would be 5.5 m/s.
- That scale is wrong for horizontal motion: a vertical person is foreshortened by about sin(tilt), and ground motion has a different scale.

So I set up an affine camera with tilt θ from nadir and a weak perspective correction:
- **Person scale.** I measured head-top-to-sole extent at the feet-together, mid-stance frames 17, 34, 51 and 67 (person_extent.py): 39.5, 38.3, 38.5, 39.7, so about 39 px. At full stride it is about 48 px, because the leading foot reaches toward the camera.
  - The model: E0(θ) = 1.64·sinθ + 0.11 (head) + 0.17·cosθ (toe) metres, and k_person = 39 / E0 px/m.
- **Perspective.** A sub-pixel template scale search on the boat (scale_fine.py) gives d ln(scale)/dy = 7.4e-5 per px. The boat at y ≈ 955 is therefore imaged 4.0% larger than the person at y ≈ 430.
- **Tilt θ.** The evidence disagrees, so I took a compromise of about 33–35°:
  - Gait (gait.py): the planted-foot plateaus are 25.5 px apart along the image vertical and the cadence is 1.37 steps/s. A natural step of 0.75–0.9 m needs θ ≈ 28–35°. At 45° the step would be 1.2 m.
  - Person width: 15.6 px across the arms. A width of 0.45–0.5 m needs θ ≈ 33–43°.
  - Boat edges (roof.py, hatch.py): the cabin roof and hatch edges give the image direction of the boat's transverse axis. They suggest roughly 39–50°, but the roof overhang and hatch side faces bias those edges.
  - Field of view: the perspective gradient means tanθ / f ≈ 7.6e-5. If the field of view is at least about 7°, θ is at most about 33–35°.
- **Ground speed.** Image x maps straight to ground x. Image y is divided by the local cos(tilt), about 0.85 at the boat row.

## Result
| θ | k_boat (px/m) | speed (m/s) |
|---|---|---|
| 28° | 39.4 | 3.64 |
| 33° | 35.4 | 4.07 |
| 35° | 34.1 | 4.24 |
| 38° | 32.3 | 4.49 |
| 45° | ~31 | ~4.7 |

I answered 4.15 m/s.

Sanity check at θ ≈ 34°: the boat is about 9 m long with a 2.5 m beam, cruising at about 8 knots, and the person walks at about 1.2 m/s.

## Confidence
Medium. The main uncertainty is the camera tilt, which is worth about ±10%. The pixel velocity is good to under 1%, and the person's pixel extent to about 2%.
