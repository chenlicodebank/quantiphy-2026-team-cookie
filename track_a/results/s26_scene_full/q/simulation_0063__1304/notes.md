# Q1304 — height of the walking pedestrian (m)

Prior: white car (the white van) acceleration = 4 m/s^2. Depths given at t=0.58 s (f14) and t=1.58 s (f38) for the
man, the van, the taxi and the bike. File fps = question fps = 24, so f14 and f38.

## Answer: 1.88 m

## Method
1. **Horizon** (`posts.py`, `postedge.py`). I measured identical lamp posts at different depths (finial top and base
   bottom, sub-pixel 50% edges): R(1985) 399.7/740.2, A(620) 342.6/836.5, P1(162) 459.3/639.1. Each pair gives the
   horizon: 526.5 / 526.0 / 526.1, so v_h = 526.3. The scene record's 532 (from a regression on the man) is ~6 px off.
2. **Van motion** (`wheel.py`, `windows2.py`, `joint2.py`). I tracked:
   - the rear-wheel hub (template match, f23-53 without the man occlusion), and
   - the left edges of the van's two brown side windows (f3-32 and f14-68, without lamp-post and man occlusions).
   The van starts from about rest at frame ~1-2. Joint 3D model: a level camera; the van moves on a straight
   horizontal line with constant acceleration 4 m/s^2; the hub moves in a plane k below the camera
   (v = v_h + f·k/Z); the window edges are fixed horizontal offsets from the hub. For each focal length f, I solved
   by least squares for position, k, heading, start time and offsets. Residuals: hub 0.3 px, windows 0.4 px.
   The van origin is the hub + 0.8·H along the heading − 0.45·H across, toward the far side (typical van
   proportions). I chose f so that |origin(f38)| = 29.8093 m.
   - **f = 2149 px.** The given f14 van depth (29.2444) on its own gives 2157: the two depths are consistent.
   - Sensitivity: offsets ±25% give 2114-2199; frame subsets give 2130-2230; horizon ±1 px gives ±2 px.
   - I used f = 2150.
3. **Man.**
   - Head top: sub-pixel colour edge (`headprof2.py`): f14 570.3, f38 574.0.
   - Ground under him (shoe bottoms on zooms and in code): f14 824 (stance foot; the other foot is in swing),
     f38 ≈ 845 (mean of rear foot 843 and front foot 847-848).
   - Pixel heights: 253.7 and 271.
   - Depth along the optical axis: Z = d / sqrt(1 + r²/f²) at the pelvis pixel. f14 (425,688): Z = 15.911;
     f38 (460,703): Z = 14.854.
   - Height = h·Z/f: f14 → 1.877 m (mid-stance, near full height); f38 → 1.872 m (with the front foot 848: 1.89).

## Checks
- The man's own geometry: camera height above his ground = Z·(feet − v_h)/f gives 2.203 m (f14) and 2.202 m (f38).
  So the given man depths agree with v_h and f.
- Independent route: camera height from the van fit alone is k·(tyre contact − v_h)/(hub − v_h)
  = 1.759 × 180.7/145.3 = 2.19 m. Then the man's height = 2.19 × 253.7/297.7 = 1.865 m (0.7% from the direct route).
- With the record's horizon of 532 the result would be ~2-5% different. The post-based horizon is used.

## Confidence
About ±3% (f ±2%, head/feet ±1.5 px). A walking pose may read slightly below rest height; I took the mid-stance
frame (f14) as the main value.
