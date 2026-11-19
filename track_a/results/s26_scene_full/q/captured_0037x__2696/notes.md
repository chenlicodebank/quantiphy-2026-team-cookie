# q 2696 – width of the tape (cm)

Lab video, 24 fps (file fps = question fps = 24), 1280x720. Camera static. f = 0.5959 x 1280 = 762.8 px.
depth_info: tape at 1.038 m (t = 1.0 s; the tape does not move).

The object is a pale yellow tape roll lying flat on the table between the glass jar and the card tent
(scene bbox 521–591 x 430–473, which I confirmed on frames 0, 2, 5, 24 and 48).

## Measurement
- `measure_tape.py`: threshold mask (V > 175, S < 80). Its horizontal extent is 67–68 px in every checked frame,
  so it is static. A threshold mask cuts off the soft edges, so it reads low.
- `edges.py`: mean of frames 0–6 and 22–26. Half-max sub-pixel edge crossings on rows 436–459, on both the black
  background (upper rows) and the table (lower rows). Left edge ≈ 520.5–521.6, right ≈ 591.1–592.4.
  Width = 70.5–71.8 px (median 71.7, about 70.6 on the table rows). I used 71 px.
- Width = 1.038 m x 71 / 762.8 = **9.66 cm**, with a range of 9.6–9.76 cm across the rows. Answer: 9.7 cm.

## Ambiguity in the name
The roll is round and lies flat, so its horizontal extent in any direction is the outer diameter. I followed the
benchmark convention (width = horizontal extent): **≈ 9.7 cm**.
Other reading: the tape strip width, which is the roll's vertical height here. The silhouette spans 43 px vertically
(y 430–473), and this includes the top ellipse. That gives roughly 39–41 px of side, i.e. about 5.3–5.6 cm (a packing-tape
width of about 4.8–5 cm is plausible). This value is less precise. I did not use it.

## Check
Scale check using the prior's ball: at t = 1.0 s (frame 24, near the apex) the ball should be 4 x 762.8 / 105.5 = 28.9 px.
The record's mask gives 24.6 (minor axis) to 31.8 (equivalent diameter, includes some blur). This agrees within the
mask's accuracy, so the camera-card focal length is consistent with the scene. I also checked the width on several
rows and frames and against two backgrounds: 70.5–71.8 px, a spread of about ±1%.
Confidence: high for the diameter (±3%). The main risk is the naming ambiguity.
