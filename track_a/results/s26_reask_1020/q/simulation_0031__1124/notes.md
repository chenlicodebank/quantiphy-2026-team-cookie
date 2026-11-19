# Q1124 – height of the boat (m)  → 9.1 m

Time base: question_fps = 24 (file is 25 fps); t=1 → frame 24, t=2 → frame 48 (scene/ frame column used).
Static camera (scene/ record). 3D scene, 960x960, principal point assumed at image centre.

## Camera model (geom.py)
- Camera pitch α vs focal f: the boat origin must stay at one height between t=1 and t=2 (depths 130.35 → 133.74,
  ref pixel (228.8,762.9) → (141.0,722.2)). Exact pinhole solve gives f·tanα ≈ 1345 px for any f.
  Independent check: the eagle, assumed in level flight (139.76 → 130.25 m), gives f·tanα ≈ 1364. Agreement 1.5 %.
- f itself: depth ratios / scale changes are f-independent, so f needs a known size. The prior (person 1.3 m/s)
  cannot fix it: the person's depth_info stays at 139.95/139.98 m while the body clearly walks toward the camera
  (origin does not follow the body), and on flat ground the body's toward-camera component alone already gives
  ~1.3 m/s, so speed is dominated by the unknown beach slope (flat ground: 1.46 m/s at f=6250; ~2° slope reconciles
  it). So the scale is taken from the standard object, the adult person: head-top to lowest foot median 76 px
  (scene track, checked on 6x crops at frames 24 and 48: 74–76 px), body distance ≈139.3 m, β≈13.4°, minus ~0.05 m
  for the forward foot → rest height 1.75 m gives f ≈ 6150 px (HFOV ≈ 8.9°, α ≈ 12.3°).
- Check: eagle max image span 74.6 px at ~136.6 m → 1.65 m image span, ≈1.95 m after the ~0.84 foreshortening of
  its span (it flies mostly toward the camera) – a realistic eagle wingspan.

## Boat height (sanity.py)
- Boat moves ~4 m per second, along its keel (bow upper-left, rounded stern with rudder lower-right).
  Centreline plane = vertical plane through the boat ref point along its motion direction.
- Points on 5–6x crops: mast top (198,433.7) / (109.2,400.3) at frames 24 / 48; lowest point = rudder heel seen
  through the water below the stern (325,912) / (232,866). Rays intersected with the centreline plane.
- Height mast top – rudder bottom: 9.14 m at f=6150 (frames 24 and 48 agree to 1 mm); H ≈ 56150/f.
- Sanity of the reconstruction at this f: draft 1.05 m, stern freeboard 1.1 m, bow 2.0 m above water, hull length
  ≈10.8 m, cabin roof 3.5 m above water, mast 4.6 m above roof; mast top and mast foot reconstruct at the same
  station (vertical mast) – a plausible ~11 m fishing boat.

## Uncertainty
- Person rest height 1.70–1.80 m → 8.9–9.4 m. Keel may be slightly lower than the rudder heel (would add a little).
- Answer: 9.1 m. Confidence moderate (±5–8 %).
