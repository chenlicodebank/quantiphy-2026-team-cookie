# q1257: width of the purple car (m)

The purple car is the static maroon/purple BMW-style sedan, parked with its rear to the camera (bbox ~x 1253-1398, y 739-850).
Prior: white car (the cargo van) accelerates at 4 m/s^2. depth_info: van 43.81 m at f14 and 43.00 m at f38; taxi 38.60 m at f14; human 30.97 m at f14.
question_fps = file fps = 24.

## Method (3D pinhole and ground plane)
1. Vanishing point of the main road, from code-detected curb edges on scene/bg_full.png (`vp.py`): (1260, 707). The record said (1258, 702).
   Horizon y = 707 (no roll). The camera is pitched *up* a little: the horizon is below the image centre, so the record's
   "pitched down" is wrong. The cross street direction D is the ground direction perpendicular to the road.
2. Focal length (`final.py`): the van origin (patch_cx track, row 745.5) is placed at 43.812 m at f14 and moves along a line
   parallel to D. The other frames' rays are intersected with that line, and s(t) is fitted with a quadratic.
   Setting the fitted acceleration to 4 m/s^2 gives f = 2204 px (2146 with the bbox centre instead).
   Check: the predicted depth at f38 is 42.94 m against the given 43.00 m. Matching that depth exactly needs f = 2302, a very sensitive route.
   Sanity check: van 108 x 300 px gives 2.13 x 5.9 m; taxi side length gives 5.2 m. Both plausible.
3. Camera height from the given depths and code-measured tyre-contact rows:
   - van: contact row 801.5, near side 1.0 m closer than the origin. h = 1.80 / 1.78 m (f14 / f38).
   - taxi at f14: contact row 814.5. **The record's y_max 803 is wrong; the tyres end at 813-816.** h = 1.81 m.
   - pedestrian: feet at row ~822, not 815 as in the record. h = 1.57 m + the sidewalk curb. Not used.
   Used h = 1.80 m (f = 2204).
4. Sedan (`contact.py`, `mirror.py`, `width_final.py`):
   - Rear tyre contact is at row 850.5, giving a ground distance of 28.1 m. The rear face is taken 0.9 m nearer.
   - Rear bumper extent: x 1256.5-1398 (141.5 px) at row 816.5. Back-projected onto the rear-face plane and measured along D,
     this gives a **body/bumper width of 1.71 m**.
   - The left side mirror sticks out beyond the body: leftmost x 1252.5 at row 768. Its depth is fixed by an assumed mirror height of 0.95-1.05 m.
     Mirrored about the bumper centre, this gives a **mirror-to-mirror span (the AABB width) of 1.80-1.83 m**.
5. Sensitivity:
   - f = 2146 to 2302 gives body 1.76 to 1.64 and mirrors 1.87 to 1.72.
   - Overhang 0.7 to 1.1 m changes the result by ±0.013 m.
   - A contact row error of ±3 px changes it by about ±2 %.

## Second route
The taxi at f71 is front-on at almost the same distance (contact row 852 vs 850.5 for the sedan).
Its 181 px width at about 26.5 m gives 2.18 m, which is a Crown Victoria's width with mirrors (~2.2 m). This confirms the metric scale.

## Answer
The world AABB width should include the mirrors (≈1.81 m); the body-only reading is ≈1.71 m.
The answer is 1.77 m, chosen within about 5 % of both readings and of the focal-length range.
Confidence: moderate, about ±6 %.
