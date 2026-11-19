# Round 2 addendum (q1688, boat length)

## Verified (own code: person.py, boat.py, rudder.py, length.py, route2.py)
- I confirm round 1's switch: my value is **10.25 m**, against round 1's 10.3 and C1's 10.4.
- Person rest height (frame 0, standing). The sub-pixel extent is 527.3 → 580.4 = 53.0 px, so f = 3478 px (range
  3445–3511). Rows 581–583 under the feet are a halo or shadow (darkness 9–14); thresholds of 10 and 20 include them,
  which gives 57 and 54 px.
- Track heading from the given depths (frames 24 and 48, hull-bbox-centre origin): 43.7°, at 4.0 m/s.
- Along-track check: the constant-velocity track fits the hull-centre pixel within 0.8 px over frames 12–72. Evaluated
  along that track, L = 10.20–10.32 at frames 12, 24, 36, 48, 60 and 72. The length is constant, so the boat moves
  along its own axis at this heading, and the "crabbing" point left open in round 1 is closed.
- Stern cue: the rudder's aft edge is at x≈428 (frame 24), 17 px inside the silhouette extreme at 444.7. The aft
  centreline point must lie between them, so the offset is 0–17 px; rounded-stern models give 9–15 px.
  L(off 8/12/17) = 10.40 / 10.22 / 10.02.

## Ruled out
- A square-transom far-corner offset of 30 px or more (C3). It would put the aft centreline point forward of the
  rudder.
- f=3150 (C2, from the walking height), which makes the standing person 1.93 m.
- f=3806 (C3, which includes the halo).

## Open
- The exact stern plan shape (±2%) and where the origin sits along the hull (±1.8% for ±30 px).
