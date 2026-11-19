# Q4: speed of the boat at 1.0 s (m/s). Prior: boat length = 3.62 m

The file rate and question_fps are both 24, so t = 1.0 s is frame 24. The video is a 2D top-down view with a static camera (scene/ record: camera shift ≤ 0.003 px).

## Measurements (measure.py: my own HSV mask, filled outer contour, PCA axes)
- Boat length along its axis: 209.7 px at frame 0 (stick tip included), 207.8 px at frame 24 (the tip is partly in shadow) and 206.0 px at frame 36.
- Boat width: 71.6 px.
- Horizontal extent in the image (AABB x): 197 px at frame 0 and 195 px at frame 24. The boat is tilted about 22° in the image.
- SAM 3 mask ("white rowboat"):
  - Frame 0: length 206.9 px, horiz 194 px.
  - Frame 24: length 206.9 px, horiz 194 px.
  - SAM leaves out the thin stick at the lower-left tip, which my mask and the frame-0 record include. On a 4× zoom of frame 24 (frames/my_mask_f24.png) the stick is visible.
  - The difference is within 1.5%, below 3%.
- Centroid speed:
  - Steps around frame 24: 23→24 = 3.32 px and 24→25 = 3.26 px.
  - Mean step over frames 12-36: 3.247 px/frame.
  - Linear fit over all 74 frames (scene record): 3.249 px/frame. The motion is constant-velocity with ~0.13 px of noise.
  - I use 3.248 px/frame × 24 = 77.95 px/s. The raw one-frame value at frame 24 is 3.32 px, 2% higher, which is noise.

## Scale and the ambiguity
- Reading A, length along the boat axis (~208 px, 206.9–209.7): 0.01740 m/px, so v = 1.356 m/s.
- Reading B, world-AABB x extent if the boat is yaw-rotated in world (~196 px, 194–198): 0.01847 m/px, so v = 1.440 m/s.
- The answer is 1.39 m/s, taken between the two readings (~203 px). It is within about 3% of either reading.

## Second-route check
- The window 12-36 (3.247 px/frame) and the full-clip fit (3.249 px/frame) agree to 0.1%.
- SAM's centroid moves (843.0, 703.4) → (770.7, 731.3) over 24 frames, which is 77.5 px/s. This agrees with my value to within 0.6%.

## Confidence
The pixel speed is good to about 1%. The main uncertainty is which pixel length matches the prior's "length" (about ±3%).
