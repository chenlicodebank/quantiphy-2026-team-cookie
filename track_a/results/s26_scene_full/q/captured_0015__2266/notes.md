# q_2266 — height of the person (cm), prior g = 9.8 m/s^2, no depth_info

File fps = question_fps = 24. Static camera. 2D clip: the scale comes from gravity acting on the tossed plush toy.

## Pixel acceleration of the toy (topedge2.py)
- In the free-flight frames, the record's centroid tracks (best_cy, core_cy) give curvatures from 3.4 to 6.2 px/frame^2,
  because the plush toy deforms and rotates, and its mask merges with the arms near release and catch. So they are not used.
- I measured the toy's head-top edge instead. It is always above the hands, and it is clean in every free frame.
  Method: colour difference to a median background (frames 0-7, 30-42, 66-72), then a sub-pixel crossing at a fixed
  fraction of the head contrast (K = 290), in columns within ±12 px of the toy x. The overlay
  (frames/top_sheet.png) shows the line sitting on the head top in every frame.
  A 50% crossing of a motion-blurred edge sits at the mid-exposure time, so it is unbiased by blur.
- Quadratic fits, a in px/frame^2:
  - Toss 2, threshold 0.5: frames 52-58 give 5.25 (rms 0.14 px); 51-59 give 5.21; 52-59 give 5.27.
    Thresholds 0.3 and 0.7 give 5.12-5.40.
  - Toss 1: frames 16-22 or 17-21 give 5.03-5.66 (noisier; the toy rotates).
  - Record's top edge (best_y0) as a check: 5.05-5.29.
- Adopted a = 5.24 px/frame^2, which is 3018 px/s^2. Scale = 9.8 / 3018 = 3.247 mm/px.

## Person height in pixels
Hair top is at y ≈ 134, shoe sole at y ≈ 641 (checked on zoomed crops frames/head.png and frames/feet.png, matching
scene/tracks/person.csv). That is 507 ± 1.5 px in all frames; the person stands still.

## Result
507 px x 3.247 mm/px = 1.646 m. Answer: **165 cm**.

## Checks and caveats
- Toss 1 and toss 2 give the same acceleration within about 3%, as does the record's independent top-edge column.
- Pinhole check with f = 763 px: the toy depth comes out at 763 x 3.247e-3 = 2.48 m. A 1.65 m person at that depth
  would be 507 px tall, so this is consistent only if the toy is at about the person's depth.
- The toy is tossed from the hands, slightly in front of the body (mostly to the side in the image). If it is about
  0.1-0.2 m nearer the camera, the true height would be 4-8% larger (about 170 cm). The shoe soles (+2-3 cm) work in
  the opposite direction.
- Answer kept at the direct 2D value of 165 cm. Confidence: about ±5%.
