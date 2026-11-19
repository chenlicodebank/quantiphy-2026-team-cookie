# q_1701: length of the boat (m)

Prior: eagle speed = 12 m/s. Depths: boat 133.9572 m at t=1 s and 131.2557 m at t=2 s; eagle 139.7035 m at t=1 s and 147.1583 m at t=2 s.
question_fps = 24, while the file runs at 25 fps. So t=1 s is frame 24 and t=2 s is frame 48. I used the frame columns from scene/, not its seconds.

## Focal length (focal.py)
- I took the eagle's centroid at frames 24 and 48 from local linear fits (±2 to ±6 frames), giving (236.5, 522.5) and (411.0, 528.7). The principal point is (480, 480).
- Assuming the eagle flies at a constant 12 m/s in a straight line, the 3D distance between those two back-projected points must be 12 m. Solving for f gives f = 2650–2654 px (horizontal FOV about 20.5°). I used f = 2652.

## Boat orientation and length (orient.py, fitlen.py)
- The boat's 3D motion between frames 24 and 48, from the back-projected centroid and the given depths, is (-3.10, -0.15, -2.73) m. That is a speed of 4.13 m/s, heading 41.4° out of the image plane (moving left and toward the camera).
- The boat's image length grows 11.8 % over frames 0–74. Pure depth change would explain only 6.6 %, so the boat is oblique to the camera, not side-on. The visible cabin front face and the short-looking hull agree with this.
- I fitted a 3D model (bow tip plus two stern corners, width k·L) to the bow-to-stern pixel extent in all 75 frames, using the 3D centre track:
  - k=0.3: L = 9.76 m, heading 41.6°. This heading matches the motion heading on its own, which makes it the second, independent check. rms 0.62 px.
  - k=0: L = 9.92 m, heading 33°. k=0.4: L = 9.67 m, heading 44°.
  - Side-on (θ=0) fits badly (rms 2.4–2.9 px) and would give 8.3 m, so I rejected it.
- Answer: **9.76 m**. The model spread is 9.67–9.92 m.

## Confidence
Moderate to good. The main assumptions are: the eagle flies straight at constant speed (this sets f), the boat's long axis is along its motion (supported by the free fit), and the reference length is the boat's own long axis.
