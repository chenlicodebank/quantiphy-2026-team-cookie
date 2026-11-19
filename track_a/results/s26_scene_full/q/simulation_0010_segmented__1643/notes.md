# q_1643 — width between the two widest eaves of the small house

File fps is 22; question_fps is 24. Times are converted with 24 fps, so t=1 s is frame 24.

## Method (3D pinhole)
- Prior: bird length = 1.19 m. The bird is seen in profile, flying left to right, so I read its length as its beak-to-tail
  extent along the flight direction, i.e. its horizontal image extent. That extent was measured in frames where the
  wings are vertical or folded (my own mask against scene/bg_median.jpg: `measure.py`; it matches the scene track bbox_w):
  - f0–11: ~146–154 px
  - f18–28: ~142–150 px
  - f44–46: ~147–149 px
  - Typical value 148 px. Wing-up frames (~115–125 px) were ignored because the body is pitched there.
- Bird depth comes from depth_info, interpolated linearly: 34.584 m at f0 and 33.999 m at f24.
- Focal length: sqrt(f²+r²) = L_px·D/L, where r is the bird's distance from the image centre.
  - f0–11 gives f ≈ 4250–4290; f18–28 and f44–46 give f ≈ 4150.
  - Mean f ≈ 4200 px, so the horizontal field of view is about 26°.
- House eaves: the two eave tips at the gable front are at x = 86 and x = 1021 (y ≈ 790). That is 936 px, measured in
  code on the median background (`house.py`) and checked on zoomed crops (frames/eaves.png).
- W = W_px · D_house / sqrt(f² + r_h²) = 936 · 55.083 / sqrt(f² + 436²):
  - f = 4250 gives 12.07 m
  - f = 4200 gives 12.21 m

## Check
- A shortcut ratio, W ≈ (936/148) · 1.19 · (55.083/34.55) ≈ 12.0 m, agrees with the full calculation.
- The bird calibrations from different frame windows differ by about 3%.

## Answer
12.1 m.

Confidence: medium.
- If "length" meant the wingspan, the answer would be about half (about 6 m). Real-world sizes would then look more
  realistic (door about 1.8 m tall), but the stated convention (length = extent along the body, wingspan named
  separately) favours the body-length reading.
- The eaves sit at the gable front, a little nearer to the camera than the house origin. That could make the true width
  a few percent smaller.
