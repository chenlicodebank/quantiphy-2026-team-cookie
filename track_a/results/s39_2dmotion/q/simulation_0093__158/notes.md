# Q158 — speed of the plane at 0.5 s (m/s)

Prior: car length = 5.67 m. 2D video, file fps = question_fps = 24, so t = 0.5 s is frame 12 and the speed is the step from frame 11 to frame 12.

## Measurements (my scripts: measure.py, subpix.py, check_sam.py)
- **Plane pixel speed**: I took the contrast-weighted centroid of the tail fin (a rigid reference point).
  - Step from frame 11 to 12: −40.35 px.
  - Mean step over frames 10–14: 40.34 px. Mean over frames 2–18: 40.35 px. The steps stay within ±0.05 px, so the speed is constant.
  - The nose and tail edges agree: about 40.4 px per frame.
  - **Value used: 40.35 px/frame = 968.4 px/s.**
- **Car pixel length**: I found the sub-pixel crossings at half contrast of the column max-contrast profile.
  - Frame 12: 1076.03 → 1167.21, so 91.2 px.
  - Frames 0–14: 90.1–91.2 px (mean ≈ 90.8). Frames near the image centre give the minimum, about 90.5 px.
  - The car looks longer as it moves off-centre (96.5 px at frame 37). That is perspective on a 3D box, so I used the central and early frames.
  - **Value used: 91.0 px.** The scale is 5.67 / 91.0 = 0.06231 m/px.
- **Speed**: 968.4 × 0.06231 = **60.3 m/s**. Using 91.2 px gives 60.2 m/s; using 90.5 px gives 60.7 m/s.

## SAM 3 check
- **Plane** (frames 11 and 12):
  - Box left edge moves 317.5 → 277.1 (40.4 px). Right edge moves 39.6 px. Centroid moves 39.8 px.
  - Mean ≈ 40.0 px, within 1% of my 40.35 px.
- **Car** (frame 12):
  - The SAM mask spans columns 1073–1166 (94 px), 3.1% longer than my 91.2 px.
  - Its leftmost columns 1073–1074 have a contrast of only 4–6 against the background, which is background. I checked the zoomed overlay `frames/car12_sam_vs_mine.png`: the SAM outline bulges about 3 px past the rear of the car, while my edge lines sit exactly on the car's ends.
  - My measurement is correct and SAM's is too wide.

## Second route / sanity check
- The plane is 608 px long, which gives 608 × 0.06231 = 37.9 m. A real A320 is 37.6 m, so the two objects sit consistently in one plane.
- The scene record (40.36 px/frame, car 91 px) agrees with my numbers.

Confidence: high, about ±2%.
