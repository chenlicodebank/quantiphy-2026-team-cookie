# Measurement for question 1883

Answer: **0.574 m/s^2**, reported as a positive magnitude as requested. The fitted change of scalar speed is negative: the tracked body is decelerating at this instant.

## Inputs and time convention

- Exact prior: astronaut height 2.2 m.
- Camera-to-origin distance at frame 24 (1 s): 18.147 m.
- File and question rates both 24 fps; 0.5 s corresponds to frame 12.
- The calculation uses the speeds of displacements 10 -> 11 and 11 -> 12, multiplied by 24 to obtain the acceleration.

## Tracking and geometry

The white background was thresholded and the largest connected component measured one frame at a time. The astronaut's silhouette is strongly affected by limb movement, so its centroid was not used as the origin. A set of backpack features was tracked using pyramidal optical flow. Robust similarity transforms map an approximate hip/root point (795, 875) in frame 12 into adjacent frames. Masks and tracked points are saved in `frames/pack_mask.png`, `frames/track_12.png`, and `frames/hip_mask.png`.

There is a distinct movement transition between frames 14 and 15. All local acceleration fits end at frame 14, before that transition. Four quadratic position fits begin at frames 1, 3, 5, and 7 respectively. No fit crosses the transition.

The silhouette height is 342 px at frame 12, 380 px at frame 24, and reaches 418 px at frame 42. Correcting the full-clip heights by the tracked backpack scale gives a maximum equivalent height of 373.49 px at frame-12 scale. I used an estimated standing equivalent of 380 px, allowing for the remaining knee bend and orientation. This standing-height interpretation is an assumption, not an independently measured exact quantity.

The backpack scale at frame 24 is 1.0513 relative to frame 12. Combining the equivalent height with the exact height and distance gives focal length 3290.85 px, using image centre (1152, 648) as principal point and treating the supplied distance as Euclidean range. The axial depth at frame 24 is 18.12214 m. The resulting 3D point has Euclidean norm 18.147 m by construction.

The local scale changes only slightly. A linear fit over frames 1-14 gives scale(t) = 0.98499409 + 0.03011022 t. I regularized this scale change to linear because its second derivative cannot be distinguished reliably from pose changes and subpixel tracking errors. Depth at the other frames is inferred from the inverse scale. Root image coordinates are back-projected with those depths and the estimated focal length.

The provided data contain only one exact size and one distance at one time. Consequently, two fully independent metric focal-length calibrations are not possible. A direct frame-24 silhouette-height calibration would give about 3130 px, approximately 5% below the adopted standing-height estimate; this is consistent with a bent walking pose. No external object size or external data were used.

## Results and second route

Backpack/root estimates of the signed scalar acceleration:

- Frames 1-14: -0.5740 m/s^2.
- Frames 3-14: -0.5934 m/s^2.
- Frames 5-14: -0.5733 m/s^2.
- Frames 7-14: -0.5614 m/s^2.

The median magnitude is 0.57365 m/s^2. Representative speeds at frames 11 and 12 are 1.5664 and 1.5425 m/s. These are physically plausible at the supplied height scale.

An independent broader torso feature set gives approximately -0.64 to -0.74 m/s^2. Its larger variation is associated with shoulder and arm deformation. Direct tracking of a hip image patch gave substantially different results; inspection showed that the visible patch includes the rotating upper thigh, so that route is unsuitable for estimating the rig origin. The backpack method is preferred because it samples a rigid part and is stable across local fitting windows. The difference between the torso and backpack estimates remains a systematic uncertainty rather than proof of exact recovery.

Confidence: **low to moderate**. The window-to-window variation of the preferred estimate is small, but the unobserved rig origin, standing-height interpretation, and weakly constrained depth acceleration limit accuracy. A 5% error guarantee is not justified by these images.

## Reproduction

All measurement scripts are in this folder. `measure.py` measures silhouettes; `track.py`, `packtrack.py`, and `hiptrack.py` track features; `calibrate.py`, `fit_geometry.py`, `analyze.py`, `estimate.py`, `final_measure.py`, and `sensitivity.py` provide diagnostic checks. `solve.py` computes the final geometry and backward speed differences and writes `answers.json` and `results.json`. Frames were decoded as needed; no full-resolution video array was retained.
