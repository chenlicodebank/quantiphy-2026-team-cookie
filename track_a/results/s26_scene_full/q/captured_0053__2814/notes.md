# q 2814 – displacement of the trashbin, 0.4 s -> 1.4 s (frames 10 -> 34 at question_fps 24 = file fps)

The "trashbin" is the blue box-shaped object (white/yellow patches) that the scene record calls "blue toy car";
it is the only moving object. Track: scene/tracks/blue_car.csv (mask centroid cx, cy), which looks right on the
contact sheet.

Method (measure.py, sens.py): f = 0.5959*1280 = 763 px, c = (640, 360). Bin at frame 10 is back-projected with
the given 2.73 m. Depth is given only at 0.4 s, so the floor plane comes from the cup (2.516), book/white card
(2.082) and basketball (2.925) back-projected with their depths. The bin is assumed to keep a constant height
above that plane, and the frame-34 ray is intersected with the plane through the bin's frame-10 point that is
parallel to the floor.
- Plane through the raw object centres: displacement 1.000 m, depth at frame 34 = 3.28 m, path 1.002 m.
- Plane corrected for the centre heights (cup 5 cm, book 1 cm, ball 12 cm): 1.037-1.046 m.
- Neighbouring windows (9->33, 11->35): 0.98-1.05 m.
Second route (apparent size): sqrt(area) ratio gives depth 3.23 m and 0.97 m; the bbox-width ratio gives 0.92 m.
The oblique view and the turning body make this route less reliable.
Prior check: per-frame 3D speeds are about 1.0 m/s, apart from the double steps at 11->12 and 35->36. That matches
the prior of 0.996 m/s at 0.4 s, and with nearly constant speed over 1 s it gives about 1.0 m.
Answer 1.01 m. Confidence: moderate to good. The floor-plane route spans 1.00-1.05 m and the size route 0.92-0.97 m,
so the answer is probably within about 5 % and very likely within 10 %.
