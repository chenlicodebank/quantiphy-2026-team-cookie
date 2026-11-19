# q_2793 — length of the shoe (cm)

Lab video, 24 fps (file fps = question_fps = 24). f = 0.5959 x 1280 = 762.8 px. depth_info: shoe at 2.231 m (t = 1.0 s).

Method (lab card): length = depth x pixel length / f.
- measure.py: foreground = max BGR diff to the per-row background (columns 880-1020) above a threshold, cropped to the
  shoe region, open/close, largest component; the max Feret diameter (convex hull) is the length along the shoe's
  diagonal axis (~37 deg to the image x-axis, toe lower-left to heel upper-right).
- Frames 0, 10, 24, 48 and thresholds 25/40/60: Feret 83.4-85.3 px (the static shoe is the same in every frame).
  Mask overlay (frames/mask.png) shows a thin light rim at the upper-left is left out of the mask, so ~85-86 px.
- L = 2.231 x 85.5 / 762.8 = 0.250 m -> 25.0-25.3 cm. Answer 25.2 cm.

Check: the same convention on the basketball (92 px wide, 1.9365 m) gives 23.4 cm, close to a real basketball (~24 cm),
so the scale is consistent. The scene record (85 px along the axis) agrees.
Caveat: the shoe lies on the floor partly angled in depth, so foreshortening could make the true length a bit
longer (~27-29 cm). I followed the card's convention (projected pixel extent). Confidence: moderate-good.
