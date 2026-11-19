# Q1121: length of the boat (m). Answer: 9.9 m

The file runs at 25 fps but question_fps is 24, so t=1 s is frame 24 and t=2 s is frame 48. I used the frame columns from scene/tracks.

## Focal length from the eagle prior (solve.py)
- Eagle centre (bird.csv, cx_interp/cy_interp, with light linear smoothing over ±0–5 frames): (235.6, 521.8) at frame 24 and (409.7, 527.8) at frame 48.
- I back-projected each point with its given depth (139.70 m and 147.16 m) and the principal point at the image centre. Then I solved for the f that makes the 1 s displacement 12 m (constant speed: the eagle's pixel speed is steady at about 7.3 px/frame).
- Result: f = 2644–2652 px across all smoothing and centre variants. I used **f = 2646 px** (hFOV 20.6°).

## Boat (boat.py, fit_hull.py)
- I back-projected the hull-box centre with the boat depths at t=1 and t=2. The boat moves at 4.12 m/s, heading about **41.6° from the image plane toward the camera** (bow at the left).
- The frames confirm this orientation: the front face of the wheelhouse is clearly visible (about 21 px), next to its side (about 26 px).
- A naive conversion, 164 px x 134 m / f, gives 8.25 m. That is the foreshortened projection, so it is not the length.
- **Model:** a perspective model of the hull outline in top view, placed on the straight 3D trajectory through the two depth-anchored points. I fitted it to the measured hull pixel length (length_px_hull) in all 75 frames. That length grows 157→176 px, about 4.7% more than the depth change alone would explain, because the viewing angle changes. This growth constrains the yaw and beam terms.
- **Results:**
  - Tapered hull (pointed bow, transom): L = 9.6–10.2 m for B/L between 0.4 and 0.25. A joint fit of L and B gives L = 10.24 m, B = 2.2 m, rms 0.84 px.
  - Box hull: L = 8.2–9.0 m, which fits worse (rms 1.1–1.6 px). A joint fit gives L = 10.2 m with a nearly zero beam.
- **Answer:** L ≈ 9.9 m (tapered, B/L ≈ 0.3).

## Checks
- **Second route:** the wheelhouse face ratio implies a front-to-side ratio of about 0.9 at yaw 42°, which is plausible. The growth of the pixel length over time is reproduced only with yaw near 42° and a small beam term, consistent with the hull model.
- **Confidence:** moderate, ±8%. The main uncertainties are the hull plan shape (beam contribution) and the assumption that the boat moves along its own axis.
