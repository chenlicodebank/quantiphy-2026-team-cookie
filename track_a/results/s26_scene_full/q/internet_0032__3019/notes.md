# q3019 – boat acceleration from the 0–2 s window to the 2–4.5 s window

- Prior: boat length = 3.5 m. Static camera (record: shift < 0.2 px). Single planar scale, as the annotators used.
- Time base: question_fps 30 vs file 29.85. The difference is 0.5%, and the results agree to within 0.001 m/s². I used 30: frames 0, 60, 135.
- Track: scene/tracks/boat.csv hull centre (bow/stern midpoint). Spot-checked on zoomed frames 0, 60 and 134; the bow and stern tips match within ~2 px.
- Hull pixel length: 212 px at frame 0, 226 px median over 0–4.5 s, 232 px whole-clip median. The boat approaches the camera, so the length grows.
- Hull centre x: 866.5 → 784.5 → 672.0. That is 82 px in 2 s (41 px/s) and 112.5 px in 2.5 s (45 px/s).
- a = (v2 − v1) / (time between window midpoints, 2.25 s):
  - scale from frame-0 length (212 px): v1 = 0.677 m/s, v2 = 0.743 m/s, a = 0.029 m/s²
  - scale from mid length (226 px): a = 0.0275 m/s²
  - linear fit inside each window instead of endpoints: 0.021–0.022 m/s²
- Second route: the two people's x centres give a = 0.020 for the rower, who moves with the strokes, and 0.034 for the stern person. Their mean is 0.027.
  The bow alone gives 0.022–0.025 and the stern alone 0.031–0.035. Part of the apparent speed-up is perspective, since the scale grows as the boat approaches.
- Answer: 0.028 m/s² (endpoint method, scale between the frame-0 and mid-window lengths).
- Confidence: low to moderate. The acceleration is small (a ~10% change in speed), so the convention and point choice give a spread of ±25%.
