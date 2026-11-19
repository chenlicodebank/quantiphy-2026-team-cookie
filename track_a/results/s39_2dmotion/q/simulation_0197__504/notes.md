# q_504: speed of the bubble at t = 1 s (m/s)

The file and the question both run at 30 fps, so t = 1 s is frame 30. This is a 2D scene, so one metres-per-pixel scale comes from the prior.

## Scale (prior: horizontal width of the "skynova" text = 0.00188 m)
- The brand text runs vertically down the left side of the bottle. Only "…NOVA" is in frame; "SKY" is cut off at the bottom edge.
  Because the text is vertical, its horizontal width is the letter height across the column of letters.
- My own measurement (measure_text.py, text_edges.py, frame 30; frames 0 and 49 give the same):
  - Blue-channel thresholds 170 and 190 give x = 1106–1185, a width of 78–80 px.
  - Sub-pixel crossings at 50 % and 70 % of the way from background to letter level give 81.3 px and 79.4 px.
  - **Text width = 80 px.**
- SAM 3 ("white text", box prompt, frame 30) gives horiz_px = 88 (x = 1102–1189). That is 10 % more than my
  measurement. On the zoomed crop (frames/text.png) and the column profile, the SAM mask starts where the blue level is
  still at background (~107 at x = 1102–1103). So SAM includes the soft blur halo, and the threshold edge (80 px) is
  the right one.
- Scale = 0.00188 / 80 = 2.35e-5 m/px.
- Other readings: if the prior meant the length along the curved surface (arc correction on the cylinder, ~125 px),
  the scale would be 0.64× and the speed ~0.0055 m/s. I rejected this because sizes are world axis-aligned
  bounding-box extents, which equal the horizontal image extent.

## Bubble motion
- The scene record track (scene/tracks/bubble.csv, background-difference hull centroid) and an independent SAM 3 track
  (tracks/bubble_0.csv, phrase "bubble" with a box at frame 30, frames 23–49) agree within ~2 px around frame 30.
- Raw backward difference |p30 − p29|: 11.14 px/frame (scene record) and 12.06 px/frame (SAM). Single steps carry
  ±1.5 px of centroid noise.
- Local quadratic fit of position along the motion axis (windows of ±3 to ±5 frames), derivative at frame 29.5, which
  is the time the backward difference represents:
  - scene record: 12.26–12.36 px/frame
  - SAM: 12.12–12.22 px/frame
  - **Speed = 12.25 px/frame.**
- Second route: the chord from frame 27 to 33 gives 12.15 px/frame (scene record) and 12.27 px/frame (SAM), which
  agrees. The bubble is in its near-steady phase (frames ~17–31) and only starts to slow after frame 31.

## Answer
12.25 px/frame × 30 fps × 2.35e-5 m/px = **0.0086 m/s**.

Confidence: moderate-high on the pixel speed (±2 %). The scale depends on how the prior is read: ±3 % for the text
edge definition, plus the cylinder-wrap ambiguity described above.
