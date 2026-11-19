# Q1277: pedestrian's average speed over the whole clip (m/s)

The file and question_fps are both 24 fps. t=0.58 s is frame 14 and t=1.58 s is frame 38. The camera is static.
The white car is the van (depths 45.52 / 43.95 m). The yellow car is the taxi.

## Focal length (scripts measure.py and measure2.py)
- Each object is back-projected with its given depths at f14 and f38 (principal point at 1080, 540). This defines a straight 3D path line, and every frame's ray is intersected with that line.
- Van, prior a = 4 m/s²:
  - A free quadratic fit of the van's path coordinate gives a = 4 at f = 2095–2209 px, depending on the frame window. The fitted start is at frame −2 to 0, which matches the record's "starts from rest at f0–1".
  - With the start fixed at frame 0 or 1, a = 4 at f ≈ 2200–2400.
  - Using the kinematic distance from f14 to f38 (4.17–4.33 m) instead gives f ≈ 2300–2400.
- Size checks with real-world objects:
  - Taxi side length 286 px at about 40.4 m, taken as a Crown Victoria of 5.38 m: f ≈ 2150.
  - Van, 290 px at 45.5 m, taken as about 5.8 m long: f ≈ 2275.
  - Pedestrian, 125 px at 33.4 m, taken as about 1.75 m tall: f ≈ 2390.
- Chosen value: f = 2200 px, with a plausible range of 2100–2400.

## Pedestrian (ped.py)
- Track: scene/tracks/pedestrian.csv. I checked it on frames: he is the man in the white T-shirt on the left pavement.
- The depths 33.43 m and 32.42 m at f14 and f38 set a straight walking line. Each frame's ray is intersected with that line.
- Results at f = 2200, using the hip or mask-centroid point:
  - Net displacement from f0 to f71, divided by 71/24 s: 1.18 m/s.
  - Linear-fit slope: 1.18 m/s.
  - Raw sum of per-frame steps: 1.18–1.20 m/s.
  - Bbox-centre point: 1.18–1.20 m/s.
- Second route: the 3D distance between the two given-depth points (f14 to f38, 1 s apart) is 1.21 m, i.e. 1.21 m/s.
- Sensitivity to the focal length: 1.16 m/s at f = 2400 and 1.20 m/s at f = 2100.

## Answer
1.19 m/s. Confidence is fairly good, about ±4%.
