# Q1732 – height of the rock (m)

The file's frame rate and question_fps are both 24.

## Scale
- Prior: the person walks at 1.3 m/s. depth_info gives 122.8569 m at t=1 s and 122.8588 m at t=2 s.
- The two distances differ, by 1.9 mm. A static origin would give identical values. So the origin moves with the body along a path almost perpendicular to the camera ray. For a perpendicular path at 1.3 m/s the expected change is up to about 7 mm per s, which fits. So I treat the motion as transverse.
- Pixel speed comes from a linear fit of the pelvis track (scale/tracks/person.csv, checked against the centroid, feet and head x): 1.728 px/frame in x and 0.094 px/frame in y, so 41.54 px/s.
- The person is about 5.3 deg off the optical axis, which gives an optical-axis depth Z = 122.32 m.
- Focal length: f = 41.54 · 122.32 / 1.3 = 3909 px. The scale at the person is 0.0313 m/px.
- Check: the person's walking bbox is 60–64 px tall (my own masks at three thresholds; person_h.py), which gives 1.92–1.99 m. That is tall but within the plausible range.
- The height shrinks by about 6 % over the clip. That cannot be a depth change (it would need more than 7 m at 1.3 m/s), so I put it down to pose and mask noise.

## Rock (rock_h.py)
- The rock is static. Its mask spans y 594–733: 139 px, unrotated.
- The rock's bottom edge slopes down to the right by 2.2 deg, and the person's path slopes by 3.1 deg. That points to a camera roll of about 2–3 deg, with the rock's base level in the world.
- With the mask rotated by 2.2–3.1 deg, the vertical extent is 118.5 px. Measured at the peak's column (x≈140), from the peak (y 595) down to the bottom-edge line, it is about 116 px.
- Height = 116–118.5 px × 0.0313 m/px = 3.63–3.71 m. I assume the rock is at the person's depth (its tip ends next to the person).

## Second route / uncertainty
- If instead the person were a standard 1.75–1.8 m (walking bbox ≈1.72 m), the scale would be 0.0285 m/px and the rock about 3.35 m.
- Without the roll correction (the raw 139 px) the rock would be 4.35 m.
- Answer: 3.65 m. Confidence is moderate; the main risks are the rock's depth and the camera roll.
