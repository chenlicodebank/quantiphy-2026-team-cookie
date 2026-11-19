# Q1016: fish (shark) displacement from 0.5 s to 1.0 s

- The video is 2D and top-down, with one swimmer (a shark). fps and question_fps are both 24, so the times map to frames 12 and 24.
- Prior: speed = 0.67 m/s. The record's template track (scene/tracks/shark.csv, checked earlier with overlays) shows nearly constant pixel speed: about 23.4-23.7 px/frame over frames 2-70, and 23.44 px/frame in the clean frames 40-70. The path is close to straight. Scale: 0.67/24 m per frame ÷ 23.5 px/frame ≈ 1.19e-3 m/px.
- Displacement in pixels from frame 12 to 24 (centre.py): the head reference point moves 286.8 px. I also corrected the point backward along the body axis by 100-220 px to approximate the body-centre origin, which gives 283-284 px. The snout/tail midpoint moves 274.7 px, but it is noisier because the tail swings.
- Results: 0.332-0.342 m, depending on the reference point and on which frames set the px speed. The simplest route is a straight path at constant speed: 0.67 × 0.5 = 0.335 m. It sits in the middle of that range.
- Answer: **0.335 m**. Confidence is high (about ±3%).
