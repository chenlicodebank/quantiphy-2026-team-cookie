# Q2058: length of the grey car (m); prior lane width = 3.66 m

- The grey car is `dark_car` in scene/ (the dark grey SUV going up the right carriageway, x≈1173–1229). The camera is a static top-down drone shot, so this is a 2D problem with one scale taken from the lane width.
- Lane width (lanes.py, frame 54): I found the centre of each dash line row by row and took the centre-to-centre spacing of adjacent lane lines in both carriageways. It is 95.6–96.0 px near the image centre (y≈1800–2200) and 96.4–96.5 px at y≈2600, where the car is mid-track. Near the top and bottom of the frame it rises to 97.4–97.7 px, from mild lens distortion.
- Car length, bumper to bumper along the road: the record's per-frame edge lengths are 131 px at frame 0 (y≈3160), 127 px at frame 54 (y≈2656) and 123 px at frame 107 (y≈2177). I checked frame 54 by eye on a zoomed crop (front ≈2591, rear ≈2718, so ≈127 px). My own threshold-profile script (carlen.py) did not work: the dark rear windscreen is close to road colour, so the profile breaks up. It was not used.
- Scale, from the same image region as the car: 127 px / 96.4 px × 3.66 m = **4.82 m**.
- Second-route check, the same ratio at the ends of the track: frame 0 gives 131/97.3 × 3.66 = 4.93 m, and frame 107 gives 123/95.8 × 3.66 = 4.70 m. With the global lane width of 96 px and the mid length of 127 px, it is 4.84 m. All are within about 2.5% of the answer.
- Time base doesn't matter for a size question.
- Confidence: about ±3%. A 4.8 m SUV is plausible.
