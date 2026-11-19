# q1039 – distance at t=3 s from the outer end of the pier to the boat

Answer: **2.75 m**

## Time base
question_fps = 24, but the file is 22.80 fps and has 66 frames (0-65). t = 3 s → frame 72, which is past the last
frame. So the boat position is extrapolated 7 frames. The bow track is smooth and nearly uniform (quadratic fit,
rms 0.37 px). Depth frames: t=0 → f0, t=1 → f24.

## Geometry
- **Focal length.** Taking the boat origin as the centre of the full-boat box (scene track ref_x/ref_y) and assuming
  constant camera depth (the hull height stays at 88 px in every frame), the two given distances (7.452 m at f0,
  6.655 m at f24) give f = 1000 px and Z_boat = 5.854 m (`solve_f.py`). Moving the origin ±30 px changes f by only ±1.5 %.
- **Prior check.** At this scale, 0.75 m = 128 px. The visible stem-post height above the water is about 125 px
  (post top y≈620, stem waterline about 740-747), which is consistent with a near-zero draft.
- **Alternative model.** The bow's pixel speed falls by 8 % and the stem waterline rises by 7 px. This could mean
  the boat is slowly receding (Z +0.066 %/frame). That model gives f = 908 and Z0 = 5.63, but then the visible post
  alone would be 0.79 m, which is more than the 0.75 m prior. So I used constant depth; the receding model changes
  the answer by only −0.05 m.
- **Horizon.** From the receding board ends and corner blocks of the pier deck, the horizon is at y_h ≈ 531-535,
  so the camera is nearly level. The pier runs along the optical axis, with its vanishing point at x≈550.
- **Pier near (outer) end, Z_n, by two routes:**
  - Route A: the pier origin (11.579 m) is the centre of the pier box, between the front face (top edge y=630) and
    the far edge of the deck (y=591.5). This gives Z_n = 8.68 m.
  - Route B: I measured the water plane from reflection mirror axes (`mirror_axis.py`, `mirror_bow.py`). The pier
    front face and legs mirror about y=675.5, and the stem waterline mirrors about y=740-747 at depth ≈ Z_boat−0.07.
    This gives Z_n = 8.54 m.
  - The two routes agree to 1.6 %. Mean Z_n = 8.61 m.
- **Check on where the pier origin is.** The pier origin cannot be at the outer end: even Z_boat ≤ 6.655 m would
  put the near end no deeper than 10.5 m, short of 11.579 m. Its distance fits the box centre.
- **Boat at frame 72.** Bow u ≈ 251, origin u ≈ 573, v ≈ 688. That is in front of the pier's outer end, inside the
  pier's width and at about the height of its front face. So the minimum distance is almost exactly the depth gap.
  The 3D distance from the boat origin to the centre of the front edge is 2.76 m (`final.py`); with the receding
  model it is 2.72 m.

## Other readings
- Boat origin to pier origin (centre), origin-to-origin: about 5.7 m. Not used, because the question names the
  outer end.
- Distance to the near hull surface instead of the boat origin: about 2.2 m.

## Confidence
Moderate. The answer hinges on Z_n (8.4-8.9 across the horizon range and both routes) and on the 7-frame
extrapolation. Expected error is about ±6 %.
