# q_3157 – Bicycle sign distance to ground

Prior: average speed of the "person riding scooter" = 1.95 m/s. No scooter is visible. The only moving person is the
woman crossing right to left (scene/tracks/pedestrian.csv), so the prior is taken to refer to her. fps = question_fps = 30.

Scale (single planar scale, annotator convention). Script: speed.py
- Pedestrian pixel speed over frames 0-74: bbox centre path 250.7 px/s, net 248.7; head top 242-245; stabilised
  centroid net 245. Taking ~247 px/s gives a scale of 1.95/247 = 0.00790 m/px (range 0.0078-0.0080).
  The camera drift is ~1%, so it was ignored.

Sign (frame 0, zoomed crops frames/sign.png and frames/base.png):
- Bottom vertex of the yellow bicycle diamond: y ≈ 273. Arrow plaque bottom: y ≈ 325. Diamond centre: y ≈ 191.
- The pole meets the mulch of the splitter island at about (928, 665).
- Diamond bottom to ground = 392 px, which is **3.10 m** (answer).
- Other readings: arrow-plaque bottom to ground 340 px = 2.69 m; diamond centre to ground 474 px = 3.74 m.

Check: different reference points on the pedestrian give scales within ±2%. Sanity: at this scale her height (~290 px)
comes out at ~2.3 m, so the prior's scale is inflated compared with real-world size. The answer still follows the
convention of one scale taken from the prior. Confidence: moderate. The main uncertainty is which point counts as the
sign's "distance to ground".
