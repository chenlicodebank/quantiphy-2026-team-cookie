# q_1486: dragon body length (m)

The file is 24 fps and question_fps is 24, so frame = round(t*24). Principal point is (1439.5, 719.5); the rendered area is 2560 px wide.

## Scale (focal length)
- Prior: speed 1.29 m/s. Depths are 5.2108 m at frame 24 and 6.3261 m at frame 48. I used the hip track from scene/ as the origin proxy.
- Route 1 (`fitf.py`): solve f so that the 3D chord between the back-projected hip at frame 24 (d1) and at frame 48 (d2)
  is 1.29 m. With 0-3 frames of smoothing this gives f = 3430-3490 px.
- Route 2: fit a straight line at constant velocity (|V| = 1.29, passing through d1 and d2) to the whole hip track. Windows
  2-71, 16-56, 20-52 and 48-71 give f = 3428, 3463, 3411 and 3601. The velocity direction in camera coordinates is about (-0.56, -0.38, 1.10).
- Adopted f is about 3450 px (horizontal FOV about 41 deg).

## Body length
- The dragon flies away from the camera and is always seen from behind and above, so the nose-to-tail axis is strongly
  foreshortened and the snout is hidden behind the head and neck.
- Model (`bodylen.py`, `tailglide.py`): the body axis lies along the 3D flight direction w. For each landmark (tail tip,
  head/horns) I find how far along ±w from the hip, at the hip's model depth, its projection falls.
  - Frame 60 (glide): the tail tip is 0.73 m behind the hip (14 px residual). The head (horns) is 0.29 m ahead of the hip and
    about 0.09 m above the axis.
  - Glide frames 52-71, tail tip taken from the bbox bottom: 0.71-0.97 m, mean 0.84 m. This is biased high because the tail droops.
  - Frame 0 (flapping, tail drooped): tail 0.59 m and head 0.21 m.
- Estimate: tail about 0.75 m + hip to snout about 0.35 m (horns 0.29 m + snout) = **about 1.1 m**.
- Sanity check: the widest wingspan is about 1050 px at d ≈ 4.6 m, which is about 1.4 m. A body/wingspan ratio near 0.8 is plausible
  for a wyvern.

## Confidence
Low to moderate, roughly ±25%. Seen end-on, the foreshortening depends on the body axis matching the flight direction.
The tail droop and the hidden snout cannot be resolved from this view.
