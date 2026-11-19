# Q45 – width of the turning yellow car (prior: length = 5.44 m)

2D top-down render (24 fps both in file and question; no retiming issue). The only car (peach/yellow sedan) turns
right through the intersection. Width = 5.44 m x (pixel width / pixel length), same object, same frames -> scale cancels.

## Measurement
- `profile2.py`: frames 0/1 (car vertical) and 70/71 (car horizontal). Colour distance from local road grey,
  half-max edge crossings per row/column. Length 217.2 px, body width 79.3 px (frame 0) / 76.8 px (frame 70).
  No mirror protrusion stands out (the widest single row is at most about 2 px wider than the median).
- `rotprof.py` (main route): every 3rd frame, rotate the map by the tracked heading, then take the length from the axial
  profile and the width as the median of cross profiles. Over 23 frames across the turn: L = 216.8 px (very stable),
  W = 79.7 px, median W/L = 0.368 (range 0.356–0.371).
- The scene record's mask sizes (222.5 x 88 px) come from a loose threshold that adds a ~3 px halo to every side, which
  inflates the width/length ratio (88/222.5 = 0.395 -> 2.15 m). The half-max edges correct for this.

## Result
width = 5.44 x 0.368 = 2.00 m (the frame-0/70 checks give 1.93–1.99 m). This is plausible for a 5.44 m sedan, measured
wheel to wheel or body width.
Confidence: about ±3 %.
