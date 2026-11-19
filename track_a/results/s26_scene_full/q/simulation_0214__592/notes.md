# Q592 — speed of the dog at t = 1 s (frame 24, 24 fps; file fps = question fps)

**Object identification:** the scene record calls the lower animal a "tabby_cat". It is actually the dog: a large brindle animal with a placeholder head patch, walking right to left. The black cat is the upper animal, walking left to right.

**Scale (2D top-down, same floor plane):** the black cat walks at a steady speed. Its front bbox edge goes 647 → 1185 px over 49 frames, and its body centroid goes 570.1 → 1107.7 px. Both give 10.98 px/frame, i.e. 263.5 px/s. The prior is 0.94 m/s, so the scale is 0.003567 m/px.

**Dog speed:** `track_dog.py` NCC-tracks three fur patches on the dog (rear/hips, mid-back, shoulders) with sub-pixel peaks over frames 16–32.
- One-frame steps at frame 24: rear 13.01, mid 12.48, front 12.54 px/frame.
- Mean steps over frames 20–28: rear 13.04, mid 12.76, front 12.82 px/frame.
- Record cross-check: the record's torso track gives 12.5 px/frame at frame 24, bbox_x0 gives 12.75 px/frame on average over frames 20–28, and the body centroid gives 12.2 px/frame (noisy).

I take 12.8 px/frame, which is 307 px/s, so the speed is **≈ 1.10 m/s**. The plausible range is 1.07–1.11 m/s.

**Confidence:** moderate to high, about ±4%. The main uncertainties are where the root/pelvis is relative to the tracked patches, and a small perspective effect because the dog's back sits higher than the cat's.
