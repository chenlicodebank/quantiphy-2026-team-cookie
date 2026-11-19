# q_1927 — length of the wooden bench (m)

Prior: black cat speed = 0.94 m/s. 2D side-on clip, static camera, 24 fps (file fps = question_fps, so no re-timing).

## Method (measure.py)
- Cat speed in px: I tracked the dark-fur centroid (columns with >=20 black px, largest cluster) over all 50 frames.
  Mean step 17.85 px/frame, linear-fit slope 17.81 px/frame. The scene record's `cx` gives 17.6 px/frame.
  I used 17.75 px/frame, which is 426 px/s. The walk is steady with no acceleration.
- Scale: 0.94 / 426 = 0.002207 m/px.
- Bench horizontal extent: I measured the mask of saturated, non-white pixels on frame 48: x 25–491, which is 467 px.
  The record's max-background box gives 466 px. I confirmed it on a zoomed crop: the left seat corner is at about
  x=26 and the right seat corner at about x=491.
- Length = 466.5 px × 0.002207 m/px = **1.03 m**.

## Checks
- Second route: using the record's cx (17.6 px/frame) gives 1.037 m, and my centroid fit (17.81) gives 1.025 m.
- The bench stands slightly behind the cat's line (feet at y≈990 vs. paws at ≈1021). This is a small depth offset,
  and I applied no perspective correction, following the single-scale 2D convention.
- 1.03 m is plausible for a bench.

Confidence: moderate-high (about ±4%).
