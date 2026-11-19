# q_1015 – width of the fish (shark), prior: speed 0.67 m/s

- 2D top-down clip, 24 fps (file fps = question_fps, no re-timing). The shark swims right to left at a nearly constant speed.
- Scale: the template-tracked body point from scene/tracks/shark.csv. Mean per-frame step over frames 1→70 = 23.65 px, which is 567.6 px/s.
  Early window (frames 4-24): 571.8 px/s. Late window (frames 44-68): 562.5 px/s. Speed is constant to about 1%.
  m/px = 0.67 / 567.6 = 0.001180.
- Width = horizontal extent across the body, from pectoral fin tip to fin tip (in a top view, the shorter horizontal AABB extent).
  I re-read the span on 2x gridded crops at frames 48 and 60: about 228 and 232 px, which agrees with the record's manual values
  (225-260 px, larger around frames 26-34 where the fins and body flex; frames 42-70 average 234 px).
- Width = 234 px × 0.001180 = 0.277 m. Using the early or late speed window instead gives 0.275-0.279 m.
  Taking the fin span as anything from 225 to 245 px gives 0.27-0.29 m.
- Excluding the fins, the body alone is about 110-120 px (about 0.14 m). I didn't use this, since the AABB includes the fins.
- Confidence: moderate-high on the scale (±2%). The fin-span reading has a spread of about ±5%.
