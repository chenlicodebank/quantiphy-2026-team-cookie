# Q856 – speed of the box at t = 1 s (m/s)

Prior: the box's side parallel to the slope is 0.611 m. No depth_info. fps = question_fps = 24, so t = 1 s is frame 24, and
speed = |p24 − p23| × 24.

## Geometry seen in the video
- The camera views the incline from the side. The box shows its camera-facing **side face**, which is light tan and
  ~91 × 50 px, plus a thin dark **top face** strip. A shaded **end face** is visible on the downhill side early on
  (~10 px at frame 15), shrinks to ~0 near frames 26–28, then appears on the uphill side (~20 px at frame 38). This is
  perspective. So the silhouette length along the slope (103–116 px, from scene/ minAreaRect) is NOT the box edge;
  it includes the end face and corner effects.
- I rotated each frame so the slope is horizontal (4× crop, `rot.py`, `rotenh.py`) and measured the side face's
  along-slope edge from averaged column profiles (`sideface.py`):
  - left edge: b* half-contrast against the background;
  - right edge: L* half-drop into the dark end face/shadow.
  Results: 95.1 px at frame 15, smoothly falling to 92.3 (frame 20), 91.3 (23), 91.1 (24), then ~90 at frames 26–30
  (a gentle perspective scale change along the path). The edge-to-edge b* width was 93.4 px at frame 24, and it sits
  ~2 px above the side-face value even where no end face is visible. **Used L_px = 91.6 ± 1 px at frames 23–24.**
  Scale = 0.611 / 91.6 = 0.00667 m/px.
- The box translates rigidly, so every point has the same world speed. The pixel motion and the reference edge are
  both measured on the camera-facing side, at the same location and frames, so the scale applies directly.

## Pixel step 23→24 (`speed.py`)
- Frame timing: frames 10/11 and 27/28 are duplicated (one frame dropped, the next shown twice), but the track is
  back in sync after each glitch, so frame 24 is correct. Frame 27 was excluded from the fits.
- Centroid (scene track, projected on the path): raw step 37.19 px; local quadratic fits over windows 16–32, 18–30,
  19–29 and 20–28 give 36.8–37.1 px.
- Second route, the side face's left edge (re-measured): raw 37.34 px, fits 37.5–37.6 px. That point is ~45 px uphill,
  where the scale is ~0.7 % larger, so it is equivalent to ~37.3 px at the centre.
- Adopted step = 37.15 px/frame.

## Answer
v = 37.15 × 0.611 / 91.6 × 24 = **5.95 m/s**.
Sanity check: the pixel acceleration is ~1.45 px/frame², which is ≈ 5.6 m/s². That is plausible for a box sliding with
friction on a ~44° incline (g·sin44° = 6.8 m/s²).

Confidence: about ±3 %. The main uncertainty is the edge definition of the side-face length (91.1 vs 93.4 px).
