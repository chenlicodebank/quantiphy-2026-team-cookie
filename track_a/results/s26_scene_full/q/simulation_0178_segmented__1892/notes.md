# Q1892: average speed of the small elephant (m/s)

Prior: the big elephant's speed is 2.313 m/s. This is a 2D side view. Both elephants walk right along the same ground line (y ≈ 694 px), so they are at the same depth and one m/px scale applies to both. I used the file's 24 fps, which matches question_fps.

## Method (measure.py → tracks_mine.csv)
- **Mask:** pixels whose darkest channel is more than 25 below white, cleaned with a 3x3 opening.
- **Splitting the two animals:** at the widest empty column gap.
- **Reference point:** the mask centroid of each animal in every frame (0–59).

Since one scale is shared, the answer is 2.313 × (calf pixel speed / adult pixel speed).

## Pixel speeds (px/frame)
| Reference point | Calf | Adult | Ratio |
|---|---|---|---|
| Centroid, mean per-frame step (2D) | 6.151 | 7.074 | 0.8696 |
| Centroid, linear fit of x | 6.109 | 7.008 | 0.8717 |
| Centroid, net x over 59 frames | 6.124 | 7.056 | 0.868 |
| Bbox centre (affected by trunk and tail swing) | 6.33 / 6.00 | 7.10 / 6.71 | 0.89 |

The scene record's values agree: centroid steps of 6.12 and 7.06.

## Answer
2.313 × 0.869 ≈ 2.01 m/s.

The centroid is the most robust stand-in for the rig origin. The bbox-centre route gives about 2.06 m/s, roughly 2% higher. That gap comes from the swing of the tail and trunk.

Confidence: good, with an expected error of about 3%.
