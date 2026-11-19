# q_2762 — diameter of the tape (cm)

Lab video, 1280x720, 24 fps (file fps = question fps). Static tape roll lying flat on the table (scene/ tape_roll,
box ~[551,437,629,484]). Lying flat -> diameter = horizontal extent of the roll in the image.

Method (lab method card): f = 0.5959 x 1280 = 763 px; D = depth_tape (0.973 m) x pixel width / f.
- measure.py: grey-level column profile over rows 450-478 (frame 0): left edge ~551.5, right edge ~628 -> 76.5 px;
  bright/low-saturation run per row: 553/554 to 627 (74-75 px, slightly conservative threshold); visual read on
  3x zoom 550.7-628 (~77 px). Same in frames 10 and 20 (static). Adopted 77 px.
- D = 0.973 x 77 / 763 = 0.0982 m = 9.8 cm. (Off-axis cos correction would give ~9.7; card convention used.)

Second route (scale check): the credit card (navy card at table front, depth 0.69 m) has long edges of ~90 px (back)
and ~97 px (front), mean ~94 px; predicted 85.6 mm x 763 / 0.69 = 94.7 px -> implied f ~758 px, consistent with 763.
With f = 758: D = 9.88 cm.

Answer: 9.8 cm. Confidence: good (±3%). Note: depth_info "white_cup 8420m" is clearly a typo, unused.
