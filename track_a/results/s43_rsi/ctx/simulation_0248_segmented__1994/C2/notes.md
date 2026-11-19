2D scene: the brown (chestnut) left horse's torso track is linear at 77.12 px/s (rms 0.34 px), so the prior 0.874 m/s gives 0.011333 m/px; this makes the horses 2.18 m and 2.61 m long (realistic), whereas assigning the prior to the dark right horse would make them 1.2-1.4 m (rejected). SAM 3 rabbit masks give a median horizontal nose-to-tail extent of 47 px (range 40-54 with hop pose; direct nose-to-rump read on the stretched frame 46 px), so length = 47 x 0.011333 = 0.53 m.

Final message:
**Answer: 0.533 m**

Method summary:
- **Scale (2D, one m/px from the prior):** the "brown horse" is the chestnut left horse; its torso-centroid track is extremely linear at 77.12 px/s (residual rms 0.34 px over frames 0–48), so 0.874 m/s → **0.011333 m/px**. This makes the two horses 2.18 m and 2.61 m long (realistic); assigning the prior to the dark right horse would make them 1.2–1.4 m, which is implausible and rejected.
- **Rabbit length:** SAM 3 masks across frames give a median horizontal nose-to-tail extent of 47 px (40–54 px depending on hop pose; direct nose-to-rump read on the stretched frame ≈46 px). 47 px × 0.011333 = **0.53 m**, consistent with a hare-sized animal and a hop speed of 1.70 m/s.
