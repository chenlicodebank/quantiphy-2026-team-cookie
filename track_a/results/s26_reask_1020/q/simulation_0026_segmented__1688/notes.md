# q_1688 – length of the boat (m)

File is 25 fps, question_fps = 24, so t=1 s is frame 24 and t=2 s is frame 48 (I used scene frame indices, not the scene's seconds).

## Scale (focal length)
- I measured the person's pixel height in code (`human_h.py`): with threshold d>20 it is 46–50 px (about 48 px), and 47 px at frame 24 with the stricter d>40 threshold.
  Depth at t=1 is 114.83 m. f = 48 x 114.83 / 1.75 ≈ 3150 px (horizontal FOV ≈ 17°). Uncertainty is about ±100 px
  (faint head, walking pose, mask halo).

## Boat orientation (key point)
- `traj.py`: I back-projected the boat's hull/bbox centre at frames 24 and 48 using the given distances (103.157 and 106.091 m).
  The displacement is (-3.19, 0, +2.73) m over 1 s, which gives a speed of 4.2 m/s and a heading 40.5° away from the image plane
  (bow pointing left and away). This yaw shows in the image too: the wheelhouse side face and back face look about equally wide (40 vs 36 px),
  and the rounded stern is visible on the right. The boat is therefore foreshortened. Its 251 px bbox at frame 24 is only about 8.2 m of
  horizontal extent at that depth.
- The origin moves in a straight line at constant speed: the projected track matches the measured centres to 0.58 px rms over all 75 frames.

## Length fit
- `fit.py` / `fit2.py`: I modelled the hull with a point bow at +a along the heading and a stern at -b (either a rounded half-disc of radius w or square
  corners ±w). I projected it with the pinhole model along the 3D track and fitted it to the bbox x0 (bow) and x1 (stern) in every frame.
  - Rounded stern (it looks rounded in the frames), w = 0.75–1.25 m, f = 3150: L = 10.9–11.1 m (rms 0.72 px).
  - Square stern with w free: L = 10.75 m. Square stern with w = 1 m: L = 10.4 m.
  - Changing f by ±100 px changes L by about ∓2 %. Moving the origin pixel by ±20 px changes L by about ±1.2 %.
- Answer: L ≈ 10.9 m. This is the true hull length, bow to stern along the heading; the projected image extent alone (8.2 m) would underestimate it.

## Checks
- The yaw comes from two independent routes: the 3D trajectory gives 40.5°, and the wheelhouse face ratio gives about 45°.
- Plausibility: speed 4.2 m/s (8 kn), total height including the mast about 10.5 m, hull about 3.8 m deep. These fit a roughly 11 m boat.
- Confidence: moderate. The main uncertainties are f (from a 48 px person) and the stern shape. The likely range is 10.3–11.3 m.
