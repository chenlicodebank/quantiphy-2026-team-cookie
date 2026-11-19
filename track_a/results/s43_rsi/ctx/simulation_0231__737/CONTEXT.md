# Context of question 737 (organised record; every round adds to it)

## Question
- Text: What is the width of the orange chair next to the blackboard in meters?
- Its own prior: speed of the black cat = 0.714m/s
- Its own depth_info: none
- question_fps: 24
- Video: simulation_0231.mp4 (simulation, V2MC)

## The answer currently submitted
0.455 - the Claude line's answer 0.455, unchanged.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 0.485 | 1.066 |
| C2 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run, width re-run under --size-names (user ok 2026-10-18) | 0.455 | 1.000 |
| C3 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 0.672 | 1.477 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 0.5 | 1.099 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 0.671 | 1.475 |

DeepSeek median over its 3 runs: 0.671.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v1; files in context/round1/)
- Answer: 0.476 (switch, confidence medium, follows C1)
- Where the answers part: depth of the cat (on the teacher's desk) relative to the chair: desk rear flush with the wall (C2, Z_cat=0.985 Z_w) vs desk placed from its front floor contact (C1/me, Z_cat~0.93 Z_w); C3/C5 used the full 199 px extent at the cat's 2D scale
- Fault proven: C2 assumed the desk touches the wall, but the desk's front leg is visible to y>=1022 and the under-desk floor band ends at 1029.5, putting the desk rear edge at ~0.957 Z_w and the cat at 0.929 Z_w (not 0.985); C3/C5 counted the perspective spread of the front legs and ignored the chair being nearer than the cat
- Closure on the prior: 0.0 pct

# Round 1 addendum (q737)

**Established** (scripts and overlays in the round folder):
- The scene has perspective. Horizon at y = 540 (camera level); wall–floor line at y = 951.5.
- The chair faces the camera squarely: the right legs' x-ratio is 1.0505 and the floor-row ratio 1.048.
- Chair backrest left–right extent (half-saturation mask): x 1603.2–1751.8 = 149.4 px.
- Chair floor contacts: front legs at y ≈ 1027; back legs at 1005 ± 2. So Z_back = 0.885 Z_w (backrest 0.889) and
  Z_front = 0.845 Z_w.
- The right-hand extreme of the chair is the backrest edge or the front-right leg; the two agree within 0.1% in world X.
- Cat pixel speed: 8.93 px/frame (fits 8.91–9.00), so s_cat = 0.003332 m/px.
- Teacher's desk:
  - top surface rear edge at y 733.5 and front edge at y 762.5 (the 763–767 band is the top's front face);
  - the top's rear/front ratio of 1.150 matches the corner x-ratio of 1.147;
  - the front leg is visible to y ≥ 1022, and the under-desk floor band ends at 1029.5.

  So the desk is not flush with the wall: the rear edge is at about 0.957 Z_w and the cat (midline y 739.5) at
  0.929 Z_w.
- Width = 0.476 m (sensitivity range 0.468–0.486).
- Plausibility at this scale: camera height 1.48 m, chair seat 0.42 m, chair height 0.85 m, desk height 0.81 m, cat
  torso 0.49 m.

**Ruled out:**
- The full 199 px extent at one 2D scale (0.67 m, C3/C5). It includes the front-to-back perspective spread and
  ignores the depth difference, and a 0.67 m classroom chair is implausible.
- A flush desk (C2, 0.455 / 0.448). It contradicts the desk front-leg visibility and the floor band.

**Open:** the desk front-leg floor contact is hidden behind a foreground chair (bound ≥ 1022, band end 1029.5),
which gives about ±1.5%. The cat midline row gives ±0.7%, and whether the backrest leans back gives up to +2%. An
independent focal-length route (for example a ceiling-tile grid) could check the leg-inset assumption, which is
worth about 1%.

### Round 2 (harness v2; files in context/round2/)
- Answer: 0.478 (switch, confidence high, follows C1)
- Where the answers part: depth of the cat on the teacher's desk relative to the chair: desk rear flush with the wall (C2) vs desk placed from its leg floor contact (C1, round 1)
- Fault proven: C2's flush desk puts any desk leg's floor contact at y<=1013, but the desk front leg is visibly crisp down to y 1026-1027 (occluded there), so the desk stands in front of the wall (rear at 0.944-0.967 Zw); the flush model gives 0.457 with the same edges
- Closure on the prior: 0.0 pct

# Round 2 addendum (q737)

**Verified from round 1, with independent code** (leg_check.py, backleg.py, desk_geom.py, final_calc.py):
- The desk is not flush with the wall.
  - The front-right desk leg (x 752.6–767.2) is crisp (grey 28 against floor 65) down to y 1026–1027, where the
    foreground chair's seat edge covers it.
  - A flush desk would put any leg's floor contact at y ≤ 1013. The fault in C2 is real.
  - C2's model with the same edges gives 0.457.
- Round 1's "under-desk band end 1029.5" is the occluding seat edge, not a desk feature. It is only a lower bound
  on the contact row.

**New:**
- Desk leg depth ratio from the leg centres = 1.140 (round 1: 1.130). The top's ratio is 1.150, so the inset is
  only 0.5%.
- Upper bound on the contact: below the foreground chair back's lower edge (y 977.5), the back-right desk leg
  (x 779–790) does not appear as a crisp bar, only as a soft reflection smear that fades by y ≈ 1005. So the back
  leg's contact is at ≤ 978, which puts the front leg's contact at ≤ 1039.
- The front contact is bounded to [1027, 1039]; I used 1033.
- Backrest 148.8 px (x 1603.1–1751.9).
- Chair back-leg contact 1004 (crisp end of the back-right leg ≈ 1003; the ratio route gives 1004).
- Paw midline at 740.
- W = 0.478 m. It is bounded to 0.4725–0.4842 by the contact range; the other sensitivities are each ±0.5%.

**Plausibility:** camera height 1.49 m, desk height 0.82 m, chair height 0.86 m, cat torso 0.49 m.

**Decision:** switch to 0.478, following C1 and round 1.

**Open:** only the exact desk-leg contact row inside [1027, 1039]. Neither end changes the answer by more than
1.3%. Nothing else is open.
