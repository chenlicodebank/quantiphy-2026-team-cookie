# q1912 — speed of the box at t = 2 s (m/s)

2D simulation (segmented), fps 120 = question_fps; t = 2 s -> frame 240. Prior: box width = 1.33 m.

## Scale
Brown-box mask (track_box.py -> box_track.csv): horizontal extent 277.9 px around f240 (record: 278 px at f240,
280 px at f0). Using 278.5 px gives 1.33 / 278.5 = 0.004776 m/px. The visible horizontal extent across the rear-facing
box is taken as its width. Check: the container is 567 px = 2.71 m, which is plausible for a truck body.

## Motion
The box rides on the rising container. Its bottom edge moves with container_dy to within 1 px over the whole clip.
Its top edge drifts down relative to the container (up to 18 px), because the apparent height shrinks (the top
face is foreshortened). So the bottom edge and the container show the true motion of the origin.
- Route 1: container_dy (template match, ±0.1 px), quadratic fits around f240 over windows 160–320, 200–280 and 220–260:
  0.229–0.230 px/frame.
- Route 2: my own box-mask centroid, quadratic over the same windows: 0.204–0.236 px/frame (noisier). Consistent.
- Horizontal motion is about 0.

Speed = 0.230 px/frame x 120 = 27.6 px/s, x 0.004776 m/px = 0.132 m/s.

Confidence: good (±3%). The main uncertainty is the width reading. If the visible extent were the box's
length rather than its width, the scale would differ, but the reading used here is the natural one.
