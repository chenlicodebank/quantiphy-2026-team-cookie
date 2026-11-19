# q996: displacement of the dragon from 0.5 s to 1.0 s (m)

The file rate and question_fps are both 24, so the interval is frames 12 to 24. The camera is static (scene record). The dragon flies right to left roughly across the image plane, so I used one m/px scale from the prior (length 0.75 m).

## Where the earlier answers part ways
The step is the **pixel length of the dragon** (the scale):
- C1 used 600 px, the median of bbox_w over frames 0-49.
- C2 used 816 px from its SAM mask at frame 37.

I checked frame 37 on a full-resolution crop. Its 816 px horizontal extent runs from the tail tip (x ≈ 1020) to the tip of the **wing**, which is swept forward and down (x ≈ 205). It does not end at the head. So C2's scale includes the wing, and its answer (0.35) is too small. Their pixel displacements also differ: C1 got 443 px (hip track), C2 got 383 px (silhouette centroid, which is biased by the wing pose and the 24-frame wingbeat).

## My measurements (crops.py, zoom.py; frames/*.png)
Dragon length in px, nose tip to tail tip, read on zoomed frames where the head is visible:

| Frame | Head | Tail tip | Length | Note |
|---|---|---|---|---|
| 9 | (1485, 835) | (2040, 725) | 566 px | |
| 30 | (725, 830) | (1278, 762) | 557 px | |
| 33 | (608, 835) | (1172, 722) | 572 px | tail straight |
| 0 | ~1785 | 2280 | ≈500 px | tail curled |
| 22 | — | — | ≈517 px | tail curled |

- Frame 0 world-AABB analogue: bbox x-extent 1715-2284 = **570 px**. This includes the wing tip just ahead of the head.
- Scale: **L = 570 px**. This matches both the frame-0 bounding-box extent and the straight-tail nose-to-tail chords (557-572 px). It is 1.316e-3 m/px.
- C1's 600 px would give answers about 5 % lower.

Displacement of the body (origin ≈ pelvis/body) from frame 12 to frame 24, read from anatomical landmarks on 3x zooms:

| Landmark | Frame 12 | Frame 24 | Displacement |
|---|---|---|---|
| Hip / top of thigh | (1615, 825) | (1165, 770) | 453 px |
| Hind foot | (1655, 895) | (1195, 835) | 464 px |

- C1's independent hip track gave 443 px.
- The start of the dorsal white stripe gives 504 px, but it is unreliable: the wing covers it in frame 12.
- My own chained template tracker (track2.py) jumped erratically, so I did not use it.
- Adopted: **455 px**.

## Second-route check
Full-wingbeat centroid speeds are 33 px/frame (frames 0-24) and 38 px/frame (frames 12-36). Over the 12 frames in between, that is about 400-460 px of path, which is consistent with 455 px.

## Answer
455 × 0.75 / 570 = **0.60 m**.

I agree with C1's method (body point, not centroid; length without the wing sweep). I differ slightly on the length: 570 px instead of 600 px.

Confidence: moderate. The plausible range is 0.55-0.62, depending on which pose the reference length was taken from.
