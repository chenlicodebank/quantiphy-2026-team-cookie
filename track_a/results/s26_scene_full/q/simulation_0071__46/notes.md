# Q46: walking pedestrian's speed at 1.0 s (m/s)

The video is 2D: a top-down orthographic-like view with no visible perspective. fps = question_fps = 24, so t = 1.0 s is frame 24.

**Scale.** The prior gives the yellow (peach) car a length of 5.44 m.
- The record's PCA length is 222.5 px.
- My own background-subtraction bbox, with the car heading vertical (frames 0–5), gives 224–226 px, which may include a 1–2 px edge.
- I used 223 px, which gives 0.02439 m/px.

**Pedestrian.** The pedestrian is at about (1381, 844) at frame 24 and walks +x at a nearly constant pace. The centroid is noisy with the stride, so I used linear fits of the centroid in windows around frame 24:
- Record track: 14–34 smoothed gives 2.12 px/frame and 18–30 gives 2.02. The whole clip (2–71) gives 2.03.
- My own re-tracking (`measure.py`, median background over the crop): 14–34 gives 2.15, 18–30 gives 2.20, 10–40 gives 2.08, and 2–71 gives 2.01.
- Adopted value: 2.10 px/frame.

**Result.** Speed = 2.10 × 24 × 0.02439 = 1.23 m/s. Across the window choices the result ranges from 1.18 to 1.29 m/s.

**Second-route check.** The whole-clip mean speed is 2.02 px/frame, or 1.18 m/s. This agrees within about 4 %, and the value is plausible for a walking person.

**Confidence:** moderate to good, about ±5 %.
