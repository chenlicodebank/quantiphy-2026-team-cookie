# Q1110 — length of the eagle (m)

Answer: **0.75 m** (beak to tail, along the body / direction of flight).

File is 25 fps and question_fps is 24. I used frame = round(t x 24), so t=1 s is frame 24 and t=2 s is frame 48.

## Scale (focal length)
- Person: depth_info is about 114.83 m at both times. The origin distance barely changes (0.004 m/s), but the body walks
  in front/back view (legs move along the line of sight). The person's image moves only 37 px left over 74 frames.
  - If that were all their 1.3 m/s, f would be about 1170 px and the person 5.4 m tall: impossible. So the person walks
    mostly along the line of sight.
  - The prior speed cannot fix f here: the radial part of the walk is ill-conditioned (apparent height 54.7 -> 54.3 px,
    within noise).
- So the scale comes from standard sizes:
  - The person's walking mask height is 54.5 px at 114.83 m. For a walking height of about 1.70 m (standing about 1.75 m),
    f is about 3600-3700 px.
  - Check with the eagle (bald eagle: white head, dark body). With f = 3700, the eagle's heading comes from depth_info
    (116.05 -> 108.28 m) and the smoothed centroids at frames 24 and 48 (both in the same wings-up pose). That gives
    11.3 m/s, at 48.6 deg to the line of sight.
  - The level-wing span (48 px at frame 42), corrected for that heading, gives a wingspan of 2.16 m. That is plausible
    for a bald eagle, so it agrees with f of about 3600-4000.

## Eagle length
- In the wings-up V frames (22, 24, 26, 28, 46, 47, 49, 51) the body sits at the bottom of the V. The white head is at its
  right end. The body runs along the heading, which projects horizontally in the image.
- I measured the horizontal extent of the bottom rows in code. The mask is the difference to a median background,
  threshold 25 (`rows.py`). Extents: 15.5-19.5 px.
- Length = width x depth / f / |sin(heading vs line of sight)|. The depth at each frame is interpolated linearly from
  depth_info (`geom.py`).
  - f = 3700: L = 0.736 m (sd over frames 0.033). Early frames 0.741, late frames 0.731. Two independent windows at
    different depths agree.
  - L is insensitive to f: f = 3300 gives 0.78, f = 4100 gives 0.70. A larger f makes the image scale smaller but turns
    the heading toward the camera, and the two partly cancel.
- Final value: 0.75 m. This adds a little for the edge fringe. The result is plausible for a bald eagle (0.7-1.0 m).

## Confidence
Moderate. The body is only about 17-19 px long and is not cleanly separable from the wing roots. The tail may be hidden
behind the body, in which case the length is underestimated by up to about 10%.
