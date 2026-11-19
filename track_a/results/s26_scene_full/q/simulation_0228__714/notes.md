# Q714: speed of the swimming ring at t = 0.5 s (frame 12, 24 fps)

The prior is "black cat speed = 1.041 m/s". The cat is the black animal walking on the deck (scene/ calls it "dog"). The view is top-down, so I treat the scene as 2D with one m/px scale. fps = question_fps = 24.

Script: `measure.py`, which writes `my_tracks.csv`. It re-measures both objects from the video.
- **Cat:** black-pixel mask (V<45, deck strip y 520–615, area ~1580 px). It walks at constant speed. Linear fit of x: 5.457 px/frame. Net displacement: 5.455 px/frame. The mean of the per-frame steps is 5.479, slightly inflated by gait jitter. I used 5.455 px/frame = 130.9 px/s, giving a scale of **0.00795 m/px**. This matches the scene/ record (5.45–5.48).
- **Ring:** mask R>50 on the water. The centre comes from an ellipse fit to the outer contour; the mask centroid gives the same result.
  - Raw backward step at frame 12: 7.88 px (1.50 m/s).
  - Neighbouring steps (frames 10–14) are 7.63, 8.09, 7.88, 9.47, 9.06, so they jitter by about ±0.7 px.
  - The ring is accelerating smoothly, about 1 px/frame per frame.
  - Local cubic fits of position over ±3…±8 frames give a step of 8.31–8.56 px between frames 11 and 12, i.e. 1.58–1.63 m/s.
- **Answer:** 8.45 px/frame × 24 × 0.00795 = **1.60 m/s**.
- **Second route:** two ring centre definitions (ellipse fit vs mask centroid) and several fit windows all give 1.58–1.63 m/s. The raw single-frame step gives 1.50 m/s.
- **Confidence:** moderate, about ±7%. Uncertainties:
  - the raw step versus the smoothed step;
  - a small depth difference between the cat's pelvis on the deck and the ring on the water, which I ignored.
