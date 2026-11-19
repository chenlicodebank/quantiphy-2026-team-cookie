# q_3098: distance between the ball and the white line (m)

**Setup.** Internet footage, 30 fps (the file's rate and question_fps agree). The camera looks top-down at a court floor. The "white line" is the light-blue/white stripe at x≈1170–1240, running from the maroon line (y≈507) down to the bottom of the frame. The ball rolls left to right and passes over the stripe at frames 13–14. The question gives no time, so I took the start of the clip (frame 0), when the ball is at its starting position.

**Scale.** One factor from the prior: v(0.5 s) = 2.94 m/s.
- Ball centre in frames 15 and 16, from the scene record's blur-model fit (±1–2 px): (1239.8, 512.2) and (1318.7, 509.3).
- Forward difference: 78.95 px/frame = 2368.6 px/s, so the scale is 1.2412e-3 m/px.
- Camera drift is ≤1 px/frame, which is negligible here.

**Distance.**
- Ball centre in frame 0: (77.9, 577.6). The ball is cut by the left edge, so this is good to about ±3 px.
- White stripe centreline at y = 560–600 in frame 0 (measured by `stripe.py`, blue-minus-red mask): x ≈ 1194.5. The stripe is about 47 px wide.
- Horizontal distance from ball centre to stripe centreline: 1116.6 px, which gives **1.386 m**.

**Checks.**
- With the speed smoothed over frames 13–17 (77.9 px/frame), the scale is 1.259e-3 m/px and the distance is 1.406 m. With the backward difference (77.2 px/frame), it is 1.417 m. The answer is 1.39 m.
- Other reading: the gap from the ball's edge to the near edge of the stripe is (1171 − 189) = 982 px, or 1.22 m.
- Sanity check: the ball's 225 px diameter would be 0.28 m at this scale. That is roughly basketball size, a bit large, so the prior speed may be slightly high.

**Confidence.** Moderate. The main uncertainty is which time and which reference points (centre-to-centre or edge-to-edge) the reference answer used.
