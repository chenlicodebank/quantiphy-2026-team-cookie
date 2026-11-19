# Q704: height of the black cat, including its tail

- The video is 2D: a static camera and a cat walking right at constant speed. The file fps of 24 matches question_fps, so I used 24.
- **Scale from the prior.** I used the cat's body centroid from scene/tracks/cat.csv. It moves from x = 571.74 to 835.26 over 49 frames, which is 5.378 px/frame. A linear fit gives 5.389 px/frame. That makes 129.1 px/s, so the scale is 1.041 / 129.1 = 0.00806 m/px.
- **Height in pixels** (`measure.py`). In each frame I found the topmost pixel of the largest dark (fur) component, which is the tip of the raised tail. The tail is held up through the whole clip, and its tip sits at y ≈ 842–847. The paw bottom (mask y1) is at y ≈ 918–920. Height = 76 px (median 75.5, typical range 73–77).
  - I left out frames 34–38, where the dark lounger legs merge with the dark mask.
  - The scene record's `bbox_h` often misses the thin tail (55 px in frame 0). The crops in frames/cat_*.png show the tail reaching about y 843.
- **Answer:** 76 px × 0.00806 = **0.613 m**.
  - Without the tail (paw to head ≈ 54 px) the height would be 0.44 m.
- **Second check:** frames 0–8 and frames 18–26 each give 75–77 px independently. The speed from the endpoints agrees with the fit to within 0.2%.
- **Confidence:** moderate-high, about ±4%.
