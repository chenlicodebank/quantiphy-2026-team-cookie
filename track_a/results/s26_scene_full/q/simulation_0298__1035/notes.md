# q1035 – width of the fire truck (m)

- 2D top-down view; truck drives left at constant speed. Prior: speed = 11.18 m/s.
- Time base: file fps 24.005 vs question 24.0 – difference 0.02%, irrelevant; used 24.
- Pixel speed (measure.py, linear fits on scene/tracks/truck.csv): front edge 26.10, rear edge 26.20
  (frames 0–68), bbox centre 26.30 px/frame -> adopted 26.2 px/frame = 628.8 px/s.
- Scale = 11.18 / 628.8 = 0.01778 m/px.
- Width profile measured in code on frame 28 (centred, column-by-column mask extent, threshold 40 vs
  background colour): body/cab 160 px (bed 154–160 px); at the mirror arms (x=550) 190 px (record bbox: 184 px).
- Width (body, wheel-to-wheel convention): 160 x 0.01778 = 2.85 m.
  Width incl. mirrors (raw AABB reading): ~185 px -> 3.29 m.
- Check: edge speeds differ by <1% (perspective), so scale uncertain by ~1%. Length 534 px -> 9.5 m,
  width 2.85 m: plausible fire truck proportions.
- Answer: 2.9 m (body width, nudged slightly toward the mirror-inclusive reading). Confidence moderate
  (main ambiguity is mirrors in/out).
