Frame 24 (t=1s). Depth constant (rigid neck-ring width 27-33 px, no trend), so scale = 2.2 m / standing pixel height. Standing height measured from the skeleton at the most extended pose (frame 42, same depth) = ~418 px (max bbox 416 px); at t=1 the astronaut is crouched (bbox 383 px). Scale = 0.00526 m/px. Pelvis speed at f24: horizontal 726 px/s (central diff f22-26), vertical ~290 px/s (torso centroid -303 px/s, ballistic hop check ~280) -> 782 px/s. Speed = 782*0.00526 = 4.12 m/s. Independent neck-ring track gives 786 px/s (4.14 m/s).

Final message:
Answered question 1409: **4.12 m/s**.

Method summary:
- **Scale**: from the prior height (2.2 m) and the given depth (18.147 m at t=1). The astronaut's *standing* pixel height was measured from the skeleton at the most extended pose (~418 px, matching the clip's max bbox of 416 px), not the crouched bbox at t=1 (383 px), giving 0.00526 m/px. Depth constancy was verified with the rigid red neck-ring width (27–33 px, no trend).
- **Pixel speed at frame 24**: horizontal 726 px/s (central difference, frames 22–26) plus vertical ~290 px/s from the hop (torso-centroid track and a ballistic check of the takeoff/apex) → 782 px/s.
- **Check**: an independent neck-ring track gives 786 px/s (4.14 m/s), consistent.
