# Q1321 – width of the white car (white cargo van), metres

The file rate and question_fps are both 24 fps. The van drives straight away from the camera along the road. The camera is static.

## Focal length (geometry, no size assumptions)
- Vertical VP from 7 pole centre-lines (traffic lights, lamp posts; `poles.py`): (1071, 6886). Its x is about cx, so the
  principal point at the image centre is consistent.
- Road VP from the two far-road curbs (`curbs.py`): (804, -200). The scene record had (800, -208).
- Orthogonal VPs: f^2 = -(v1-pp)·(v2-pp), which gives **f ≈ 2167–2179 px**. I used 2173 (HFOV ≈ 53°).
  Sanity check: the pedestrian (154 px tall at about 25.4 m) comes out at ≈ 1.7 m.

## Metric scale from the prior (a = 4 m/s²)
A rigid point moving along road direction D projects onto a line through the road VP, with |p − vp| = C/Z, so
s(t) = A/r(t) + B. I tracked the van's centre high-mounted brake light (rear face, red blob, sub-pixel centroid;
`brake.py`) and fitted s = v0 t + 2 t² (frames 2–40, rms 0.7 cm). Frames 2–71 give the same scale within 0.5%.
Brake-light depth Z(f14) = 18.05 m.
Check against depth_info: the origin (box centre of a ~5.7 m van) is ≈ 2.7 m farther along D and ≈ 1 m lower.
That gives Euclidean ≈ 21.45 m, against the given 21.365 m (0.4%), so the scale and f are consistent.

## Width (`width.py`)
I took points in 3D from the common travel s(t) and the per-point line fits, back-projected them, and projected the
differences onto the horizontal cross-road direction E. Frames 2–44:
- Body width (twice the rear-left corner to the centred brake light; rear face): **1.95 m** (per-frame 1.92–1.97).
- Mirror to mirror: **2.34 m** (per-frame 2.17–2.54, noisier because the mirror depth comes from its own track).

## Answer
The task's naming rule says a car's width runs "wheel to wheel", which reads as the body width, not mirror to mirror.
The body AABB may be slightly wider than the rear corners (wheel arches, side flares). I answered **2.0 m**. That is
within 3% of the body width, and if the reference includes the mirrors it is 15% low.
Confidence: about 2% on the body measurement. The main uncertainty is whether the reference includes the mirrors.
