# q_1772 — height of the walking pedestrian (m)

Prior: the white car (the van) accelerates at 4 m/s². depth_info gives distances at t=0.58 s and t=1.58 s (frames 14 and 38 at
question_fps = 24, which is also the file's rate) for the human, the yellow car (taxi), the white car (van) and the bike.
The camera is static (scene record). I assumed the principal point is at the image centre (1080, 540).

## Focal length (from the van's acceleration)
- I back-projected the van's mask centroid at frames 14 and 38 using its depths (23.589 m and 19.990 m), which defines its straight 3D path.
  Every frame's centroid ray was then put on that path, with s(t) = 2(t - t0)², i.e. a = 4. I fit f (and t0) to the
  reprojection of the image track (`focal2.py`).
  - Early windows (frames 2–40 and 2–50, where the van is small and its centroid is close to its origin) gave f ≈ 873–915, with
    t0 ≈ 0 to 0.015 s.
  - Late windows are biased because the big van's centroid drifts off its origin, so I left them out.
- Start time check (`early2.py`): the centroid's along-track displacement in frames 0–24 fits motion starting at frame 0 (k0 ≈ 0)
  better than at frame 1.
  - With t0 = 0 fixed, f ranges from 838 to 919 px depending on the assumed origin offset (centroid to 0.3 × the van's pixel height lower).
  - Second route: the 0.58→1.58 s displacement for t0 = 0 is 4.333 m. Matching it with depth-based 3D points needs f ≈ 852.
- Adopted **f ≈ 885 px** (horizontal FOV ≈ 101°), uncertainty about ±40 px.

## Height (`height.py`)
- Ground "up" direction: the cross product of horizontal 3D chords between frames 14 and 38 (van × taxi, van × pedestrian,
  cyclist × taxi). This gives a camera pitch of about 26–30° down.
- The pedestrian is about 37° off the optical axis, so the simple d·px/f (2.4 m) badly overestimates. Instead:
  - pelvis = d(t)·ray, with depth interpolated linearly between the two given values;
  - I intersected the rays of the head-top row and the lowest-foot row with the vertical line through the pelvis.
- Pixel extent: I re-measured it on the raw frames with thresholds 15/40/90 (`pedmask.py`). It agrees with the track within ±1 px:
  95–97 px for frames 24–69.
  - Frames 14–17 have a shortened bbox.
  - Frames 70–71 touch the taxi.
  - Both were excluded.
- Results over frames 18–69 at f = 885: the maximum is 1.82–1.87 m, the 90th percentile 1.79–1.85 m and the median 1.74–1.80 m.
  At f = 852 (displacement route) the maximum is about 1.87 m; at f = 930 it is 1.76–1.82 m.
- Answer **1.82 m**: the upper range of the walking height, standing in for the standing height.

Confidence: moderate (about ±5–7%). The main uncertainties are f, which depends on the van's start time and origin, and the
camera tilt.
