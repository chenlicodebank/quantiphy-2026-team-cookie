# q_1679 – width (beam) of the boat, metres

Prior: boat speed 4 m/s. depth_info: Z(t=1 s) = 90.1103 m, Z(t=2 s) = 90.4360 m. question_fps = 24; the file is at 25 fps,
so I used frame numbers with t = frame/24 (scene/ seconds are at 25 fps and were not used).

The boat is seen almost exactly side-on (the bow points left and it moves left), from above. The width (beam, the shorter
horizontal AABB extent) points almost straight along the line of sight. It shows only as the vertical gap
between the near and far gunwales, so the answer depends on the camera's look-down angle.

## Geometry
- Straight line at constant speed: Z^2 = Zmin^2 + v^2 (t - t0)^2. The two depths give t0 = -0.338 s and Zmin = 89.95 m.
  This gives dZ/dt = 0.326 m/s, so the motion is about 85 deg to the line of sight.
- track2.py: I tracked the hull/cabin by template matching (subpixel) over frames 3-74. The image motion is
  dx = -6.43 px/frame and dy = -0.259 px/frame, and both are linear.
- fit.py: a pinhole camera (principal point at the image centre, no roll) fitted to the origin track (the origin is taken
  as the hull bbox centre (528.5, 600) at frame 37) and to the depth model. Result: f = 3499 px, pitch 20.5 deg, yaw -6.0 deg,
  depression of the line of sight to the boat beta = 22.55 deg. RMS is 0.16 / 0.12 px, and the given depths are reproduced exactly.
  Sensitivity (sens.py): moving the origin x by +-40 px changes beta by -+2.6 deg. Moving the origin y has no effect.
- Check of f: 38.6 px/m at Z = 90.3 m gives a hull length of about 396 px / 38.6 = 10.3 m (plausible).
- Check of pitch with vertical lines (mast.py, verticals.py: their tilt versus image x gives the vertical
  vanishing point). The pole gives 15.8 deg, the mast 6.5-17.7 deg and the cabin edge 28.6 deg. These are inconsistent
  (thin features, possibly a little roll), so I used them only as a rough check. The track fit is the primary
  estimate.

## Gunwale band (gunwale.py, profile.py, frame 38)
- Amidships behind the wheelhouse (x 530-560): the far cap-rail top is at y 553-555. The near white cap strip runs
  y 590-597, and the red hull starts at 598.
- Near the bow (x 420): far top at 535, near cap top at 574, red at 580.
- So the gap between the gunwale tops is 36-40 px, and 43-45 px if measured to the near red line. The near
  outer edge lies inside the 7 px white strip. I adopted 40-41 px.
- beam.py: 1 m of beam projects to 14.59 px vertically at frame 38 (beta 22.55 deg).
  Beam = 40/14.59 = 2.74 m, or 41/14.59 = 2.81 m.
  The range is 2.4-3.3 m when combining the band range (37.5-44.5 px) with beta 20-25 deg.

## Answer
Width ≈ 2.8 m. This gives length/beam ≈ 3.7, which is a plausible proportion for a ~10 m fishing boat.
Confidence: moderate, about +-12 %. The main uncertainties are the look-down angle (it depends on where the
origin is) and which white edge counts as the near gunwale's outer edge.
