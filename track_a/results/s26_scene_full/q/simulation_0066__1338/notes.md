# q1338 — bicycle wheel diameter (simulation_0066, 3D render, static camera, 2160x1080, 24 fps = question_fps)

Answer: **D ≈ 0.595 m** (outer tyre diameter of the front wheel).

## Focal length (from scene geometry; principal point at the image centre is confirmed)
- Vertical vanishing point from 5 consistent poles (lamp posts and traffic-light poles, sub-px line fits on bg.png;
  `poles.py`, `poles2.py`): ≈ (1075, 2090). Two poles were left out because the trace slipped off them (tlR) or they lean (tlL).
- Road-A vanishing point from two long curb edges (`roads.py`): (621.1, 77.6). Road-B VP from two near curbs: (3184, 56).
- f from A+vertical = 845; A+B = 861; B+vertical = 872. The orthocentre of the three VPs is (1062, 534), close to the image
  centre, so the camera is a standard pinhole with square pixels (solving fx, fy separately gives 858 / 847).
  **f ≈ 855 px** (HFOV ≈ 103°).
- Cross-check with the prior (white van, a = 4 m/s², `vanfit.py`): fitting the van's start from rest along its 3D line
  gives a = 4.1–4.4 at f = 850 (bottom point / centroid used as its reference). That route is weak (a changes slowly with f) but agrees.

## Depth chain (bike given at f14 = 19.065 m, f38 = 14.6515 m)
- Up vector comes from the horizon through vA and vB. Wheel hubs move on a horizontal plane. The front hub track
  f46–f70 (ellipse centres) is straight with constant speed (rms 0.0008 in plane units, heading constant to ±1°, ~5.5 m/s).
- The hub plane's depth below the camera (hh) comes from extrapolating that track back to f14 and f38, with the bike
  origin taken 0.55 m behind the front hub (half wheelbase) at hub height or at ground height (`hhcheck.py`, `final.py`):
  hh = 6.74 m (all variants 6.70–6.80). Reading the hubs by hand at f38/f14 instead (`geom2.py`) gives 6.79 / 6.72, which agrees.
- An earlier route used the box centre as a proxy for the origin (`geom.py`). It gave hub distances ~3% larger, but the
  box-centre point drifts vertically by 0.18 m between f14 and f38, so it was not used.

## Wheel measurement
- The front tyre's outer edge was fitted as an ellipse in code (`wheels2.py`, `seeds_c.json`; overlays in frames/ov_*.png),
  using rays out from the hub and the outermost tyre pixel at the half-threshold crossing. The angular sector covered
  by the fender and frame was left out. Good fits at f46, 48 and 56–70: the major axis grows from 42.8 to 70.6 px.
- Model: a circle of radius R in a vertical plane along the measured heading, centred at the hub on the hub plane, with
  full perspective projection (off-axis stretch reaches 34° at f70). R is solved so the projected major axis equals the
  observed one. The model's major-axis angle matches the observed angle within 0–5°.
- Per-frame D at f = 855: 0.628, 0.591, 0.600, 0.585, 0.577, 0.585, 0.574, 0.602, 0.606, 0.579 → **mean 0.593**.
  Allowing a wheel lean that reproduces the observed minor axis (the observed minor axis is ~6–9 px wider than a thin
  vertical circle; tyre width only explains ~2 px) gives a mean of 0.598.
- Sensitivity to focal length (hh re-derived each time): f = 830 → 0.607, 846 → 0.598, 865 → 0.587, 880 → 0.579.

## Second-route checks
- Near-centre frames f46/f48 (off-axis ≤ 12°, nearly independent of heading): D = 0.63 / 0.59 (±2 px fit noise at
  ~43 px). Their mean, 0.61, agrees with the off-axis frames.
- The rear wheel is mostly occluded. At f71 and f68, where it fits cleanly, it gives D ≈ 0.60 / 0.59.

Confidence: about ±5%. The main error sources are the focal length (±2% → ±1.5% in D), the bike-origin assumption
for the depth chain (±1%), and ellipse edge placement (±1–2 px).
