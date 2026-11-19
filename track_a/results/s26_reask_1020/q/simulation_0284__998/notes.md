# Q998: width (wingspan) of the plane

- 2D top-down render with a static camera. The file is 24 fps, but question_fps = 25 is used for timing, as the convention requires.
- Prior: speed = 22.16 m/s. Track (scene/tracks/aircraft.csv, ref_x): after frame 1 the per-frame dx is constant at -34.25 px/frame
  (median and mean of frames 2-60 are 34.25 and 34.26).
  Pixel speed = 34.25 x 25 = 856.25 px/s, so the scale = 22.16 / 856.25 = 0.02588 m/px.
- Width = wingspan (across the direction of travel) = 725 px. This comes from the record's shadow-free median stack.
  Two checks: the frame-24 grid read gives y ~369-1091 (about 722 px). wingspan.py gives 734 px at frame 24 (threshold 40), but the shadow
  inflates that mask at lower thresholds and in later frames.
- Width = 725 x 0.02588 = 18.76 m. This is plausible for a fighter-type aircraft with wingtip pods.
- Under the other reading, length = 566 px x 0.02588 = 14.6 m.
- Confidence: good, about ±2% (the uncertainty is in the pixel wingspan).
