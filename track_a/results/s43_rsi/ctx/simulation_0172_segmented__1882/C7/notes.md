# Measurement notes

- Question 1882: astronaut speed at 0.5 s, in m/s.
- Answer: **1.604 m/s**.
- File and question frame rates both equal 24 fps. The requested backward difference is between frames 11 and 12.
- Only the supplied video, the astronaut height prior (2.2 m), and the camera distance at frame 24 (18.147 m) were used. No external size reference was used.

## Image measurements

The foreground was extracted from the white background using a threshold and the largest connected component. The astronaut bounding boxes at frames 0, 12, 24, and 36 have heights 342, 342, 380, and 411 px. Leg articulation makes these raw heights unsuitable as a constant depth cue.

Rigid upper-suit and backpack features were tracked with Lucas–Kanade flow. Similarity transformations transfer a pelvis reference point near (790, 875) in frame 12. Its local displacement is approximately 9.1 px horizontally and 3.5 px vertically per frame. Point overlays and separate region masks are saved in `frames/`.

For scale, approximate extended head-to-sole chains were measured independently in frames 0 and 12, with landmarks and annotated images saved by `finalize.py`. After correcting the first pose to the frame-12 apparent scale, they yield 366.26 and 379.45 px. Their mean is 372.86 px for the supplied 2.2 m height. This pose correction is approximate: it assumes the visible segment lengths adequately represent the extended height. The two measurements differ by 3.5%.

## Geometry and time convention

Assuming the principal point is the image center (1152, 648), the height and frame-24 distance imply a focal length of about 3244 px (horizontal field of view approximately 39 degrees). The tracked frame-24 pelvis is about (1067.7, 801.9), and its axial depth is 18.1205 m; its Euclidean camera distance is therefore 18.147 m, reproducing the supplied depth. The approximate frame-12 axial depth is 19.1427 m.

Relative rigid-feature scale provides local axial-depth changes. Positions are back-projected with the pinhole model. A local quadratic fit over frames 9–14 suppresses compression and feature-localization noise; the fitted positions at frames 11 and 12 are differenced and multiplied by 24. The fit stops before the marked change in motion at frame 15.

## Independent checks and uncertainty

1. Sequential backpack tracking gives 1.702 m/s. Expanding the local window to frames 8–14 gives 1.694 m/s.
2. Direct registration of each nearby frame to frame 12, using a separately detected backpack feature set, gives 1.506 m/s; the expanded window gives 1.523 m/s.
3. Tracking the larger upper-suit region gives 1.699 m/s, close to the sequential route.

The principal disagreement is in depth velocity: roughly 0.45 versus 0.86 m/s, while the image-plane velocity components agree closely. A per-frame scale change of only about 0.1–0.2% is difficult to distinguish from compression, minor articulation, and feature-set changes. The reported answer averages the two backpack routes (1.604 m/s), rather than treating either noisy scale derivative as exact.

Confidence is moderate. The remaining uncertainty is mainly depth velocity and the interpretation of the 2.2 m height under a bent-leg pose, approximately 10–15% overall. There is only one supplied depth and one known object size, so two fully independent absolute geometric calibrations are unavailable; the checks above reuse the allowed prior in different frames and use independent tracking routes.

## Reproduction

Run the supplied Python interpreter on `measure.py`, `track.py`, `check.py`, `backpack_track.py`, and `finalize.py`. These scripts decode frames on demand and retain only small measurement arrays. Numerical geometry and route comparisons are in `geometry.json`; the benchmark output is in `answers.json`.
