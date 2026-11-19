# q_2467 – shoulder breadth of the person (cm)

Lab video at 24 fps (the file fps and question_fps are the same). Focal length f = 0.5959·1280 = 762.75 px, principal point (640,360).
depth_info: book (the ball) 1.0995 m at t=0.2 s and 1.151 m at t=0.6 s. Person's left shoulder 1.2750 m, person's right shoulder 1.2305 m.

## Scale check
Ball edge diameter at f5 = 49.06 px. 1.0995·49.06/762.75 = 7.07 cm, which matches the 7 cm prior, so f is consistent.
At f14 the diameter is 40.8 px, which gives 6.2 cm. That second depth is less consistent.

## Shoulder edges (edges.py)
I used half-level crossings between skin and the bright background, as the median over all 49 frames. The person is static, with an sd of about 1–2 px.
- Image-left shoulder (the person's right, arm raised forward): x = 760 / 755 / 750.5 / 746 at y = 100 / 105 / 110 / 115.
- Image-right shoulder (the person's left): x = 993 / 995 / 997 / 998 at the same rows. Viewed by eye, the outer edge is about 1000–1003, because the dark monitor behind it pulls the half-level inward.
- I took the deltoid level y ≈ 110–115, which gives a pixel width of about 247–252 px.

## Result
- Back-projection P = ((u−cx)/f, (v−cy)/f, 1)·depth, with the person's left assigned to image-right (1.275 m) and the person's right to image-left (1.2305 m). The 3D distance is 0.421 m (y=110) to 0.430 m (y=115).
- Second route: the simple size formula (mean depth × px / f) gives 0.405–0.413 m. With the depths swapped the result is 0.394–0.403 m. Treating depth as Euclidean range would give about 0.36 m, but the method card uses Z.
- Answer: **42 cm**. Confidence is moderate (±5%). The main uncertainties are the exact clicked shoulder points and the depth-to-side assignment.
