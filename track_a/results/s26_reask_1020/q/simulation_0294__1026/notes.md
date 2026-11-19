# q_1026 – length of the butterfly's wings (simulation_0294)

The file and the question both run at 24 fps, so frames convert directly.

## Scale (2D, from the prior: speed 0.32 m/s)
- The body point (`scene/tracks/butterfly.csv` `body_x`) moves at a steady 30.90 px/frame. That is the mean of the steps over frames 1–71, sd 0.53; a linear fit gives 30.88. Frames 0 and 1 are duplicates. The flight is horizontal, the camera is static, and there is no trend in step size, so the butterfly's depth does not change.
- Pixel speed = 741.7 px/s, so the scale is 0.32 / 741.7 = 4.315e-4 m/px.

## What is being measured
- Zoomed frames 0, 4, 9, 20, 30 and 62 (in `frames/`) show the butterfly side-on: head to the left, body along the direction of flight. When the wings are raised they are seen face-on; when they are flat they are seen edge-on as a thin line.
- Following the convention that an animal's length runs along the body and the direction of travel, and that wingspan is its width, I read "length of the wings" as the front-to-back extent of the wings: forewing tip to hindwing tip.
- The wingspan lies along the viewing direction, so it cannot be measured here without a focal length.

## Measurement (`measure.py`, which also uses the record's mask box)
- **Face-on raised-wing frames** (little perspective effect). Mask box width:
  - 414, 397, 402 px at u≈2060 (frames 8–10)
  - 392, 388, 393 px at u≈1418 (frames 29–31)
  - 409, 399 px at u≈785 (frames 50–51)
  - Blue-only extents are about 10 px smaller, because they leave out the dark wing border.
- **Flat-wing frames.** The extent forms a V against image position: 498 px at u=2311, ~420–427 px near u≈1700, ~422–438 px near u≈1080, 520 px at u≈430. The wingspan sits along the depth axis and adds about 0.13 × |u − cx| of perspective spread. Extrapolating the V to the image centre gives roughly 375–405 px, which agrees with the raised-wing value.
- **Adopted value:** 390 ± 10 px → 390 × 4.315e-4 = **0.168 m**.

## Second route
The flat-wing V, extrapolated to the image centre, gives 374–404 px, i.e. 0.161–0.174 m. This is consistent with the face-on raised-wing value.

## Other readings (not chosen)
- The largest raw box width in a flat frame (525 px) would give 0.227 m. It is inflated by perspective.
- The length of a single forewing from root to tip, seen face-on in frame 30, is about 315 px, i.e. 0.136 m.
- The wingspan cannot be measured; it is roughly 0.22–0.26 m if the flat wings are assumed to reach out sideways at about 0.85 × the forewing length.

## Confidence
The measurement itself is good to about ±3%. The interpretation of "length of the wings" is the main uncertainty.
