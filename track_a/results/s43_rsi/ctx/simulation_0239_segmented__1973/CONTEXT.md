# Context of question 1973 (organised record; every round adds to it)

## Question
- Text: What is the width of the house in meters?
- Its own prior: speed of the brown horse = 0.874m/s
- Its own depth_info: none
- question_fps: 24
- Video: simulation_0239_segmented.mp4 (segmentation, V2MX)

## The answer currently submitted
8.93832 - a fixed-rule blend exp(0.7 ln A + 0.3 ln B) of the Claude line's answer A = 8.2 and an earlier DeepSeek median B = 10.93; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 8.2 | 0.917 |
| C2 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 10.96 | 1.226 |
| C3 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 10.9 | 1.219 |

DeepSeek median over its 2 runs: 10.93.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v3; files in context/round1/)
- Answer: 8.1 (switch, confidence medium, follows C1)
- Where the answers part: which pixel extent is the house width: eave-level y extent of the top-down roof (619.6 px, shorter side) vs the full horizontal image extent 800 px (ridge-level cross-gable ends, longer side)
- Fault proven: C2/C3 (30 pct of the blend) used the 800 px ridge-level x extent, which perspective inflates 1.15x over the eave-level 700 px and which is the longer side (length), not the width
- Closure on the prior: 1.2 pct

# Round addendum for q1973 (house width)

## Established (measure.py, bandline.py)
- **Top-down camera.** Ridge and eave rake pairs put the nadir at row 538.3, and the ridge/eave ratio is 1.166. The
  cross-gable tab edge stays at y=380 straight across x 720-1320, with no kink at the main ridge x=1018. That rules out the
  "box corner at eye level" reading of scene/notes.md.
- **Footprint at eave level.** y extent 619.6 px (gable eave corners y 95.6 → 715.2); x extent 700 px (eaves x 661-1361). The
  cross-gable eave corners are flush with the main eaves. Its ridge ends at x 618/1423 are pushed outward by perspective
  (factor 1.144-1.152).
- **Horse pixel speed.** 2.64 px/frame (whole-cycle centroid 2.63-2.66, nose 2.648; frames 0-48, frame 49 is a reset). That gives
  0.013794 m/px at the horse's body. The horse comes out 2.03 m long.
- **Width.** 619.6 × 0.013794 = 8.55 m uncorrected. With the eaves about 1.5 m above the horse body and f ≈ 1600-2600 px
  (from a roof pitch of 33-47°), k = 0.93-0.96, so **W = 7.95-8.19 m, central 8.10**.

## Ruled out
- 10.9 (C2/C3): an 800 px ridge-level extent along the longer side.

## Open
- The exact depth correction (eave height and focal length) cannot be measured; it leaves about ±3%.
- If the reference took "width" to be the x extent, the answer would be 9.0-9.25 m. By convention width is the shorter side, so
  the answer submitted this round is 8.1.

### Round 2 (harness v3; files in context/round2/)
- Answer: 8.05 (switch, confidence medium, follows C1)
- Where the answers part: which pixel extent is the width: eave-level y extent of the top-down roof (618 px, shorter side) vs the 805 px cross-gable ridge-level x extent (longer side)
- Fault proven: C2/C3 used the 805 px x extent measured only at the cross-gable ridge row (eave-level 699 px, inflated ~1.15x by ridge height) along the longer side; the submitted blend carries 30 pct of it
- Closure on the prior: 0.6 pct

# Round 2 addendum for q1973 (house width)

## Verified (my_measure.py: new routes, i.e. a 5-frame median mask with direct eave-corner reads, and horse texture template matching)
- Round 1's proposal is reproduced.
  - The eave-level y extent is 618.0 px from direct corner reads and 618.1 px from the rake fit (round 1 had 619.6).
  - The eave-level x extent is 699 px (x 662-1361).
  - The ridge/eave ratio is 1.168, with the nadir at row 538.4, so the camera is top-down.
  - The cross-gable band is 805 px wide only at its ridge row y=380. At y=270 and y=520 it is flush with the main eaves
    (661/1362).
- Brown horse speed:
  - Template matching over one gait cycle gives 2.657 px/frame. The centroid gives 2.665 and the nose 2.636.
  - Adopted 2.65 px/frame, so the scale is 0.013742 m/px at the horse's body. Closure is within 0.6%.
  - The horse comes out 2.03 m long.
- W = 618 × 0.013742 = 8.49 m uncorrected. Correcting for eave height (single storey, Δh ≈ 1.5 m, pitch 35-45°,
  f ≈ 1700-2430 px) with k = 0.936-0.955 gives **7.95-8.11 m, central 8.05**.

## Ruled out
- 10.9-10.96 (C2/C3): a ridge-level extent along the longer side.
- The blend 8.94 carries 30% weight from that value.

## Open
- The eave height and focal length cannot be measured from the roof-only top-down view. This leaves ±2-3%. If the house
  were two-storey, W would be about 7.0-7.5, but nothing in the clip supports that.
- If the reference took "width" to be the x extent, the answer would be about 9.0-9.2. The convention (width is the shorter side)
  gives 8.05.
