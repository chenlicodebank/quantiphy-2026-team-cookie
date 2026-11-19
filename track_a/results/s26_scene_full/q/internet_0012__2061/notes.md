# q2061: average velocity of the car in the leftmost lane

**Answer: 11.6 m/s**

## Object
The car in the leftmost lane is `white_car_lower`, the smaller white car on the left carriageway. Its centre is at x≈829→820,
just left of the first dash line (x≈843). The other white car (x≈868) sits right of that line, so it is in the middle lane.
The car is visible and moving in every frame from 0 to 107.

## Scale (prior: lane width = 3.66 m)
`lanes.py` measures the dash-line centres (subpixel intensity-weighted peaks on 5-row strips, frame 50):
- Left-carriageway lane width between the dash lines: 96.2 px overall, and 96.5 px at y 2600–3200, where the car drives.
- Right carriageway: about 96–97 px where it is not contaminated.

I used 96.5 px, so the scale is 3.66 / 96.5 = 0.03793 m/px.

Another reading: from the outer solid edge line (x≈742) to the dash line (x≈843) is about 100 px. That edge line probably
bounds a shoulder, so I did not use it. With 100 px the answer would be 11.2 m/s.

## Motion
- The camera is static (see scene/notes.md and the scene record), so no background compensation was needed.
- Net displacement of the tracked centre from frame 0 to frame 107: 546.1 px, which is 5.10 px/frame.
- Linear fit over the 62 frames that are not duplicates: 5.11 px/frame for `cy` and 5.105 for the independent `edge_cy`.
- The path length is 546.6 px, practically the same as the net displacement because the car moves in a straight line.
- 46 of the 108 frames are duplicates (3 in every 7). Using the whole-clip displacement over the whole time avoids the problem.

## Time base
- At question_fps = 60: 5.1035 × 60 × 0.03793 = **11.61 m/s**.
- At the file's 59.35 fps: 11.49 m/s.

I used the stated question rate of 60. Either rate gives about 42 km/h, which is plausible for traffic on a bridge.

## Check
- Speed in the first half: 5.03 px/frame. Second half: 5.18 px/frame. The ±1.5% difference matches the lens-distortion scale
  change noted in the scene record.
- The two independent position measures (template `cy` and `edge_cy`) agree within 0.2%.

**Confidence:** about ±3–5%. The main uncertainty is which lane-line pair the annotators used for the prior.
