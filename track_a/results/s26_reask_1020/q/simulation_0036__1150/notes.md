# Q1150 – height of the person (simulation_0036)

File fps 24 = question_fps 24. Static camera, 1080x1080, principal point taken at the image centre.

## Scale (focal length) from the boat (prior: length 10 m) + depth_info
- The boat's 3D centre at t=1 s and t=2 s comes from back-projecting the hull centre (linear fit of the track) using the given
  depths 133.9572 / 131.2557 m. The heading is the direction of motion (it moves bow-first, left and toward the camera).
- Model: the bow stem (on the centreline) is the left hull edge, and the near-side stern corner (offset by an effective
  half-beam B/2) is the right hull edge. Both are projected for every frame (0-71) and fitted to the measured red-hull
  edges, with f, the bow offset and B as unknowns (`fit_f.py`).
  - Record edges (`hull_x0/x1`): best fit f = 3130 px, effective B = 0.9 m, rms 0.69 px.
  - My own sub-pixel edges (`edges.py`): f = 3260 px, B = 0.2 m, rms 0.49 px.
  - If B is forced to 3.5 m, f = 2670 px. That fits worse (rms 0.81 px) and does not reproduce the width growth of
    173→195 px (ratio 1.11–1.13, against a depth ratio of only 1.06; the extra growth comes from the view rotating).
    It would also make the person 2.16 m tall, which is implausible. The stern looks rounded (cruiser stern), so its
    rightmost point lies near the centreline, which explains the small effective B.
- Result: f ≈ 3200 px (horizontal FOV about 19°), heading about 42° from the image plane, boat speed about 4.1 m/s (plausible).
  Sanity checks at f = 3200: wheelhouse about 48 px tall → 2.0 m; mast top above the waterline about 9 m. Both are plausible.

## Person
- Head-to-feet pixel height from my own background-difference mask (`pheight.py`): 43 px (count) in frames 0-12,
  41-42 around t=1-2 s, and 40 near the end. After subtracting about 1 px of blur, the early or standing-like extent is about 41.5-42 px.
- Depth of the person's origin is 139.10 m (constant; the walk animation leaves the origin at the start, so the depth fits
  the body best at the start).
- H = 139.1 × 41.5 / f: 1.84 m at f = 3130, 1.77 m at f = 3260. The rest standing height is about 1-2 % more than the walking extent.

## Answer
1.82 m (f ≈ 3200 px). Confidence is moderate: about ±6 %, coming mainly from the boat's beam/stern geometry that sets f,
and from ±1 px on a 41 px person.
