# q_971 – height of the raccoon (prior: length with tail = 1.51 m)

2D video, side view, static camera, fps 24 (same as question_fps). One planar scale from the prior.

## Measurements (measure.py + scene/tracks/raccoon.csv, checked on zoomed crops of frames 0 and 7)
- Length (nose tip to tail tip, bbox_w): 330 px at frame 0, mean 326.7, max 333, minimum about 310 when the body is compressed.
- Feet bottom: about y=866. The contact shadow is at y=865–871. My own mask includes the shadow (bottom 871); the
  scene record trims it (bottom 864). Toes on the crops sit at about 866.
- Top: the raised tail reaches y=722 at frames 0–1, 16–17, 32, 47 and 62–63. In the other frames the back/head top
  is at y=731–744.
- Height in px: frame 0 is 145, with the tail raised. Over the animation it ranges from 123 to 145, mean 130,
  median 128.

## Scale and candidates
The scale is 1.51 m / length px. The answer depends on which pose the reference used:
- frame 0 (first frame) h/w: 0.663 m
- largest height / largest length over the clip: 0.658 m
- mean per-frame h/w: 0.601 m
- the rest pose cannot be seen. With straight legs it would probably be about 0.60–0.66.

Answer: **0.63 m**. This is a compromise that is within about 5% of every candidate.
Confidence: moderate. The pixel measurements are good to ±2 px; the main uncertainty is which pose was used.
