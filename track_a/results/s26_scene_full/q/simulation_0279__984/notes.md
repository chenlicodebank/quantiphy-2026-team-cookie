# Q984 – height of the whale (prior: whale speed 1.67 m/s)

2D video at 24 fps (file fps and question_fps are the same, so no re-timing). The camera is static, and the whale swims to the left at a uniform rate in a plane facing the camera.

## Scale
- Rigid head / snout track (scene record, head_chain_x): -8.02 px/frame, std 0.1.
- My own check (measure.py, snout edge from the Sobel gradient): -7.99 px/frame over frames 2→70 and -8.00 over 10→50.
- Pixel speed = 8.02 × 24 = 192.5 px/s, so the scale is 1.67 / 192.5 = 0.008676 m/px.

## Height (vertical extent of the bounding box, flipper included)
- Frame 0: top of the dorsal fin is at y≈396–400 and the flipper tip at y≈1009–1010, so h ≈ 613 px → **5.32 m**. The tail is off the right edge here but roughly level, and it sits inside that vertical range.
- Across the clip the height changes with the tail beat: min 523 px (4.54 m), median 604 px (5.24 m), mean 624 px (5.42 m), max 869 px (7.54 m, tail raised at the end).
- With the body straight (frames 47–52) it is about 535 px (4.64 m).

## Answer
5.3 m. This is the frame-0 value, which is close to the median and mean over the clip. The question does not say which pose to use, and that ambiguity is the main risk: the straight-body pose would give 4.6 m and the maximum 7.5 m. My confidence is moderate.
