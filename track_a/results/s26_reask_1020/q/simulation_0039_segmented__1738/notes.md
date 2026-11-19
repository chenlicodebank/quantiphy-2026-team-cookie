# q1738: height of the boat (m). Prior: boat speed = 4 m/s

The file is 25 fps; the question uses 24 fps. Duplicate frames 1, 26 and 51 confirm a 24 fps render, so I used render steps (non-duplicate frames) at 24 fps.

## Scale / camera
- Boat track (scene ref point, template-matched): 8.398 px per render step, which is 201.6 px/s (`speed.py`). Positions at t=1 s and t=2 s are (553.2,1356.6) and (359.1,1302.1).
- `focal.py`: I back-projected both positions with the given depths (177.2077 and 177.9993 m) and required |P2-P1| = 4 m. This gives f = 9105 px (HFOV 9.6 deg). The velocity in camera coordinates is (-3.80,-1.01,0.73) m/s, so the boat heading points slightly away from the camera.
- Check: the hatch's long edge in the image has slope 0.281. The predicted image direction of the velocity is 0.280.
- Camera tilt: the boat's cross-direction is horizontal and perpendicular to the velocity. Edges along it (teal hatch sides -2.79 and -2.94, wheelhouse roof aft edge -2.85) give a camera depression of about 62 deg (`tilt2.py`, `height_f0.py`). An image-only orthographic solve (`ortho3.py`) gives 63.5 deg.
- The wheelhouse corner and window edges, the mast and the exhaust pipe all lean right of the predicted vertical. I put this down to wheelhouse tumblehome and an aft-raked mast and pipe, so I did not use them for the tilt. Using them would give about 55 deg.
- Person check at 183 m (49.8 px/m): at 62 deg, a 1.75 m person would project to roughly 54-80 px, and the observed mask length is 54-71 px. At 45 deg the shortest length would be about 70 px, which is too long, so the steep view is supported.
- At 62 deg, one metre of vertical height projects to 21.7 px at the boat; one metre across the boat is 47.9 px and one metre along it is 50.75 px.

## Height
- I intersected rays with planes at a known offset from the centreline plane (`height_f0.py`, `silscan.py`). Heights are relative to the mast base on the wheelhouse roof; the mast base was checked to sit at the roof's mid-width.
- Mast tip (mask top, 703,1198 at frame 0): +6.54 m.
- Deck beam is about 2.0-2.3 m, from the gunwale and railing sections and the 1.4 m roof width. The lowest hull outline (bilge on the near side, about 0.9-1.1 m off the centreline) has its minimum amidships at about -5.3 m (from -4.9 to -5.4 m).
- The keel is hidden below the bilge outline; I added about 0.3 m for it.
- The answer is the vertical bounding-box extent including the mast: 6.54 + 5.3 + 0.3 ≈ **12.0 m**.
- Other boat dimensions from the same model: length about 10 m, beam about 2.2 m.

## Sensitivity / confidence
- Depression 58.7 deg gives H ≈ 10.5-11.0 m; 64.9 deg gives H ≈ 13.2-14.0 m. The bilge's offset from the centreline adds ±0.5 m.
- On screen the vertical and cross-boat directions are nearly parallel, so the hull bottom is the weakest part of the measurement.
- No eagle is visible in the clip, so its depth_info went unused.
- Confidence: moderate (roughly ±15%).
