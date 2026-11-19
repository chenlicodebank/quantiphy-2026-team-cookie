# Q1064 – bird flight speed at t = 1.0 s (m/s)

Answer: **11.0 m/s**

Time base: question_fps = 24 (file is 21.75 fps); t = 1.0 s -> frame 24; speed = backward difference frame 23 -> 24.

## Scale (focal length) from the gravity prior
- The nest tips off the branch (rotating) in frames ~13–28, then falls free in frames 29–40 (impact 40/41).
- I re-tracked the nest in frames 24–41 with a darkness mask (max RGB < 25; the nest core is ~0–15 while the tree behind it
  is 40–80); scripts `track_nest2.py` -> `nest_track2.csv`. The scene record's background-difference mask loses the upper part
  of the nest over the dark tree (frames 33–36), so its centroid is noisy (±15 px).
- Quadratic fit of the dark-core centroid y over frames 29–34 (24 fps): a_y = 3184 px/s² (residual sd 0.5 px);
  29–33: 3217, 30–34: 3283. Frames ≥35 are motion-blurred (mask shrinks), which pulls a down (29–35: 2961).
  Adopted a ≈ 3200 px/s².
- Apparent nest size stays about the same (393 px at frame 0, ~382 px ball shape at 30–33, 414 at rest), so Z during the fall
  ≈ Z on the branch. With Z = d/sqrt(1+r²/f²) and f = a·Z/g:
  using the t=0 depth 4.932 m at origin (308,270): f ≈ 1282 px; using t=1 depth 4.895 m at (345,420): f ≈ 1357 px.
  Adopted f ≈ 1320 px (hfov ≈ 72°).
- Check: free fall from rest consistent with the pixel drop (270 -> 1746 px) and fall time (~1 s, start ~frame 16); camera height
  ~3 m with the nest bottom on the ground and the cart (26.3 m) base giving a horizon row ≈ 990 (level camera).

## Bird
- Bird track = mask centroid (scene/tracks/bird.csv; checked it is the flying bird). Local quadratic fit around frame 24
  (windows ±6 … ±17 frames): pixel velocity ≈ 19.0 px/frame in x, small y (wingbeat bob).
- 3D: P = d(t)·unit ray, d linear between the given 35.960 m (t=0) and 34.077 m (t=1): radial speed −1.88 m/s.
- Speed at frame 24: f=1282 -> 11.2–11.5 m/s; f=1357 -> 10.7–11.0 m/s (spread from smoothing window and ±vy).
  Answer 11.0 m/s.

## Second route / sanity
- With a = 2961 (frames 29–35) the answer would be 11.7–12.4; with 3283, ~10.6. Range ≈ 10.6–12.4, central 11.0.
- 11 m/s is a realistic flight speed for a magpie-sized bird. Note: at this scale the bird (and nest, ~1.2 m) are rendered
  oversize (bird ~3 m long at 34 m); the prior is gravity (realistic), so the gravity-based scale is used.
- Confidence: moderate (~±10 %), dominated by the nest pixel acceleration and which nest depth applies during the fall.
