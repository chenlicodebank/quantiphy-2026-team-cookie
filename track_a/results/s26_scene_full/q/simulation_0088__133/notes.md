# Q133 – wingspan (width) of the big bird (eagle)

The scene is 2D: a fixed camera looks up at both birds, which fly right to left across the frame. The eagle's wings
point straight up and down in the image, so the wingspan is the vertical pixel extent of its mask.
fps = question_fps = 24.

## Scale (from the prior: eagle speed 17.98 m/s)
- I re-measured the tail-end x in every frame with measure.py. The steps are 119 or 120 px per frame (f1→f14),
  mean 119.69 px/frame = 2872.6 px/s.
- Scale = 17.98 / 2872.6 = 0.006259 m/px.

## Wingspan
- Vertical mask extent per frame (threshold 40): 183, 199, 226, 269, 306, **324 (f6)**, 316, 289, 248, 211, 184,
  175 (f12), 176, 189 px. With the looser threshold of 20 the peak is 327 px.
- At its widest (wings fully spread, f6), 324–327 px gives 2.03–2.05 m. **Answer: 2.04 m.** This also fits a real
  bald eagle (about 2 m).
- Other readings: the narrowest span (175 px) is 1.10 m, and the mean over the flap cycle is 1.45 m. I answered with
  "wingspan" as the fully spread width.

## Check
- The scene record gives the same numbers: a 324 px maximum and a 119.69 px/frame step.
- The scale is sound: the eagle's body length of 138.7 px works out to 0.87 m, which is plausible for an eagle.

## Confidence
The measurement is solid. The main uncertainty is which reading the question wants (maximum versus another phase
of the flap).
