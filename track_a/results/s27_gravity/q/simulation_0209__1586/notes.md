# q_1586 – height of the typewriter (m)

The prior is free fall at g = 9.8 m/s² before 0.45 s. The given distances are 4.32 m to the typewriter at t = 0,
4.501 m at t = 0.5 s (frame 12, rocking on the desk) and 4.704 m to the gun. The file rate and question_fps are both 24.

## Camera
- **Tilt and principal point** (`lsd.py`, `vps.py`): I ran a line-segment detector on the desk edges and found three
  vanishing points.
  - The vertical vanishing point is at (1062.7, 11698), so the principal point column is the image centre and roll is 0.
  - Long edges → VP (5861, -77); short edges → VP (-450, -93); the horizon at the centre column is at v ≈ -89.
  - The pitch is θ ≈ 12.9° from the vertical vanishing point and 13.1–14.1° from the horizon. I use 13° (checked at
    13.5° and 14°).
  - The orthogonality of the short-edge and vertical vanishing points gives f ≈ 2658 px, an independent check.
- **Focal length from gravity** (`fit_fall3.py`): I fitted a pinhole model to the bbox centre for frames 2–9 with
  g = 9.8 and |P(0)| = 4.32 m. This gives f = 2520–2625 px (rms 0.3–1.3 px); I use f ≈ 2560 px.
- **Consistency check** (`rest_check.py`): back-projecting frame 12 at 4.501 m puts the typewriter at the same
  horizontal spot as the extrapolated fall path (within 2–3 cm). The implied drop of about 0.96 m gives first contact
  at frame ≈ 10.3, which matches the video (it lands at about frame 10).

## Height
The typewriter is yawed about 20–28° and does not change its yaw during the fall. Its world bounding box height is H.
1. **Route A, in the air** (`height_box.py`, `height_box_sub.py`): I fitted a box (W, H, depth extent) on the
   trajectory to the mask's top, bottom, left and right edges, frame by frame. The view angle changes from about 3° to
   12°, which separates H from the depth extent.
   - Frames 2–6 (little motion blur): H = 0.172–0.175, W ≈ 0.48.
   - Adding frames 7–9 gives H = 0.154–0.164. Motion blur makes the later silhouettes taller, which pushes the fitted
     depth up and H down, so I count these as biased low.
2. **Route B, at rest** (`rest_box2.py`): the box sits on the desk plane (from the gun, or left free) with its centre at
   4.501 m, fitted to the rest bbox (1094–1366 by 524–692). This gives H = 0.176–0.193, depending on the assumed
   footprint and the desk-plane height. The bottom edge may include 2–4 px of contact shadow, so these values may be
   about 0.007 too high.

**Answer: H ≈ 0.177 m** (the routes span 0.16–0.19).

Plausibility: the scale makes the typewriter about 0.37–0.45 m wide and about 0.18 m tall, a realistic portable
typewriter. The revolver comes out about 0.2 m long, so the scene looks real-scale.

Confidence: moderate, about ±8%. The main uncertainties are the box approximation of the typewriter's shape, motion
blur and contact shadow.
