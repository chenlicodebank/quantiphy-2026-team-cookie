# q_2983: canoe displacement in the first 5 s

- The clip runs at 29.97 fps, and the question gives 30 fps. In both cases t = 5 s is frame 150, so the frame rate does not change the result.
- **Scale from the prior (boatman = 1.75 m).** I read the boatman's height from head top to feet on 8x crops (`crop.py`, frames/crop_0.png and crop_150.png):
  - frame 0: 401 to 439/440, about 39 px
  - frame 150: 398 to 437, about 39 px
  - An automated measure from head top to the stern-deck top (`height.py`) gives a median of 36.5 px (range 34–38). It falls short because the deck line sits slightly above the feet in some frames.
  - I used 38.5 px, giving 0.0455 m/px.
- **Displacement from frame 0 to frame 150** (`height.py`, `measure.py`):
  - Stern end: +72 px.
  - Bow tip: +72 px.
  - Quadratic fits over frames 0–160 give 72.4 px at the stern and 70.6 px at the bow.
  - The mask centroid moves +75 px, but it is affected by the person's own motion.
  - Vertical movement is about −4 px (the boat rises slightly).
  - Net displacement: about 72.1 px.
- **Answer:** 72.1 px × 1.75 / 38.5 = 3.28 m.
- **Check:** the scene record (cx 584.5 → about 656) also gives about 72 px. The background is white, so camera motion cannot be checked; I assumed the camera was static.
- **Confidence:** moderate. The main uncertainty is the person's pixel height (36–40 px), which gives roughly ±5%.
