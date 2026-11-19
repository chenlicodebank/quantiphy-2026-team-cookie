# q1182: speed of the walking person at t = 1.0 s (m/s)

The file and the question both run at 33 fps, so t = 1.0 s is frame 33. The video is a 3D Blender scene with a static camera.
The prior is a bicycle wheel diameter of 0.65 m. depth_info gives bike depths of 12.62 m and 13.21 m and walker depths of 14.77 m and 15.18 m, at t = 1 s and 2 s.

## Focal length from the bicycle wheel (wheel2.py, solve.py)
- I fitted circles to the outer tire edge of both wheels in each frame, using a median background and the dark ring at its outer edge.
- **Front wheel diameter:** about 99.7 px at f33 and 94.8 px at f66, from a 1/D-linear trend over the unoccluded frames f35-71. The rear wheel comes out 1-2 px larger and is noisier.
- **Focal length:** f = D·z/0.65, where z is the depth along the optical axis, z = d/|ray|, and the principal point is the image centre. This gives 1897 px at t = 1 and 1883 px at t = 2 from the front wheel, and about 1920 px if the rear wheel is included. I used f ≈ 1900-1940 px.
- **Check:** the bike's z-ratio predicted from its two depths is 1.044. The measured wheel-size ratio is 1.051, so they agree. The bike hub's rise in the image also matches its recession.

## Walker
- **Pixel track:** the walker moves right to left at a steady 5.07-5.15 px/frame (linear fits over f18-48, f13-53 and f34-66). He is hidden behind the cyclist over f13-33, where the head x is used. Fitted u33 = 1510 and u66 = 1342, with the pelvis at v ≈ 430.
- **Route B (positions from the given depths):** I back-projected P(t=1) and P(t=2) and took |P2 − P1| over 1 s, at constant pixel speed.
  - f = 1900: 1.311 m/s
  - f = 1940: 1.290 m/s
  - The displacement is about (−1.10 lateral, +0.68 in depth).
- **Route A (image only):** I took the lateral speed as pixel velocity × z/f, with z from the t = 1 depth, and the recession from the walker's apparent shrink (≤ 0.1 m/s).
  - Result: 1.21-1.26 m/s.
- **Inconsistency:** the given walker depths rise from 14.77 to 15.18 m while he moves toward the image centre. That requires about 0.7 m/s of recession. But his apparent height (246→244 px) and foot row (559→558) show almost none, while the bike's depths match its image exactly. So the walker's origin seems to recede more than the visible body does.
- The two routes differ by about 5%. I answered at the midpoint, about 1.27 m/s, which is within about 3% of each.

## Answer
1.27 m/s. Confidence is moderate, ±5%. The main uncertainty is whether the walker's speed follows the body (≈1.23) or the depth-implied origin motion (≈1.30). Per-frame gait oscillation at f33 cannot be measured because the walker is occluded there.
