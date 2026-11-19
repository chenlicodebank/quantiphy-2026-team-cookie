# Q839: rabbit speed at t = 1 s (frame 24)

- Time base: file fps and question_fps are both 24, so no re-timing is involved.
- "The horse at the back" is the chestnut horse (horse_red). It trails the group in the direction of motion (+x) and also stands slightly further back (hooves at y≈630, the dun's at 634). I checked this on frame 24 (frames/f24.png).
- Camera is static, and the scene is treated as 2D: one m/px scale taken from the prior (red horse speed = 0.874 m/s).
- Red horse pixel speed: a linear fit of the torso x over frames 0–48 (frame 49 is an animation-loop reset, so I left it out) gives 3.224 px/frame = 77.4 px/s. That makes the scale 0.01129 m/px. The centroid gives 0.01131 m/px and the bbox 0.01148.
- Rabbit: its x step changes with its crouch-and-stretch gait (about 10-frame period, 4–9 px/frame). The prior is one constant speed, so I take the origin to move steadily and use the rabbit's mean rate.
  - Linear fit over all frames: 6.24 px/frame. Average over the gait period around frame 24 (frames 19→29): 6.29–6.33 px/frame.
  - Speed = 6.27 × 24 × 0.01130 ≈ 1.70 m/s. The torso, centroid and bbox routes give 1.69–1.73.
- Second route: the rabbit/red-horse pixel speed ratio (1.94) is the same for the torso, centroid and bbox tracks.
- Caveats: the 1-frame difference at frame 24 depends on the reference point (1.40–2.07 m/s), because body shape changes over the gait cycle. I used the gait-averaged value. The rabbit stands a few px lower (closer to the camera) than the red horse, so the true answer may be a few % lower.
- Answer: 1.70 m/s. Confidence: moderate.
