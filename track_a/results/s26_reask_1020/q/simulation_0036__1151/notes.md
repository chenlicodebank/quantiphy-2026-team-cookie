# Q1151 – average speed of the boat (m/s)

Prior: the boat is 10 m long. Depth_info: boat 133.957 m at t=1 s and 131.256 m at t=2 s; person about 139.10 m.
The file and the question both run at 24 fps.

## Method (speed.py)
- Boat track: scene/tracks/boat.csv hull centre (hull_cx, hull_cy) for frames 0-71. I checked it on zoomed frames
  and it is the red hull. u runs from 609.5 to 395.5 px with a nearly constant pixel speed (quadratic fit, residual
  sd 0.5 px).
- Depth is taken as linear in time from the two given values: -2.70 m/s.
- For each candidate focal length f, I back-project ray(u,v) x depth to get 3D points. The answer is the mean of
  the per-frame speeds. Motion is uniform, so the mean speed equals the net speed.
- Speed vs f: 2600 -> 4.60, 2700 -> 4.49, 2800 -> 4.39, 2900 -> 4.30, 3000 -> 4.21, 3100 -> 4.13,
  3200 -> 4.06, 3300 -> 3.99 m/s.

## Focal length: two routes
1. Boat, 10 m long. The boat is assumed to move along its own axis (bow left), so its heading follows from the 3D
   velocity. The predicted hull extent from the bow tip to the near stern corner, L cos(th) + (B/2) sin(th) with
   beam B = 3 m, matches the observed 181 px at t=1 when f is about 2760, which gives a speed of 4.43 m/s.
   This route depends on the assumed beam and on whether the 10 m bounding box equals the visible hull. With the
   length term alone, f is about 3300.
2. Person, adult standing height. The person is 40 px tall on average and 43 px at most, at 139.1 m. A height of
   1.75-1.8 m gives f of about 3150-3350 and a speed of about 4.0-4.1 m/s. At f = 2760 the person would be over
   2.0 m tall, which is implausible.

The two routes differ by about 9 % in speed. I used f of about 2950, between them, which gives **4.25 m/s**. It is
within about 5 % of either route. Confidence is moderate, with an uncertainty of about ±6 %.
