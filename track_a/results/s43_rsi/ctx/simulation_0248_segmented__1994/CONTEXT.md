# Context of question 1994 (organised record; every round adds to it)

## Question
- Text: What is the length of the rabbit in meters?
- Its own prior: speed of the brown horse = 0.874m/s
- Its own depth_info: none
- question_fps: 24
- Video: simulation_0248_segmented.mp4 (segmentation, V2MX)

## The answer currently submitted
0.283 - the Claude line's answer 0.283, unchanged.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 0.283 | 1.000 |
| C2 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 0.533 | 1.883 |
| C3 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 0.516 | 1.823 |

DeepSeek median over its 2 runs: 0.524431.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v1; files in context/round1/)
- Answer: 0.51 (switch, confidence medium, follows C3)
- Where the answers part: which horse the prior's 'brown horse' is: left chestnut (77.4 px/s -> 0.01129 m/px) vs middle grey-brown (142.4 px/s -> 0.00614 m/px); rabbit pixel length (45-46 px) is agreed
- Fault proven: C1 assigned the prior to the middle horse, which makes both horses ~1.2-1.4 m long and ~1.0 m tall (about half real size) although the prior is a realistic horse walking speed; the left-horse reading makes both horses and both speeds realistic
- Closure on the prior: 0.0 pct

# Round addendum — q1994 (rabbit length)

## Established
- 2D side view at 24 fps (file rate = question_fps).
- Pixel measurements are agreed by every candidate and by this round:
  - Left horse (dark red chestnut, hue 7°, sat 0.58): 3.22–3.24 px/frame = 77.4 px/s. Its length is 192 px and height 165 px.
  - Middle horse (grey-brown, hue 16°, sat 0.33): 5.93–5.94 px/frame = 142.4 px/s. Its length is 229 px and height 177.5 px.
  - Rabbit length: binary bbox median 46 px and antialias-coverage median 43.3 px; adopted 45 ± 1.5 px.
- The only crux is which horse is the "brown horse".
  - Left horse: 0.01129 m/px, rabbit about 0.51 m. Both horses come out real size (2.2 and 2.6 m long, about 1.9–2.0 m to the head top) and the middle horse walks at 1.61 m/s.
  - Middle horse: 0.00614 m/px, rabbit about 0.28 m. Both horses come out about half real size (1.2 and 1.4 m long, about 1.0 m tall), even though the prior is a realistic speed.

## Decision this round
Switched from 0.283 (C1) to 0.51 (the C3 reading), on the real-scale plausibility rule.

## Open
Colour naming alone leans slightly toward the middle horse being "brown". If future evidence shows the scene is deliberately scaled down,
C1's 0.283 would be right. No other measurable reference was found to settle this independently.

### Round 2 (harness v2; files in context/round2/)
- Answer: 0.515 (switch, confidence medium, follows C3)
- Where the answers part: which horse is the prior's 'brown horse': left chestnut (77.2 px/s -> 0.01132 m/px) vs middle grey-brown (142.5 px/s -> 0.00614 m/px); rabbit extent 45.5-46 px agreed
- Fault proven: C1 assigned the prior to the middle horse, making both horses ~1.2-1.4 m long and ~1.0-1.1 m tall (~45 pct below real size) under a realistic walking-speed prior; reproduced with own code
- Closure on the prior: 0.0 pct

# Round 2 addendum — q1994 (rabbit length)

## Established (re-measured with own code: measure2.py, feet.py, overlay.py)
- Pixel values reproduce round 1:
  - Left horse: 77.37 px/s (centroid) and 77.02 px/s (torso band).
  - Middle horse: 142.50 and 142.55 px/s.
  - Horse lengths are 192 and 229 px; heights are 165 and 178 px.
  - Rabbit bbox median is 46 px (frame 0: 45). Frames reading 53 px include a touching horse hoof.
- Round 1's fault proof is reproduced. Putting the prior on the middle horse gives 0.00614 m/px, which makes the horses 1.18 and 1.41 m long and 1.0–1.1 m tall (about 45 pct below real size). The left-horse scale, 0.01132 m/px, gives real-size horses.
- My own value is 45.5 px × 0.01132 = 0.515 m, which agrees with round 1 (0.51) and C3 (0.516).

## Ruled out
- Gait timing as an independent scale. Both horses' hooves stay planted (no foot slip), with stride periods of about 0.9 s (left) and 0.71 s (middle). Dynamic similarity favours opposite readings for the two horses, because the playback rate is matched to each horse's speed. It is not decisive.

## Decision this round
Switch confirmed: 0.515 (follows C3). Confidence is medium.

## Open
The colour word "brown" by itself fits the middle horse slightly better. If the scene is a deliberately scaled-down one, 0.283 would be right. No in-clip absolute reference exists to settle this.
