# q_2988: speed of the toy truck at 0.50 s (cm/s)

Prior: total height of the sofa = 90 cm. depth_info: none. question_fps is 30 and the file rate is 30.0003, so t = 0.50 s is frame 15.

## Main problem: the prior's object is not visible
The background was replaced with white, so the sofa does not appear in any frame (checked on the contact sheet and on frame 15). Its pixel height cannot be measured. The scale therefore had to be estimated from body proportions at about the people's depth. This is the dominant uncertainty.

### Scale estimate
SAM 3 "head" masks at frame 15:
- **Man's head:** 126 px from crown to chin (box 816-922 x 59-184). The head is tilted forward. Taking about 23-24 cm (vertex to chin plus hair) gives about 0.19 cm/px. The man's feet are lowest in the image (y≈500), so he is the closest to the camera.
- **Child's head:** 82 px vertical and 87 px along the long axis. Taking about 17-18 cm for a toddler gives about 0.21 cm/px. The child is the farthest of the three (bottom at y≈443).
- **Truck:** its wheels touch at y≈480, so it is between the two. Interpolating gives about 0.20 cm/px. Sanity check: this makes the truck 41 cm long and its wheels 12 cm across, which is plausible for a toy dump truck.
- **Sofa:** a sofa in a living-room background most likely stands behind the people. A scale taken from it would then be somewhat coarser (more cm per pixel). I used **0.215 cm/px** as a compromise. The plausible range is 0.19-0.25.

## Truck speed in pixels (`measure_speed.py`)
- **Mask:** my own non-white connected-component mask. Its centroid matches scene/tracks/truck.csv to within 0.1 px. SAM 3 "toy truck" at frame 15 gives centroid (652.5, 396.5) and a horizontal extent of 207 px. My mask gives a centroid x of 652.7, and the record gives a length of 207 px. They agree to well within 3%.
- **Camera:** it pans and zooms. Following "measure against the background", I stabilised the track with the camera fit in scene/tracks/camera.csv. This is consistent with the child's and the man's box drift: about 9-15 px over frames 10-20.
- **Duplicate frames:** every 5th frame is a repeat, from a 25 to 30 fps conversion. The step from frame 15 to 16 is therefore a 1.2x step. The single forward difference (390 px/s stabilised, 340 raw) is an artefact, so I used smoothed estimates.
- **Stabilised speed at frame 15:**

  | Method | Speed |
  |---|---|
  | Central difference over 4 frames | 264 px/s |
  | Central difference over 10 frames | 260 px/s |
  | Quadratic fit, frames 8-22 | 260 px/s |
  | Linear fit, frames 10-20 | 256 px/s |
  | Quadratic fit, frames 5-30 | 257 px/s |

  These give **≈259 px/s**. The raw (unstabilised) image speed is about 223 px/s.

## Answer
259 px/s × 0.215 cm/px ≈ **56 cm/s**.

- At 0.20 cm/px (truck depth) the result would be 52 cm/s.
- At 0.25 cm/px (sofa well behind the people) it would be 65 cm/s.

**Second route:** the scale from the man's head alone (0.19 cm/px) gives 49 cm/s, and the scale from the child's head alone (0.21 cm/px) gives 54 cm/s.

**Confidence:** low to moderate. The pixel speed is reliable to about ±3%, but the cm-per-pixel scale is an estimate (±20%) because the sofa is not in the video.
