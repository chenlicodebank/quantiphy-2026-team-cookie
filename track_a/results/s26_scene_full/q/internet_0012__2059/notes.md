# Q2059: average velocity of the grey car (m/s). Prior: lane width = 3.66 m

**Object.** The grey car is the record's `dark_car`: a dark grey SUV in the middle lane of the right carriageway, moving up the image (−y). I checked frames 0 and 107 with crops. The car centre is at y≈3160 in frame 0 and y≈2177 in frame 107, which matches the track.

**Camera.** The drone shot looks straight down and the camera is static (see the record). I treated the scene as 2D and used one scale.

**Lane width in pixels** (`lanes.py`, frame 54). I took row profiles across the right carriageway at the dashed-line rows and found the half-max centroid of each lane line, then measured centre to centre:
- Middle lane, which is the car's lane: 95.2–97.9 px. Along the car's path (y 2100–3300, excluding rows where the truck covers the lines) it averages ≈96.4 px.
- The other lanes measure 98–100 px (inner) and 99–100 px (outer). Total width / 3 ≈ 97.5–99.
- Lens distortion makes the lanes about 2% wider near the top and bottom of the frame.

I used 96.4 px, the car's own lane along its path, so the scale is 3.66 / 96.4 = 0.03797 m/px.

**Displacement.** Centre track (template match): 982.8 px net, almost entirely along y. The independent edge-based centre gives 981.8 px. A linear fit over the unique (non-duplicate) frames gives 546.6 px/s at 59.35 fps, against 545.1 px/s from the net displacement over 107 frames. The steps between unique frames are steady at about 16.3 px.

**Time base.** The file runs at 59.35 fps and the question states 60 fps. That 1.1% difference can't be settled on physical grounds, since both give a plausible ≈75 km/h.
- At 59.35 fps: 545.1 px/s → 20.70 m/s.
- At 60 fps: 551.1 px/s → 20.92 m/s.

**Answer: 20.8 m/s.** This is the midpoint of the two time bases. It also sits inside the spread from the lane-width reading (96–98 px gives about ±1%).

**Second route.** The fit over unique frames and the edge-based centre agree with the net displacement within 0.3%. Confidence: high, about ±3%.
