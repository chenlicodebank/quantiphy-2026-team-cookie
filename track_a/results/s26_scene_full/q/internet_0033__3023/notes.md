# Q3023 – speed of the plate (bowl) of tomatoes from 1 s to 1.6 s (m/s)

Prior: fork = 20.3 cm. Internet video, overhead view, single planar scale (annotator convention).

## Scale (fork)
The only fork lying free and fully visible is on the top-right (pink-blazer diner's) green-pasta plate:
handle end ~(1832, 207) to tine tips ~(1720, 296) at frame 0 (zoom `frames/fork2c.png`, brightness profile
along the axis in `fork_profile.py`, frames 0 and 10): 145-149 px -> use 147 px.
Scale = 0.203 / 147 = 1.381e-3 m/px. The other forks are held in hands (partly hidden) and only roughly
consistent (bottom fork ~133+ px with tines in pasta). Sanity: plate 226 px -> 31 cm, table ~120 x 225 cm: plausible.

## Time base
File fps 19.293 vs question_fps 25. Bowl steps are smooth frame-to-frame (no periodic doubled steps), so no frames
were dropped: the clip is the original frames re-timed. Reference answers follow the original footage, whose
standard rate is the stated 25 fps -> t = 1.0 s -> frame 25, t = 1.6 s -> frame 40.
(Peak bowl speed then ~25 px/frame = 0.86 m/s, plausible for passing a bowl.)

## Track
scene/tracks/tomato_bowl.csv rim-circle centre, background-compensated (camera drifts ~1 px/frame up).
Verified by overlay at frames 25, 32, 40 (`check_track.py`, `frames/track_check.png`) – fits are good.
Independent route: tomato-pixel centroid mapped through the camera transform.

## Result (speed.py), frames 25-40, 0.6 s
- rim centre: raw path 129.4 px (0.302 m/s), SG-smoothed path 117-120 px (0.273-0.279), net displacement 112 px (0.261)
- tomato centroid: raw 123 px (0.287), smoothed 116 px (0.270), displacement 112 px (0.262)
Late part (frames 33-40) is slow with jitter, which inflates the raw path; chose ~120 px path -> 200 px/s
-> **0.275 m/s**.

If the file rate 19.29 fps were used instead (frames 19-31): ~0.43 m/s (not chosen).

Confidence: moderate – main uncertainties are the time base choice and the fork pixel length (±4 %).
