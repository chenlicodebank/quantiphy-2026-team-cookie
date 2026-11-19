# Context of question 1688 (organised record; every round adds to it)

## Question
- Text: What is the length of the boat in meters?
- Its own prior: height of the person = 1.75m
- Its own depth_info: t=1s, distance_boat_camera = 103.1570 m
t=2s, distance_boat_camera = 106.0906 m
t=1s, distance_human_camera = 114.8319m
t=2s, distance_human_camera = 114.8356 m
- question_fps: 24
- Video: simulation_0026_segmented.mp4 (segmentation, S3MX)

## The answer currently submitted
9.62549 - a fixed-rule blend exp(0.5 ln A + 0.5 ln B) of the Claude line's answer A = 10.9 and an earlier DeepSeek median B = 8.5; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 10.4 | 1.080 |
| C2 | Claude Opus 5.5 (Claude Code agent), 26_59 real-scale re-ask, real-scale re-ask (26_59, --real-scale, user go 2026-10-20) - stage 1 | 10.9 | 1.132 |
| C3 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 8.5 | 0.883 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 7.45 | 0.774 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 9.0 | 0.935 |

DeepSeek median over its 3 runs: 8.5.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v3; files in context/round1/)
- Answer: 10.3 (switch, confidence medium, follows C1)
- Where the answers part: focal length from the person's pixel height (48 vs 52.75 vs 58 px) and the boat heading/stern-offset model in the bow-to-stern back-projection
- Fault proven: both blend legs mis-scaled f: C2 used the walking-frame height (48 px, f 9% low) and C3 the halo-inclusive 58 px (f 10% high) plus an oversized square-corner stern offset; the upright frame-0 person is 52.75 px
- Closure on the prior: 0.0 pct

# Round 1 addendum (q1688, boat length)

## Established (own code: person.py, vert.py, fit.py, fit2.py, overlay.py)
- Person rest height: at frame 0 (upright, legs together) the person is 52.75 px (sub-pixel). Thresholds
  10/20/40 give 57/54/51 px; walking frames give 48–50 px. So f = 3444 px (range 3380–3510).
- Boat heading from the exact depths (frames 24 and 48, origin proxy at the bbox centre): ΔX=-2.92 m, ΔZ=+2.77 m,
  speed 4.02 m/s, heading 43.4° from the image plane. Shifting the origin pixel by ±20 px moves it ±0.3°.
- Bow tip = stem top at x≈195.5 (frame 24). Stern extreme at x≈444.8; the near stern corner crease is at x≈410; the
  rudder and the deck-rail end lie 10–30 px inside the extreme. Aft centreline point = extreme − 8 to 17 px.
- L from the back-projection onto the centreline (route A, frames 24 and 48 agree within 0.1%): 10.30 m at f=3444
  and offset 12 px. The range over offset 8–17 and f 3380–3510 is 10.0–10.55 m.

## Ruled out
- C2's f=3150 (walking-frame height): the standing person would then be 1.91 m.
- C3's f=3806 (halo-inclusive 58 px) and its square-corner stern offset of about 30 px.
- C4's near-broadside yaw of 8–15°: the track heading is 43°.
- Headings fitted to the length trend: they give 34–44° depending on the frame window, so they are ill-conditioned.

## Open
- Whether the boat moves exactly along its own axis (crabbing or turning). Only the length trend argues for a lower
  heading (38°, which gives L ≈ 9.4), and that trend is noise-limited.
- The exact stern plan shape, which moves L by ±2%.

## Decision
Switch to 10.3 m, following the C1 method (C1 = 10.4). Confidence: medium.

### Round 2 (harness v3; files in context/round2/)
- Answer: 10.25 (switch, confidence medium, follows C1 (round-1 proposal 10.3, verified))
- Where the answers part: focal length from the person's pixel height (standing frame-0 53 px vs walking 48 px vs halo-inclusive 58 px) and the aft-centreline offset from the stern silhouette extreme in the bow-to-stern back-projection along the depth-derived track heading
- Fault proven: both blend legs mis-scaled f: C2 used walking-frame height 48 px (f=3150, gives a 1.91 m standing person), C3 used 57-58 px including the 3-px halo/shadow below the feet plus a ~30 px square-transom offset that the rudder position (17 px inside the extreme) rules out
- Closure on the prior: 0.0 pct

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
