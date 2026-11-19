# q2035 – average speed of the motorcycle (prior: lane width = 3.66 m)

- Object: the scene record calls it "cyclist"; zoomed frames (frames/f1.png, f30) show a rider on a motorcycle
  in the right lane, driving down the image. It is the only two-wheeler. Track scene/tracks/cyclist.csv
  checked against frame 30: track (572, 1061) matches the bike on the image (≈573, 1063).
- Camera: static nadir drone (background drift < 2 px total), so no compensation is needed.
- Scale (lane.py, lane2.py): median road-brightness profiles over 5 bands of frame 169. Asphalt edges at
  x≈522–527 (left) and x≈595–599 (right), so the road is 73–76 px wide (the record says 75–77). Centre line is at x≈560,
  so the left lane is ≈37 px and the right lane ≈39 px. Lane = 38 px, giving 3.66/38 = 0.0963 m/px.
  (If the dark kerb lines were included, the lane would be ≈41.5 px and the answer 8 % lower: 24.6 m/s.)
- Pixel speed (speed.py), using template-matched centres for frames 0–118, while the bike is fully visible:
  mean per-frame speed is 9.295 px/frame. The net displacement / frames gives 9.293, and a linear fit gives 9.301.
  The three thirds of the clip give 9.26, 9.41 and 9.25, so the speed is constant.
- Time base: the file runs at 29.68 fps and the question at 30 fps. The difference is only 1 %. I used question_fps = 30,
  which gives 26.86 m/s (29.68 fps gives 26.57).
- Answer: 9.295 × 30 × 0.0963 = **26.9 m/s** (≈97 km/h).
- Check: the speed over each third of the track and the net displacement agree within about 1.5 %. The main
  uncertainty is the lane pixel width (±2 px, about ±5 %). Confidence: moderate to good.
