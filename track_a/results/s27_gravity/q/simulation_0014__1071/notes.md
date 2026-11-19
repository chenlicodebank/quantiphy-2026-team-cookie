# Q1071 – height of the cargo box on the cart (simulation_0014)

File fps = question fps = 24. Static camera, 1920x1954. Cart distance 27.562 m, house 55.767 m, nest 5.661 m (t=0) / 5.630 m (t=1).
The moving "fur ball" in scene/ is the bird's nest (distance_nest_camera).

## Focal length
1. Gravity route (fit_fall.py, fit_fall2.py): ballistic 3D fit of the nest centroid (frames 34-48) with depth anchors.
   This route is ill-conditioned: f trades off against the camera pitch. The nest's pixel acceleration is only about
   6 px/frame² (≈3500 px/s²). With the nest at ≈5 m that means f ≈ 1500-2800 if the fall were free. Adding the nest's
   approach to the camera (its apparent size grows about 1.4-1.6x) pushes f even lower (to unphysical values).
   With f ≈ 2000 the everyday objects become implausible: barrels 2+ m tall, a 4-8 m door, a 2-3 m cart wheel.
   So the soft-body nest is not falling freely; Blender soft-body air friction would explain the damping.
   The gravity prior therefore gives no usable scale.
2. Scale from standard objects instead, as the rules allow: the two barrels in front of the house are 98 px tall
   (rim y≈1097 to base ≈1197, measure_box.py). A 0.9 m barrel at the house front, about 50 m away (the house origin
   is 55.8 m, i.e. behind the front wall), gives f ≈ 5300 (horizontal FOV ≈ 20°).
   Checks at f = 5300: barn door ≈ 0.86 x 2.1 m, nest width ≈ 0.3 m, cart wheel (190 px at 27.4 m) ≈ 0.98 m.
   All are realistic. Uncertainty in f is about ±12%, mainly from where the house origin sits.

## Box height
The cart's side faces the camera (the wheel looks circular). The box is tilted about 14° because the shafts rest on
the ground.
- The vertical extent of the box (world-AABB reading) runs from its top back corner at y≈1019 (sky edge, measured in
  code) to its bottom front corner at y≈1187: about 168 px. At a forward depth of 27.56·cos(5.3°) = 27.44 m this is
  168·27.44/5300 = 0.87 m.
- The other reading is the box wall height perpendicular to its own long axis: about 92-95 px, i.e. 0.50 m.
  I answer with the world-AABB vertical extent, following the benchmark's size convention.
- Second route: box vertical extent / wheel diameter = 168/190 = 0.88. With a typical 1.0 m cart wheel that is
  0.88 m, consistent.

Answer: 0.87 m. Confidence: moderate. The scale rests on realistic object sizes, not on the gravity prior, and the
reading is ambiguous (0.50 m under the box-wall reading).
