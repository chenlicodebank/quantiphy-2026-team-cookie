# q1391: width of the road the bike crossed through. Answer: 8.6 m

The file rate and question_fps are both 24, so frame = round(t*24).

## Reading the scene
The camera is static and looks at a 4-way intersection. The bike's ground track runs straight toward the vanishing
point of the near road (D1, VP ≈ (2754, 525)). So the bike rides along the main road toward the camera and goes
through the intersection, crossing the **cross street** (D2, VP ≈ (-3400, 540)). That street runs in front of the
corner building, between the building-side kerb (far) and the near-left corner sidewalk (near). The answer is that
street's kerb-to-kerb width, measured along the bike's direction. In the overlay check (frames/overlay.png) the bike's
front-wheel contact sits on the far edge at frame ≈31 and on the near edge at frame ≈69.

## Geometry
* Vanishing points come from code fits of road markings (lines.py, geom.py) and of facade/side-face brick courses
  (facade_vp.py, side_vp.py). Focal length f = sqrt(-(v1-c)·(v2-c)) ≈ 2780-2810 px (HFOV ≈ 38°).
  - Check 1: back-projecting the bike origin with depth_info (28.219 m at t=0, 25.554 m at t=0.5) gives a 0-12
    frame displacement of 2.73-2.76 m. The prior predicts 5.52 x 0.5 = 2.76 m, so this checks out.
  - Check 2: that displacement is parallel to the ground plane (slope 0.3°).
* Ground plane normal comes from the horizon (v1 × v2).
* Road edges, all at road level, measured from intensity profiles (kerbs.py, kerbs2.py, nearwhite.py):
  - Far edge: thin white line at the building-side kerb base, y = 659 at x=420 up to 667 at x=688.
  - Near edge: white edge line along the near-corner kerb, visible past the kerb end at x 682-694, y ≈ 762.
  - Alternative near edge: the top arris of the near-corner kerb (y 736-748), lowered by the kerb height. The kerb
    height is 0.08 m, measured from the visible front kerb face.
* Scale (camera height H) comes from the prior: bike speed 5.52 m/s against the ground-contact track over frames
  0-79. This gives H ≈ 1.13-1.33 m depending on the horizon solution. The width barely depends on that choice.

## Results (width3.py, crosstime.py, sens.py)
| route | width (m) |
|---|---|
| white line to white line, speed scale (4 VP solutions) | 8.57 / 8.79 / 8.61 / 8.59 |
| kerb arris with kerb-height correction, speed scale | 8.66 / 8.92 / 8.72 / 8.69 |
| crossing time (frame 31.3-32.4 to 69.0) x 5.52 m/s | 8.43 / 8.66 / 8.66 / 8.56 |
| scale from depth_info + assumed contact geometry instead of speed | 8.06-8.51 |

The second route (crossing time x speed) does not need the camera height at all and agrees within 2%. The routes
scaled by depth alone come out a bit lower, because they depend on an assumed origin-to-front-wheel offset (0.5 m).
Without the kerb correction the arris route gives 7.8-8.1 m. The road-level white lines confirm that the correction
is right.

## Other reading
If the question meant the bike's own road (the main road it rides along), that is a different number. It was not
measured, because the bike crosses through the cross street.

Confidence: moderate-good. The answer is 8.6 m; the routes spread over about ±0.2 m.
