# q3011: average speed of the player in the black shirt, 0.5 to 5.53 s

- Object: the dark-kit player (`goalkeeper_dark` in scene/). This player stands near the top of the goal area until about frame 84, then walks down-left.
- Time base: the file runs at 29.80 fps and the question at 30 fps, a 0.6% difference. Frames used are 15 and 166 (round(t x 30)), so the interval is 5.03 s. The choice of rate barely changes the result.
- Scale (internet convention, one factor): goal frame length is 7.32 m. On frame 0 (check.py) the white goal frame runs over rows 413/414 to 513, about 100 px on the outer edges; the posts are 97.9 px apart centre to centre (scene record). I used 99 px, which gives 0.0739 m/px.
- Displacement (centres.py): I averaged the player's centre over frames 10-20 (standing still) and over frames 161-171 (a window centred on 166, while walking at a steady pace). The four centre estimates give:
  - background-difference centroid: 36.0 px
  - bbox centre: 36.9 px
  - dark-pixel centroid: 33.5 px
  - the record's track: 38.7 px
  
  The mean is about 36.3 px. The walk is close to a straight line: the smoothed track path is only about 3% longer than the net displacement, and most of that is centroid jitter. I used about 36.5 px.
- Speed = 36.5 px x 0.0739 m/px / 5.03 s = 0.536 m/s, giving the answer **0.54 m/s**.
- Second check: the record's track alone gives 38.7 px, i.e. 0.57 m/s; its smoothed path length (w=15, 39.9 px) gives 0.59 m/s. The dark-blob estimate gives 0.49 m/s. Spread is about ±8%.
- Confidence: moderate. The main uncertainty is which point on the tiny top-down body (about 12 px across) counts as the player's position, plus whether the answer means average path speed or net displacement over time; the two are close here.
