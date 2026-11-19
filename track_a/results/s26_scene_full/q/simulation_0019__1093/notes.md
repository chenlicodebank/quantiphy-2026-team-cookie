# Q1093 – height of the central sculpture (excluding pedestal)

Answer: **1.68 m**

## Geometry
- The render is rotated 90°, so world up points to image −x (as recorded in scene/).
- Camera pitch is 0. World-vertical edges sit at constant image y over the whole frame (pitch.py):
  - The wall edge at y = 863.6 stays within ±0.1 px from x = 40 to 580.
  - The dark pedestal edges at y = 446.6 and 747.8 are also constant.
  - So the horizon is at image x = 540 and v = 540 + f·(h_cam − Y)/Z.
- The time base (33.26 vs 33 fps) does not matter for a static size. t = 1 s maps to frame 33 at either rate.

## Focal length (calib.py)
Both routes use the person (height 1.87 m, given distances 6.84 m at t = 0 and 6.49 m at t = 1 s). The person walks parallel to the image plane at constant depth.
- **Route A** (both distances, same Z, pelvis image radius 361 px → 194 px):
  - f = 888.5 px, Z = 6.336 m.
  - This predicts a rest height of 262 px. The measured walking maximum is 261 px, with soles sometimes 2–5 px short.
- **Route B** (rest height in px and one distance):
  - 259–263 px gives f = 876–890.
- Adopted: f = 886 ± 10 px, person Z = 6.33 m.

## Sculpture pixels (frames 0 and 67, look.py, prof.py)
- The sculpture tip (the highest point, world up) is at image x = 389.8.
- The pedestal is a dark box (front face x 772–895.5) with a light stone cap on top:
  - cap front face x 703–766.5
  - cap top face x 672 (far edge) to 703 (near edge)
- The sculpture stands on the cap top. Projected at the sculpture's depth, its base is at x ≈ 684–686.

## Height
- With the origin at Z = 5.085 m (Euclidean) minus a small lateral correction (Z = 5.01–5.08), H = (v_base − v_tip)·Z/f = 1.675–1.687 m at f = 886.
- **Second route:** a chain from the floor and the camera height, independent of the given sculpture depth:
  - Person soles at 786 give a camera height of 1.76 m.
  - The floor line of the dark box gives its front at Z = 4.38.
  - The dark box is 0.61 m high and the cap is 0.32 m, so the cap top is 0.93 m above the floor.
  - The cap spans Z 4.49–5.54, with its centre at Z = 5.02. This matches the given 5.085 m Euclidean distance once the lateral offset is included.
  - The chain then gives H = 0.854 (tip above camera) + 0.826 (camera above cap top) = 1.676 m.
- Sensitivity:
  - Changing f by ±10 px moves H by ∓0.019 m.
  - If the tip's depth differs from the origin's by ±0.25 m, H moves by about ±0.04 m.

## Confidence
Good. The estimate is about 1.68 ± 0.04 m.
