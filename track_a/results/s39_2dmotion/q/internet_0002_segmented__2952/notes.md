# Q2952 — speed of the red car (m/s); prior: lane width = 3.66 m

Video: 1280x720 file at 24 fps (44 frames), question_fps = 30; all times/differences use 30 fps per file frame.
Static nadir camera (scene/ record: dashes move < 0.5 px). File frames 3, 8, 14, 19, 25, 30, 36, 41 repeat the
previous frame (an ~25->30 fps style pull-down, consistent with the original being 30 fps).

## Scale (measure.py)
Lane-dash centroids from the temporal-median background, a line fit per dash row. The red car's lane lies between rows at
y ≈ 327.5/433.2 (x=200) … 332.0/439.9 (x=1150): centre-to-centre spacing 105.7–107.9 px, mean 106.8 px along the car's
path -> 3.66/106.8 = 0.03427 m/px. (The other lanes are 101–112 px; the mean over all 5 lanes is ≈106 px, within 1%.)
SAM 3 check ("white line", f0): dash centroids at y 328.2 and 434.4 (x≈250) -> 106.2 px vs. mine 105.8 px at
x=250 (0.4% apart).

## Motion (measure.py -> red_track_own.csv, speed.py)
Red car mask = difference from the median background, largest blob in y 300–500. Fully in view f0–f35.
Centroid (150.7, 382.4) at f0 -> (1171.4, 426.6) at f35. SAM 3 "red car" gives (150.6, 382.5) and (1171.3, 426.7):
the same to within 0.1 px. The overlays hug the car.
- Route 1: the mean per-frame 2D step over f0–f35 is 29.23 px/frame -> x30 x 0.03427 = **30.05 m/s**.
- Route 2: a linear fit of x vs. frame (centroid 28.74, front bumper 28.71 px/frame) gives 29.6 m/s. The fit is slightly lower
  because of where the duplicates fall; the end-to-end displacement is 1021.7 px / 35 frames = 29.19 px/frame -> 30.0 m/s.
Other readings, for reference: the non-duplicate step (35.2 px) x30 gives 36.2 m/s; the file's 24 fps gives 24.0 m/s.
The answer follows the question_fps convention averaged over frames (the duplicates are real elapsed frames).

Answer: 30.0 m/s (≈108 km/h, plausible for a highway). Confidence: moderate-high on the pixels and scale (±1–2%). The main
risk is the fps/duplicate-frame convention.
