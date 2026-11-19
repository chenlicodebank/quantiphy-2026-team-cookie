# q1486: dragon body length (m)

The file is 24 fps and question_fps is 24, so frame = round(t*24). The principal point is (1439.5, 719.5).

## Where the earlier answers part ways
- **C1 (1.1 m):** f ≈ 3450 px. It corrects for foreshortening by putting the body axis along the 3D flight direction.
- **C2 (0.72 m):** f ≈ 3800 px. It takes nose-to-tail at frame 0 as **646 px fronto-parallel, with no foreshortening correction**.
  - Its f comes from a 430 px torso shift between t = 1 and t = 2. I measure about 395 px for both the hip and the head.
  - Its planar length ignores that the dragon flies almost straight away from the camera. The body axis is only about
    43 deg from the line of sight at frame 0, and about 24 deg in the glide.
- The deciding step is **foreshortening**, plus a ~10% difference in f.

## My measurements (scripts: fitline.py, axislen.py, crops.py, crop_abs.py)
- **Focal length (fitline.py).** I fit a straight, constant-velocity 3D line to the scene/ hip track, with |V| = 1.29 m/s
  and depth 5.2108 at frame 24 and 6.3261 at frame 48.
  - Windows 2-71, 8-64, 16-56, 20-52, 2-48 and 24-71 give f = 3529, 3599, 3584, 3550, 3431 and 3583 px.
  - The flight direction in camera coordinates is (-0.43, -0.30, 0.85).
  - A two-point chord check gives f ≈ 3450 (C1). I use f ≈ 3530.
  - C2's 3800 is not supported.
- **Body length (axislen.py).** For each landmark (read on gridded native crops), I find the point on the body axis (hip + s·w) closest to the landmark's camera ray.
  - Horns / back of the head: s = +0.25 (frame 0), +0.25 (4), +0.20 (8), +0.26 (60), +0.25 (71).
  - Tail tip, flapping frames 0/4/8: −0.58, −0.63, −0.54 (frame 8 also misses the axis by 0.09 m, so 3D ≈ 0.55).
  - Tail tip, glide frames 60/71: −0.80, −0.73.
  - The glide values are biased long. With the line of sight 24 deg from the axis, a tail droop δ adds about δ·cot 24° ≈ 2.2δ
    (a 0.1 m droop gives +0.2 m). At frame 0 (43 deg) the factor is only about 1.07. So the tail behind the hip is about 0.6-0.7 m.
  - The snout is hidden; it points away from the camera in every frame. Horns-to-snout is estimated at about 0.1-0.15 m.
  - **Total length ≈ 0.65 + 0.25 + 0.12 ≈ 1.0-1.1 m.**
- **Second-route check (wingspan).** Level-wing bbox widths are about 1050 px at frame 13 (depth about 4.7 m) and 748 px at
  frame 52 (about 6.5 m). Both give a wingspan of about 1.4 m. A body/wingspan ratio of about 0.75 is plausible for a wyvern.
  The shadow was too broken by the rough terrain to use.

## Answer
I take 1.05 m. I agree with C1's approach (foreshortening along the flight axis) and with its f. My tail estimate is
slightly shorter because I weight the less droop-sensitive frames 0-8. I reject C2's 0.72 m: it is a planar projected length.

Confidence: low to moderate, about ±20%. The hidden snout, the tail droop and the assumption that the body axis lies
along the flight direction cannot be fully resolved from this rear view.
