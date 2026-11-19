# q_845: length of the rabbit (m)

Prior: the speed of the horse at the back is 0.874 m/s. The view is top-down (2D), so one m/px scale applies. fps is 24 (the file rate and question_fps agree).

## Which objects
- **Horse at the back:** the dark-brown horse in the top lane. It trails the tan horse by about 360 px in x (its tracks are in `scene/tracks/brown_horse.csv`).
- **Rabbit:** the small orange-brown animal in the bottom lane (`small_brown_animal`).

## Scale
- Brown horse pixel speed over frames 0–48. Frame 49 is an animation-loop reset, so it is excluded.
  - Core (torso) centroid: end-to-end mean of the per-frame steps is 4.44 px/frame; the linear-fit slope is 4.36.
  - Mask centroid: 4.39 px/frame.
  - Bbox: noisy, because the head pose stalls it at frames 46–48.
  - Adopted value: 4.40 px/frame = 105.6 px/s.
- Scale: 0.874 / 105.6 = 0.00828 m/px.

## Rabbit length
I measured it myself (`chroma_rabbit.py`, `measure_rabbit.py`). The x-extent of the chroma mask, which excludes the neutral-grey shadow, was taken over all 50 frames:
- Median 66 px at chroma > 6, 60 at > 10, 58 at > 15, 54 at > 25.
- The scene record's median is 64 px.
- Checked by eye on the zoomed frame 24, the body spans about 57–58 px. A lower threshold picks up the blurred halo and shadow.

Adopted length: 59 px. 59 × 0.00828 = **0.488 m**, rounded to 0.49 m.

## Second-route check
- Using the mask-centroid speed (4.385 px/frame) instead gives 0.490 m.
- The extent across thresholds 10–15 gives 0.48–0.50 m.
- Sanity check with the same scale: brown horse 246 px = 2.04 m and tan horse 295 px = 2.44 m, which are plausible horse lengths.
- The other reading of "at the back" (the tan horse as reference) would make the horses 1.2–1.4 m long. That is implausible, so I rejected it.

## Confidence
Moderate to good, about ±8%. The main uncertainty is where the blurred mask edge lies and the pose variation of the rabbit (58–74 px across frames).
