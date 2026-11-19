# q3062 – length of the black car (prior: white car length = 4.572 m)

Internet convention: one scale = 4.572 m / white-car pixel length (bumper to bumper, along motion = image y);
black car length = its pixel length × that scale. No timing involved, so fps vs question_fps (28.70 vs 30) does not matter.

## Measurements (edges.py, centreline intensity profiles, x 990-1080)
- White car (fully visible frames 11-21): 453 px (frames 11-16), 449-451 px later; scene record says 457 (looser mask). Visually
  checked on frame 14: rear ~103, front ~559 → 456 px.
- Black car: the scene record's rear_y includes the shadow halo (e.g. frame 0: 2583, true dark outline ~2597-2600).
  Re-measured bumper-to-bumper: 450 px (frame 0) rising smoothly to 488 px (frame 19) – perspective: lower in the
  image the tailgate/rear face becomes visible and ground scale grows (~12 % top to bottom).
  Frames 0-10: 450-472; frames 11-19 (both cars fully visible): 474-488, mean ~481.

## Candidates
- Same-frame (frames 11-19) ratio: 481/452 × 4.572 = 4.86 m
- Black car at frame 0 (its clearest, least tilted view) vs white 455: 450/455 × 4.572 = 4.52 m
- Mean over all full frames: ~469/453 × 4.572 = 4.73 m; scene record 472/457 → 4.72 m
Answer 4.70 m: within ~4 % of all of these readings. Real-world check: a compact SUV/hatchback of ~4.5-4.8 m, plausible.

Confidence: moderate (the main uncertainty is perspective / which frame the annotators used, ±4 %).
