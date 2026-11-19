# Q600 — width of the wooden bench (m)

2D top-down scene, 24 fps (file fps = question_fps, no re-timing). The prior's "black cat" is the black animal
walking right along y≈359 (the scene record calls it a dog). It is the only moving object.

## Scale (from the prior: cat speed 0.94 m/s)
- Pixel speed: the record track (scene/tracks/dog.csv) gives linear slopes of 10.98–11.00 px/frame for nose_x, mask_cx
  and torso_cx, over frames 0–44 and 0–49. The pace is steady, with no acceleration. That is 11.0 × 24 = 264 px/s.
  My own quick mask in measure.py gave 10.7–10.8 px/frame, but it drops the grey-rendered head from f45 on, so it is
  biased low. Over f0–44 the record values agree.
- Scale = 0.94 / 264 = 0.00356 m/px.

## Bench
- Colour mask at frame 48 (measure.py) gives bbox x 246–531 and y 174–289. The record gives 244–533 and 172–290. A
  zoomed grid view (frames/bench.png) shows the slats running about y 173–290.
- Width = the shorter horizontal extent, i.e. front-to-back = the image y-extent ≈ 116–119 px, taken as 117.5 px.
- Width = 117.5 × 0.00356 = 0.418 m. Length = 288 px, about 1.03 m. This is plausible for a slatted bench.

## Check
- Room floor ≈ 1555 px, about 5.5 m wide, and the cat is about 191 px, about 0.68 m nose to tail. Both are plausible.
- Perspective: the bench top is slightly above the floor, so its pixel size may be a few percent too large. That
  effect is not quantifiable here, so it is ignored.

Answer: 0.42 m. Confidence: moderate-high. The scale error is about 1–2%; the bench edge error is about 2%.
