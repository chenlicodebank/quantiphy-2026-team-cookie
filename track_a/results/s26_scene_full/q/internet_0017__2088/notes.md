# Q2088 – speed of the right hand's middle fingertip at 0.4 s (cm/s)

Prior: credit card width = 5.4 cm. This is the held black Visa card's short side.

## Time base
The question uses 22 fps and the file runs at 22.368 fps. Either rate puts t = 0.4 s on frame 9 (8.8 and 8.95 both
round to 9). I used question_fps = 22 for the frame-to-seconds conversion. Using 22.37 would give an answer 1.7 % higher.

## Fingertip track
The camera does not move (the scene record shows a background shift under 1 px). The right hand's index and middle
fingers are extended. Seen from above with the palm down, the middle finger is the right-hand one of the two, on the
side away from the thumb. I read the nail-tip apex on 2x zoomed crops (`crops.py`, frames/z*.png):
f7 (3355,1172), f8 (3285,1106), f9 (3212,1049), f10 (3162,1002), f11 (3135,975).
Per-frame steps: 7→8 96 px, 8→9 93 px, 9→10 69 px, 10→11 38 px.
Check by code (`tip.py`): I took the extreme skin pixel along the motion direction at three thresholds. That gave
9→10 = 70.4 / 71.6 / 74.2 px and 8→9 ≈ 94–96 px, which agrees with the manual readings.
I used the internet convention, a forward difference at frame 9: about 70.5 px/frame (±3).

## Scale
The card's short edge at frame 9: I measured about 198 px from its corners (2779,1093) to (2865,1271), and the
scene-record mask gives 199.5 px. I used 199 px, so the scale is 5.4/199 = 0.02714 cm/px.

## Answer
70.5 px/frame × 22 fps × 0.02714 cm/px = **42.1 cm/s**.
Other conventions: a central difference (~83 px/frame) gives ~49.6 cm/s, and a backward difference (~94 px/frame) gives
~56 cm/s. The fingertip is slowing down quickly at this moment, so the choice of difference matters. I answered with
the stated forward-difference convention.
Confidence: moderate. Motion blur on frames 8–9 adds about ±5 % to the tip positions, and the choice of convention is
the main risk.
