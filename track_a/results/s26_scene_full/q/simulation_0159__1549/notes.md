# Q1549 — How long is the shark (m)?  Answer: 3.16 m

File fps = question fps = 24, so frame i means t = i/24. Principal point assumed at (960, 540).

## Focal length (from the turtle prior; scripts turtle_tm.py, fit_turtle2.py)
- I tracked the turtle shell by template matching (high-pass NCC, with a scale search, chained over reference frames 20 and 40). It is sub-pixel and much steadier than the core centroid in scene/.
- Model: straight-line motion with |a| = 2.639 m/s² (the prior). The origin starts at D0 = 15.232 m along the core-centroid ray, and |O(f12)| must equal 14.968 m.
- Best fit: F = 2617 px (HFOV about 40°), rms 0.7 px in u and 0.4 px in v. It reproduces D(0.5 s) to 0.3 mm. The fit gives v0 ≈ 0 (the turtle starts from rest) and a direction of (-0.78, 0, -0.62) in camera coordinates. The cost profile over F has its minimum at about 2600–2700.

## Shark trajectory (extract.py, fit_dorsal.py)
- Shark mask: same segmentation as scene/scripts/track.py. From it I took the dorsal-fin tip (topmost point), the snout tip (leftmost point) and the tail tip (rightmost point).
- The dorsal-fin tip fits pure translation with uniform acceleration from rest, rms about 1 px over f0–39, so the shark does not rotate.
- **Independent check on F:** with F = 2617, the scale-free fit predicts |P12|/|P0| = 0.9565. The given ratio is 15.744 / 16.474 = 0.9557. So the shark confirms the turtle's F.
- Metric scale comes from D0 and D12. Fitted distances are 16.468 and 15.751 m. Shark acceleration is about 6.9 m/s², in the same direction as the turtle.

## Length (shark_len.py, shark_len_check.py)
- Because the shark is a rigid translating body, snout = P(t) + ds and tail tip = P(t) + dt. I solved for the 3D offsets ds and dt from their image tracks: snout over f12–37 (f0–9 snout is under-segmented), tail over f20–37 (fully in view). The changing viewpoint gives the parallax that fixes the depth of each offset.
- Snout-to-tail vector = (-2.99, 0.25, -1.01) m. That gives a horizontal length of 3.158 m (3D 3.167 m). The body is yawed about 19° from the image plane, which is not along the motion direction.
- Snout rms 6 px; tail rms 5 px, consistent with the tail beat.

## Second-route checks
- **Per-frame length:** with the fitted depth and yaw, I solved L in each frame f20–37 from that frame's pixel span. Values run 3.08–3.22 m with no trend (mean 3.165, median 3.177). A wrong yaw would produce a trend.
- **Frame windows and v-weights:** different choices give L = 3.15–3.25 m. The short f20–33 window gives 2.98 m.
- **F sensitivity:** F = 2400 gives 3.38 m; F = 2800 gives 3.00 m. Both F routes agree on 2617.
- **Body axis forced along the motion direction:** this fits clearly worse (13 px rms against 6 px) and gives L of about 4.1–4.6 m. I rejected it.

## Reading of "length"
Length here is the snout-to-tail-tip extent along the body (horizontal), 3.16 m. If the shark's axis-aligned bounding box were taken in a world frame rotated against the body, it would be larger, but nothing in the video shows such a frame.

Confidence: moderate-high, about ±5%.
