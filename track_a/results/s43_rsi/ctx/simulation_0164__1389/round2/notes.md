# q1389: acceleration of the bowling ball at t = 1 s (frame 24); round 2

**Answer: 0.415 m/s²**, the size of the deceleration. This verifies round 1's switch to 0.41: my own value is within 1.2 %.

## Inputs
- Prior: ball diameter 0.21 m.
- depth_info: 9.391 m at t = 0.5 s, i.e. frame 12.
- question_fps 24, the same as the file's fps (66 frames, 1920x1080).
- t = 1 s is frame 24. The ball rolls with clean tracking over frames 6–37 and hits the pins at frames 37–38.

## Crux
Where the ball's vanishing point (VP) sits on its image path. The lane lines put it at x ≈ 5648; the ball-diameter trend puts it at x ≈ 5300. That gives a ≈ 0.41 versus ≈ 0.30 (C5–C7, C9; C3 averaged the two).

A second possible crux, found this round: the focal length f. The answer is sensitive to it (f = 2450 would give a = 0.54).

## Measurements (my own code)

### 1. `vp_mine.py`: lane VP from the floor lines
- Sub-pixel fits on frame 0 of three cyan floor lines:
  - cyanA: rms 0.064 px;
  - cyanB: rms 0.066 px;
  - cyanC: rms 0.6 px.
- Their pairwise intersections are (5651.2, 207.6), (5648.8, 207.7) and (5646.0, 208.2).
- **VP = (5648, 208) ± 3 px.** This reproduces round 1's (5643.5, 208.4) within 5 px.
- The ball path y = −0.0832x + 678.6 passes at y = 208.7 at that x.

### 2. `roll.py`: second route to the ball VP
- Edges of the wall screens and the pit box near the centre column have a tilt of about 0 (+0.09° at x = 937), so the camera roll is about 0.
- With zero roll the horizon is the row y ≈ 208. The ball path crosses it at **x = 5656**, which agrees with route 1.
- A diameter-trend VP at about 5300 does not fit: it would need the horizon to be tilted 4.9°, parallel to the ball path itself.

### 3. `recon_mine.py`: 3D reconstruction
- Model: the ball centre lies on a 3D line in the direction of the VP ray, anchored at 9.391 m on the frame-12 ray. I used my own least-squares intersection of each ray with that line.
- Time base: frames / 24.
- Results:

| f (px) | a, quadratic fit 6–37 | a, cubic at 1 s | a, slope of per-frame speeds | v(1 s) |
|---|---|---|---|---|
| 3670 | −0.412 | −0.410 | −0.411 | 3.58 m/s |
| 3573 (self-consistent from the late clean frames, with off-axis factor) | −0.419 | −0.416 | — | 3.64 m/s |

- Residuals are 3.3 mm rms.
- Across fit windows a ranges from −0.39 to −0.43.
- With the VP at 5656: same result. With the VP at 5300: a = −0.31, the low answers' value.

### 4. Focal length
The tilts of the "vertical" screen and pit edges, and the slope of the pit's top edge, fit f ≈ 2450 if the principal point is at the image centre. I ruled that out:
- f = 2450 makes the ball 0.30 m at the given depth, 45 % above the exact prior.
- Pins would then be about 0.5 m tall.
- f is fixed directly by the pinhole relation (82 px at 9.391 m for 0.21 m), which gives f ≈ 3570–3670.

`shift_test.py` tests the other way to reconcile the tilts, a lens shift (principal point at (950, 947) or (960, 300)). It changes a by less than 1 % (−0.418 to −0.422). So the tilt conflict comes either from a lens shift or from scene objects that are not truly vertical or perpendicular. Either way it has no effect on the answer.

### Abandoned route
`track_mine.py` tried to measure the vertical diameter from a half-maximum blueness profile. It was too noisy because of the ball's marbled texture (±5 px), so I did not use it. The centres it found agree with the scene's circle-fit centres to within about 3 px.

## Rechecks
- **a. Closure:** with f from the frame-12 pinhole and the cos θ correction (about 3614), the late clean frames 28–37 re-derive the diameter at about 0.208 m (−1 %). Over all frames 6–37 it comes back at 0.211 (+0.5 %). Even the crude f = 3670 gives −2.6 %, within 5 %.
- **b. Plausibility:**
  - A speed of 3.6 m/s is a typical bowling-ball speed, and a deceleration of 0.4 m/s² is a mild rolling loss.
  - Pins come out at about 0.33 m (regulation 0.38).
  - The camera height is about 1.2 m.
  - The lane surface is wide in this model (about 1.85 m per round 1). That is scene modelling and does not enter a.
- **c. Units and time base:** the answer is in m/s². Frame 24 is t = 1 s at question_fps 24. The fits stay before the impact.
- **d. Fault proof:**
  - **Diameter-led VP (C3's second route, C5's second route, C7, C9):** a VP at 5300 lies about 25–35 px off the three floor lines, which meet within 5 px at 5648. It gives a = 0.31 in my own code.
  - **C6:** its lane slopes put the VP at y = 242. My sub-pixel lines meet at y = 208.
  - **Submitted 0.339:** this is a fixed-rule blend with the DeepSeek median, which rests on those wrong VPs. It is not a measurement.

## Decision
Round 1's proposed switch to 0.41 is verified: I reproduced its VP and my value is within 2 %. I answer **0.415**, the centre of my f routes (0.412–0.419). Confidence is high.
