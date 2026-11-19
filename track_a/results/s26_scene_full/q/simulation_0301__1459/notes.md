# q1459 — forklift speed at t = 2.0 s (frame 48 at question_fps 24 = file fps)

Prior: the forklift has a constant acceleration of 2 m/s². Frames 0 and 1 are identical, so it starts from rest.

## Onset (onset.py)
I fitted the image displacement of the forklift reference point from frame 0 as k·(t−t0)² over frames 0–15, 0–19 and 0–23.
The fit gives t0 = −0.08 to +0.06 frames, so the motion starts at t = 0 with s = a·t²/2. The frame-1 step would be only about 0.25 px,
which explains why frames 0 and 1 look identical. The bbox top-left corner gives the same result.

## Answer
Speed is the backward difference at frame 48: a·(48² − 47²)/2/24² × 24 = a·(2 − 1/48) = 2 × 1.97917 = **3.958 m/s**.
(Reading the speed as a·t instead would give 4.0, about 1% higher.)

## Second route (recon.py): 3D reconstruction from depth_info
- Pinhole camera with the principal point at the image centre. I chose the focal length so that the forklift's
  displacement between t = 1 and t = 2 (depths 16.795 and 19.098 m) equals the prior's a/2·(2² − 1²) = 3 m. This gives f ≈ 3330 px (HFOV 42°).
- Per-frame depth: d = A/scale + B, with the apparent-size scale calibrated to the two given depths. I back-projected
  the track to 3D positions.
- Fitting the net displacement over frames 8–59 gives a = 1.96 m/s² and t0 = −0.03 s, which agrees with the prior and with a start at t = 0.
- Speed from the 3D track at frame 48 (smoothed over frames 44–52): 3.86 m/s, within 2.5% of 3.958.
- Sanity check: the car moves 7.4–7.6 m between t = 1 and t = 2, so it is faster than the forklift, which matches the record (it overtakes the forklift).

Confidence: high (the prior fixes the answer once the start time is known, and the measured start is t ≈ 0).
