# q_621 — length of the TV stand (m); prior: black cat speed = 0.94 m/s

fps = question_fps = 24 (no re-timing issue). Static camera. Walking cat, plausible speed at 24 fps.

## Scale from the cat (catspeed.py)
- Background-subtracted dark-fur mask, upper-body column profile matched between frames.
  Per-frame step mean 18.0 px; long-baseline matches (n = 19/28/37/46 frames) 17.81-17.88 px/frame;
  upper-body centroid slope 17.91. Used 17.84 px/frame = 428.2 px/s (record: 17.73, nose 870/49 = 17.76).
- Scale at the cat's depth: 0.94 / 428.2 = 0.002195 m/px.

## TV stand pixels (standedges.py, legs.py)
- Front face edges x = 651.5 and 1423.5 at rows 805-900 -> **772 px** (record 773). Legs lie inside this span.
- Perspective is clearly present: top surface visible (back edge y≈776, front edge y≈794); back corners at x≈671.5 / 1391.5
  (width 720 px) -> back/front depth ratio 1.072; implied horizon y≈526 (≈ image centre 540).
- Metal leg tubes touch the floor at y = 988.5 (front) and 958.5 (back): ratio 1.067-1.069 with horizon 526-540,
  agreeing with the top surface -> front legs are at the front face depth.

## Depth of cat vs stand front
- Cat paw contacts read on crops (frames 12, 24, 40): 1015-1029 (far-side paws ≈1020, near-side ≈1028); centreline ≈ 1024 ± 3.
- Z_stand_front / Z_cat = (1024 - H)/(988.5 - H) = 1.077 (H=526) to 1.079 (H=540); ±3 px contact -> ±0.008.

## Result
L = 772 × 0.002195 × 1.078 = **1.83 m** (1.827).
- Single-scale 2D reading (no perspective correction): 772 × 0.002195 = 1.69 m. I rejected it because the visible
  top surface and the floor contacts show the stand is ~7-8 % farther from the camera than the cat.
- Second route: the depth ratio comes from two independent cues (top-surface convergence 1.072 vs leg contacts 1.068),
  which agree, and the horizon they imply matches the image centre.
- Confidence: moderate-good. Error ≈ ±3 %, mostly from the cat's contact line and the root-speed convention.
