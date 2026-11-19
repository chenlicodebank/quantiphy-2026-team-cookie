# q3136: height of the lamp (m)

Prior: the rider's average speed is 4.46 m/s. The internet convention uses one planar scale = prior / pixel speed. fps is 30 (file and question agree).

**Pixel speed** (scene/tracks/rider_scooter.csv; camera drift ≤2 px, which is negligible):
- scooter_cx: frames 0-73 gives 547 px/s; the full clip gives 540 px/s.
- rear_wheel_cx: 551 px/s over 0-73 and 543 px/s over the full clip.
- upper_body_x (independent body track): 547 px/s over 0-73 and 538 px/s over the full clip.
- Adopted value: 545 px/s, so scale = 4.46/545 = 0.00818 m/px.

**Lamp pixel height** (lamp.py at frame 78, with 4x zoom crops in frames/top2.png and frames/bot2.png):
- The finial tip is at y ≈ 123 and the dome top at y ≈ 132.
- The bottom of the black base foot is at y ≈ 689. The concrete pad below it reaches about 702.
- Finial tip to the bottom of the foot is about 566 px. The scene record gives 553 px (y 135-688, without the finial).
- Adopted value: about 563 px.

**Answer:** 563 × 0.00818 ≈ 4.61 m.

**Check:** with the record's 553 px the answer is 4.53 m, and with 566 px it is 4.63 m. Taking the scale from the 0-73 window or from the full clip changes it by less than 2%. Rule-of-thumb real lamp-post heights of about 4-5 m agree. The lamp stands farther from the camera than the path, so its true height is probably a bit larger, but the convention ignores perspective.

Confidence: moderate-high (±5%).
