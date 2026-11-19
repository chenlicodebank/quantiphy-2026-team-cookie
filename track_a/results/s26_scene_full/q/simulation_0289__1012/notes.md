# q1012 — length of the fish (m); prior: fish speed = 0.67 m/s

2D Blender scene with a static camera. The fish swims leftward, parallel to the image plane, at a constant
height (bbox height stays at 290–292 px). fps = question_fps = 24, so there is no re-timing.

## Method (measure.py, using scene/tracks/koi_fish.csv; I checked the track against a contact sheet)
- Pixel speed: the rigid trunk-texture track over the moving frames 2–70 averages 22.64 px/frame, i.e. 543.3 px/s.
  Frames 0–1 and 70–71 are duplicate static frames, so I left them out.
- Scale: 0.67 / 543.3 = 1.2333 mm/px.
- Fish length: the snout-to-tail-fin bbox width once the whole fish is visible (frames 4–71) has a median of
  613.5 px. It grows from about 593 to 643 px over the clip, apparently because of fin/tail animation.
- Length = 613.5 × 1.2333e-3 = **0.757 m**. Over the frame range it spans 0.726–0.797 m.

## Second route
Using the bbox-centre speed instead (535.8 px/s) gives a scale of 1.2504 mm/px and L = 0.767 m, about 1.4% higher.
The two routes agree.

## Confidence
Moderate to good. The main uncertainty is that the fish's apparent length changes by ±4% over the clip.
The scale itself is good to about 1.5%.
