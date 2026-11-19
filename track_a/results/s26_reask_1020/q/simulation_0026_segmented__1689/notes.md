# q_1689 – average speed of the person (m/s)

Prior: the person is 1.75 m tall. depth_info: the person's distance is 114.8319 m at t=1 and 114.8356 m at t=2, so it barely
changes. The file runs at 25 fps; the question uses 24 fps. Frames are treated as consecutive, so speed = px/frame × 24 × m/px.

## Scale
- I measured the person's height on frame 0, where the head is clearest. Head top (d>10) is at y=526.3 and the sole (d>60) at
  y=580.2, so the height is 54.0 px (`size.py`). The head is very faint later in the clip.
- From shoulder top to sole the person is about 46 px. Taking the shoulder at about 0.84 of stature gives a height of about
  55 px, which agrees.
- I used 54.5 px for the 1.75 m standing height, which gives **0.0321 m/px at the person's depth**. Because m/px = 1.75 / h_px,
  this scale does not depend on the depth.

## Motion in the image (`measure.py`, `size.py`; linear fits over frames 3–74)
- Horizontal: −0.527 px/frame. The centroid, xmin and xmax all agree.
- Vertical: sole +0.142, shoulder +0.154, centroid +0.176 px/frame. For the pelvis I took +0.148 px/frame.
- Combined: 0.547 px/frame → 0.547 × 24 × 0.0321 = **0.42 m/s** across the view.

## Motion in depth
- The given distances change by only 3.7 mm in 1 s, but the body visibly walks. This is the case where the character's
  origin stays put, so I did not use those distances for the body's motion.
- The gait cycle is 36 frames (1.5 s). Silhouettes 36 frames apart match well; those 18 frames apart do not.
- I estimated the change in apparent size by registering frames 36 frames apart in scale and shift, with the faint head
  left out (`scalefit2.py`). The median scale is 0.993, and 0.988–0.994 for lags of 35 and 37 frames. The body shrinks by
  about 0.7% every 1.5 s, which means it is moving away at about 0.54 m/s.
- Other size measures, which are noisier, give between −0.3 and +1.1 m/s: the trend in shoulder-to-sole height gives
  −2% over 71 frames (≈0.8 m/s away); mask area gives ≈+0.35% linear (slightly towards the camera).
- I adopted a depth speed of about 0.55 m/s, uncertain by roughly ±0.3 m/s.
- The feet move down 10 px while the body shrinks. On level ground (horizon about y=466, taken from the boat), moving away
  would move the feet up. So the body must also be moving down by about 0.38 m over the clip, for example walking downhill.
  That vertical motion is already in the 0.42 m/s figure.

## Result
- Speed = sqrt(0.42² + 0.54²) ≈ 0.69 m/s. Swaying and bobbing in the per-frame pelvis motion add a few percent, so the answer
  is **0.70 m/s**.
- Check by gait: a stride period of 1.5 s at 0.69 m/s means a stride of 1.03 m (step 0.52 m). That is a normal slow walk for
  a 1.75 m adult. The in-plane-only reading (0.42 m/s) would need 0.32 m steps.
- Confidence is moderate. The depth component is the main uncertainty: the answer could be anywhere from about 0.45 to
  0.95 m/s. 0.70 is below the 0.9 m/s guideline for walking, but the slow cadence supports a slow walk, so I kept the
  measured value.
