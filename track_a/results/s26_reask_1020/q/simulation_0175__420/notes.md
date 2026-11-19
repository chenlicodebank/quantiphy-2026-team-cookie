# Q420 – airplane length (m)

2D side-on render, 24 fps (file and question fps agree), static camera. The plane flies horizontally right to left.

Scale from the prior: speed = 153.582 m/s.
- Per-frame shift (measure.py, median-background diff): the left-edge fit gives 61.38 px/frame, the right-edge fit
  61.97, and the column-profile cross-correlation gives 61.22 ± 0.30 (frames 10–31). scene/ reports 61.5 ± 0.2. I use
  61.5 px/frame, which is 1476 px/s.
- m/px = 153.582 / 1476 = 0.10405.

Length, nose tip to tail tip, over the fully visible frames 9–31: 468 px at threshold 8, 465 px at 15 and 462 px at
25; scene/ gives 466. A zoomed view of frame 18 shows the nose at about x 840 and the tail at about 1305, which is
about 465 px. I use 466 px.

Length = 466 × 0.10405 = **48.5 m**. The plausible range from the measurement spread (shift 61.2–61.7, length
462–468 px) is about 48.1–49.0 m.
Check: this is larger than a real business or regional jet (about 30–36 m), but it is within about 40%, and the prior
is exact. Confidence: high for the prior-based scale.
