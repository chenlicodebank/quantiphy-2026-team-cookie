# Q793 – length of the front horse (m)

2D side-on clip, 24 fps (file fps = question_fps, so no retiming). Two horses walk +x at the same depth (hooves on the
same ground line), so one m/px scale applies to both.
- Front horse = tan horse (ahead in the walking direction, on the right). Back horse = chestnut/brown horse (prior object).
- Checked on frame 0 (frames/f0.png): tan horse tail-to-nose ≈ x 395-620, brown ≈ 153-339.

Scale from the prior (back horse speed 0.874 m/s), measure.py:
- Linear fit of the brown horse x over frames 0-48 (frame 49 is an animation-loop reset, excluded):
  ref_x 3.238, torso_x0 (rump) 3.229, bbox_x0 3.263, bbox_x1 3.161 px/frame → ~3.23 px/frame = 77.6 px/s.
  Halves agree (3.43 / 3.35 px/frame on the rump marker). A slope is used rather than mean |Δx| because per-frame
  differences of the mask markers are noisy; the rig root moves smoothly.
- Scale = 0.874 / 77.6 = 0.01127 m/px.

Size: tan horse bbox length (nose to tail, along motion) median 228.5 px over 50 frames (mean 227.8, p10-p90 218-237;
manual frame 0: 226 px). Length = 228.5 × 0.01127 ≈ 2.57 m.

Check: brown horse length 183 px → 2.06 m, ratio tan/brown 1.25 consistent with the visibly larger tan horse; 2.57 m is
a plausible horse nose-to-tail length. Confidence: moderate-good (±5%, mainly mask nose/tail extent and gait-speed variation).
