# q2035 – average speed of the motorcycle (prior: lane width = 3.66 m), internet video, 2D convention

Object: the two-wheeler in the right lane driving down the image (scene record calls it "cyclist"; zoomed frame
t=1.0 s, frames/road.png, shows a rider on a motorbike at ≈(573,1063), matching the track). Camera static.

## Where the candidates part ways
Both measure the same pixel speed (~9.3 px/frame). They differ only in the pixel width given to "lane width":
- C1: half the road (one lane, 38 px) → 0.0963 m/px → 26.9 m/s.
- C2: the whole road surface (73 px) → 0.0501 m/px → 13.9 m/s.

Plausibility check with the standard object (white car 78 px long, 37 px wide):
- C1 scale: car 7.5 m long and 3.6 m wide, which is impossible.
- Whole-road scale: car 3.8 m long and 1.8 m wide, which is realistic.
So the "lane" is the road surface curb to curb, the same as the benchmark convention. I agree with C2's reading.

## My measurements
- road_width.py: median background over every 10th frame, with brightness and saturation profiles across the road at 9
  y-bands. The asphalt runs from x≈521 to x≈597 at every band, so the road is **76 px** wide. Centre line at x=559.
  The dark kerb lines just outside (x≈514–517 and x≈600) would give about 87 px.
  C2's 73 px is a little narrow. The record gives 75–77 px.
- speed.py: template-matched track for frames 0–118, while the bike is fully visible. Mean per-frame
  displacement 9.295 px/frame, net/frames 9.293, linear fit 9.301. The motion is constant.
- Time base: question_fps = 30 (the file runs at 29.678 fps).
- Speed = 9.295 × 30 × 3.66/76 = **13.43 m/s**. Other road widths: 73 px → 13.98, 87 px → 11.73.

Second route: net displacement and the linear fit give the same pixel speed to within 0.1 %. The scale reproduces
realistic car dimensions. The result is about 48 km/h, which is plausible on a country lane.
Confidence: moderate to good. The main uncertainty is the road-edge pixel width (±2 px, about ±3 %).
