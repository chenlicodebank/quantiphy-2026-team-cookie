# q_2077 — motorcycle length (prior: lane width = 3.66 m)

Top-down static drone view (2D, planar); single scale from the prior. Time base irrelevant (size question).

## Scale (measure.py)
Brightness row profile over x 1000–1900 on frame 140 (empty road), line centroids:
upper edge line y = 519.1, centre double line 564.2 / 571.9, lower edge line 618.5.
Upper lane (the motorcycle's lane), line centre to line centre = 45.1 px (lower lane 46.6; inner edges 41, outer 48.5).
Used 45.1 px -> 3.66 / 45.1 = 0.0812 m/px.

## Motorcycle pixel length
The "cyclist" in scene/ is the motorcycle (red/white with rider, keeps pace with the cars at ~12 px/frame).
- Visual, 10x zoomed crops (crops.py; frames/moto_tiles*.png): f0 ≈ 33.5 px, f10 ≈ 32, f20 ≈ 32, f30 ≈ 29.5,
  f40 ≈ 28.5, f50 ≈ 29. The front (left) end merges with the cast shadow, which causes most of the spread.
- Background difference (frame 140 as background), body rows 543–551, extent where diff > 60: 35–38 px for f0–f16
  (includes some shadow), 30–34 px for f18–f40, 27–29 px for f46–f58 (lighting gets dimmer).
- scene/ record gives ~34 (28–35).
Adopted 31.5 px (±2.5).

## Answer
31.5 px × 0.0812 m/px = 2.56 m -> answering 2.55 m.
The second route (the background-difference extents, 30–34 px in the clean middle frames) gives 2.4–2.8 m.
That is somewhat longer than a typical motorcycle (~2.1–2.2 m), likely because of motion blur and the shadow
at the front. The annotators measured visible pixels, so the visible length is kept.
Confidence: moderate (±8%).
