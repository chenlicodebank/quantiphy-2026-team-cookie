# Q346: length of the train door (m)

Prior: side window width = 1.8 m. No depth_info. fps = question_fps = 24, so no re-timing issue (and the answer is a size, so timing does not matter).

## Method
The answer is a ratio of sizes on the train's near side. The door and the side windows lie in the same plane, which is
roughly parallel to the image, so they share one metres-per-pixel scale. I measured both in pixels from column-brightness
profiles (scripts `prof.py`, `edges.py`, `door.py`, `win.py`; crops from `crop.py`, saved as frames/d7.png and d15.png).

- Door panel (the lighter leaf with two narrow windows), horizontal extent:
  - f16: 482.3 -> 827.3, which is **345 px** (sharp edges in bands y760-800 and y800-845)
  - f7: 1459 -> ~1801, which is **342 px** (the right edge is softer because of shading)
- Side window (prior object):
  - glass edges: f14 712.5->1064.5 = 352, f16 1018.5->1372.5 = 354, f17 631->985 = 354 (f7 gives 347)
  - each edge has a black gasket about 5 px wide, then a thin bright rim. Inner dark boundary to outer dark boundary is
    about 363 px. Outer rim to outer rim is about 372 px.

## Scale and answer
door = 1.8 x 345 / W_window
- W = 353 (glass only): 1.76 m
- W = 363 (with gasket): 1.71 m
- W = 372 (with outer rim): 1.67 m

It is not clear which window outline the 1.8 m refers to, so I took the middle of this range: **1.73 m**.
At most about 3.5% separates this value from either extreme.

## Check
Two different frames, with the door on opposite sides of the image (f7 on the right, f16 on the left), give door widths
of 342 and 345 px. Several frames and positions give window glass widths of 352-354 px. Together these show the scale
is the same across the image, so perspective changes are negligible.
The door's two windows measure 111-112 px each in both frames, which is consistent.

Confidence: moderate-high. The main uncertainty is which window outline defines the prior (±3%).
