# Context of question 1014 (organised record; every round adds to it)

## Question
- Text: What is the length of the fish in meters?
- Its own prior: speed of the fish = 0.67m/s
- Its own depth_info: none
- question_fps: 24
- Video: simulation_0290.mp4 (simulation, V2SC)

## The answer currently submitted
0.854936 - a fixed-rule blend exp(0.7 ln A + 0.3 ln B) of the Claude line's answer A = 0.775 and an earlier DeepSeek median B = 1.075; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 0.775 | 0.907 |
| C2 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 1.05 | 1.228 |
| C3 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 1.1 | 1.287 |

DeepSeek median over its 2 runs: 1.07471.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v3; files in context/round1/)
- Answer: 0.775 (switch, confidence high, follows C1)
- Where the answers part: pixel length of the fish: C1 ~640-670 px snout-to-tail vs DeepSeek 835-845 px max SAM extent at frames 6-8 (plus pixel speed 566 vs 500-541 px/s)
- Fault proven: DeepSeek's 845 px extent at frames 6-8 starts at the grey wedge of the black shadow ~360 px ahead of the pectoral fins (true snout is 207-215 px ahead in every clear frame, length ~675 px), and its centroid speeds are shadow-contaminated and low (two template tracks give 23.6 px/frame)
- Closure on the prior: 0.1 pct

# Round 1 addendum – Q1014 (fish length; prior: speed 0.67 m/s)

## Established
- **Pixel speed: 23.6 px/frame (566 px/s).** Two independent template tracks agree:
  - the scene record's head patch gives 23.65;
  - my mid-body patch with rotation search (`speed2.py`) gives 23.63, over frames 2-70.
  - Scale: 1.181e-3 m/px.
- **Pixel length: snout to caudal-filament tip, 627-675 px** across frames 8, 14, 38, 44, 50 and 66 (mean 650). The
  fish's snout is always 207-215 px ahead of the pectoral-fin tips.
- **Length: 0.768 m** at the mean extent, 0.794 m at the straight-body maximum. C1's 0.775 is confirmed to within 1%.

## Ruled out
- **DeepSeek's 845 px (C2, C3).** In frames 0-30 the black shadow lies ahead of the fish, and its grey snout wedge sits
  ~360 px ahead of the fins. The SAM extent included it. The true frame-8 length is ~675 px.
- **DeepSeek's 500-541 px/s.** These are silhouette-centroid speeds, biased low.
- Hence the DeepSeek median (1.075) is faulty. The blend 0.855 that uses it is replaced by C1's 0.775 (decision:
  switch).

## Open
- Whether the reference uses a rest-pose (straight) length (~0.79) or a typical swimming-pose length (~0.77). Both are
  within 3% of 0.775.

### Round 2 (harness v3; files in context/round2/)
- Answer: 0.775 (switch, confidence high, follows C1)
- Where the answers part: pixel length of the fish: snout-to-tail ~640-670 px (C1) vs 835-845 px from the grey wedge ahead of the black shadow at frames 6-8 (DeepSeek), plus centroid vs template pixel speed
- Fault proven: DeepSeek's front point at frame 8 sits ~370 px ahead of the head ref point while the fish's snout stays 172-202 px ahead of it in every frame, so the 845 px includes the shadow; its centroid speeds (20.8-22.5 px/frame) are below the 23.6-23.7 px/frame of three independent tracks
- Closure on the prior: 0.3 pct

# Round 2 addendum – Q1014 (fish length; prior: speed 0.67 m/s)

## Verified (round 1's switch to C1's 0.775 stands)
- **The shadow wedge fault is reproduced.**
  - Relative to the record's template ref point on the head, the fish's snout is at −172 to −178 px in frames 34-70
    and its pale head front at −187 to −202 px in frames 10-26.
  - The grey wedge at frame 8 (x ≈ 1703) is ≈ −370 px from ref, and ≈ 360 px ahead of the pectoral fins against
    208-222 px late.
  - It therefore belongs to the black shadow, which lies ≈ 215 px ahead of the fish in early frames. DeepSeek's
    835-845 px length is wrong.
- **Pixel length, own 3x crops:** f46 636, f54 646, f62 ~652 px. The record's late manual values are 624-652; early
  lengths are 651-674 px.
- **Pixel speed:** the record's template track gives 23.65 px/frame, my snout readings over frames 46-62 give 23.6,
  and the record's manual tail tips give 23.7. Scale = 1.181e-3 m/px.
- **Length:** 0.76 m from the late frames, 0.78 m from the early ones. C1's 0.775 is within ≈1.5%. Decision:
  switch to 0.775 (high confidence).

## Open
- Rest-pose against swimming-pose bounding-box length: 0.76-0.79 m. This is under 3% either way and does not
  matter for scoring.
