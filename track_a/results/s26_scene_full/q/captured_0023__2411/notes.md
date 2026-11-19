# q_2411: height of the book (cm)

Reading: height = vertical extent. The book lies flat on the table from frame 37 on, so its height is its thickness.
The question fps and the file fps are both 24. t = 1.6 s is frame 38, and the depth there is 0.851 m.

## Measurement (edges.py, profile.py)
- I took vertical intensity profiles over x 490-640, both on the mean of frames 38-48 and on single frames 38, 42 and 46,
  and found the edges at sub-pixel precision (medians):
  top-back edge of the cover (white ramp → blue) at 480.8, top-front edge at 495.7, end of the page block at 507.3,
  dark bottom-cover/contact line at 510.0, table start at 511.4.
- Front-face (thickness) pixel height: from the top-front edge to the contact line is 14.0-14.6 px (to the table start it is 15.7 px). I used 14.3 px.

## Scale (compute.py), f = 0.5959 × 1280 = 762.75 px
- Route A (lab card, using the depth to the book centre): 0.851 × 14.3 / 762.75 = 1.60 cm.
- Route B (perspective-corrected): the front face sits closer to the camera than the centre. Comparing the image rows of the top-back
  and top-front edges gives W/2 = 0.058 Z. That puts Z = 0.834 m and the front face at z = 0.785 m, so T = 1.47 cm (W ≈ 9.7 cm).
- Depth-scale check: the book's long-axis length is 146 px at t = 1.2 s (d = 1.02 m), giving 19.5 cm. At rest it is 173 px (d = 0.851 m),
  giving 19.3 cm. The two agree, so the given depths are consistent.
- Answer: 1.53 cm, between routes A and B. Uncertainty is about ±10 %, mostly from where the bottom edge is
  (book versus contact shadow) and from the depth correction for the front face.

## Other readings (not the answer)
- Long side (spine) about 19.3 cm. The front-to-back width is roughly 10 cm.
