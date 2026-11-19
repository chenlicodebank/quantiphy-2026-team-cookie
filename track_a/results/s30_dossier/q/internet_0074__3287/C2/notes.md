2D nadir view: court width 6.1 m = 916.5 px at frame 90 (150.4 px/m, cross-checked with the 13.41 m court length, 0.3% agreement). Ball centroid tracked by colour threshold; per-original-frame displacement at frame 90 (t=3.00 s -> frame round(3.00x30)=90) is 18.2-18.9 px, so v = 18.5 px/frame x 30 fps / 150.4 px/m = 3.7 m/s. Second route using the file's own 23.976 fps and per-file-frame displacement gives the same 3.7 m/s.

Final message:
Answered: **3.7 m/s** (question 3287).

Method summary:
- **Scale (2D planar):** measured the pickleball court lines on frames 0 and 90 — width 916.5 px = 6.1 m (150.4 px/m at frame 90), independently confirmed by the 13.41 m court length (150.6 px/m, 0.3% agreement).
- **Ball:** colour-thresholded subpixel centroid; the file has a 4-frame pulldown (dropped frames from a 30 fps source), so each interval was normalised to per-original-frame displacement. Around frame 90 the ball moves 18.2–18.9 px per original frame (decelerating before being hit at frame 94).
- **Velocity:** 18.5 px/frame × 30 fps ÷ 150.4 px/m ≈ 3.7 m/s; the alternative route using the file's own 23.976 fps gives the same value.
- Noted in notes.md the residual ambiguity: if 3.00 s were read as real elapsed time in the 23.976 fps file (frame 72, mid-flight) the value would be ~8.3 m/s; the stated convention (frame = round(t × question_fps)) selects frame 90.
