# q2037 – average speed of the white car (prior: lane width = 3.66 m)

Static nadir drone shot. The background drifts by 1.7 px at most, so no camera compensation is needed. The file runs at 29.68 fps; I used question_fps = 30.

## Where the earlier answers part ways
Both used the same pixel speed (8.69 px/frame). They differ only in which pixel width the 3.66 m "lane" was mapped to:
- C1 used half the asphalt (37.75 px), giving 25.2 m/s.
- C2 used the whole carriageway (76.5 px), giving 12.5 m/s.

## My measurements (measure.py)
- **Pixel speed.** I used the scene template track, frames 0–152, while the car is fully in the frame. Mean per-frame displacement is 8.69 px/frame (median 8.73). A linear fit of y gives 8.68 px/frame.
- **Road width.**
  - Saturation profiles over 3 frames × 5 bands give 77–82 px. That run includes some edge or verge pixels.
  - Zoomed crops at frame 30 show the grey asphalt edges at x ≈ 522 and x ≈ 598, so 76 px. The scene record gives 75–77 px.
  - I take 76.5 px as the road width.
- **Size check (decisive).**
  - The white car is 78 px long and about 30–37 px wide.
  - With one lane = half the road (0.097 m/px), the car would be 7.6 m long and 3.0–3.6 m wide. That is impossible.
  - With the whole road = 3.66 m (0.0478 m/px), the car is 3.7 m × 1.6 m. That is plausible, so the road is a narrow carriageway about 3.7 m wide.

## Answer
- v = 8.69 × 30 × 3.66 / 76.5 = 12.5 m/s (about 45 km/h).
- Second route: net displacement of about 1380 px over 5.07 s (152 frames at 30 fps) gives about 12.5 m/s.
- If the road is 78 px wide instead, the answer is 12.2 m/s.

I agree with C2. Confidence is moderate: the scale reading is settled by the car's size, and the remaining uncertainty is about ±3 % from the road-edge pixel width.
