# q3128 — distance between the brown (Jeep) and green (Fiat 500) car

Time base: file fps = question_fps = 30.

Scale (single planar scale from the prior, internet convention):
- Rider reference point = bbox centre in pan-removed coordinates (scene/tracks/rider_scooter.csv); I checked the
  frame and the record's description.
- Speed: net 863 px / 49 frames = 528.4 px/s. The 5-frame-smoothed mean per-frame speed is 528.4 px/s and the raw
  mean per-frame speed is 531.3 px/s, so they agree.
- Scale = 2.07 / 528.4 = 0.003918 m/px. Without pan removal it would be 519.8 px/s, +1.6% on the answer.

Car positions (frame 0, read from zoomed 2x views with a 20 px grid: frames/jeep.png and frames/fiat.png):
- Jeep body x 457–720 (centre 588); rear plate centre x 566.
- Fiat body x 1135–1355 (centre 1245); rear plate centre x 1251. The vertical offset is about 23 px, which is negligible.
- Centre to centre: 657 px (bbox centres) or 685 px (plate centres). I used about 670 px, giving 2.62 m (range 2.57–2.68).
- Other reading: edge-to-edge gap of 415 px = 1.63 m. I did not use it because distances between objects are taken
  between their centres.

The scooter rider is closer to the camera than the cars, so the real distance is larger. The benchmark's
single-scale convention is followed anyway.

Answer: 2.62 m. Confidence: moderate. The main uncertainty is whether the reference used centres or the gap.
