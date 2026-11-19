# q1688: length of the boat (m). Round-2 investigation (verifying the round-1 switch to 10.3)

The file runs at 25 fps, but question_fps is 24, so t=1 s is frame 24 and t=2 s is frame 48 (frame indices are used
throughout). The clip is a 3D Blender render with a white background. The boat moves left and away, bow first, in a
3/4 view showing its near side and stern. A small person stands, then walks, to the right of the boat.

## Crux
Two steps separate the answers. (1) The focal length from the person's pixel height: the standing frame 0 versus the
walking frames, and whether the halo is included. (2) The aft-centreline offset from the stern silhouette extreme,
with the heading taken from the track through the given depths.

## Measurements (own code)
- `person.py`, person rest height. Frame 0 is the upright, legs-together pose. Thresholds 10/20/40/80 give
  57/54/51/46 px. The row profile shows the head top at row 527 (darkness 34, pale head core 35–60) and the feet at
  row 580 (75, about 40% coverage). Rows 581–583 hold a faint halo or shadow at 9–14. The sub-pixel extent is
  527.3 → 580.4 = **53.0 px** (52.5–53.5). That gives **f = 53.0 · 114.832 / 1.75 = 3478 px** (range 3445–3511). The
  walking frames read 46–50 px at th20.
- `boat.py`, sub-pixel hull extremes measured on the hull band only (mast excluded). Frame 24: bow (stem top)
  195.37, stern extreme 444.71, length 249.3 px. Frame 48: 110.24 / 347.71, length 237.5 px. These match round 1
  (195.5 / 444.8). Overlay: `frames/ends24.png`.
- `rudder.py`, stern plan cue. At frame 24 the rudder's aft edge is at x≈427–428 (rows 602–620), 17 px inside the
  extreme. The stern rail end is at 434–435. The rudder sits on the centreline, so the aft centreline point lies
  between 428 and 444.8, which puts the offset between 0 and 17 px. A rounded stern with R≈1–1.6 m gives an offset of
  R(1−cos ψ) ≈ 9–15 px. A square transom with the far corner at about 30–35 px is ruled out, because it would put the
  aft centreline point forward of the rudder. I use 12 px (8–17).
- `length.py`, route A. Back-project the origin proxy (hull bbox centre) at frames 24 and 48 using the given depths.
  The track heading is **43.7° from the image plane** at a speed of 4.0 m/s. L is the distance between the points
  where the bow and aft pixel rays meet the centreline.
  - f=3478, off=12: **L = 10.22 (f24) / 10.24 (f48)**.
  - Over off 8–17: 10.40 → 10.02. Over f 3445–3511: ±0.5%. Moving the origin proxy by ±30 px, or using the mask
    centroid instead, changes L by ±1.8%.
- `route2.py`, route B. Use the constant-velocity origin track through the two depth frames, evaluated at frames
  12, 36, 60 and 72. The predicted origin pixel matches the measured hull centre within 0.8 px. L comes out at
  10.20 / 10.22 / 10.28 / 10.24 / 10.28 / 10.32 for frames 12 to 72. The length is constant within 1.2%, so the boat
  is a rigid body moving along its own axis at the track heading, with no visible crabbing.
- A third cue, the wheelhouse faces (side 38 px, aft 37 px), gives ψ≈44° if the wheelhouse is square in plan. This
  agrees with the track heading.

Result: **L = 10.25 m** (range 10.0–10.45).

## Rechecks
- a. Closure: the prior sets f, so the standing frame-0 person comes out at 1.75 m (0%). In the walking frames
  (49 px) the same scale gives 1.62 m.
- b. Plausibility, at f=3478: boat 10.25 m, speed 4.0 m/s (7.8 kn), wheelhouse about 1.56 × 1.59 m in plan, keel to
  mast top about 9.5 m. All are realistic for a small fishing boat.
- c. Units and time base: metres; t=1 and t=2 s are frames 24 and 48 at question_fps 24. The file rate is 25 fps.
- d. Fault proof:
  - C2 (10.9, blend leg A): f=3150 comes from the 48 px walking-frame height. At that f the standing frame-0 person
    would be 53·114.83/3150 = 1.93 m. With my edges and offset, f=3150 gives 10.73 m. Its f is 9% low.
  - C3 (8.5, blend leg B): its 58 px includes the halo or shadow below the feet (rows 581–583, darkness 9–14), so
    f=3806 is 9% high. At f=3806 my geometry gives 9.85 m. The remaining gap to 8.5 comes from its square-box far
    stern corner (offset about 30 px), which the rudder position rules out.
  - C4 (7.45): it used a yaw of 8–15°, but the track heading from the exact depths is 43.7°.
  - C5 (9.0): f=3543 comes from the th20 height (54 px, which includes the halo), and it fitted a length series
    with an unstated stern model. I cannot reproduce its exact step. My geometry at its f gives about 10.1 m.
  - C1 (10.4): within 1.5% of my value, and I find no fault.
  - The submitted 9.63 is the geometric-mean blend of C2 and C3. Both legs carry focal-length faults, in opposite
    directions, and C3 also carries the stern-model fault.

## Decision
I confirm round 1's switch. I reproduced its fault proof and its value: mine is 10.25 m against its proposed 10.3,
within 0.5%. Answer **10.25 m**. Confidence: medium. The remaining uncertainty is the stern plan shape (±2%) and
the origin proxy (±1.8%).
