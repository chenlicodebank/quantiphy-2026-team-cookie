# Q14: speed of the person at t = 1.0 s (frame 24), prior: person height 1.75 m

Time base: fps = question_fps = 24, so frame 24. There is no re-timing issue.

## Image motion (scene/tracks/person.csv, checked)
- The head top moves very steadily down the image: 371 -> 476 px over frames 2-71, which is 1.52 px/frame. Over frames 16-32 (around t = 1 s) both the centroid and the head move 1.55 px/frame. The x drift is about 0.1 px/frame.
- So v_img ≈ 1.53 px/frame ≈ 36.8 px/s, moving straight down the image (toward the camera, along the ground).
- Feet plateaus (the lowest foot planted) give a step of 25.7 px every about 16.9 frames.

## Scale: the view is oblique, not 2D
The camera looks down at an angle phi. Under near-orthographic projection (the person shows no perspective lean or size change), a vertical length maps to s·cos(phi) px/m and ground depth (the walking direction) maps to s·sin(phi).
- Vertical scale: the head-to-feet height at mid-stance is about 38.5-40 px (frames 17, 34, 51, 68) for about 1.73-1.75 m, so c = s·cos(phi) ≈ 22.3 px/m.
- Tilt phi, from three independent cues:
  - Rectangle on the boat's foredeck hatch (`zoomboat.py`, frames/hatch.png): sin²phi = -b1b2/(a1a2), giving phi ≈ 49.5°.
  - Green deck mat: phi ≈ 45°.
  - Person's width across the shoulders and arms, 17.5 px (`body.py`), taken as about 0.50 m: s ≈ 35 px/m, so cos(phi) = 0.64 and phi ≈ 50°.
  - The cabin roof gave inconsistent readings (its shape is non-box or the overhang is unclear), so I discarded it.
- Taking phi ≈ 49°, the ground-depth scale is d = c·tan(phi) ≈ 26-27 px/m.

## Answer
speed ≈ 36.8 / 26.3 ≈ 1.40 m/s. The individual routes give 1.36 (width-based s), 1.41 (hatch) and 1.65 (mat).
Cross-check: the naive single-scale 2D route (1.75 m / median 45 px height) × 36.8 px/s also gives 1.42 m/s.

Caveat: a "natural gait" argument (cadence 85 steps/min with a typical 0.7 m step) would suggest about 1.0 m/s and phi ≈ 57°. The geometric cues disagree with that, which implies an animated step of about 1 m, so I trusted the geometry.

Confidence: moderate, about ±15%.
