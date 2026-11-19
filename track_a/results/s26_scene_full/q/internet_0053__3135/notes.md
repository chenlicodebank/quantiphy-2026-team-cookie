# q3135: height of the person riding the scooter (m)

Prior: the rider's average speed is 4.46 m/s. No depth_info. The file and the question both run at 30 fps, so I used 30 fps.

## Method (internet convention: one scale from the prior)
- The camera is static (drift ≤2 px, subtracted anyway). Motion is side-on, left to right.
- Average pixel speed = mean of the per-frame displacements × 30 (`measure.py`, using the tracks in scene/):
  - scooter_cx: 547.0 px/s over frames 0-73, 540.1 px/s over 0-80
  - rear wheel: 551.0 / 543.5 px/s
  - upper-body template track (independent): 546.6 / 538.3 px/s
  - Adopted value: 543 px/s.
- Scale = 4.46 / 543 = 0.00821 m/px.
- Rider standing height, cap top to shoe sole: 304 px at frame 40 (checked on a zoomed grid crop: cap top ≈386, sole on the deck ≈690). Frame 40 is mid-clip, and its wheelbase (152 px) equals the clip-mean wheelbase (152.9 px), so it matches the perspective scale of the average speed. The rider measures 315 px at frame 0 and about 297 px at frame 72.
- Height = 304 × 0.00821 = 2.50 m.

## Checks and caveats
- The three tracks and the two frame windows agree on pixel speed within ±1.3%.
- Alternative reading, cap top to the ground (including deck and wheels): 327 px, which gives 2.69 m.
- This scale is not physically plausible. A 2.5 m rider and a 1.25 m wheelbase are about 1.45× real-world sizes. The question's fps equals the file's fps, so there is no re-timing to explain the difference. I kept the benchmark convention, height = prior × h_px / v_px.
- Confidence: moderate. The measurement follows the convention well, but the prior itself seems inflated.
