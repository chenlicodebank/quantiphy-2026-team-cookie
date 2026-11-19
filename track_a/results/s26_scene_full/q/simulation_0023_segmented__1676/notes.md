# q_1676 — eagle wingspan (m)

File is 25 fps, but question_fps is 24. All time-to-frame conversions use 24 (t=1 s → frame 24, t=2 s → frame 48). The scene/ track frame column is used directly.

## Focal length (focal.py)
- Eagle centroid track from scene/tracks/bird.csv, smoothed with a local linear fit over ±6 frames: frame 24 is at (471.1, 375.7) and frame 48 at (742.7, 373.1). Principal point is (480, 480).
- Back-projection with the given depths (116.05 m and 108.28 m). I solved for the f that makes the 3D displacement over 1 s equal 11.84 m. Chord method: f = 3399 px. Mean per-frame path speed with linear depth: f = 3414–3419 px. **Used f = 3410 px** (HFOV ≈ 16°).

## Wingspan (span.py)
- Mask on each frame: min(RGB) < 200, then the largest component. I measured the bbox width and the max Feret diameter. I left out frames 10–13 (mast overlap) and 63+ (cut by the frame edge).
- Metric size = px × d(frame) / f. d is linear in time through the two given depths.
- Flat, spread-wing frames: f17 46 px → 1.60 m; f34 46 px → 1.52 m; f42 48 px → 1.55 m; f58 53 px → 1.63 m; f60 52 px → 1.60 m; f61 53 px → 1.62 m. Max ≈ 1.62–1.63 m.

## Orientation check (geom.py, flapfit.py)
- Suppose the bird faced its 3D velocity, which is about 47° off the line of sight. Then the projected span factor would fall from 0.70 (f17) to 0.60 (f61). In fact the metric projected span holds steady or grows slightly (1.60 → 1.62). That means the wing axis is not tied to the heading. It stays roughly parallel to the image plane, which also fits the symmetric V-shapes seen in the upstroke.
- A small tilt (≤ ~18°) would explain the slight growth and would add up to about 5%. I tried a rigid flapping-V fit (flapfit.py). It came out degenerate (fitted values at their limits) and was not used.

## Answer
Wingspan ≈ 1.65 m: the measured max projected span is 1.62–1.63 m, plus a small allowance for tilt.
Confidence: moderate. The main risk is the bird's orientation. If the wings were really foreshortened by the heading, the span would be about 2.2–2.4 m, but the stable image span across the clip argues against that.
