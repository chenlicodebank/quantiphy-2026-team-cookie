# q_672 — diameter of the white fur carpet (m)

Prior: robot vacuum diameter = 0.438 m. No depth_info. The video is a 2D overhead render with a static camera, and both
objects lie on the floor, so I used one m/px scale from the vacuum's pixel diameter. fps 24 = question_fps, so time
does not matter for this size question.

## Measurements (frame 77, all objects static; robot stopped by frame 70)
- `rug_fit2.py`: I cast rays from the approximate rug centre and placed the edge at the half-level crossing between
  the rug (~160 gray) and the carpet (~115). I fitted a circle to the visible arc (left, top, bottom; the sofa hides
  the right side) with outlier rejection. Result: centre (434.9, 832.7), **diameter 477.4 px** (fit residual
  1.6 px, 361 points). Using the max-gradient edge instead gives 478.3 px. The overlay (`frames/rug_fit2.png`) sits
  on the fur edge.
- `robot_fit.py`: the same half-level edge method on the vacuum gives **120.56 px** at frames 72/77 (stationary),
  and 120.4–121.7 px at moving frames. The scene record's 117.8 px comes from a tighter mask threshold (gray > 185),
  which sits inside the anti-aliased edge (its bbox is 119 px). I used the same edge definition for both objects so
  the ratio is consistent.

## Answer
1.734 m = 477.4 / 120.56 × 0.438. For comparison:
- Using the record's 117.8 px for the vacuum gives 1.775 m (+2.4%).
- Using the max-gradient rug edge gives 1.737 m.

## Check / caveats
- The rug edge is soft fur, so its exact boundary carries about ±1% ambiguity.
- The vacuum's top is a few cm above the floor. With an unknown camera height this could make the vacuum look about
  1–2% larger than floor level, which would push the true answer slightly up. I made no correction.
- Plausibility: a fur rug about 1.7 m across is realistic.
- Confidence: about ±3%.
