# q_996: displacement of the dragon from 0.5 s to 1.0 s (m)

fps = question_fps = 24, so the times are frames 12 and 24. The camera is static and the scene is 2D (flight across the image plane), so I used one metres-per-pixel scale from the prior (dragon length 0.75 m).

## Displacement in pixels
- The record's silhouette centroid is a poor stand-in for the origin. The wingbeat period is about 24 frames, and frames 12 and 24 are half a cycle apart: in frame 12 the wings are swept forward and down, and in frame 24 they are raised. So the centroid bias differs between the two frames. Centroid displacement: (-360, -87), i.e. 370 px.
- Body point instead: I tracked a patch on the hip/thigh (just ahead of the tail base) with chained masked template matching from frame 12 to frame 24 (`chain.py`). Start (1600, 815), end (1162, 750): **443 px**. Both endpoints were checked visually on the same anatomical spot (frames/chain_12_24_*.png).
- Second route: reading the hind foot by eye, (1650, 895) to (1185, 840), gives about 468 px. The legs move relative to the body, so I weighted the hip result more. I used 445 px.
- Sanity check: whole-cycle centroid speeds are 33 px/frame (frames 0-24) and 38 px/frame (frames 12-36). Over 12 frames that is 400-460 px, which agrees.

## Scale (the main uncertainty)
The tail flexes, so the dragon's projected length changes from frame to frame:
- horizontal bounding box (wings included): 570 px at frame 0, median 602 px over frames 0-49, minimum 517 px
- nose to tail tip: about 500-515 px when the tail curls down (frames 0 and 24), about 610-667 px when it is straight (frames 10, 12, 35)

I took L ≈ 600 px for 0.75 m, which is 1.25e-3 m/px.

## Answer
445 × 0.75 / 600 = **0.556 m**.

Confidence: moderate. Depending on which length definition the reference used, L could be anywhere from 570 to 650 px, giving 0.51-0.59 m.
