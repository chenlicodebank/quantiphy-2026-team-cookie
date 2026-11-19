# Q1543 – acceleration of the yellow car at t = 1 s (frame 24 at question_fps = 24; file fps also 24)

## Method
- The car moves left→right parallel to the image plane at constant depth: the hub row stays at 798.4±0.1 px and the rim radius
  stays at 63.5 px. So the image x of a point on the car is linear in world X, and one metres-per-pixel scale applies.
  The origin's acceleration equals the hub's, because this is a rigid translation (for a point farther away, the pixel
  motion and the m/px scale change by inverse factors that cancel).
- Hub tracking (`hubtrack.py` → `hubs_mine.csv`): I fitted a sub-pixel circle to the near-side white rim edge (72 radial
  rays, with outlier rejection) in every frame. The front hub is clean for frames 13-28; the rear hub for frames 26-35.
  These agree with scene/ ref_x to about 1 px.
- Scale (`tyre2.py`, `tyre3.py`): the outer tyre edge measured along radial rays on the sides, away from the floor
  contact shadow, gives R = 92-94 px for both front and rear tyres in several frames. The straight-down edge reads 95-96
  px, but that is inflated by the contact shadow. So D = 186 px ↔ 0.764 m, which gives 0.004108 m/px.
- Acceleration (`accel.py`), following the benchmark convention a(24) = (v24 − v23)·fps with v = backward difference:
  - raw second difference of the front hub at frame 24: 1.61 px/frame² → 3.81 m/s²
  - cubic/quartic fits of the front hub over windows within 14-28: 1.569-1.582 px/frame² → 3.71-3.74 m/s²
  - second route: front hub plus rear hub shifted by the wheelbase (729.2 px), fitted over 16-34: 1.563-1.570 → 3.70-3.71 m/s²
  - The acceleration falls smoothly (3.8 px/f² at frame 15, 1.6 at 24, 0.3 at 28). The car reaches peak speed around
    frame 30 and then slows. Its speed at frame 24 is ≈ 9.97 m/s.
- Answer: 1.58 px/frame² × 576 × 0.004108 ≈ **3.74 m/s²**.

## Check against the cart / depth_info (not used for the answer)
- Cart tyre ≈ 111 px (±3) for 0.369 m. With 9.312 m to its front-right (near-side) tyre, this gives f ≈ 2760 px
  (hfov ≈ 38°). The car tyre would then put the car's near side at Z ≈ 11.3 m.
- Floor-plane geometry with the horizon at y = 539 (the corridor vanishing point) gives about 10.4-10.7 m instead,
  a 6-8 % inconsistency. It probably comes from the tyre pixel sizes (shadows, tread perspective) or the horizon
  estimate. The car-tyre prior is the direct scale for the car, so I used it.

## Confidence
- Pixel acceleration: ±3 %. Tyre scale: ±1.5 %. The main risk is how the reference defines tyre diameter, versus the
  visible tyre radius of 93 px.
