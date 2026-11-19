# q598: black cat length including the tail (m)

The scene record calls the animal a "black dog". The frames show a black cat with a thin tail, seen from directly
above and walking in +x. It is the only moving object. The record's track covers the right animal.

Time base: fps = question_fps = 24, so no re-timing.

Scale (2D top view, one depth): prior speed = 0.94 m/s.
- Pixel speed: linear fits over frames 0–44 give 10.98 px/frame for the nose, 10.99 for the torso centroid
  (scene record) and 11.24 for the tail-side bbox edge, which is noisier because of the tail swing. I used
  11.0 px/frame = 264 px/s.
- Scale = 0.94 / 264 = 0.00356 m/px.
- I left out frames 45–49 because the head is rendered grey there, which spoils the dark mask in my re-measurement.

Length: the x-extent of the dark mask from nose to tail tip (`measure.py`, frames 0–44).
- With grey < 45: median 192 px, mean 191.2 px.
- With grey < 70: median 193 px, mean 192.2 px.
- The scene record gives a median of 191 px over all frames (range 183–200, depending on tail pose).
- On the frame at t = 1.0 s, the tail tip seen by eye (x ≈ 717) matches the mask edge.
- I used 192 px, so the length is 192 × 0.00356 = 0.684 m.

Second route: dividing the nose-to-tail length by the per-frame advance gives 192 / 11.0 = 17.45 frame-steps of
travel. At 0.94/24 = 0.0392 m per frame, that is 0.684 m. This is the same scale, so it is not an independent
check. Across the gait, the length ranges over 183–200 px, which is 0.65–0.71 m.

Confidence: moderate-high, about ±5%. The main uncertainty is which pose the reference bounding box used.
