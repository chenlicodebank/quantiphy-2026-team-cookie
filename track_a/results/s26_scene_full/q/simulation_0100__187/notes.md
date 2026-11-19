# Q187 — boat speed at 1.0 s (m/s)

- 2D side view, static camera, 24 fps (file and question agree). t=1.0 s -> frame 24.
- Scale: prior boat length 10 m. Full bounding-box length of the boat (stern 665 -> bow tip 1523 px at frame 57,
  checked on a zoomed grid frame frames/f57.png) = 859 px -> 0.011641 m/px.
  (Rows 460-540 alone give 821 px because the bow tip and stern overhang lie outside them; the full extent is the bbox.)
- Speed: own red-hull bow-edge measurement (measure.py): step 23->24 = 17.86 px/frame, 24->25 = 17.95,
  mean 2->57 = 17.878 px/frame, 21->57 = 17.883 (uniform motion). Matches the scene record (17.876).
- v = 17.88 px/frame x 24 fps x 10/859 = 4.995 m/s (≈ 5 m/s, a plausible round render value).
- Second route: span-averaged speed equals the local one-frame difference to within 0.5%. Confidence high;
  main uncertainty is the length in pixels (±2 px, 0.2%).
