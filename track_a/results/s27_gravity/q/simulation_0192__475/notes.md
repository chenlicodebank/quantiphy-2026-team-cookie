# q_475 — width of the box (simulation_0192)

The prior is that the box accelerates at 9.8 m/s² while it falls (before 0.6 s). There is no depth_info. question_fps = 120, the same as the file's fps.

## Scale from the fall
- The box falls straight down at a constant depth. The front-face centre moves exactly like the origin, so
  its pixel acceleration is a_px = f·g/Z_front. The front-face width is f·W/Z_front, so W = W_px · 9.8 / a_px.
  This does not depend on depth or focal length.
- The rendered box position skips: some frames show the next frame's position and some frames are frozen
  (see scene/notes.md). I fitted a parabola to frames 0–58 and let each frame's time shift by −1, 0 or +1 frame
  (fit2.py, retrack.py):
  - scene template track: a = 2070.1 px/s², rms 0.095 px
  - my own template on a different patch (retrack.py): a = 2069.0 px/s², rms 0.11 px; sub-windows give
    2068–2074
  - the face-top-edge track gives 2017. It is noisier (rms 0.33) and is biased by the flap and edge
    sampling, so I did not use it.
- Scale = 9.8 / 2069.5 = 4.735e-3 m/px at the front-face depth.

## Width in pixels
- Front-face horizontal extent, from sub-pixel saturation edges over about 45 rows (width.py): 281.7, 281.5,
  281.7 and 281.7 px at frames 0, 100, 150 and 199. Frame 30 reads 279.8 because of motion blur. The scene
  record gives 281.6. I used 281.6 px.
- W = 281.6 × 4.735e-3 = **1.333 m**. For comparison, the height is about 197 px = 0.93 m.

## Which horizontal extent is the width
- I could not measure the depth extent D directly. The underside seen at frame 0 gives D/Z_front ≈ 0.16–0.18,
  but turning that into metres needs the focal length, and I found no clean route to it.
- The open top flap is hinged on the right side edge. It reaches 140 px, which is exactly half the front
  width. In a regular slotted carton the flap height is half the shorter horizontal side, so the front
  dimension is the shorter one, which is the width. With any focal length of about 1650 px or more
  (horizontal FOV ≤ 60°, which includes Blender's default 50 mm), D ≥ W.
- If D turned out to be the shorter side, the answer would be D. I cannot measure D without the focal length;
  it would be about 0.8–1.3 m.

## Checks
- The scale is plausible: the truck rear is 566 px, about 2.5–2.7 m at this scale, a realistic box truck.
- Two independent acceleration tracks agree within 0.1 %.
- Confidence: high for the front-face width (about 1 %). The main risk is the reading of "width" if the box is
  shallower front to back than it is wide.
