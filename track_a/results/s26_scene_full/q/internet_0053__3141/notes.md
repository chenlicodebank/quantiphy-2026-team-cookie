# q3141: fire hydrant height (m)

Prior: the scooter rider's average speed is 4.46 m/s. The video is internet footage, so I used the annotators' convention: one planar scale = prior / pixel speed. The file runs at 30 fps and question_fps is also 30, so there is no re-timing issue.

## Pixel speed (from scene/tracks/rider_scooter.csv; the wheel centres were checked by overlays in the record)
- Rear wheel centre, frames 0-80: 406.5 -> 1855.5 px, i.e. 18.11 px/frame = 543.4 px/s. The motion is monotonic, so the mean of the per-frame speeds equals net distance / time.
- Second check: scooter_cx over frames 0-73 gives 1331.8 px / 73 frames = 547.3 px/s, which agrees within 0.7%.
- Camera drift is under 2 px over the clip, so it is negligible.
- Scale = 4.46 / 543.4 = 0.00821 m/px.

## Hydrant pixel height (hyd_profile.py, frame 0, column intensity profiles at x 1835-1860)
- The top of the cap is at y 559.5, where the green screen gives way to the white cap.
- The grey body ends at y 664. A darker base section (y 665-685) hides the white fence curb strip, so it is part of the hydrant. Below it, the dark ground starts at y 686.
- The full height is 685.5 - 559.5 = 126 px, which matches the record's 126 px. The grey body alone would be 105 px.
- Height = 126 x 0.00821 = 1.03 m. If the base is excluded, it is 0.86 m.

## Sanity and confidence
The prior's scale is large: the rider (about 310 px) would be about 2.5 m tall. So the prior probably overstates the real speed, but the benchmark's answer follows the prior's scale. Answer: 1.03 m. The scale is solid to about 1%. The main uncertainty is whether the annotator included the dark base (about 17%).
