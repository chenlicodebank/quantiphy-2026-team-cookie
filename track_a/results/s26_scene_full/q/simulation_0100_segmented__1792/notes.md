# Q1792 – average speed of the boat (m/s)

The scene is 2D: a side view with no perspective and a static camera. The file and the question both give 24 fps, so no re-timing is needed.

## Scale
- Prior: the boat is 10 m long.
- The boat's mask at frame 57 runs from the stern at x=666 to the bow tip at x=1521, so the boat is 856 px long (`measure.py`, checked on a gridded crop at frame 57). This matches the scene record.
- Scale: 10/856 = 0.01168 m/px.

## Motion
- The boat's x-shift per frame comes from normalised cross-correlation with a template of the bow and wheelhouse taken from frame 57, with sub-pixel refinement (`measure.py`).
- Frames 0 and 1 are identical, so the boat is at rest there. From frame 2 on it moves 17.3–18.2 px per frame, a mean of 17.857 px/frame. There is no acceleration and no vertical drift.
- The net shift from frame 0 to frame 57 is 1000.0 px, matching the scene record (1000.1 px).

## Speed
- Over the moving frames only: 17.857 × 24 × 0.01168 = **5.007 m/s**. That is very likely the speed set in the render, 5 m/s.
- As the mean of all 57 per-frame speeds, including the 0 for frame 0→1: 17.544 × 24 × 0.01168 = **4.919 m/s**.
- Answer: **4.96 m/s**, between the two conventions, so it is within about 1% of either one.

## Second check
The template track and the scene record's independent track agree: both give 1000 px total shift and 17.86 px per moving frame.

Confidence: high, within about 2%. The main uncertainties are the ±2 px on the 856 px length and which convention the reference used for the start frame.
