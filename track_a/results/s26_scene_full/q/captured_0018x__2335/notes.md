# q_2335 — width of the box (cm)

Lab video, 24 fps (file fps and question_fps are the same), 1280x720, f = 0.5959*1280 = 763 px, principal point (640,360).
The prior (g = 9.8) is not needed for a size. The scale comes from depth_info.

## Object
A white carton held upright in the left hand (image-left) of the far person, next to the soccer ball, which is in her other hand.
Both are dropped at frame 29.

## Pixel width (measure.py, f0prof.py)
- Frames 0 and 20 (held, front face with label facing the camera): per-row profiles in rows 254-269 give the box from x=469 to x=489/490,
  so the **face width is about 21.5 px**. Its top is hidden by the fingers. Visible height is at least 52 px.
- Fall frames 33-38: the box turns, showing a corner and two faces. The per-row width medians are 25-27 px, and minAreaRect gives 25.7-31 px
  (edge blur included). This fits a cross-section of about 21.5 x ~17 px seen diagonally. The front face (21.5 px) is the horizontal
  extent across the face, which is the width.
- On the floor at frame 48, lying down: long axis 56-62 px (the box's height, about 20-22 cm), which is consistent.

## Depth
The box is not in depth_info. It is held at the same height as the soccer ball, by the same person's other hand: ball distance 2.80 m
(Z = 2.755 m). Floor-contact rows put the box roughly at Z 2.65-2.75 m (camera height about 0.85 m, from the far person's feet at y=577 with
distance 3.13 m). I used distance 2.80 m. That gives Z = 2.72 m at the box pixel (480,266).

## Result
- width = 21.5 px * 2.72 / 763 = 7.66 cm (with Z), or 21.5 * 2.80 / 763 = 7.89 cm (method card, distance used directly). **Answer 7.8 cm.**
- Alternative reading: the other horizontal side is about 17 px, or 6.1 cm. A diagonal or rotated extent of 26-27 px gives 9.5 cm.
  The 9.5 cm is not a box dimension.
- Check: the box height is about 52-60 px, or 19-21 cm, which is plausible for a carton. The persons come out at 1.64 m and 1.61 m from the
  same intrinsics, so the scale is consistent.

## Confidence
Moderate. The box's depth is inferred, worth ±5%. The pale edges blend into the white background, worth ±1 px (±5%).
