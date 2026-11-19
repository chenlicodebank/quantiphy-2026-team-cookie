# q_2979: distance between the airplane and the roof top at 0 s

Method (internet convention: one planar scale from the prior). Script: measure.py, run on frame 0.
- Airplane length nose to tail at f0: 70 px (mask bbox x 356-425), which matches scene/. Scale = 40 m / 70 px = 0.571 m/px.
- Airplane centre at f0: y ≈ 192-193 (bbox centre 192.0, centroid 193.2).
- Roof directly below the plane (the left tall block, x 200-432): the first dark row per column in x 356-425
  falls between y 308 and 322, median 315. The median over the whole block is 313.
- Vertical gap from plane centre to roof: 315 - 192.5 ≈ 122.5 px, which gives 70.0 m.
- Second route: using the plane's belly (y≈199) instead of its centre gives 116 px = 66 m. Using the median roof
  line of the whole block (313) gives 69 m. The fps choice does not matter because t = 0 is frame 0.

Answer: 70 m. Confidence is moderate: the main uncertainty is which reference points the annotators used
(plane centre or belly, and the roof edge or rooftop clutter), which is about ±6%.
