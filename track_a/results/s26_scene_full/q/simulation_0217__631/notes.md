# q_631: speed of the dog at t = 1 s (frame 24)

- 2D top-down render at 24 fps (file and question rates agree). The dog is the tan animal on the lower line, walking −x. The black cat is on the upper line, walking +x.
- Scale comes from the prior, cat speed = 0.94 m/s. The cat moves at a steady pace: its front edge goes from 647 to 1185 px over 49 frames (10.98 px/frame) and its centroid from 563.9 to 1098.8 (10.92 px/frame). I used 10.95 px/frame, which gives 0.94/(10.95·24) = 3.577e-3 m/px. (Template tracking of the cat's black body was unreliable, so I did not use it.)
- Dog pixel speed (track.py): chained, sub-pixel template matching of three torso patches (front, mid, rear/pelvis), with correlation of 0.92–0.99.
  - Step into frame 24: front 12.8, mid 12.5, rear 13.0 px/frame.
  - Mean over frames 23–25: 12.6, 12.5, 13.0.
  - Mean over frames 21–27: 12.6, 12.7, 13.1.
  - Second route: the scene/ torso-centroid track gives 13.1 px/frame over frames 22–26 and 12.7 over frames 20–28.
  - I used 12.8 px/frame. The dog speeds up during frames 15–20, then cruises at about 12.5–13 px/frame.
- Speed = 12.8 × 24 × 3.577e-3 = 1.10 m/s (the ratio to the cat is 1.17).
- Confidence: about ±4%, mostly from gait jitter in the dog's per-frame step and the unknown pelvis offset.
