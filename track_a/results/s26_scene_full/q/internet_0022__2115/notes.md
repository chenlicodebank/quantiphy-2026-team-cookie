# Q2115: average velocity of the man's moving hand, 0.40–1.00 s (cm/s)

Answer: **50 cm/s**

## Time base
The file runs at 16.667 fps and the question at 25 fps, so I used **25 fps**: 0.40 s is frame 10 and 1.00 s is frame 25.
- At 25 fps, the window covers the start of the transport and the peak speed of the hand carrying the folder
  (frames 13–28). That fits a question about the "moving hand".
- At 16.67 fps, the window would be frames 7–17. Over those frames the hand is almost still, adjusting its grip, which
  gives 5–11 cm/s. That reading does not fit the question.
- Plausibility: the folder moves about 57 cm in about 0.76 s, with a peak hand speed of about 1.5 m/s. That is a
  normal brisk reach.

## Scale (one factor, as the annotators did)
- Prior: the mouse is 57 mm wide. `mouse.py` measured its minAreaRect on frames 0, 5, 10 and 34 at three thresholds.
  The width was 101.2–103.1 px, so I used **102.5 px**, giving 0.0556 cm/px.
- Check: the same scale makes the mouse length 198 px = 110 mm and the keyboard 502 px = 279 mm. These match an Apple
  Magic Mouse and Magic Keyboard (57 x 114 mm and 279 mm), so the scale is consistent.

## Hand track
- The moving hand is the man's right hand (on the left of the image). It grips the folder and carries it to the centre.
- `hand_skin.py` builds a YCrCb skin mask in the region x 700–1850, y 950–1700 and takes the centroid of the largest
  blob. I checked the overlays on frames 10, 19 and 25.
- Frame 10: (930.2, 1317.5). Frame 25: (1452.0, 1231.3). Net distance: 528.9 px.
- The camera is static (from the scene record: phase-correlation shift below 0.1 px).

## Results (25 fps, T = 0.6 s)
- Net displacement / time: 528.9 px × 0.0556 / 0.6 = **49.0 cm/s**.
- Mean of the per-frame speeds (path 550.9 px): 51.1 cm/s, or 50.0 cm/s with 3-frame smoothing.
- Robustness: stricter skin masks and stronger morphological opening (`hand_strict.py`) gave 49.4–49.6 cm/s.
- Answer: about 50 cm/s. The two readings (mean velocity vector vs mean speed) differ by only 4%.

## Second route and caveats
- The folder centre from `scene/tracks/folder.csv`, frames 10→25, gives 68 cm/s net. It is higher because the folder
  also swings and rotates about the hand, and it is a different point, so it does not apply to the hand.
- Reading the hand position by eye on zoomed crops gave (920,1305) → (1483,1217), which is about 53 cm/s.
- Confidence: moderate to good if 25 fps is the right time base. At 16.67 fps the answer would be about 5–11 cm/s.
