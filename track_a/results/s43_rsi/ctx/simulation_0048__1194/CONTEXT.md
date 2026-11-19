# Context of question 1194 (organised record; every round adds to it)

## Question
- Text: What is the height of the moving bicycle (from the handlebar to the ground, including below the wheel) in meters?
- Its own prior: height of the walking person = 1.8m
- Its own depth_info: t=1s, distance_bike_camera = 16.4919m
t=2s, distance_bike_camera = 11.9277m
t=1s, distance_human_camera = 11.9259m
t=2s, distance_human_camera = 10.8165m
- question_fps: 33
- Video: simulation_0048.mp4 (simulation, S3MC)

## The answer currently submitted
1.49 - the Claude line's answer 1.49, unchanged.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 1.49 | 1.000 |
| C2 | Claude Opus 5.5 (Claude Code agent), 30_x adjudication, 30_3 S3 adjudication (DeepSeek differs 25 pct to 2x) | 0.97 | 0.651 |
| C3 | Claude Opus 5.5 (Claude Code agent), 40_5 fresh per-question run | 1.6 | 1.074 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 0.96 | 0.644 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 0.96 | 0.644 |
| C6 | OpenAI GPT-6 Astra (Codex agent) | 1.06 | 0.711 |

DeepSeek median over its 2 runs: 0.96.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v1; files in context/round1/)
- Answer: 1.0 (switch, confidence medium, follows C2)
- Where the answers part: focal length: f~1185 from the walker's given depth (C1,C3) vs f~1890-1980 from vanishing points / real-scale ground plane (C2,C4-6)
- Fault proven: C1/C3's f~1185 needs a horizon at y~213, but level building cornice/siding lines converge at y~-82 (f~1890-1960); the walker's depth belongs to an origin offset from its body, and with that f the road would lie 2.7 m below the sidewalk
- Closure on the prior: 1.5 pct

# Round addendum: q1194 (bike handlebar-to-ground height)

## Established
- **Horizon.** The level building's horizontal lines (11–16 cornice and siding segments, x 1160–1320, y 0–140, frame 0) meet at VP (1830, −82). The bootstrap range of y is −86 to −81 (`facade_vp.py`).
  - This matches C2's rider scale-growth VP (1777, −93).
- **Vertical VP.** (958, 8040) from 41 edges (earlier sessions: 7936–8620).
- **Focal length.** f = 1887–1958 px; the pitch is 13.5°.
- **f ≈ 1185 is ruled out.** It would put the horizon at y ≈ 213, but the building's level lines above that row rise toward the right.
- **Camera height above the sidewalk.** 4.66 m from the 1.8 m walker (15 keyframes, sd 0.03).
- **The bike's given depth (16.49 m at t = 1 s) agrees with this camera** within about 1.5 % (front contact at 15.7–16.25 m, origin about 0.5 m behind it).
  - The walker's given depth (11.93 m) does not: the body is at about 17.5–18.2 m, so the walker's origin is offset from the body.
- **Bike pixels at f33.** Grip top y ≈ 424, contact y ≈ 559.5 (135.5 px). All sessions agree on this.
- **H at frame 33:**
  - ground route: 0.975–1.01 (r = 0.3);
  - bike-depth route: 0.99–1.03 (r = 0.3);
  - over r = 0–0.4, the whole range is 0.97–1.08.

## Ruled out
- **1.49 (C1) and 1.6 (C3):** both rest on the walker-depth focal length of about 1185.
- **r = 0, grips over the axle (C6, 1.06):** the bike has swept-back city bars, so the grips are behind the front contact. This makes 1.06 a slight overestimate.

## Open
- **The grips' set-back behind the front contact (r).** A free multi-frame fit gives r = 0.62 ± 0.10 and H = 0.90–0.93. That is ill-conditioned (residual model error) and the r is implausible; r = 0.3 gives 1.00. This is the main remaining uncertainty, about ±5 %.
- **Submitted now:** 1.00 m.

### Round 2 (harness v2; files in context/round2/)
- Answer: 1.0 (switch, confidence high, follows C2)
- Where the answers part: focal length / which given depth to trust: f~1185 from the walker's given depth (C1,C3 -> 1.49-1.6) vs f~1870-1980 from vanishing points or the walker's ground plane (C2,C4-6 -> 0.96-1.06)
- Fault proven: C1/C3's f~1185 needs a horizon at y~213, but my own LSD fit of the level facade lines puts it at y=-77 (f=1874, vertical VP y=8023); the walker's given depth belongs to an origin offset from its body (body at 17.4 m, not 11.93), and equal rider/walker head sizes rule out the 16.49 vs 11.93 ratio
- Closure on the prior: 3.0 pct

# Round 2 addendum: q1194 (bike handlebar-to-ground height)

## Verified (independent code: vp.py, geom.py, plaus.py)
- **Round 1's switch to 1.00 is verified.** Round 2 answers 1.00 (switch from 1.49), confidence high.
- **Horizon and focal length.** My own LSD + RANSAC on the facade cornice lines gives a street VP of (1793, −76.5); the bootstrap y range is −80 to −73.
  - The vertical VP is (958, 8023) from 65 segments.
  - So f = 1874 and the pitch is 13.8°.
  - This agrees with round 1 (−82, f 1887–1958). f ≈ 1185 is ruled out.
- **Camera height.** 4.61 m above the sidewalk, from the 1.8 m walker over 86 frames (sd 0.024).
- **Walker-ground route.** It barely depends on f (under 0.3 % between f 1874 and 1950).
  - H at r = 0.3: 0.97–1.02 over frames 0–60, mean 1.00.
  - H at r = 0.4: mean 0.97.
  - H at r = 0: about 1.07.
- **Bike's given depth.** The model puts the bike origin at 15.9–16.0 m against 16.49 m given (3 % at f = 1874, about 0 % at f = 1950). Closure on the walker's 1.8 m through the bike-depth scale is 3 %.
- **New route: head sizes.** At f33 the rider's head is about 20 px wide and the walker's about 17 px, so the two real heads are about the same size.
  - At the given depths (16.49 vs 11.93 m) the rider's head would be about 1.6× the walker's, which is impossible.
  - This confirms that the walker's given depth refers to an origin offset from the body.
- **Plausibility.**
  - The rider's head is 1.65–1.69 m above the road.
  - The bike moves at 4.66 m/s and the walker at 1.24 m/s.

## Ruled out
- **1.49 (C1) and 1.6 (C3):** both rest on the walker-depth focal length.
- **1.06 (C6):** it uses r = 0.

## Open
- **The grip set-back r (0.3–0.45 m)** leaves about ±3 %.
- **The curb height (0–0.15 m)** leaves about ±2 %.
- Overall the answer range is 0.96–1.03.
