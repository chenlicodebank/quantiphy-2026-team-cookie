# q_231 – speed of the swim ring at 1.0 s

2D top-down Blender render. The question uses 24.0 fps, so t = 1.0 s is frame 24. The file rate is 24.0048 fps, which makes almost no difference here.
Scale comes from the prior: the ring's outer diameter is 1 m.

## Measurements (my own scripts: measure.py, radial.py)
- **Ring centre per frame** (measure.py → my_track.csv)
  - Method: mask on max(R,B) − G at half-maximum, take the largest component, fill it, use the centroid.
  - Linear fit over frames 0–119: vx = 0.2851 and vy = 0.2857 px/frame, so speed = 0.4036 px/frame.
  - Fit over frames 14–34 only: 0.390 px/frame.
  - Raw step 23→24: 0.458 px. This is noisy, because segmentation noise is about 0.1 px.
  - The motion is uniform, constant-velocity drift with no events, so the speed at frame 24 is the fitted velocity.
- **Outer diameter**
  - Radial half-maximum edge over 180 angles (radial.py), median: 73.55 / 73.36 / 73.00 / 72.86 px at frames 0 / 24 / 60 / 119.
  - Half-maximum mask extents: 74 × 74 px.
  - scene/ record: ellipse fit 73.6–74.2 × 70.9–71.4, recommended value 73.
  - I use **73.5 px**.
- **SAM 3 check**
  - Segment at frame 24: box 75 × 75 px (length 77.3 / width 75.8 along its principal axes), centroid (401.1, 394.3).
  - My values: 74 px extents and centroid (400.6, 393.9).
  - Extents differ by about 2% (under 3%). In the zoomed crop (frames/f24.png) the SAM mask takes in a little of the antialiased blur. Centres agree within 0.5 px.
  - SAM track: linear speed 9.64 px/s at the file fps, which is 0.4016 px/frame. This matches my 0.4036.

## Result
- Speed = 0.4036 px/frame × 24 fps = 9.69 px/s.
- 9.69 px/s ÷ 73.5 px/m = **0.132 m/s**.

## Second route
- The scene/ record's independent fit (0.4023 px/frame) with D = 73 px gives 0.1323 m/s.
- The SAM track's speed with its own 75 px diameter gives 0.1285 m/s.
- The routes lie within about 3% of each other.

Confidence: high (±2–3%). The main uncertainty is where the ring's edge is drawn: 73–75 px.
