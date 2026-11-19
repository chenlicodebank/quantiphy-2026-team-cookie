# q3028 – width of thumbnail (cm); prior: toilet paper roll size = 100 mm

Internet video, static camera, 2D planar convention: one scale = prior / roll pixel size.

Scale: roll seen side-on, axis horizontal (the main motion direction). Checked on frame 59 (crop.py ->
frames/roll59.png): ends x ~1617 to ~2207 = 590 px (record: 589 +- 3); diameter 1063-1760 = 697 px.
"Size = 100 mm" read as the roll's axial length (standard roll width ~10 cm; diameter/length = 1.18 matches a
real roll of ~10 x 11.8 cm). Scale = 100 / 590 = 0.1695 mm/px.

Thumbnail: thumb lies on the roll's front, pointing left; nail width measured across the thumb (vertical,
perpendicular to the roughly horizontal thumb axis) on 5x zoomed crops (frames/n59.png, n53.png):
- frame 59: nail edge top y ~1461, bottom y ~1566 -> 105 px
- frame 53 (second check, different frame): top ~1459, bottom ~1567 -> 107 px
Mean 106 px -> 106 x 0.1695 = 18.0 mm = 1.80 cm.

Alternative reading (prior = roll diameter, 697 px): 106 x 100/697 = 15.2 mm = 1.52 cm.
Answer: 1.8 cm (length reading). No time conversion needed (static size; fps 24.1 vs question_fps 30 irrelevant).
Confidence: moderate (nail edges +-3 px; the bigger risk is which roll dimension the prior names).
