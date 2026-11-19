# q_357 – shark length (m), prior: shark speed = 7 m/s

2D Blender scene, static camera, fps 24 (= question_fps, no re-timing). One m/px scale from the prior:
scale = 7 m/s / (shark pixel speed). Length = pixel length x scale.

## Pixel length (snout.py)
Background = per-pixel median of frames where the shark is elsewhere. Tail tip x1 from |diff|>20 (crisp edge);
the snout is faint, so it is found with a sensitive threshold (blurred |diff|>5) in the snout rows y 290–345,
walking left from the body. Frames 14–30 (shark fully in view): length 907–933 px, median 920, mean 920.2, sd 6.4.
Visual check at frame 18 (zoomed crops): snout tip x≈739, upper tail-lobe tip x≈1661 → ≈922 px. The record's
911 px (threshold 7, jittery snout) is slightly short; threshold-20 masks miss the snout (≈847 px).
Shark is horizontal, so silhouette length ≈ world AABB length (snout to tail tip).

## Pixel speed (speed.py, speed2.py)
Template matching of rigid body parts frame to frame (sub-pixel):
- front (head/gills/dorsal) frames 6–31: 58.2 → 60.2 px/frame, mean ≈ 59.2
- rear body frames 15–35: 58.5 → 59.9 px/frame, mean ≈ 59.2
- single template from frame 18 matched over frames 11–33: 59.2 px/frame
Over the length window (14–30) ≈ 59.3 px/frame = 1423 px/s. (Tail-tip x1 alone gives 55–59 px/frame because the
tail fin flexes; not used.)

## Result
scale = 7 / 1423 = 0.00492 m/px; length = 920 x 0.00492 = 4.53 m.
Check: the record's own numbers are independent of mine. Its snout x0 differences over frames 0–13 give ≈57.7 px/frame and its 911 px length gives 4.60 m. Taking the ends of my measured ranges (length 913–927 px, speed 58.8–60 px/frame) gives 4.45–4.60 m around the central value. (I did not compute a per-frame length/speed ratio.)
Confidence: ±3 %.
