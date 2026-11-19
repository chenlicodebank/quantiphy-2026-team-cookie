# q_2420 — height of the book (cm)

Lab clip, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959 x 1280 = 762.8 px, cx,cy = 640,360.
Height = the book's vertical extent (its thickness, since it lies flat on the table at the end).

## Measurement
- Book at rest on the table in frames 37–48 (t = 1.54–2.0 s); depth_info gives 0.851 m at t = 1.6 s (0.857 m at 1.4 s).
- `profile.py`: vertical gray profiles at the front face. Each column shows the cover top face (~212 gray), a dark
  band = front edge of the top cover board (~3 px), the cream page block, a dark band = bottom cover edge/contact,
  then the table (~135).
- `thick.py`: per frame (37–48) and per column (x 495–645, every 5 px) the top of the front face (half-point of the
  top-face → dark-lip drop) and the bottom (half-point of the dark bottom band → table rise).
  Front-face extent: median 15.4 px (mean 15.3, std 0.75; 372 samples). Top-to-darkest-line variant: 14.0 px.
- Size = depth x px / f: 0.851 x 15.4 / 762.8 = 1.72 cm (method card). Using the axial depth
  Z = 0.851 / 1.021 = 0.833 m (the ray is off-axis at (565, 500)) gives 1.68 cm. Using the t=1.4 depth (0.857 m)
  gives 1.73 / 1.69 cm.

## Check
- Same extent in every column along the book (15–16 px, and the bottom edge tilts with the book's slight yaw), and
  it stays the same over all 12 resting frames.
- The two dark bands (cover boards) are each ~3 px ≈ 3 mm, which is a plausible hardcover thickness. That supports
  the scale.
- Book length 175 px gives about 19 cm, so thickness/length ≈ 0.09, a plausible book.

## Answer
1.70 cm (between the method-card 1.72 and the axial-depth 1.68). Confidence: moderate-high. The edge placement
uncertainty is ±1 px, which is ±6 pct.
