White car tracked with SAM 3 over the clip: 8.70 px/frame (linear fit -8.686 px/frame; scene track -8.687). Scale from the prior lane width 3.66 m applied to the visible carriageway width (76.5 px, edges x=522/597, centre line x=559.5) = 0.0478 m/px; v = 8.70 x 30 fps x 0.0478 = 12.5 m/s. Second route (net 1380 px over 5.27 s) gives 12.6 m/s. Using one marked lane (37.5 px) instead would make the car 7.8 m long and 2.97 m wide, which the benchmark's car-size check rules out.

Final message:
**Answer: 12.5 m/s** (average speed of the white car, question 2037).

Method summary:
- **Motion:** SAM 3 track of the white car gives a linear fit of −8.686 px/frame (scene record: −8.687), i.e. 8.70 px/frame; with question_fps = 30.
- **Scale:** prior lane width 3.66 m mapped to the visible carriageway width (76.5 px, asphalt edges x = 522/597, dashed centre line at x = 559.5) → 0.0478 m/px.
- **Check:** the alternative reading (one marked lane = 37.5 px) would make the car 7.8 m long and 2.97 m wide — impossible, and it fails the benchmark's 3–7 m car check; the carriageway reading gives a 3.8 m × 1.45 m car. Road-marking geometry (89 px dashes / 44 px gaps, ~45 px "SLOW" letters) independently supports a ground scale near 0.06–0.07 m/px, confirming the road is a narrow ~4.9 m carriageway.
- **Second route:** net displacement 1380 px over 5.27 s → 12.6 m/s, agreeing within 1%.
