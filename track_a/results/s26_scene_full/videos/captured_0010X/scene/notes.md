# captured_0010X — measurement record

**Scene.** A lab (Orbbec, 24 fps, 1280x720, 49 frames, 2.04 s) clip of a pendulum: a small ball on a thin dark string
hanging from a pivot at about (637, 229) px. The background has been replaced with pure white, so there is no
ground, furniture, horizon or other object. The only other thing in the image is a grey watermark at the bottom right.
The camera is static: the pivot stays fixed within about ±4 px, which is also the detection noise.
Intrinsics by the benchmark convention: f = 763 px, principal point about (640, 360).

**Motion.** The ball is already swinging at frame 0. The swing plane is mostly along the camera's line of sight, with
a small sideways part toward +x. Far end of the swing (ball high in the image and smallest, about 29–31 px):
frames ~3 and ~32–33. Near end (ball low in the image and largest, about 40–41 px): frames ~16–18 and ~45–47. The
lowest image position, y ≈ 391, is at frames ~12 and ~22 and again at ~41–42. Because of foreshortening, the
pivot-to-ball distance in the image ranges from 60 to 166 px, so image distances are NOT true distances. The 3D
position needs depth_info, or the size ratio: depth ∝ 1/apparent diameter. With a known ball diameter D:
Z ≈ 763·D/diam_px.

**Files.**
- `scene.json`: inventory, camera, events.
- `tracks/ball.csv`: one row per frame (0–48) with:
  - the centroid of the filled mask (cx, cy), which is the reference point
  - bbox, plus mask extents along the major and minor axes
  - area, area-equivalent diameter, minimum enclosing circle
  - appearance (`red` or `pale_mask`); occluded is 0 in every frame.
- `tracks/string.csv`: per frame, the top pixel of the string (≈ pivot), the bottom of the string, the visible
  length, the image angle from vertical, and the pivot-to-ball-centre distance in pixels.
- `scripts/`:
  - `track.py` produces the tracks and an overlay check
  - `survey.py` and `pix.py` are colour surveys
  - `look.py` is a crop viewer.

**Method and reliability.**
- Frames 0–11: the ball mask is the red pixels.
- Frames 12–48: the ball appears as a flat pale-pink fill (a segmentation artifact; it is the same ball). There, the
  mask is the bright pixels with r−b ≥ 7, followed by open/close, the largest component and hole filling.
- The overlays (every 3rd frame) confirmed that the masks cover the whole ball and the centroids sit on it.
- Centroid precision: about ±1 px. Diameter: about ±2 px. The pale masks have slightly ragged outlines, and the red
  frames have motion blur during the fast phases (frames 8–12, 26–29, 36–39), which stretches the bbox along the motion.
- Use `equiv_diam_px` rather than the bbox for size.
- String top detection: the thin top of the string is faint in frames 1–6 and 44–48, so `top_y`/`top_x` vary by
  ±4–15 px there. Use the fixed pivot (637, 229).
- The string angle is noisy (±5°), because the string is 2–3 px wide and is partly hidden behind the ball.
- No motion models, speeds or accelerations were computed.
