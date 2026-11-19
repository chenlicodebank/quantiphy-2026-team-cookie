# Q1036: fire truck displacement from 0.5 s to 1.0 s

- Prior: the truck's speed is 11.18 m/s. This is a 2D top-down render. The truck drives straight left.
- Time base: the file runs at 24.005 fps and the question at 24. Both put 0.5 s at frame 12 and 1.0 s at frame 24.
- Re-measurement (`measure.py`): I segmented the truck by its colour difference from the purple background and took the bbox centre in frames 0–47.
  - A linear fit gives 26.29 px/frame.
  - Steps over each 12-frame window: 319, 318.5, 318.5 (frames 12→24), 315, 311.5 and 312 px. The motion is near uniform; the small drift comes from perspective at the edges.
  - The record in scene/ agrees: 318.5 px for frames 12→24 and a mean of 26.33 px/frame.
- Route 1 (uniform speed): 11.18 m/s × 0.5 s = **5.59 m**.
- Route 2 (pixel ratio): 318.5 px / 26.29 px per frame × (11.18 / 24) m per frame = 5.64 m. This is within 1% of route 1.
- Answer: 5.59 m. Confidence is high, at about ±1%.
