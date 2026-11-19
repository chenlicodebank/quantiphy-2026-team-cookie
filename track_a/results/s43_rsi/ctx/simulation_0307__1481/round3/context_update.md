# Round 2 addendum: Q1481 (length of the plane)

## Established (own code: fitf.py, track.py, manual.json, tri.py, world.py, windows.py, closure_boot.py)
- **Scale.** Constant-velocity fit with |V| = 22.16 and both depths:
  - f = 3390 (hull origin) or 3240 (bbox origin).
  - Closure speed 22.22 m/s (+0.3 %) and 22.38 m/s (+1.0 %).
- **Round 1's fault is reproduced.**
  - The central fuselage rear end (RC) and the ventral-fin bottom (VB) lie on the centreline, 4.9–5.1 m aft of both pod tips (LR and RR, which are symmetric: aft 9.45 / 9.37 from the pod front).
  - This holds in every frame window (0–36, 12–48, 24–71, 0–71). Track rms is < 2 px.
  - Model-light check: from frame 2 to frame 71, RC and VB move 1155 px and the right pod tip moves 1099 px.
  - So the 10.6–10.8 answers (pod front to pod tip) miss the fuselage tail.
- **Front.** The pod front top corner (LF) is the frontmost point; the antenna is 1.5 m behind it and the fin tops 5.4 m behind.
  - The automatic LF track slides along the edge (by 9 px at frame 24), so I used 10 hand clicks (frames 2–60, rms 2.0 px).
  - A bootstrap with ±1.5 px click noise gives sd 0.18 m.
- **Length** (LF → RC along the flight direction): 14.43 at hull f, 14.67 at bbox f; the windows give 13.98–14.45. **Answer 14.5 m.**
  - Round 1's 14.8 agrees within 2 %. Its upper variants (15.4) came from C3's LF clicks, which sit 0.9 m further forward, with rms 3.05 px.
- **Other measurements.** The span across the fin tops is 18.2 m. In the level-flight frame, the pod axis is pitched 11.5° nose-up and the fuselage end sits 0.5 m above the pod front.

## Ruled out
- 10.6–10.8 (pod only).
- 17.4–20 (span or silhouette).
- 15.9 (PCA box).

## Open
- The depth of the LF corner (±0.3 m).
- How far the rounded fuselage tail cap extends beyond the RC corner (0.1–0.3 m). The sliding fin-edge point VM gives 15.0 m.
- Whether the reference box is aligned with the flight direction.
