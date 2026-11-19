# Q61: speed of the bicycle at 1.0 s (m/s)

The prior is "length of the white car = 6 m". The white car is the white van. The bicycle is the cyclist in the vertical
road (scene `pedestrian_road`, x≈917). This is a 2D top-down clip, so one metres-per-pixel scale comes from the van.
The question and the file both run at 24 fps, so t = 1.0 s is frame 24.

## Scale (measure_van.py)
- I took a vertical brightness profile through the van centre at f0, when the van is at rest and has no motion blur.
  - The front edge is the grey front bumper, which has a highlight, so it is geometry and not shadow. It starts at y≈801.5.
    (Above it, y 768–800, there is only a soft shadow gradient.)
  - The white body begins at y 811.6 and the rear edge is at y≈1046.5.
  - Bumper-to-bumper length = **245 px**. The width is 86 px.
- SAM 3 "white van" at f0 gives box y 802.6–1048.1 (245.5 px) and length_px 244. That agrees with my 245 px within 0.4%.
  The overlay outlines the whole van.
- The scene record gives 236 px (body only, without the bumper) and 246 px for the track mask. I use 245 px, which includes the bumper.
- Scale: 6 / 245 = 0.02449 m/px.

## Bicycle speed (measure_bike.py → bike_track.csv)
- The bicycle rides straight up at constant speed (x varies by only 917–918.5).
- Per-frame steps around f24 are 8.1–9.4 px, which is pixel noise around a constant value.
- Linear fits over f2–71: 8.94 px/frame (centroid), 8.94 (weighted centroid), 8.90 (bbox middle).
- Mean step over f21–26: 8.84–8.93 px/frame.
- Second route: a SAM 3 box-prompted track ("person", tracks/person_0.csv) gives 214.24 px/s = 8.93 px/frame.
  Its step at f24 is 622.2 vs 631.4 = 9.2 px. The overlay follows the rider over the whole clip.
- The scene record gives (825.4−204.5)/70 = 8.87 px/frame.
- Adopted value: 8.93 px/frame = 214.3 px/s.

## Answer
214.3 px/s × 0.02449 m/px = **5.25 m/s**.
If the scale used the 244 px SAM length instead, the answer would be 5.27 m/s, which is within 0.5%.

Confidence: high (about ±2%). The main uncertainty is whether the van's 6 m includes the front bumper. A body-only length
of 236 px would give 5.45 m/s.
