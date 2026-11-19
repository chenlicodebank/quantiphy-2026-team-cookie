# q_1947 — acceleration of the red general chess piece at t = 1 s

File fps 24 = question_fps 24, so t = 1 s is frame 24. 2D video; the scale comes from the prior (piece diameter = 0.097 m).

## Object
The scene record's "block" is the Chinese chess piece. It is a disc lying flat and is seen obliquely, so it looks like a
cream-coloured rounded oblong. It slides down the trough of a wooden chess-board ramp. It is the only moving object
and it is both the asked object and the prior's object. Its red face is not visible, but nothing else in the clip
could be the "red general".

## Measurements (scripts in this folder)
- `track.py`: background = median of frames, piece mask = colour difference > 45, then morphological clean-up, then
  centroid per frame. The centroids agree with scene/tracks/block.csv within about 1 px.
- Pixel diameter: the ellipse's major axis equals the disc's diameter. Median PCA main-axis length over frames 0–36 is
  81.5 px. `size_profile.py` shows the threshold sensitivity: 82–83 px at diff threshold 20–30, 81 px at 45,
  79–80 px at 70. I use 81.5 ± 1.5 px, which gives 0.097/81.5 = 1.190e-3 m/px.
- `accel.py`: position s along the straight path (direction (-0.899, 0.438)).
  - The clip has duplicated frames (6, 13, 25, 28, 35, 38) and double steps (5, 10, 23, 27, 34, 37), so the raw
    one-frame backward difference at frame 24 is meaningless (-16 m/s²).
  - With the true render-index mapping from the scene record, the speeds rise linearly (uniform acceleration).
  - Quadratic fit of s(t), true index: 585 px/s² (frames 4–36), 583 (8–36), 581 (14–34), 579 (4–38).
  - Quadratic fit, raw frame index: 580 (4–36), 581 (8–36).
  - Second route, a linear fit of the per-render-step speeds (frames 5–36): 583.7 px/s².
  - These give a ≈ 584 px/s² × 1.190e-3 = **0.695 m/s²**. The motion is uniformly accelerated, so this is the value
    at t = 1 s.

## SAM 3 check
- Box-prompted "beige disc" masks on frames 12, 24 and 30 (the text prompt "chess piece" found nothing).
  - SAM centroids are within 1–3 px of mine (the vertical offset is constant, so it does not affect acceleration).
  - SAM main-axis lengths are 90–97 px against my 81 px, which is more than 3 % apart.
- Zoomed overlay `frames/cmp24.png` (blue = mine, red = SAM): the SAM outline spills about 5–8 px onto the brown rim
  and the dark trough shadow around the piece. My mask follows the light piece's ends. I therefore keep 81.5 px.
  With SAM's ~93 px, the answer would be about 0.61 m/s².

## Confidence
Good. The fitted acceleration is stable to about ±1 % across windows and methods. The main uncertainty is the
pixel diameter (±2 %).
