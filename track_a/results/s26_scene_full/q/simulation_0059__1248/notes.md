# q1248: length of the turning yellow car (taxi), simulation_0059

The file is 24 fps and question_fps is also 24. Frame = round(t*24): t=0.58 -> f14, t=1.58 -> f38.
Prior: the white van accelerates at 4 m/s^2. depth_info gives the distance from the camera to the van, taxi,
bike and human at f14 and f38.

## Focal length (from the van prior and its depths): f = 2215 +- 20 px
- Principal point at the image centre (1080, 540).
- Van track: `patch_cx` from scene/tracks/van.csv (sub-pixel side-panel template).
- The van's 3D line comes from its centres at f14 and f38, back-projected with depths 43.812 and 43.003 m.
  The line slopes slightly toward the camera going right: its direction is (0.998, -0.005, -0.066).
- For every frame I intersect the panel ray with that line to get the arc position s(frame). I fit a quadratic
  and pick f so that the acceleration equals 4 m/s^2 (scripts focal2.py and focal3.py).
- Results: f = 2210 for frames 10-50, 2215 for 4-71 and 2225 for 25-71. The residual is under 1 cm.
- The simpler two-point displacement method gives 2263-2336 (focal.py). It depends on the assumed start time.
  The fit gives t0 ≈ -0.7 frames, so the van is already moving at frame 0.

## Taxi pixel length (bumper to bumper, side view before the turn starts)
- The taxi is in side view from f0 to about f20 and starts turning around f25. The front face (headlights and
  grille) is slightly visible.
- The record's x_min/x_max are only the yellow-paint extent. Its x_max misses the pale bumper tip, and the
  cyclist overlaps the front from f12 on. Its "~300 px" length is therefore not reliable. I re-measured:
  - Front bumper tip (difference from the clean background at rows 780-790; pixd.py and rearscan.py):
    899 (f2), 929 (f6), 961 (f10), 977 (f12), 984 (f13). That is a steady 7.7-8 px/frame, so f14 ≈ 992.
  - Rear bumper (read on zoomed montages, montage.py): 688 (f14), 705 (f16), 718 (f18), 734 (f20). That is
    7.7 px/frame, the same speed as the front, so the car is rigid and still going straight. The rear is hidden
    by the green bin at f10-12 and by the pedestrian before that.
  - Pixel length is about 304 px at f8, f10 and f14 (±3 px).
- Height check: body without the roof sign is about 77 px, or 1.33 m. The length/height ratio of 3.7 looks like
  a sedan.

## 3D size
I model the taxi as a box (L × 2.0 m × 1.45 m) centred at its f14 depth point (38.596 m along the ray to
pixel (840, 772)). The box is aligned with the van's cross-street direction, and the camera is pitched down
(horizon y ≈ 700). I project the 8 corners and solve for L so the horizontal extent equals 304 px
(taxilen3.py).
- f14: L = 4.92 m.
- Sensitivity:
  - f ±20 px: ±0.05 m.
  - W from 1.8 to 2.2 m: ∓0.035 m.
  - ±3 px on the ends: ±0.05 m.
  - Origin at ground level instead of the body centre: -0.01 m.
- The naive estimate pixel length × Z / f gives 5.24 m. It is too large because the visible front face adds
  about 20 px to the image extent.

## Second route
I place the taxi on the same cross-street line through its f14 point and measure at other frames (route2.py).
- f10: 303.8 px at 38.69 m gives L = 4.90 m.
- f8: 303.2 px at 38.74 m gives L = 4.88 m.
- f14: L = 4.92 m.
The routes agree within 1%.

## Answer
Length ≈ 4.9 m. Confidence: moderate-high, about ±4%. The error is dominated by the focal length and the
bumper-edge reading.
Side note: the pedestrian's feet (y ≈ 815) do not sit where the ground plane from the cars predicts (about
y 840 at its depth). It may be on a raised sidewalk. This is not used.
