# Q1018: height of the fish (m)

- 2D side view with a static camera. One koi swims along −x at constant depth. The file fps and question_fps are both 24, so I used 24 fps.
- Scale comes from the prior, speed = 0.67 m/s.
  - The fish's pixel speed comes from scene/tracks/fish.csv ref_x/ref_y, which are sub-pixel head-template shifts.
  - The mean per-frame speed over the moving frames 2-70 is 22.45 px/frame = 538.9 px/s. Net displacement over that time gives the same value, 538.9 px/s.
  - Frames 1 and 71 are held frames (speed 0), so I left them out.
  - Scale = 0.67 / 538.9 = 1.243e-3 m/px.
- Pixel height is the vertical bbox extent, including fins: median 293 px over frames 5-71 (290-294).
  - Second route: a zoomed, gridded crop of frame 36 shows the dorsal fin tip at about y=496 and the lower tail-lobe tip at about y=788, so about 292 px. This confirms the record.
  - A frame-difference mask (check.py) gives 278 px because it misses the faint translucent fin edges, so I rejected it.
- Height = 293 × 1.243e-3 = **0.364 m**.
- Sensitivity: if all 71 speeds were averaged, including the held frames (523.7 px/s), the height would be 0.375 m (+3%).
- Confidence: good, within about 4%.
