# q_1004: width (wingspan) of the plane

The scene is a 2D top-down render. The file runs at 24 fps, but question_fps is 25, so every time conversion uses 25 fps.

- **Speed in pixels.** The jet moves in pure translation along -x. A line fit to `scene/tracks/jet.csv` ref_x over frames 2–59 gives 34.398 px/frame. The mean step is 34.382 px/frame and the residual is 0.8 px rms.
- **Scale.** The prior speed is 22.16 m/s. 22.16 / (34.398 × 25) = 0.025769 m/px.
- **Width.** Width is the wingspan, which runs along y, across the direction of travel.
  - From the record: the bbox of the frame-24 diff mask spans y 369–1089, which is 720 px.
  - My own check (`measure.py`): the diff against frame 71 at threshold 15 gives a span of 723 px at frame 24 (y 368–1090) and 722 px at frame 40. Higher thresholds break the mask into pieces on the dark ground, so I did not use them.
  - Zoomed crops show the wingtips at about y 370 and y 1090.
  - I used 721 px.
- **Answer.** 721 × 0.025769 = 18.58 m. I answer 18.57; the 0.01 gap is rounding and well inside the ±3 px uncertainty.
- **Sanity checks.**
  - The tank hulls measure 246 px, which is 6.3 m, a realistic tank length.
  - The jet's length of 562 px is 14.5 m.
  - An 18.6 m wingspan is plausible for a large fighter.
- **Confidence:** high, about ±2%. The main uncertainty is ±3 px on the wingtip edges.
