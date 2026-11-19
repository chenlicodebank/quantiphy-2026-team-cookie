# Q26: length of the green car (m)

The "black_car" in scene/ is the green car: dark green in the frames, right lane. It is a 2D top-down static view, so I used one scale from the prior (orange car acceleration = -2.86 m/s²).

- `measure.py`: background-difference mask (same method as the record, re-run here). Gives the top and bottom y edges of each car per frame and saves them to edges.npy.
- **Green car length**: the y extent over the full-view frames 37–70 is 292–296 px, median **293 px** (mean 293.3). This agrees with the orange car's slow-frame length of 291–293 px, so motion blur adds little.
- **Orange acceleration** (`fit.py`): quadratic fits of the car's position against frame number:
  - centre, f30–90: -0.1815 px/frame²
  - centre, f16–60: -0.1794
  - centre, f45–90: -0.1803
  - front edge, f37–90: -0.1774
  - rear edge, f30–90: -0.1867
  - Adopted value: **-0.180 px/frame²**, i.e. -162 px/s² at 30 fps. question_fps 30 and file fps 30.003 differ by only 0.01 %.
- **Scale**: 2.86 / 162 = 0.01765 m/px.
- **Length**: 293 × 0.01765 = **5.17 m**.
- **Check**: the spread of the fit windows (-0.177 to -0.187) gives 5.0–5.25 m. The orange car comes out 292 px ≈ 5.15 m long and the lane 231 px ≈ 4.1 m wide, both plausible.
- **Confidence**: good, about ±3 %.
