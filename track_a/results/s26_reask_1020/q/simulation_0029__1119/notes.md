# q_1119: length of the eagle (m). Answer: 0.88 m

The file runs at 25 fps and question_fps is 24. All times use 24 fps: t=1 s is frame 24 and t=2 s is frame 48.
Frame numbers below are file frame indices from scene/tracks/bird.csv.

## Scale (focal.py)
- Eagle centre, smoothed with a local quadratic fit (the flapping wings make the centroid wobble):
  u = 235.6 at frame 24 and 409.7 at frame 48 (frame 48 is interpolated, because the bird overlaps the antenna there).
  v is about 522-530. The principal point is taken as (480, 480).
- The prior says the speed is 12 m/s, so the 3D displacement over 1 s is 12 m. Combined with the depths 139.70 and
  147.16 m, solving |d2 r2 - d1 r1| = 12 gives **f = 2646 px** (HFOV 20.6°). This value is stable to ±2 px across
  the smoothing choices.
- The 3D path is P1 = (-12.84, 2.45, 139.09) and the direction is (0.745, 0.03, 0.666): the eagle flies right and
  away from the camera, at about 52° to the line of sight.
- **Check:** a straight 12 m/s path predicts u to within about 2 px over all frames 0-74 (extent.py). This includes
  the slowing pixel speed as the bird recedes.
- **Plausibility:** the boat's hull is 158-176 px at about 134 m, which gives 8-9 m. Its height including the mast
  is about 9.6 m. Both are plausible for a fishing boat.

## Eagle length
The body axis lies along the flight direction. Its projection onto image x is about 0.75-0.85 times the true length,
depending on the frame.

**Route 1: body length (wingspan.py, vpose.py).**
- In frames where the wings are level, they are seen edge-on and look faint, so the dark core is the body.
- The core's x-extent at threshold 30 is 15, 14, 12 and 13 px in frames 6, 33, 57 and 58. I subtract 1 px for
  antialiasing at the edges and use depth Z/f.
- This gives L = 0.83, 0.89, 0.84 and 0.92 m, a mean of **about 0.87 m**. The result holds across quite different
  projection factors.
- The sub-pixel coverage sum gives a lower bound of about 0.57 m, because the thin tail and head are only partly covered.
- The wings-up (V) frames mix in the spread of the wings, so I did not use them. They give 0.75-1.2 m.

**Route 2: wingspan.**
- The maximum x-extent in level-wing frames, divided by the wing projection factor (0.55-0.68), gives a wingspan
  of about 2.0-2.3 m.
- An eagle's length is typically 0.40-0.45 of its wingspan, which gives L ≈ 0.85-0.95 m.

Both routes agree at about 0.85-0.95 m, which is also the range of a real eagle (0.7-1.0 m).

## Confidence
Moderate. The bird is only about 12-15 px long in the image, so ±1 px is about ±8 %. If renderer motion blur is
present, it would inflate the extents slightly.
