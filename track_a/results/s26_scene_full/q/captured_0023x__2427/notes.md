# q_2427 — length of the book (cm)

Lab video, 24 fps (file and question_fps agree), 1280x720, f = 0.5959*1280 = 763 px, principal point ~(640,360).

Method (lab method card): length = depth x pixel extent / f, with the book lying flat on the table and its long side
running left-right across the image (the long axis is nearly perpendicular to the line of sight; axis angle ~ -1 to -3 deg).

Key measurements
- t = 1.6 s (frame 38) and the rest frames 37-48: depth_book = 0.851 m. The book's left end is at x ~ 477 and its right end at
  x ~ 652-655 (zoomed crop frames/edges42.png, LAB b* column profiles in edges.py, scene bbox 477-655). The thin string at the
  left end is excluded. Pixel length ~ 176 px (range 174-178). Length = 0.851*176/763 = 0.196 m.
- Second route, t = 1.4 s (frame 34, depth 0.857 m): bbox 480-655 -> 175-176 px -> 0.857*176/763 = 0.198 m.
- Third route, t = 1.2 s (frame 29, depth 1.02 m; blurred and tilting): ~145 px -> 0.194 m.
All three agree within about ±1.5 %.

Answer: 19.6 cm. Confidence: good (about ±3 %). The edges are soft from compression and blur, which accounts for ±2 px.
