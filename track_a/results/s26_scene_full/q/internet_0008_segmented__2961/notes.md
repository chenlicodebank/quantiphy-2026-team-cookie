# q 2961: average speed of the sailboat (m/s)

Prior: sailboat length = 12 m. The video is a segmentation cut-out on a white background, treated as 2D with one scale.
The file runs at 24 fps but question_fps is 30. As instructed, frame-to-time conversion uses 30 fps.

## Method (measure.py, track.csv)
- Mask: min(RGB) < 200, watermark box excluded, largest connected component. I checked the overlays at frames 0, 120 and 239: the mask covers the hull, sails and masts.
- Boat length in pixels (horizontal extent):
  - bbox: median 100 px
  - hull, bottom 13 rows: median 98 px
  - Value used: 99 px.
  - Scale: 12 / 99 = 0.1212 m/px.
- Motion is steady along +x (cy is constant):
  - linear-fit slope: 1.414 to 1.418 px/frame (bbox left, right and centre, centroid, hull centre)
  - net displacement / frames: 1.410 to 1.418 px/frame
  - Value used: 1.415 px/frame.
- Speed: 1.415 px/frame × 30 frames/s × 0.1212 m/px = 5.15 m/s.

## Check and sensitivity
- Mask centroid, net displacement over frames 0 to 239: 1.412 px/frame, giving 5.13 m/s.
- Using the bbox length (100 px) gives 5.09 m/s. Using the hull length (98 px) gives 5.20 m/s.
- If the file's 24 fps were used instead, the result would be 4.12 m/s. That reading is not used, because question_fps governs.
- The camera pan cannot be measured on the white background, so speed is taken relative to the frame.

Confidence: good. The main uncertainty is the frame-rate convention.
