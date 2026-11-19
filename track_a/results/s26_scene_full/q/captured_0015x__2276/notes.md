# q_2276 — height of the person (cm), prior g = 9.8 m/s^2, no depth_info

File fps = question_fps = 24.

Method (measure.py): non-white foreground mask, connected components. In free-flight frames 17-22 and 53-58 the
bear is its own component. Fitted a parabola y(t) to four reference points per toss (centroid, top, bottom, bbox
centre) to get the pixel acceleration:
- toss 1: centroid 2709, top 3168, bottom 2777, bbox centre 2973 px/s^2
- toss 2: centroid 2901, top 3065, bottom 2695, bbox centre 2880 px/s^2
- mean 2896 px/s^2 (spread ±6 %; the bear turns a little in flight, so top and bottom differ). Scale = 9.8/2896 = 3.384 mm/px.

Person height: hair top y 132-136 to shoe soles y 640-641, so 505-508 px; I used 507 px. All frames agree because she
stands still.

Height = 507 x 3.384 mm = 1.716 m, about 172 cm.

Check: with the lab focal length f = 763 px, the bear is at depth f*g/a = 763*9.8/2896 = 2.58 m. That gives a bear
height of 95 px -> 0.32 m, a plausible size for a plush toy, and a 1.72 m standing woman is plausible too.
Caveat: the bear is tossed in front of her body, mostly toward the right of the image (she stands 3/4-turned). A
depth offset of about ±0.2 m between the bear plane and her body would change the answer by about ±8 %. I used the
single-plane (2D) convention. The height includes shoes.
Confidence: moderate (about ±7 %).
