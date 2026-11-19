# q1348 — width of the lane (road curb to curb), simulation_0067

The file and question_fps are both 24. t=0.58 s is frame 14 and t=1.58 s is frame 38.
White car = van, yellow car = taxi.

## Method (3D pinhole + ground plane)
1. `lines.py`: Hough curb lines on scene/bg.png. `calib.py`: least-squares vanishing points of the two road
   directions, VP1 (2737,-51) (east-west road, 12 lines, residuals ≤8 px) and VP2 (123,-43) (diagonal road the van
   drives on, 12 lines, residuals ≤2 px). The roads are taken as perpendicular and the principal point as centred, which gives
   f = 1114 px (HFOV 88°). Check: with this f the curb lines come out parallel on the ground, and curbs of the same side
   in different sections are collinear within ±0.2 m. With f = 1000 or 1200 they splay apart by 1-8 m.
2. Camera height from depth_info (`height.py`): the pedestrian's pelvis (bbox centre) at its given distance, with the
   feet on the ground. At t=0.58 this gives H = 7.05 m and a pelvis height of 0.86 m; at t=1.58, H = 6.98 m. I use H = 7.0 m.
   Checks: the van's bbox centre at f38, on the 0.65 m plane, comes out 12.79 m from the camera (given 12.81 m). The taxi and
   bike origins stay at a constant height between the two times.
3. `width.py`: curb lines are back-projected to the ground plane, and the width is the perpendicular separation:
   - Diagonal road (van's road), top-centre block's SW curb to upper-left block's NE curb: 11.84 / 11.89 / 12.16 / 12.19 m
   - East-west road (the taxi turns into it): left section 12.11 m, right section 12.09 / 11.79 m
   - Answer: about 12.0 m (both roads have the same width).

## Scale checks
- The taxi's (Crown Victoria) wheelbase from its wheel contacts at f14 is 2.83 m; the real one is 2.91 m (−3%).
- The van's (Chevy Express) wheelbase at f38 is 3.73 m. That falls between the real 3.43 m and 3.94 m versions, so it is plausible.
- The prior is the van's acceleration (4 m/s²). From the van's bbox-centre and lowest-point tracks (f16-50) I get 4.6-4.7 m/s², about
  15% high. The bbox centre is not a fixed point on the body, and making the scale 13% smaller would shrink the taxi
  to an implausible 2.5 m wheelbase. So the depth- and size-based scale is kept.

Confidence: about ±4% (H ±2%, curb-line picking ±2%).
