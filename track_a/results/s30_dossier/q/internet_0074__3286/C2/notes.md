Frame round(2.00*30)=60 (question_fps). Scale from the 6.1 m court width measured on frame 60 (sidelines x=340..1251 -> 911 px, 0.006696 m/px), confirmed by the court length (2012 px/13.41 m, 0.5% agreement). Ball centroid (1046,791) px; nearest (far) player's body centre ~(1000,565) px from the SAM mask (paddle removed), giving 230 px = 1.53 m. Body-centre variants (mask centroid, torso centroid, bbox centre) span 1.49-1.59 m; a pelvis reading gives 1.21 m.

Final message:
Answered: **1.53 m**.

Method summary:
- **Time base**: question_fps = 30 → frame 60 (file t = 2.50 s), per the benchmark rule.
- **Scale**: measured the 6.1 m court width on frame 60 (sidelines at x = 340 and 1251 → 911 px → 0.006696 m/px), cross-checked with the 13.41 m court length (2012 px → 0.006665 m/px); 0.5 % agreement.
- **Positions**: ball centroid (1046, 791) px from a colour threshold; nearest (far) player's body centre ≈ (1000, 565) px from a SAM 3 mask with the paddle removed.
- **Distance**: 230 px × 0.00668 m/px ≈ 1.53 m; body-centre variants span 1.49–1.59 m, with the main uncertainty being the player reference-point convention (pelvis reading would give ~1.21 m).
