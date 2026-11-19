# Q102: length of the yellow car

- 2D top-down video, 24 fps (the file rate and question_fps match). The prior is speed = 5.07 m/s, so the scale comes from the yellow car's pixel speed.
- Pixel speed: I fitted a line to the yellow car's bumper-to-bumper centre over frames 12–71 (the car is fully in view there). `measure.py` gives −9.877 px/frame, with the front edge at −9.80 and the rear edge at −9.95. The scene record gives −9.90. Taking 9.88 px/frame gives 237.1 px/s, so the scale is 5.07 / 237.1 = 0.02139 m/px.
- Pixel length: bumper to bumper, excluding the shadow. It is 268–276 px in the record and 270–278 px in my mask, which picks up about 2 px of shadow edge. The length shrinks slightly towards the image centre because of perspective. I used about 271 px, the value near the middle of the clip and close to the image centre.
- Length = 271 × 0.02139 = **5.80 m** (range 5.73–5.95 over the frames).
- Second route: the record's per-frame steps and lengths (9.90 px/frame, 272 px mean) give 272 × 5.07 / (9.90 × 24) = 5.80 m, which agrees.
- Confidence: high, within about 3% (perspective changes the length by about 3%).
