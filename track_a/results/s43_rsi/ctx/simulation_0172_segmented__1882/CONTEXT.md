# Context of question 1882 (organised record; every round adds to it)

## Question
- Text: What is the speed of the astronaut at time 0.5s in m/s?
- Its own prior: height of the astronaut = 2.2m
- Its own depth_info: t=1s, distance_astronaut_camera = 18.147m
- question_fps: 24
- Video: simulation_0172_segmented.mp4 (segmentation, S3SX)

## The answer currently submitted
2.6533 - a fixed-rule blend exp(0.5 ln A + 0.5 ln B) of the Claude line's answer A = 3.2 and an earlier DeepSeek median B = 2.2; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 3.2 | 1.206 |
| C2 | Claude Opus 5.5 (Claude Code agent), 30_x adjudication, 30_3 S3 adjudication (DeepSeek differs 25 pct to 2x) | 1.9 | 0.716 |
| C3 | Claude Opus 5.5 (Claude Code agent), 40_5 fresh per-question run | 1.63 | 0.614 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 2.0 | 0.754 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 2.4 | 0.905 |
| C6 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 2.05 | 0.773 |
| C7 | OpenAI GPT-6 Astra (Codex agent) | 1.604 | 0.605 |

DeepSeek median over its 3 runs: 2.05.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v1; files in context/round1/)
- Answer: 1.68 (switch, confidence medium, follows C3)
- Where the answers part: depth (approach) rate dZ/dt of the pelvis at frame 11->12; in-plane component (~1.5 m/s) is agreed by all
- Fault proven: C1 (and the submitted blend) took the depth rate from bbox height, which grows 337->348 px over f9-14 from leg extension; rigid backpack/upper-body vertical scale grows only 0.65-2.0e-3/frame (dZ/dt ~ -0.64 m/s, not -2 to -3); C4/C6 used the clip-mean depth rate dominated by the later hop
- Closure on the prior: 2.0 pct

# Context update for Q1882 (round 1 investigation)

## Established
- t = 0.5 s is frame 12 (24 fps for both the file and the question). The answer is the backward difference 11→12.
- All candidates have nearly the same in-plane component, about 1.5 m/s:
  - Image motion of the pelvis/lower torso 11→12 ≈ (9.9, 3.5) px, from several trackers (range 9.4–10.1, 2.8–4.9).
  - Z12 = 19.0 m. The rigid upper-body and backpack vertical scale from f12 to f24 is 1.047–1.049, applied to Z24 = 18.13 m axial.
  - f ≈ 3200 px, from a 2.2 m height of 380–396 px at f24-scale. Closure is within ±2 %.
- The answers part on the **depth rate at f12**. Measured from rigid parts (ECC affine, scripts ecc_scale.py, chain_scale.py, fit_rate.py):
  - Upper-body vertical scale: 0.65–1.1e-3 per frame.
  - Backpack vertical scale: 1.5–2.0e-3 per frame.
  - Adopted: about 1.4e-3 per frame, so dZ/dt ≈ −0.64 m/s.
  - The ground-path heading (dZ/dX ≈ −0.4 to −0.5 over f4–40) agrees.
- Speed at f12 = **1.68 m/s**. The 10–90 % range over the parameter grid is 1.54–1.89 m/s; with vz = 0 the speed is 1.50.

## Ruled out
- **Depth rate from bbox height (C1, 3.2; the submitted blend 2.65):**
  - The bbox height grows 337→348 px over f9–14 because the legs straighten at the end of the crouch.
  - Reproducing C1 needs a rate of 6e-3 per frame, which gives 3.26 m/s.
  - C1's Z of 20.3 m at f0–9 is also wrong; the rigid scale gives 19.1–19.4 m.
- **Helmet-only scale (about 3e-3 per frame locally):** the helmet grows 3 % relative to the backpack inside f2–14. This is an appearance change; the helmet and upper body agree over f14–30. It drove C5's 2.4.
- **Clip-mean depth rate (C4, C6; 1.2 m/s):** this is dominated by the hop after f15. The image speed doubles abruptly at f14→15.
- **Backpack horizontal scale and det:** these are affected by yaw; sx drops 20 % by f30.

## Open
- The exact local depth rate (0.65–2.0e-3 per frame) is still uncertain and dominates the error, about ±10 %.
- C2's 1.9 is at the upper edge of the bracket; I found no proven fault in it.
- The pelvis reference point could be off by ±1 px per frame in dv, which changes the speed by about 2 %.

### Round 2 (harness v2; files in context/round2/)
- Answer: 1.75 (switch, confidence medium, follows C3)
- Where the answers part: depth (approach) rate dZ/dt of the pelvis at frame 11->12; the in-plane part (~1.5 m/s) is agreed
- Fault proven: C1 (and the submitted blend) took the depth rate from bbox height (~6e-3/frame, legs straightening f9-14); SIFT rigid upper-body scale gives 1.5-2e-3/frame; r=6e-3 in the same geometry reproduces C1's 3.29
- Closure on the prior: 0.6 pct

# Context update for Q1882 (round 2)

## Established (verified independently of round 1)
- **The C1 fault is real.** The depth rate at f12 comes from the rigid upper-body scale, not from bbox height.
  - `sift_scale.py`: SIFT plus RANSAC similarity and affine fits over all frame pairs up to 12 frames apart, solved by least squares for log s. This is a different method from round 1's ECC, C2's LK and C3's template search. The local rate at 11.5:
    - Similarity: 1.4–1.7e-3 per frame.
    - Vertical scale: 1.4–2.3e-3 per frame.
    - Adopted: 1.7e-3, so dZ/dt ≈ −0.79 m/s.
  - The bbox-height rate is about 6.4e-3 because the legs straighten (337→348 px over f9–14). Putting it into the same geometry reproduces C1's 3.29.
- **Scale and depth at f12.** s12 relative to f24 = 0.937–0.946, so Z12 ≈ 19.2 m. Round 1 had 0.954, i.e. 19.0 m. The difference is small.
- **In-plane motion 11→12.** Hip band, SIFT and template routes give du 9.1–10.6 px and dv 3.0–4.0 px. Adopted: (9.9, 3.5) px, the same as before.
- **Focal length and closure.** The maximum normalised height is 394.5 px, which gives f ≈ 3233 px. Closure: 2.21 m against the 2.2 m prior.
- **Speed at f12.** **1.75 m/s.** The 10–90 % range is 1.62–1.91 and the full range 1.54–2.01. Round 1's 1.68 is confirmed within 4 %.

## Ruled out
- **3.2 and the 2.65 blend:** they rest on the bbox-height depth rate.
- **2.0–2.05 (C4, C6):** clip-mean depth rate, dominated by the hop. The scale rate is about 5e-3 per frame over f16–24.

## Open
- The exact local rate lies between 1.4 and 2.2e-3 per frame, about ±8 % on the speed.
- C2 (1.9) sits at the top edge of the range and has no proven fault. C3 and C7 (1.60–1.63) sit at the bottom edge.
