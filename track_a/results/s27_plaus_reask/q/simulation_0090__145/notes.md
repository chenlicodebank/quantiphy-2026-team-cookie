# Q145: body length of the small bird (crow)

- 2D scene, static camera, 24 fps (file and question_fps are the same). The small bird is the crow. It flies horizontally to the left at a constant speed in frames 2–18.
- Scale comes from the prior, crow speed = 11 m/s:
  - A linear fit of the crow's leading edge (x0) and trailing edge (x1) over frames 2–18 gives 95.63 and 95.74 px/frame, which is 2296 px/s.
  - m/px = 11 / 2296 = 0.00479.
- Body length is the horizontal mask extent, beak to tail (checked on a zoomed frame 4: about 1413 to 1523 px). I measured it with my own mask (`measure.py`, background = median of frames 24–29):
  - Median 112 px at threshold 20, 111 px at threshold 40.
  - This agrees with the scene record (bbox_w 110–113 px).
- Length = 111.5 px × 0.00479 = 0.534 m.
- Check: two mask thresholds give 0.532 and 0.536 m, and the leading and trailing edges give the same speed. 0.53 m is plausible for a crow or raven, so the scale passes the size check. Confidence: high (about ±2 %).
