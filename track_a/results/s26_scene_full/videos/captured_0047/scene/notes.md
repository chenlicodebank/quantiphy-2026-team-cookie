# captured_0047 — measurement record (pixels, seconds)

Lab video, 3D, 1280x720, 24 fps, 49 frames (t = frame/24, 0–2.0 s). **Camera is static** (background shift < 0.2 px, `tracks/camera_shift.csv`).
Benchmark intrinsics for this camera: f = 0.5959·1280 = 762.8 px, principal point ≈ (640, 360). These come from the stated convention, not from this video.

## Scene
A person with long dark hair, black top and trousers and white sneakers squats against the back wall in a room corner. They hold a large grey exercise ball in front of their knees, push it toward the camera and release it. The ball rolls across the floor toward the camera and to the left (it moves down and left in the image), then leaves through the bottom edge. Static items: a black wall screen at the top centre, two grey tripod stands (left near the corner, right), a near partition at the right edge, grey padded walls, and the floor with dark baseboard lines. Pixel positions are in `scene.json`.
The video was processed with the SAM2 demo: the background is artificially blurred (the person and ball are sharp), the face is greyed out, there is a watermark at the bottom right, and a bright strip covers rows y ≥ ~712. Treat **y ≈ 711 as the effective bottom edge**.

## Files
- `scene.json`: inventory, static-object pixel positions, perspective cues, events, apparent-size summary.
- `tracks/ball.csv`: one row per frame.
  - `cx,cy,diameter`: least-squares circle fitted to the outline of a GrabCut ball mask (robust, image-border points excluded). This is the **visible centre** reference point.
  - `mask_cx,mask_cy`: centroid of the visible mask. It is biased upward once the ball is cut off.
  - `bbox_*`: visible mask bounding box. `mask_len_main_axis`/`mask_width_cross` come from PCA of the visible mask. `mask_area`, `area_equiv_diam`.
  - `circle_arc_coverage_deg`: how much of the outline supports the circle fit.
  - `diam_trend`: diameter from a linear fit of 1/diameter vs frame over frames 17–33 (rms 4 px). It is extrapolated after frame 33.
  - `cx_fixedR,cy_fixedR`: centre fitted to the visible arc with the diameter fixed to `diam_trend`, for frames 16–46.
  - `pass1_*`: the noisier first pass.
  - Flags: `visible`, `truncated_by_frame_edge`, `occluded_by_person_hands` (frames 0–17), `circle_reliable`.
- `tracks/ball_pass1.csv`: first-pass RANSAC circle on Canny edges, superseded.
- `tracks/person.csv`: GrabCut mask of the person's dark clothing and hair (bare forearms/hands and white shoes are not included). Gives centroid, bbox and area per frame. Frames ≤ 24: the lower body is partly hidden behind the ball.
- `tracks/camera_shift.csv`: phase-correlation shift of two background patches.
- `scripts/`: `track.py` (pass 1 + person zone), `refine_ball.py` (final ball), `person.py`, `camera.py`, `finalize.py` (visibility flags + scene.json), plus probe/crops helpers. Pass 1 must be copied to `ball_pass1.csv` before `refine_ball.py` runs.

## Key numbers
- Ball at rest, frames 0–13: centre (566.2, 495.0), diameter **113.9 px** (±1); bbox x 510–621, y 438–552. Bottom of ball (floor contact) at y ≈ 552.
- Ball diameter over time: 114 (≤13), 117 (15), 122 (17), 129 (19), 140 (21), 150 (23), 158 (25), 174 (27), 185 (29), 202 (31), 207 (33), ~225 (35), ~248 (36), ~275–290 (38), ~310–333 (40). It grows as the ball approaches the camera.
- Centre path: (566,495) at frame 13 → (536,524) at 21 → (501,559) at 26 → (453,602) at 31 → (395,648–660) at 35 → (~321,707–717) at 38 → (~275,746–760) at 40 → (~222,820–834) at 42 (the last ones are outside the image).
- Squatting person (frame 45): head top y 348, shoe bottom y 540 (**192 px**), elbows x 522–645. The person does not translate.

## Events
- Held still: frames 0–13.
- Push begins: frame 14 (t = 0.583 s); first clear change at frame 15.
- Release (hands leave the ball): frame **18** (t = 0.75 s), ±1.
- Rolling on the floor toward the camera: frames 18–46. There is no bounce; the ball's bottom edge moves smoothly downward.
- Ball first reaches the bottom image edge at frame 30. Its centre leaves the image at about frame 38. Last sliver visible at frame 46. Gone in frames 47–48.
- Person: arms on the ball 0–17, raised 18 to ~40, folded over the knees ~41–48.

## Reliability and ambiguities
- **Frames 0–33** (full outline visible): centre ±1–2 px, diameter ±3 px. The outline is distorted by motion blur and compression or interpolation smear (for example frames 19 and 32), so the per-frame diameter jitters by a few px. Smooth over several frames if needed.
- **Frames 34–39** (bottom cut off, arc coverage 180–260°): the free-fit diameter and the trend disagree by up to ~7%. Two estimates are given (`cx,cy,diameter` and `cx_fixedR,cy_fixedR,diam_trend`).
- `circle_reliable` is 0 from frame 38 on (arc coverage < 200°).
- **Frames 40–46**: only the top cap is visible. The free fit is unreliable, and the trend values are extrapolations; use them with caution. The visible `bbox_y0` (top of ball) and the chord width are direct measurements.
- Frames 0–17: the hands and forearms cover the top rim of the ball. The fit uses the remaining outline, and the static values are very stable.
- Static-object coordinates (screen, stands, floor lines) were read by eye from gridded frames on a blurred background: ±5–10 px.
- No metric scale was assumed. The ball's real diameter, its depth and any speed must come from each question's prior.
