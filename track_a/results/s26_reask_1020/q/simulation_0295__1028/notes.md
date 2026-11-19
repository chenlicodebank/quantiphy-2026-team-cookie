# q_1028: length of the butterfly's wings (m)

Prior: butterfly speed = 0.32 m/s. No depth_info. question_fps = file fps = 24.

## Geometry
- The camera is static and sees the butterfly from the side. Its head is to the left and it flies left, at a nearly constant image height.
- Frame 30 (wings up) shows the forewing in front and the hindwing behind, with the head near x = 1290 and the abdomen reaching about x = 1490.
- "Length" here means the extent along the body and the flight direction (fore-aft), following the naming rules (a butterfly's wingspan is its width, never its length).
- Flapping turns the wings about the body axis, so it should not change the fore-aft extent. But when the wings are flat they lie partly along the line of sight, so part of the wingspan shows up in the horizontal bbox (495–522 px at frames 0 and 63). When the wings are fully up (frames 8/9, 30, 51), the span is vertical and the horizontal bbox width is the true fore-aft length. These minima are 395, 389 and 399 px.
- Foreshortening: the body axis is parallel to the velocity. Any depth component of the motion therefore shrinks the length and the pixel speed by the same factor, so their ratio cancels it.

## Measurement (measure.py, using the scene track bboxes, which I checked on zoomed frames 0, 8, 18 and 30)
- Speed from same-phase displacements (wings-up frames 8 -> 30 -> 51): 30.2–31.3 px/frame, mean 30.9 px/frame. The body-fit speed at those frames is 30.0, 30.6 and 31.2 px/frame. The slight speed-up matches a small approach toward the camera.
- Ratio of width to local speed: 395/30.0 = 13.17, 389/30.7 = 12.67, 399/31.2 = 12.79. Mean 12.88 frames.
- Length = 0.32 m/s / 24 fps x 12.88 = 0.172 m.
- Second route: global scale 0.32 / (30.9 x 24) = 4.32e-4 m/px. Mean wings-up width 394 px x 4.32e-4 = 0.170 m. This agrees.

## Answer
0.172 m.

## Confidence
Moderate. The main uncertainty is how "length" is read. The fore-aft wing extent is about 0.17 m. The flat-wing horizontal extents, which mix in some wingspan, give 0.21–0.23 m. The wingspan itself cannot be seen directly in this side view.
