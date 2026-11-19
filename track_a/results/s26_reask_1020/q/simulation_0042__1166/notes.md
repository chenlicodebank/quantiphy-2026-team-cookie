# q_1166 – eagle length (m)

Prior: eagle speed = 11.84 m/s. Depth to eagle 179.27 m (t=1) → 177.10 m (t=2), so −2.17 m/s along the line of sight
and ≈11.64 m/s across it. question_fps = file fps = 24.

Method (measure.py, final.py):
- Bird tracked using scene/tracks/bird.csv centroids (checked on zoomed crops in frames/crops.png; the black eagle flies left→right,
  tail at left and head at right, heading about 15° below the image x-axis).
- Body length in pixels: for each frame, threshold the bird at half-way between black and the local background, then take the mask extent
  along the flight direction (the local chord over ±6 frames). It is 27–29 px when the wings are not spread along the
  body axis. Frames 29–34 and 53–59 are excluded: there the wing sweep or flap shape lengthens the extent, or the bird
  is over dark water and has low contrast.
- Pixel speed: centroid chord over ±6 frames, which removes the wobble from wing flapping: 16.4→17.5 px/frame (mean 16.88).
- The body is aligned with the motion, so the ratio of pixel length to pixel speed cancels both foreshortening and the scale:
  L = (11.84/24 m/frame) × (L_px / v_px). Mean L_px/v_px = 1.687 (38 frames, std 0.03) → **L = 0.832 m**.

Checks:
- Splitting the frames into two windows gives 0.827 m (frames 9–28) and 0.838 m (frames 35–52).
- If the body is level while the bird descends toward the camera, using the cross-view speed of 11.64 m/s gives 0.818 m (−1.7 %).
- Pinhole check: 0.0287 m/px at about 178 m gives f ≈ 6200 px (horizontal field of view about 10°). With this scale the wingspan peaks at 1.6–1.8 m
  and the boat is about 10 m long. Both are plausible, and an eagle 0.83 m long is realistic (golden eagle 0.66–1.0 m).

Confidence: good (about ±5 %). The main uncertainty is ±1 px in the threshold edge on a 28 px extent.
