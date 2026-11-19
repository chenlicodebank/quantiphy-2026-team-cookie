# Q327: speed of the cup at t = 2.25 s (m/s)

fps = question_fps = 24, so t = 2.25 s is frame 54. The camera is static. The video is 2D: the cup slides along the
counter at constant image y and constant apparent size, while turning about a vertical axis.

**Problem:** at frame 54 the cup has already left the frame (the last pixels are in frame 53). So the speed comes from the
steady motion just before it leaves.

## Scale (prior: cup diameter = 0.087 m)
The cup lies on its side. It is a near-uniform cylinder with rounded ends. In the end-on view (frame 19) the flat end
face is inset from the body silhouette.
- `diam.py` measures the median silhouette width perpendicular to the main axis over the middle 50 % of the length, in
  frames 31-46. The colour mask covers the underside in these frames (overlay checked in `frames/mask_46.png`).
- Result: 126-128 px in each frame, median **127.0 px**.
- The end-on silhouette width at frames 19-20 is 125-126 px, which agrees.
- Scale = 0.087 / 127 = 6.85e-4 m/px.

## Pixel speed
- **Mask centroid** (scene track, checked): steps of about 28.1 px/frame over frames 29-46. The mean is 28.29 over
  frames 29-37 and 28.09 over frames 37-46, a very slight slowdown. Extrapolated to the 53→54 step: about 27.8-27.9.
- **Second route** (`tmatch.py`): template matching on the trailing part of the cup. It gives 27.4-27.8 px/frame for
  frames 46-50, while the cup is partly out of frame. This method reads slightly low (by about 0.8 px earlier) because the
  cup is still turning a little, and that bias shrinks as the turning slows.
- The left bbox edge moves 27.1 px/frame over frames 46-53.
- Vertical motion is negligible.

Adopted: 27.9 px/frame → 27.9 × 24 × 6.85e-4 = **0.459 m/s**.

Confidence: good, about ±3 %. The main uncertainties are the extrapolation past the frame edge (±0.3 px/frame) and the
pixel diameter (±2 px).
