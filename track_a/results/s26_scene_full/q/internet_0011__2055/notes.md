# q_2055 — displacement of the player in black

**Scale.** The prior is "court width = 4.88 m". 4.88 m is 16 ft, the standard width of the lane (key). The scene record gives the lane width
as 1077 px between line centres (x 1414-2491). I checked it on frame 0 at quarter scale: about 1084 px between the outer edges.
Two checks fit this reading: the free-throw circle is 796 px, which is 3.61 m at this scale (the standard is 3.6 m), and the
larger rectangle (1990 px) is much too wide to be 4.88 m.
Scale = 4.88 / 1077 = 0.004531 m/px. The view is a top-down drone shot, so I treat it as 2D (a planar, single-scale convention).

**Displacement.** The straight-line distance from frame 0 to frame 106 (the last frame), using the mask centroid of
player_black from scene/tracks/player_black.csv (m.py):
- camera-compensated (cx_f0, cy_f0): 694 px; raw: 687 px; averaged over 3 frames at each end: 683 px; bbox centre: 676 px.
- I used about 690 px, which gives 690 × 0.004531 = **3.13 m**.

**Second route / check.** I looked at gridded crops of frames 0 and 106. Frame 0: player under the rim, head ≈ (2010,475),
body centre ≈ (2025,490). Frame 106: torso ≈ (2110,1170), head ≈ (2125,1235), leaning forward. The visible centre agrees
with the track. Other reference points give: hip ≈ 665 px (3.0 m), head ≈ 765 px (3.47 m). The answer
depends on which point the annotator clicked, so the uncertainty is about ±10%. The time base (fps 20.43 vs question_fps 25)
does not affect a displacement.

Confidence: moderate.
