# q_1916: height of the truck (m)

The video is a 2D side view, 120 fps (the file rate and question_fps are the same). The camera is static.

**Scale from the prior (box acceleration 9.8 m/s² before 0.6 s).** `fit.py` fits a quadratic to the box's
y position over the free fall, frames 0-59; impact is at f60-61. I fitted both the centre of the front
face and the bottom edge of the front face:
- Frames 0-59 / 5-58 / 10-55: 1956-1967 px/s² (rms about 0.6 px). Sub-windows give 1845-2017.
- The value I used is **1962 px/s²**, so the scale is 9.8/1962 = **0.004995 m/px**.

**Truck height.** `truck.py` makes a non-white mask of frame 10, leaving out the box above y=300. The
vertical extent runs from y=348.5 (top of the lift cage) to y=1063.5 (bottom of the wheels), which is
**715 px**. That gives 715 × 0.004995 = **3.57 m**.

**Checks.**
- The wheel radius is about 89 px, so the wheel diameter is about 0.89 m. That is realistic for a truck.
- The truck is 1717 px long, about 8.6 m, which is a plausible catering lift truck.
- The box face is about 2.05 × 0.95 m (large, but this is a simulation).

**Caveats.**
- The height includes the lift cage on the cab roof. Without the cage, the cargo-box roof is at y=412,
  which gives 651 px or 3.25 m.
- I assumed a single planar scale. The scene has slight perspective (camera at about roof height), and
  the side face of the truck may sit at a slightly different depth from the box.

**Confidence:** moderate to high, about ±5%.
