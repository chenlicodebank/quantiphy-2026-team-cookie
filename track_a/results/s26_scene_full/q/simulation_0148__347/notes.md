# Q347: height of the central pillar of the semicircular arch (prior: train side window width = 1.8 m)

Time base: the file and the question are both 24 fps. The question is static, so the rate does not matter.

## Pixel measurements (scripts: meas.py, win.py, win3.py, enh.py)
- Pillar (the central mullion of the arch, x 1105-1203): it starts at the dark seam under the arch at y≈197
  (meas.py column profile, minimum at 196) and ends at the seam on the lower sill at y≈865 (minimum at 864-866).
  **Height ≈ 667 px.** Its edges are vertical (vert.py).
- Big side window on the near side of the train, glass width at mid-height (threshold runs, win3.py):
  346 (f6), 346 (f8), 350 (f9), 349 (f11), 352 (f12), 352 (f14), 354 (f15), 354 (f17). **≈350 px.**
  The near-layer scale is 1.8/350 = 5.14 mm/px.
- Planar estimate (one scale for everything): 667/350 × 1.8 = **3.43 m**.

## Perspective correction (the pillar is in front of the train: it occludes it)
- The camera is level. Vertical lines (pillar, post, tile grout lines at x 477-1435) have dx/dy ≈ 0, so the
  horizon is at cy ≈ 540.
- The far side of the train is at 0.72 (record value; the end faces suggest 0.735) of the near-side pixel scale,
  so Z_far/Z_near ≈ 1.37-1.39.
- On the far platform, the back-wall base is at y≈764 and the track edge at y≈825 (horiz.py). The near floor in front
  of the arch wall starts at y≈977-1000.
- Route A (both floors at the same level, as in a symmetric station; the platform edge is at the train's far side):
  Z_wall/Z_near = (825-540)·1.389/(y_b-540) = 0.85-0.91. The pillar comes out at 2.9-3.1 m. Under this geometry the
  camera is 2.0 m above the floor, the window sill is 1.0 m above the train floor and the wall is about 0.12·Z_near in
  front of the train. All of these are plausible.
- Route B (the tiles on the near floor and on the far platform are the same size; tiles.py period/(y-cy): far 0.211,
  near 0.19): Z_wall/Z_near ≈ 0.96-1.0, which gives 3.3-3.4 m. This route is weaker: the near-floor pattern looks like
  a different, sparser material, and it would put the wall almost touching the train.
- Answer: **3.1 m**. This favours route A and sits between the routes (3.0 / 3.36 / planar 3.43).

Confidence: moderate. The pillar's depth relative to the train cannot be measured directly (there is no depth_info),
so the range of plausible values is 2.9-3.45 m.
