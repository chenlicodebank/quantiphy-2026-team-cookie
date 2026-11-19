# q_179 — speed of the boat at 1.0 s (prior: shark speed = 3 m/s)

2D side-view scene, static camera, file fps = question_fps = 24, so t = 1.0 s is frame 24. The boat and the shark both
move left at a constant horizontal speed from frame 2 on, and their apparent sizes stay constant. I used one
metres-per-pixel scale taken from the shark's speed: boat speed = 3 m/s x (boat px/s) / (shark px/s).

## Measurements
- scene/ record (frames 1-72): boat -428.9 px/s, shark -258.2 px/s, ratio 1.661, giving 4.98 m/s.
- Second route (measure.py): sub-pixel template matching of each object between frames.
  - frames 23->24: boat 430.1 px/s, shark 258.6 px/s, giving 4.99 m/s
  - frames 2->24: boat 429.6, shark 260.0, ratio 1.652, giving 4.96 m/s
  - frames 24->46: ratio 1.653, giving 4.96 m/s
  - frames 14->34: ratio 1.653, giving 4.96 m/s
- The multi-frame template matches are the most precise. Their ratio is 1.653, and the scene/ record's line fits give 1.661.

## Answer
The boat's speed at 1.0 s is about 4.96 m/s (range 4.96-4.98). Confidence is high: the motion is constant and the
two routes agree within 0.4%.
