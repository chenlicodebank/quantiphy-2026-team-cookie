# Q803 – height of each glass window (m)

Prior: speed of the horse at the back = 0.874 m/s. The "horse at the back" is the chestnut horse. It trails
the pale horse and is also slightly smaller and higher in the frame, so it is farther away either way.
fps = question_fps = 24. The scene is 2D, so one metres-per-pixel scale is used.

## Speed (measure.py)
Chestnut horse, frames 0-48 (frame 49 is an animation-loop reset and is excluded):
- linear fit of mask centroid x: 77.8 px/s; bbox centre: 78.3 px/s
- net displacement over 2.0 s: 75.7 px/s (centroid), 75.0 px/s (bbox centre)
- Value used: ~76.8 px/s, which gives a scale of 0.874 / 76.8 = 0.01138 m/px.

## Window height
I took column profiles through the centres of the three arched windows (frames 0, 24 and 49, using
unoccluded ones). The window opening runs from the arch top at y≈844 to the sill at y≈949-951, about 105 px.
The glass alone is about 846-948, about 103 px. All three windows are the same height.
105 px x 0.01138 = 1.195 m. Using the glass only (103 px) gives 1.17 m.

## Check
The scale range from the fit and from the net displacement is 0.01123-0.01165 m/px. Combined with
103-106 px of window height, that gives 1.16-1.23 m. Answer: 1.19 m. Confidence: moderate (about ±4%).
