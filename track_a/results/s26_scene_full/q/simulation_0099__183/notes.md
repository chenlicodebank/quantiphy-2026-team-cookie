# Q183: boat speed at 1.0 s (m/s); prior: boat length = 10 m

- 2D side view with a static camera, 24 fps (file rate and question_fps agree). t = 1.0 s is frame 24.
- Scale: I measured the boat's length in code (`edges.py`) as bow tip minus stern edge, using the difference from the background: 861 px at frame 0, 859-861 px over frames 0-47. `measure.py` gives a mask extent of 228-1087 px (860 px). The scene record says 851-860 px. I used 860 px, so the scale is 10/860 = 0.01163 m/px.
- Speed: the boat is at rest in frames 0-1, then moves at a constant speed. Measured with `edges.py`:
  - Stern edge: 17.91 px/frame on average over frames 1-47.
  - Bow tip: 17.88 px/frame.
  - Frame 23 to 24: 17.93 (stern) and 17.68 (bow) px/frame. These single steps are noisy (std about 0.15), so I used the average.
  - The scene record agrees: rail post 17.88, mast 17.84.
  - Phase correlation on the whole hull (`measure.py`) gives 18.35 px/frame. I rejected it because reflections slide over the glossy hull; the record noticed the same drift.
- Result: 17.90 px/frame x 24 = 429.6 px/s, x 0.01163 = 4.99 m/s, so the answer is 5.0 m/s.
- Confidence: high, with an error of about 1% (mostly from how the length edges are defined).
