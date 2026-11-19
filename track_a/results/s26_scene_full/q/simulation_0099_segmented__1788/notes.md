# q1788 boat average speed
2D video, 24 fps (file = question fps). Scale from prior: boat length 10 m = 856-857 px (stern-to-bow, frames 0-47, measured in measure.py and scene record) -> 0.01168 m/px.
Boat stern x tracked per frame (measure.py): linear fit 17.888 px/frame = 429.3 px/s -> 5.015 m/s.
Mean of per-frame backward-difference speeds: frames 2-72 = 17.887 px/frame (5.01 m/s); including frame 1 (frames 0,1 identical, speed 0) = 4.95 m/s.
Second route: scene record fit 17.886 px/frame with 857 px length -> 5.009 m/s. Agrees.
Answer 5.0 m/s (likely design value; all variants within 1.5%). Confidence high.
