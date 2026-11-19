2D planar internet clip; scale from prior height 1.68 m over the swimmer's crown-to-toe pixel length ~1010 px (SAM3 masks, arm excluded) = 0.001663 m/px, cross-checked by lane-rope float diameter (75 px -> 0.125 m) and lane spacing (1363 px -> 2.27 m). SAM3 full-body track, quadratic fit over frames 0-58 (t=2.33 s at question_fps 25) gives |a| = 23.5 px/s^2; independent Lucas-Kanade flow route gives 20.2 px/s^2; adopted 22 px/s^2 -> 0.037 m/s^2.

Final message:
**Answer: 0.037 m/s²** (question 3049)

Method summary:
- **Scale**: prior height 1.68 m ÷ swimmer's crown-to-toe pixel length (~1010 px, measured on SAM 3 masks with a distance-transform test that excludes the raised arm) = 0.001663 m/px. Verified independently: lane-rope float 75 px → 0.125 m, lane spacing 1363 px → 2.27 m, swim speed ~460 px/s → 0.76 m/s — all realistic.
- **Motion**: SAM 3 full-body track over frames 0–58 (t = 2.33 s at question_fps 25); quadratic fit gives |a| = 23.5 px/s². Second route (Lucas–Kanade flow of the body) gives 20.2 px/s²; adopted 22 px/s².
- **Result**: 22 px/s² × 0.001663 m/px ≈ 0.037 m/s².
