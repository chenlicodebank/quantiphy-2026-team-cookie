# q_2183: maximum rebound height of the basketball (cm)

The file rate and question_fps are both 24. The apex is frame 46 (t = 1.92 s), which matches the depth_info "max rebounce" time.

## Measurements (scripts in this folder)
- `measure.py`: re-tracks the ball (HSV mask, circle fit on the convex hull) and writes `my_track.csv`. It agrees with scene/tracks to within about 1 px, except in frames 0–31, where the hand cut-out biases the fit.
- `width_profile.py`: measures the ball's half-level width at sub-pixel precision. The width is 108.2 px at the apex (f46), 106.1 at f43, 92.2 at f37 and 94.2 at f38. The ball is lowest at f37, and contact comes about 0.15 frame later (where the falling and rising paths meet), with the centre near pixel y ≈ 662–666.
- Camera: lab intrinsics, f = 762.8 px, principal point (640, 360).
- Positions:
  - P0 = back-projection of (483.3, 185.0) at 1.3210 m.
  - Apex A = back-projection of (528.0, 481.0) at 1.5795 m.
  - Contact centre C: depth from the width ratio against the apex and f43 depths, giving 1.82–1.86 m.
- Ball diameter from the given depths and pixel widths: 0.220–0.228 m (0.235 m from the t=0 bbox).

## Geometry (`height2.py` plus an inline sweep)
- I assume no camera roll and solve for the camera pitch so that two things agree:
  - the floor point straight below P0 lies at 2.0285 m (my reading of distance_floor_camera at t=0);
  - the contact centre sits one ball radius above that floor.
- Result: pitch ≈ 33°, camera height ≈ 1.60 m, ball centre at t=0 about 1.15 m above the floor.
- Apex:
  - ball bottom above the floor, which equals the rise of the centre from contact to apex: **0.44 m** (range 0.40–0.47);
  - ball centre above the floor: 0.55 m (range 0.51–0.58).
- The rise is insensitive to pitch: 0.39–0.43 m for pitches of 15–35° with a contact depth of about 1.80 m.
- Second route / reading: the plain depth difference floor − ball at the apex is 2.0285 − 1.5795 = 0.449 m, which agrees with the bottom-of-ball reading.
- Timing is not usable for a physics check. The fitted fall acceleration is about 36 m/s² and the rise acceleration about 5.6 m/s² (dropped or irregular capture frames), so h = gT²/2 (≈ 0.70 m) is unreliable.

## Answer
45 cm (the ball's rebound height = its bottom, or equivalently the centre's rise, at the apex). If the reference instead counts the ball centre above the floor, it would be about 55 cm.
Confidence: moderate. The contact-depth uncertainty is about ±5%, plus the ambiguity over which reading the reference uses.
