# Q986: speed of the whale at t = 1.0 s (frame 24, 24 fps)

The file's fps and question_fps are both 24, so t = 1.0 s is frame 24. This is a 2D side view with a static camera (scene/ camcheck).

## Scale (prior: whale length = 19.17 m)
- Frame 51, where the body is straightest and the whole whale is visible. Zoomed crops (frames/snout51.png, tail51.png) put the
  snout tip at x ~ 325 and the fluke tip at x ~ 3793, so the length is ~3468 px. The mask bbox_w in scene/ has a maximum of 3454, and
  that mask is 10-20 px short at the snout. I used L = 3465 px, so scale = 19.17 / 3465 = 0.005532 m/px.

## Pixel speed near frame 24
- flow.py: head template matched between consecutive frames (frames 11-38), mean -11.46 px/frame. This is probably biased slightly low
  because static background falls inside the template.
- flow2.py: the frame-24 head template located in every frame (long baseline). Linear and quadratic fits give:
  head_full 11.74-11.89 px/frame, head_front 12.08-12.11 px/frame.
  Over frames 0-56 the head moves 660 px, which is 11.8 px/frame. The motion is nearly uniform.
- scene/ head tracks over frames 14-34: jaw_front 11.2 px/frame, snout 12.75, front_780_880 12.76. Over the whole clip
  all of them give about 11.8-12.0.
- Adopted value: 11.9 px/frame (spread about +-0.2), which is 285.6 px/s.
- The head stays level (head_cy constant), so head translation is taken as the origin's translation.

## Answer
speed = 11.9 x 24 x 0.005532 = 1.58 m/s. The range across methods is about 1.53-1.61.
Second route: using the whole-clip average from scene/ snout/jaw (11.9 px/frame) gives the same value.
Confidence: good, about +-4%.
