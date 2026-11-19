2D scene, one m/px scale from the prior: the brown (chestnut, left) horse moves 77.1 px/s (linear fit over frames 0-48, three reference points agree), so scale = 0.874/77.1 = 0.011336 m/px; this scale also gives realistic horse withers heights (1.37/1.60 m), whereas the other horse's scale would make them 0.74/0.87 m. Rabbit horizontal (nose-to-tail) extent measured sub-pixel on every frame: mean 45.3 px (median 44.7, hop-cycle range 42-52). Length = 45.5 px x 0.011336 = 0.516 m; SAM mask at f10 (45 px bbox) confirms the extent.

Final message:
**Answer: 0.516 m** (rabbit length).

Method summary:
- **Scale (2D, one m/px):** the prior's "brown horse" is the chestnut horse on the left (the right one is a dark bay with black points). Its pixel speed, fitted over frames 0–48 with three independent reference points, is 77.1 px/s → scale = 0.874 / 77.1 = **0.011336 m/px**.
- **Scale check:** this scale gives withers heights of 1.37 m and 1.60 m for the two horses (realistic); the alternative (right-horse) scale would make them 0.74/0.87 m miniature horses, implausible by >40 %. A silhouette test (left-vs-right normalised IoU 0.81 vs 0.93/0.94 self-similarity) shows the horses are different models, so their size difference is not a depth effect and a single scale applies.
- **Rabbit length:** sub-pixel horizontal (nose-to-tail) extent of the rabbit mask on every frame: mean 45.3 px, median 44.7 (hop-cycle range 42–52 px). Adopted 45.5 px → **0.516 m**, confirmed by the SAM 3 mask at frame 10 (45 px bbox).
