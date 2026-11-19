# q_697: height of the black cat (including its tail)

- 2D scene with a static camera, at 24 fps (the file rate and question_fps agree). The prior is the cat's speed, 1.041 m/s.
- **Pixel speed:** the cat walks at a steady pace along +x. Several routes agree:
  - Linear fit of the mask centroid: 5.45 px/frame.
  - Net change over the clip: 5.49 px/frame.
  - bbox centre: 5.40–5.46 px/frame.
  - Nose edge: 5.41–5.43 px/frame.
  - Windows of whole gait cycles: 5.38–5.50 px/frame.
  - I adopted 5.44 px/frame, which is 130.6 px/s.
- **Scale:** 1.041 / 130.6 = 0.00797 m/px.
- **Height in pixels (measure.py, combine.py):**
  - Top: the top of the dark-fur component (the raised tail tip is the highest point), measured per frame. It runs from y 841 to 848.
  - Bottom: the lowest paw (feet_y in the track), y 918 to 921.
  - This gives 73–79 px per frame, median 77, mean 76.6.
  - Check by eye on a 4x zoom of frame 0: tail tip at about y 844 and paws at about y 920, so about 77 px.
  - The record's bbox height (median 75) is a little low because its mask misses the thin tail tip.
- **Answer:** 77.5 px × 0.00797 = **0.618 m**. The range across the gait is 0.58–0.63 m.
- **Confidence:** moderate to good. The main uncertainty is which frame or pose the reference used (±3%), plus ±1% from the speed.
