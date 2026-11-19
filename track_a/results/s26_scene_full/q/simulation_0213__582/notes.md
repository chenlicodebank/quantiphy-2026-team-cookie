# q_582 — speed of the dog at t = 1.5 s (m/s)

Prior: cat speed = 0.94 m/s (steady walk). fps = question_fps = 24, so t = 1.5 s is frame 36; speed = backward difference 35→36.

## Scale (from the cat)
- Cat pixel speed (cat_slopes.py, visible frames 0-22 and 44-49): nose bbox_x1 slope 17.76 px/frame (rms 0.7 px); centroid 17.81; torso 17.86. I used 17.78 px/frame = 426.7 px/s, so the cat lane scale is 0.94/426.7 = 2.203e-3 m/px.
- (Template matching on the cat in track_cat.py gives about 14 px/frame. The small cat template is mostly static background, which biases it, so I discarded it.)

## Dog pixel speed at frame 36
- track_dog.py: normalised cross-correlation of dog-body texture patches (rows 800-880, 220 px wide) between consecutive frames. Frame 35→36: torso 19.69, shoulder 19.38, hip 19.26 px/frame (corr about 0.94-0.96). The motion is smooth and decelerating (24.6 at f33 down to 15.9 at f40).
- Check of the method in clean frames: over 5→22 the template sum is -291 px, against torso_cx -295 and nose -290, so the method is unbiased there. In the merged frames (30-42) the record's torso_cx is pulled by cat pixels and runs low. The nose (bbox_x0) gives about 18 px/frame near f36; the sniffing head bobs.
- Adopted value: 19.4 px/frame = 465.6 px/s.

## Depth correction (the dog walks in a nearer lane)
- Paw contact rows: cat 1020 (median), dog 1066. The wall-floor line is horizontal, so there is no roll or yaw. The camera is near level: the vase mouth (y≈577) and the lamp-shade rim (y≈605) look almost flat, while the table top and vase bands are seen slightly from above. That puts the horizon at y≈550±30.
- Depth ratio Z_dog/Z_cat = (1020-550)/(1066-550) = 0.911 (0.89-0.93 over the horizon range).
- Dog scale = 2.203e-3 × 0.911 = 2.007e-3 m/px.

## Answer
465.6 px/s × 2.007e-3 m/px = **0.935 m/s**.
- With a single scale and no depth correction it would be 1.026 m/s.
- With the nose track instead of the body texture it would be about 0.87 m/s.

Confidence: moderate, about ±6%. The main uncertainties are the horizon row (±2%) and body point versus rig root (±4%).
