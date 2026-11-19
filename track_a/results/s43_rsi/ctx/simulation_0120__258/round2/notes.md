# Q258: length of the TV (m). Prior: the robot cleaner moves at 1 m/s. No depth_info. question_fps 24 (the file runs at 24.0078 fps; I used 24)

## Task
Round 1 proposed switching from the submitted 1.47 (a blend of 1.57 and 1.26) to C1's 1.57.
My job was to verify the fault it claimed (the wall plane at x = 296 versus x = 219) with my own code.

## Crux
The horizontal distance X of the TV's wall plane from the camera nadir. Since L = (Δv/u) × X_face, this is the whole answer.
- The DeepSeek runs (C2, C4, C5) took the floor edge of the white plinth's front face (x = 295.6) as the wall.
- C1 and round 1 took the marble wall's junction with the plinth top (x = 219).

## My measurements (frame 0; the camera and scene are static)
- **Principal point / nadir** (m_joints.py): four vertical marble-wall joint lines, each fitted over about 120 columns (rms 0.15–0.18 px), meet at (539.49, 539.46).
  That is exactly the image centre, so the camera is nadir with cx = cy = 539.5.
  The TV's own short edges meet at (535.4, 539.7) (m_tv2.py). That intersection is ill-conditioned along x, so I used the joint-line value.
- **TV trapezoid** (m_tv2.py): I took the dark-panel mask and found sub-pixel threshold edges in columns 154–211. The top and bottom side edges are straight lines (rms 0.11 px).
  Δv/(cx − x) = **1.0457** (sd 0.0007) at cx = 539.5. Round 1 got 1.048 and C1 got 1.045.
  The overlay (frames/ov_tv.png) shows the fits on the panel's edges.
- **Vacuum scale** (m_vacuum.py, my own background mask, frames 0–31 unoccluded):
  - circle-fit centre: 8.4035 px/frame;
  - sub-pixel leading/trailing edge midpoint: 8.3904 px/frame.
  - Mean 8.397 → 201.5 px/m at the tracked top disc (diameter 68.8 px = 0.34 m).
  - Floor scale = 201.5 × (1 − 0.08/5.9) = 198.8 px/m, for a vacuum top about 8 cm high under a camera about 5.9 m up. That correction is ±0.5 % for H between 4 and 8 m.
- **Plinth front face** (m_tv.py, 160 rows): top edge x = 284.77, floor edge x = 295.64 (sd 0.04).
- **Wall junction** (m_junction.py), texture energy per column:
  - The marble texture (|dI/dy| 2–3, sd 7–12) stops abruptly at x = 218.5–219.0.
  - x 220–284 is uniform (|dI/dy| 0.08, sd 2): the plinth top.
  - The wall's vertical joint lines also end at x ≈ 217–219.
- **The plinth top is horizontal** (m_fire.py): the fireplace frame's end edge sits at y = 408.4–408.5 constant from x = 232 to 264.
  On a vertical face it would be a radial line drifting by about 15 px. So x 219–296 is the top plus front of a low plinth, and the wall stands behind it at x = 219.

## Computation
- u_j = 539.5 − 219.0 = 320.5; u_ff = 243.86; u_ft = 254.73.
- X_wall = u_j × (u_ff/u_ft) / s_floor = 320.5 × 0.95733 / 198.8 = **1.544 m**.
- TV thickness: grey top strip from x 145.5 to 151.2 → X_back/X_face = 1.0147. With a possible 0–2 cm mounting gap, k = X_wall/X_face is about 1.015–1.035 (central 1.02).
- **L = 1.0457 × 1.544 / k = 1.56–1.59, central 1.58 m.** (Flush with no thickness at all: 1.61.)
- Under the DeepSeek reading, X = 243.86/201.3 = 1.211 m gives L = 1.0457 × 1.211 = 1.27, which reproduces their 1.21–1.26.

## Rechecks
- a. **Closure:** the two independent vacuum tracking routes agree to 0.16 %. The scale reproduces 1.00 m/s within 0.2 %, so closure is 0.2 %.
- b. **Plausibility:**
  - vacuum top disc 0.34 m;
  - a 16:9 panel gives camera height H ≈ 5.9 m;
  - plinth 0.25 m high;
  - TV from about 0.42 m to 1.31 m above the floor, 0.16 m above the plinth top;
  - L = 1.58 m is a ~71" set;
  - fireplace frame about 1.6 m long at the plinth-top scale (207.6 px/m).
  
  All realistic. Under the 1.21 m reading the TV would float in front of the wall above the plinth's front edge.
- c. **Units and time base:** metres; px/frame × 24 (question_fps).
- d. **Fault proofs:**
  - C2 (1.25), C4 (1.26), C5 (1.21) and the blend component B = 1.26: they used the plinth-front floor edge (295.6, which I measured too) as the wall. The wall meets the horizontal plinth top at x = 219.0, 0.31 m further back. Their geometry, which I reproduced, gives 1.27 instead of 1.58.
  - C3 (1.95): one planar floor scale applied to a vertical plane seen in strong perspective.
  - C6 (0.80): measured the right-wall contour art, not the TV.
  - Submitted 1.47: the blend inherits B's wrong wall plane.

## Decision
I verified round 1's switch. I reproduced its fault, and my value (1.58, range 1.56–1.59) agrees with C1's 1.57 within 1 %.
Answer **1.57** (switch, following C1).
