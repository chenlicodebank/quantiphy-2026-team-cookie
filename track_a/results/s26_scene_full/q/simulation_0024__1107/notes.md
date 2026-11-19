# q1107 – length of the boat (m); prior: boat speed 4 m/s; depths 90.1103 m (t=1 s), 90.4360 m (t=2 s)

The file is labelled 25 fps, but question_fps is 24. All times use 24 fps (t=1 s is frame 24, t=2 s is frame 48), and one frame step is 1/24 s.

## Method (speed-to-length ratio, focal length cancels)
- Boat track from scene/tracks/boat.csv, frames 2–74. I checked the hull mask edges on zoomed crops at frame 38: bow tip x≈325, red stern/transom x≈716, so ≈391 px. That matches hull_len_px.
- I fitted a line to the image motion (speed.py). hull_cx moves −6.42 px/frame and hull_cy −0.24 px/frame, so |v| = 6.43 px/frame. roof_x gives 6.48 and the centroid gives 6.40.
- Hull length is 391.9 px on average (393.5 at frame 24, 390.8 at frame 48). bbox_w is 396.9 px; it adds about 5 px of rail and blur.
- The boat sails bow-first, so its axis lies along its velocity. Image length divided by image displacement per frame therefore gives the world ratio (L / (4/24 m)):
  L = 391.9 / 6.4285 × 4/24 = **10.16 m** (bbox version: 10.29 m).
- 3D check (geom.py): back-projecting the boat at frames 24 and 48 with the given depths, and requiring a 4 m displacement over 1 s, gives
  f ≈ 3490 px (horizontal FOV 15.7°). The velocity points about 5.5–6° out of the image plane (the boat moves away while going left).
  This yaw makes the transom's far corner add about (beam/2)·sin6° ≈ 0.17 m (taking a beam of about 3.3 m) to the image x-extent. Corrected length ≈ 9.95–10.0 m.
- Direct check: L = 391 px × Z(≈90.0 m) / 3490 / cos6° ≈ 10.1 m before the beam correction. This agrees with the ratio route, as expected.

## Answer
10.0 m. Confidence: good, about ±3%. The main uncertainty is the beam/yaw correction (0–0.2 m) and whether the rudder or rail is counted (+0.1 m).
