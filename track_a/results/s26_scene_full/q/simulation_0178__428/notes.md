# Q428 – displacement of the big elephant (m)

Prior: speed of big elephant = 2.313 m/s (constant walk). fps = question_fps = 24, 60 frames (f0..f59, 2.458 s).
2D side view; big elephant walks steadily left→right the whole clip, no stops/turns (scene record, checked with check.py).

Route 1 (constant speed): displacement = 2.313 m/s × 59/24 s = 5.686 m (motion is straight, so path ≈ net; record path 413 px vs net 411 px).

Route 2 (pixel scale from prior): pixel speed by linear fit of centroid_x = 6.882 px/frame (body centroid 6.853,
body edges 6.91–7.02) → 0.01400 m/px; net dx f0→f59 = 411.1 px (centroid), 409–430 px across reference points
→ 5.76 m (centroid fit), 5.69 m (net/59 per-frame mean, identical to route 1 by construction).

Routes agree within ~1.3%. Answer 5.69 m. Confidence: high (gait oscillation is the only noise source).
