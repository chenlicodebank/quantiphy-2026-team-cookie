# Q1014 – length of the fish (m); prior: fish speed = 0.67 m/s

Top-down 2D simulation, 24 fps (file fps = question_fps), static camera. A single shark swims right to left.

## Scale (from the speed prior)
- `speed.py`: uses the template-tracked body point from scene/tracks/shark.csv. I checked this point on crops and it sits on the shark. Mean per-frame step over frames 1-70 = 23.65 px/frame (the chord gives 23.59 and a 5-frame smoothed path gives 23.64). Early frames 2-30 give 23.9 px/frame and late frames 30-70 give 23.4.
- Scale = 0.67 m/s / (23.6 x 24 px/s) = 0.00118 m/px.

## Length in pixels (`crops.py`, 1.5x gridded crops; read by eye)
- **Correction to the record:** in early frames the record puts the snout on the grey wedge at about fin - 253 px. That grey wedge in front of the black shadow is actually the shadow's snout. The real snout tip is consistently about 212 px ahead of the pectoral fin tips, and this holds in every frame: early frames 14 and 22 (the pale head front) and late frames 38, 50 and 62 (the grey wedge tip).
- Snout to tail tip: f14 667, f22 660, f38 634, f50 640, f62 654 px. The record's late manual values are 625-655. The ±10-15 px spread comes from the tail swing.
- The fish looks about 2-3% larger in early frames, and its pixel speed is higher by the same amount (23.9 vs 23.4 px/frame). The shadow scale points the same way: the fish is slowly getting farther from the camera. So I used the ratio length / pixel speed at the same time, which does not depend on depth:
  - early: about 662 / 23.9 = 27.7 frames
  - late: about 645 / 23.4 = 27.5 frames
  - maximum straight-body length: about 28.0 frames

## Answer
Length = 0.67 x 27.6 / 24 ≈ 0.77 m. Taking a slight weight toward the straight-body (rest) length gives **0.775 m**.

## Second route
The early and late windows were measured separately and give 0.773 and 0.768 m. The maximum straight length gives 0.78 m.

## Confidence
Moderate to good, about ±4%. The main uncertainties are the faint tail tip (±5 px) and tail-swing deformation compared with a rest-pose bounding box.
