# Context of question 1039 (organised record; every round adds to it)

## Question
- Text: When t=3s, what is the minimum distance from the outer end of the pier to the boat in meters?
- Its own prior: height of boat = 0.75m
- Its own depth_info: t=0s, distance_boat_camera = 7.452 m
t=1s, distance_boat_camera = 6.655m
distance_pier_camera = 11.579m
distance_stairs_camera = 17.623m
- question_fps: 24
- Video: simulation_0008.mp4 (simulation, S3MC)

## The answer currently submitted
5.68 - the Claude line's answer 5.68, unchanged.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 5.68 | 1.000 |
| C2 | Claude Opus 5.5 (Claude Code agent), 30_x adjudication, 30_6b S3 adjudication (DeepSeek differs >2x; Codex in the dossier) | 5.68 | 1.000 |
| C3 | Claude Opus 5.5 (Claude Code agent), 40_5 fresh per-question run | 2.75 | 0.484 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 3.82 | 0.673 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 2.8 | 0.493 |
| C6 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 2.9 | 0.511 |
| C7 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r4 | 2.21 | 0.389 |
| C8 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r5 | 3.9 | 0.687 |
| C9 | OpenAI GPT-6 Astra (Codex agent) | 3.34 | 0.588 |

DeepSeek median over its 5 runs: 2.9.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v1; files in context/round1/)
- Answer: 5.68 (keep, confidence low, follows C1)
- Where the answers part: which pier point is the 'outer end': the pier origin at the given 11.579 m (5.68) or a constructed lakeward deck-edge point at Z 8.0-9.65 m (2.2-3.9)
- Fault proven: none in C1's route; edge candidates use a surface point absent from depth_info (geometrically sound, but a different reading, and spread 2.21-3.9 among themselves)
- Closure on the prior: 5 pct

# Round 1 addendum — Q1039

## Established (measure.py, this round)
- Boat geometry is not in dispute: constant-depth pinhole fit gives f = 1001.6 px (994–1008 over origin choices),
  Z_boat = 5.86 m (5.83–5.89); reproduces 7.452/6.655 m exactly; boat length 3.77 m, speed 1.39 m/s at 24 fps.
- t = 3 s = frame 72 (24 fps), 7 frames past clip end; bow_x(72) = 243–252 px by lin/quad fits; boat origin
  u ≈ 570, i.e. directly in front of the pier. Closest approach to the pier origin is at frame 74 (t ≈ 3.08 s).
- Boat origin → pier origin (ray through deck pixel (549, 605–660) at 11.579 m): 5.66–5.70 m → 5.68 m.
- Water-plane check (level camera, height ≈ 1.1–1.3 m): stairs at 17.6 m land at row ≈ 604, matching the stairs
  foot; pier legs' waterline ≈ 675–680 → pier front at Z ≈ 8.3–8.7 m. So the pier origin (11.579 m) is NOT at its
  outer end; it is near the deck centre.

## Ruled out
- Arithmetic/scale errors in C1/C2: none found (independently reproduced).
- Time base: 22.80 vs 24 fps changes the answer < 0.1 m under either reading.

## Open
- Only interpretation remains: origin-to-origin (5.68, kept) vs. front deck edge (≈ 2.7–3.3; C3 2.75 best
  documented; candidate spread 2.21–3.9 comes from front-edge depth 8.0–9.65 m). Decision kept 5.68 per the
  keep-on-tie rule and the origin convention; a future round can only change it with evidence about how the
  reference treated "outer end".

### Round 2 (harness v2; files in context/round2/)
- Answer: 2.23 (new, confidence medium, follows None)
- Where the answers part: which endpoints the 'minimum distance from the outer end of the pier to the boat' runs between: pier origin->boat origin (5.68), pier front edge->boat origin (2.2-3.3), or pier front face->boat far gunwale surface (2.23)
- Fault proven: submitted 5.68 measures pier origin (deck centre, Z~11.5 m) to boat origin, ~2.8 m behind the named outer end (mirror-axis Z 8.68 m) and to the boat centre instead of its nearest surface (half-beam 0.59 m)
- Closure on the prior: -3.3 pct

# Round 2 addendum (Q1039)

## Decision
New answer **2.23 m**: the surface gap between the pier's front beam face and the boat's far gunwale at t = 3 s
(frame 72 at 24 fps). Confidence medium. It replaces 5.68, which is origin to origin.

## Established (scripts in this round's folder)
- Boat (`final.py`): f = 1002.6 px and Z_b = 5.858 m reproduce the given 7.452 and 6.655 m exactly. At frame 72 the
  origin is at u ≈ 573 (X 0.19 m). The boat (X −1.70…2.08) covers the whole pier front (X −0.70…0.84).
- Pier-front water row (`mirror.py`): the mirror axis is **675.5** in all 41 columns.
- Water row at the boat centreline (`waterline.py`, `fit_waterline.py`): **744 ± 2**. This comes from a waterline
  planform fit to the contact profile, which runs from 743 at the ends to 760 mid-ship.
- Horizon: 533–534 is the value that puts the given 11.579 m at the deck centre. The bracket used is 529–537.
- Z_pier_front = **8.68 m** (8.52–8.84). This agrees with C3's 8.54–8.68 and round 1's 8.3–8.7, and rules out C7's 8.00
  and C9's 9.29.
- Boat half-beam (`rails.py`): far rail top at row 663.5, near rail (white rubrail) top at row 692.5. This gives a
  half-beam of **0.586 m** (beam 1.17 m).
- Rail height is 0.39 m above water and the pier front beam spans 0.26–0.41 m, so the closest points are a pure depth
  gap.
- Distances by reading:

  | reading | distance (m) |
  |---|---|
  | surface gap | 2.23 (range 2.09–2.38) |
  | pier front-face centre → boat origin | 2.82 |
  | pier origin → boat origin | 5.68 |

- Closure: post top to water at the centreline is 0.725 m against the prior's 0.75 m bbox height (keel draft
  unseen), −3.3 %.

## Ruled out
- Geometry or scale errors in any route. All readings share f ≈ 1000 and Z_b ≈ 5.86.
- Time-base sensitivity: under 0.05 m.

## Open
- Only the reading is still open, as surface gap vs point to origin. Under the reading choice, the answer is 2.23
  (surface), 2.82 (edge → origin) or 5.68 (origins).
- Possible refinement: the near-rail row. If the interior band at row 686 were taken as the near rail, the half-beam
  would be 0.44 m and the gap 2.37 m. I rejected that band because it stops at the thwart knees.

### Round 3 (harness v3; files in context/round3/)
- Answer: 2.15 (new, confidence medium, follows None)
- Where the answers part: endpoints of the minimum distance: pier origin (deck centre, Z~11.5 m) -> boat origin (5.68) vs pier front face (Z 8.59 m) -> boat far gunwale surface (2.15; round 2's 2.23 verified within 4 pct)
- Fault proven: submitted 5.68 uses the pier origin, which lies at the deck centre ~2.9 m behind the outer end (front beam water row 675.5 in all columns, Z_pf 8.59 m), and measures origin to origin instead of the surface gap
- Closure on the prior: -4.9 pct

# Round 3 addendum (Q1039)

## Decision
New answer **2.15 m**: the surface gap from the pier's front face to the boat's far gunwale at frame 72 (t = 3 s at
24 fps). This verifies round 2's proposed 2.23; the two agree within 4 %. Confidence medium. The fault in 5.68 is
confirmed: it is pier origin (deck centre) to boat origin.

## Established (independent code, this round)
- **Boat.** f = 1002.5 px and Z_b = 5.858 m, reproduced. Origin at frame 72: u 571.6, X 0.18 m. Length 3.79 m, speed
  1.42 m/s.
- **Pier-front water row** = **675.5**. This is the 40-row-span mirror correlation, flat across columns 470–630, so
  the front is square to the camera. It matches round 2 exactly. Short spans scatter between 662 and 690 because they
  lock onto leg detail; do not use them.
- **Centreline water row** from the mirror axes of the stem and stern ends (route new this round):
  - stem 738–740 (frames 50, 63, 65);
  - stern 740–745;
  - round 2's planform fit gave 744.
  - Best value **742 ± 2**.
- **Horizon** ≈ 531 from the deck side-edge corners. Taken as 533 (531–537).
- **Half-beam** 0.586 m, reproduced (far rail at 663.5, near gunwale band at 692.5; the band runs stem to stern).
- **Distances:**
  - Z_pf = 8.59 m.
  - Gap = 2.15 m (range 1.98–2.31).
  - Front-face centre → boat origin = 2.73 m.
  - Origins = 5.68 m.

## Ruled out
- Pier origin at the outer end: that would need a horizon at row ≈ 607, below the boathouse base.
- Pier yaw: the mirror axis is flat across the width.
- Time-base effect: under 0.05 m.

## Open
- Only the reading remains open: surface gap (2.15–2.23) vs front edge → boat origin (≈ 2.7–2.8). The numerical
  spread inside the surface reading is ±0.15 m, mostly from the centreline water row and the horizon.
