# q_1994 — length of the rabbit (m)

- The record's "hamster" is the rabbit: the small orange-brown animal near the brown horse's front hooves (seen in frames/f1.png and r1.png).
- 2D side view, so one metres-per-pixel scale comes from the prior (brown horse speed 0.874 m/s). fps = question_fps = 24, so no re-timing.
- Brown horse pixel speed (measure.py): mean per-frame step is torso 5.918, centroid 5.942 and bbox centre 5.939 px/frame; linear-fit slopes are 5.93–5.97. Using 5.93 px/frame × 24 = 142.3 px/s gives a scale of 0.874/142.3 = 0.006141 m/px. The per-frame step swings with the gait (3.6–9.2), so I used the mean, which matches a constant-speed root.
- Rabbit length is the horizontal mask extent. Over frames 0–49 the median is 46 px (mean 46.4, range 42–53 with the hop pose). My own re-segmentation (remeasure.py) gives a median of 45 px at threshold 200, 46 at 235 and 49 at 250. The 250 threshold picks up antialiasing and merges with neighbours.
- Answer: 46 × 0.006141 = 0.2825, reported as **0.283 m**.
- Second-route check: the three horse reference points agree on the speed within 0.5 %, and the two mask thresholds give 45 vs 46 px. Any error mainly comes from the pose-dependent silhouette (±5 %).
- Sanity check: the brown horse would be 229 px × 0.00614 ≈ 1.41 m long, with the rabbit about 1/5 of that. The proportions fit, even though the absolute scale is small for a real horse.
- Confidence: moderate-high (±5–8 %).
