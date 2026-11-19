# q_2527 — width of the table (cm)

Answer: **56 cm** (the table's left-right extent, which is its shorter horizontal side).

## Setup
- Lab video: 24 fps (both file and question_fps), 1280x720, f = 0.5959*1280 = 763 px, principal point (640,360).
- Prior: tennis (yellow) ball diameter = 6.7 cm (exact). depth_info at t=1.6 s (frame 38): yellow 1.19 m, white 0.994 m.

## Depth_info is inconsistent with the image; I used the size prior as the scale
- At frame 38 the yellow ball is 55 px wide (I checked this on raw pixels; there is a white SAM outline around it).
  At 1.19 m that would be an 8.6 cm ball, not 6.7 cm. Size and f give Z = 763*0.067/55 = 0.93 m.
- The yellow ball is lower in the image than the white one (cy 452 vs 445) and has the larger radius, so on a
  level table it must be the nearer ball. The given depths say the opposite (1.19 vs 0.994).
  In my plane model the white ball is at about 1.10 m, which implies a 4.2 cm (ping-pong) ball.
- I therefore took the scale from the exact size prior plus f, not from depth_info. Note that the left-right width
  barely depends on f: it is essentially a ratio of pixel sizes at the same depth.

## Method (recon.py, edges.py, edges2.py, balldiam.py)
1. Fitted the table-top edges on frames 44-48 (the yellow ball has left the table):
   - far edge: y = 0.00985x + 421.5
   - near (top-surface/front-face) edge: y = 0.0248x + 471.1, from the brightness step
   - left and right sides: from the saturation boundary
   Corners: FL (573.5, 427.2), FR (848.7, 429.9), NL (465.1, 482.6), NR (955.4, 494.8).
   The composite mask is blocky, so the sides are uncertain by about ±2-3 px.
2. Level-plane model: the horizon passes through the side-edge vanishing point (720.6, 351.9), with a small roll.
   Camera height above the table, h = 0.155 m, comes from the yellow ball centres in frames 0-41
   (Z = f*6.7cm/diam, centre is r = 3.35 cm above the top). Rest frames give 0.121 m for the centre plane and
   rolling frames give 0.124 m, so they agree. I then back-projected the corners onto the plane.
3. Results for horizon slopes from -0.01 to +0.005:
   - far edge 0.553-0.561 m, near edge 0.552-0.561 m (the two match, consistent with a rectangle)
   - sides (front-to-back) 0.66-0.70 m, i.e. the longer side
   So by the named-size rule, width = shorter horizontal extent = left-right ≈ 0.556 m. Reading it as the
   horizontal extent across the visible front gives the same value.

## Second-route checks
- Far edge vs ball at rest. The ball's bottom touches the far-edge line in the image, so both are at about the
  same depth. Far edge 275 px * 6.7 cm / 33 px = 55.8 cm (55.0 cm if the diameter is 33.5 px).
- Near edge vs ball at frame 41 (at the front edge, 56.5-57 px). Near edge 490 px; correcting for the ball's
  contact point being 2 px behind the edge line gives about 57.0 cm.
- Range 55-58 cm. Answer: 56 cm.
- For reference, depth_info-based method-card values would be 64 cm (white depth) or 76 cm (yellow depth). I
  rejected them because both depths contradict the exact ball size and the image geometry.

## Confidence
Moderate-high for 55-58 cm. The main residual uncertainties are the ball's pixel diameter (±0.5 px, about 1.5%)
and the blocky composite table outline.
