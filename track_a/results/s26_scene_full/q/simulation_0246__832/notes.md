# Q832: speed of the rabbit at 1 s (prior: antelope speed = 1.277 m/s)

The video is a 2D top-down render at 30 fps (the file rate and question_fps agree). The antelope is the kudu, and the rabbit is the small orange animal in the upper row (the scene record calls it the "rodent"). Both walk at a steady pace in +x on the same floor plane, so one metres-per-pixel scale comes from the kudu's speed.

## Method (an.py, an2.py using the scene/ tracks)
The per-frame speeds swing with the gait: about ±30% for the kudu (period about 20 frames) and about ±40% for the rabbit (period about 13 frames). To remove this, I averaged each animal's displacement over whole gait cycles.
- **Kudu**, 60-frame (3-cycle) windows:
  - trunk 9.364, mask centroid 9.346, nose 9.398 px/frame, so I used **9.38 px/frame**.
  - The `core` point gives only 9.10. It includes the tail, which drifts backward as it straightens over the clip, so I left it out.
  - Scale: 1.277 / (9.38 × 30) = 4.54e-3 m/px.
- **Rabbit**, 65-frame (5-cycle) windows:
  - centroid 8.507, bbox centre 8.475, rear edge 8.488, front edge 8.462 px/frame, so I used **8.49 px/frame**.
  - The one-cycle window centred on frame 30 (frames 23→36) gives 8.49 by centroid, the same value. Its instantaneous per-frame value (8–11 px) is gait noise.
- **Rabbit speed** = 8.49 × 30 × 4.54e-3 = **1.156 m/s**. This equals 1.277 × 8.49 / 9.38.

## Check
Four reference points on each animal (centroid, both bbox edges, bbox centre) agree within 1% for the rabbit. Three of the kudu's points agree within 0.6%. The speed ratio of 0.905 is stable whichever window is used.

## Caveats
- If the kudu's prior speed was taken from the `core` point (9.10 px/frame), the answer would be 1.19 m/s.
- Perspective (the kudu's origin sitting higher above the floor) cannot be corrected because no depth is given.

Confidence: moderate-high, about ±5%.
