# q_3100 – distance from the left red vertical line to the white line (m)

The "white line" is the light-blue/white stripe at x≈1173–1240. The "red vertical line on the left" is the maroon line at x≈210–259. Measurements are in frame 29, which has no ball and was taken with a nearly static camera (drift ≤ 2 px horizontally). Script: `measure.py`.

**Scale (prior).** The ball's speed at 0.5 s is 2.94 m/s. Frame 15 is t = 0.5 s at 30 fps; fps and question_fps agree.
- Ball-centre step from frame 15 to 16 (forward difference, as the annotators did, using camera-stabilised centres from scene/tracks): 78.7 px/frame, i.e. 2362 px/s.
- The backward step is 77.4 px, and the mean of steps 12–18 is 78.1 px, so the speed estimate is consistent to within about 1 %.
- Scale = 2.94 / 2362 = 1.245e-3 m/px.

**Line distance in pixels (code, colour masks, frame 29).**
- Centreline to centreline: 957 px at y=540–600 (the ball's path height), 965 px at y≈680 (mid-image) and 985 px at y≈980. The lines are slightly non-parallel because of mild keystone.
- Inner gap (red line's right edge to the white line's left edge): 914–942 px.
- Outer extent: 1000–1029 px.

**Answer.** The centreline-to-centreline distance at mid-image is ≈ 962 px × 1.245e-3 = **1.20 m**.

**Other readings.**
- Edge to edge (inner gap, about 916 px near the ball path): 1.14 m.
- Outer extent: 1.25 m.

**Check.** The ball's diameter is 225 px × scale = 0.28 m, and a real basketball is 0.24 m. The ball's centre sits about 0.12 m above the floor, so it is closer to the camera; that is the right direction for the discrepancy, so the scale is plausible.

**Confidence:** moderate. The main uncertainty is which points on each line the annotator measured between (±5 %).
