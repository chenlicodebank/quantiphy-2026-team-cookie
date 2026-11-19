# q 3140: width of the sign on the ground (m)

- Object: the free-standing white "QUIET HOURS" sign board on the ground right of the gate (frame 0, x ~1064-1129, y ~575-684). Width is the horizontal extent across its face.
- Time base: file fps = question_fps = 30, so no re-timing.
- Sign pixel width (crop.py, column intensity profiles over 4 row bands, plus zoom frames/signz.png): the outer dark frame edges are at 1063.5/1127.5 (top band), 1064.5/1128.5, 1065.5/1129.5 and 1065.5/1130.5 (bottom). Width is 64-65 px, so I used **64.5 px**. The scene record says 66 px (bbox 1063-1129), which agrees.
- Prior scale: the average speed of the rider is 4.46 m/s. Pixel average speed (speed.py, mean of per-frame displacements from the scene track, which I checked as consistent): rear wheel 543 px/s (frames 0-80), scooter centre 540, upper-body track 538, and 547-551 over frames 0-73 (fully visible). I used ~543 px/s, giving a scale of 0.00821 m/px.
- Width = 64.5 x 4.46 / 543 = **0.530 m**. Range across reference points and windows: 0.522-0.535 m. Using 66 px would give 0.54 m.
- Second route: different tracked points (wheel, body, bbox) give the same speed within ±1.5%. The edge profiles in different row bands agree within ±1 px.
- Caveats: the convention uses a single planar scale. The sign stands near the fence, slightly behind the rider's path, so its true size may be somewhat larger. The rider also comes out at about 2.5 m tall at this scale, which suggests the prior's scale is generous. The answer follows the annotators' single-scale convention. Confidence: moderate-high under that convention.
