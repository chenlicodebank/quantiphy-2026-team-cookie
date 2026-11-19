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
