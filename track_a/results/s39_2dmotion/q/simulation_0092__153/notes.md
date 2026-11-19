# Q153 — speed of the plane at 1.0 s (m/s)

Prior: car length = 5.67 m. 2D video, file fps = question_fps = 24, so t = 1.0 s -> frame 24.

## Method (measure.py -> my_boxes.json)
- Each frame is compared with the uniform grey background (|RGB diff| > 12, 3x3 opening). Rows < 590 are the plane and rows >= 590 are the car. The script outputs per-frame bounding boxes.
- Car pixel length (bbox x-extent): 137 px near the image edges, falling to a minimum of 129 px at x ~ 940 (frame 35, near the image centre). The extra length near the edges comes from perspective (the end faces show off-axis). I used the clean side-on value, 129 px.
  Scale = 5.67 / 129 = 0.04395 m/px.
- Plane motion: the nose (left bbox edge) moves exactly 57 px/frame in frames 14-30, including 57 px for frame 23->24. The bbox centre moves 778.5 - 835 = 56.5 px at frame 24. The motion has constant pixel speed.
- Speed at frame 24 = 57 px x 24 fps x 0.04395 = **60.1 m/s**.

## SAM 3 checks
- Car, frame 35: SAM box 872.6-1003.0 (130.4 px) vs my 129 px (scene record: 128). The difference is 1.1%, under 3%. The overlay outlines the whole truck.
- Plane, frames 23/24: SAM box-centre step is 57.05 px and the centroid step is 56.4 px. My nose step is 57 px. SAM's length is 857-858 px, the same as mine.

## Second route / sanity
- The plane's length of 857 px x 0.04395 = 37.7 m, which matches a real A320 (37.6 m). So the plane and car are consistent with being at the same depth, and the single scale holds.
- Car speed 28.45 px/frame -> 30 m/s, so the plane moves at about twice the car's speed.
- Range of the answer for car lengths of 128-130.4 px: 59.5-60.6 m/s.

Confidence: high (about ±1.5%).
