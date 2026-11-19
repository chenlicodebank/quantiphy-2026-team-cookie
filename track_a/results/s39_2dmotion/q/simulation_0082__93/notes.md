# Q93 – speed of the yellow car at 1.0 s (m/s)

Prior: yellow car length = 5.67 m. 2D top-down render, 24 fps (file fps = question fps = 24), t = 1.0 s -> frame 24.
The yellow "car" is the yellow pickup in the upper lane (scene/ calls it yellow_truck). It moves at constant velocity
in -x from frame 1 on (frames 0 and 1 are identical), so the speed at frame 24 is the constant cruise speed.

## Measurements (scripts: length.py, measure.py)
* Length at frame 24 (own mask: saturation > 40 or min < 100 or max > 172, core rows 375–430): x 1172–1481, 310 px
  inclusive, edge-to-edge ≈ 309 px. Frames 23/25: 312/310. scene record: 310. SAM 3 mask frame 24: box 1174.1–1481.0,
  length 307 px (1% shorter). Pixel values on row 401 show the front edge ramping over x 1172–1176 (partly covered at 1172,
full yellow from 1176) and the rear edge ending at ~1481, so SAM's 1174.1 sits inside that soft front edge; both agree
within ~2 px.
  Difference < 3%. Length shrinks slightly right-to-left (314 at frame 0, 304–306 near the end; perspective), so I use
  the local value at frame 24: 309 px.
* Per-frame shift near frame 24: sub-pixel profile cross-correlation 11.38–11.46 px (mean ~11.42, frames 15–34);
  box centre frame 0->71: 794/70 = 11.34 px; record edges 11.26–11.41; SAM 3 track: net 793.1 px over 70 moving frames
  = 11.33 px/frame, linear fit 272.05 px/s. Adopted 11.38 px/frame = 273 px/s.

## Result
scale = 5.67 / 309 = 0.01835 m/px; speed = 273 x 0.01835 = 5.01 m/s.
Second route (all SAM 3): 5.67 / 307 x 272.05 = 5.02 m/s. Spread over choices of length (307–310) and rate
(11.33–11.46) is 4.97–5.05 m/s.

Answer: 5.01 m/s. Confidence: high (±2%).
