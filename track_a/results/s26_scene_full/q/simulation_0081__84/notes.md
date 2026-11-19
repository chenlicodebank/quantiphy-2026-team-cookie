# Q84 – walking person's speed at t = 0.5 s (frame 12; fps = question_fps = 24)

Scene: a fixed top-down camera looking at a grey floor (2D). The pedestrian walks +x at y≈440, and the cyclist rides −x.

## Scale (prior: bike length 1.7 m)
- The bike's cyan mask runs from the front-wheel tip to the end of the rear rack: 381–382 px at frames 10–15. The record's value matches what I see in frame 12 (x 1045 to 1427).
- Scale: 1.7 / 382 = 4.45e-3 m/px.

## Pedestrian motion (track_ped.py)
- The pelvis is hidden under the torso, so I tracked a proxy: the centroid of the shirt/torso mask (bluish-white pixels, b−r ≥ 6).
  - Its per-frame x steps are steady at 12.3–13.5 px.
  - Frames 10–14: 12.5, 12.8, 12.6, 12.3, 13.2. The step at frame 12 (11→12) is 12.6 px.
- Second route, the head blob centroid from the record: step 11→12 = 12.4 px, local mean ≈ 12.6.
  - The shirt mask's left and right edges each move 12–13 px.
- The routes agree: 12.6 px/frame = 302 px/s, which gives 1.346 m/s with the raw 2D scale.

## Perspective correction
- The rider's head shifts relative to the bike by about 0.040 px per px of image x. That implies a camera about 25 m above the rider's head.
- The bike length is measured at about 0.5 m height, while the torso proxy is at about 1.0–1.3 m. Points that are higher look slightly bigger, so the torso's pixel motion is enlarged by about 2–3%.
- Corrected speed ≈ 1.346 × 0.97 ≈ 1.31 m/s.

## Answer
1.31 m/s. This is a plausible walking speed. The bike's speed comes out at 47.4 px/frame ≈ 5.1 m/s, which is also plausible.

Confidence: moderate-high, about ±5%. The main uncertainties are the pelvis's within-gait speed variation and the size of the perspective correction.
