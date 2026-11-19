# q395 – width of the road the bike crossed through (m)

Scene: top-down (nadir) Blender render, 2D treatment, static camera, fps 24 (question_fps 24 too, so no re-timing).
The bike rides along +x in the horizontal street, enters the intersection at x≈1181 (f≈29) and by the end crosses the whole
**vertical (cross) road** (pelvis passes its far kerb x≈1728 near f≈72). That vertical road is the one it "crossed through".

## Scale (from the prior: bike speed 5.52 m/s)
- Cyclist track (scene/tracks/cyclist.csv, checked): mean per-frame displacement 14.44 px; net 14.42 px/frame; linear fit 14.42.
  (Mask-centroid fit gives 14.22; mask edges drift, so it is less reliable.)
- 14.44 px/frame x 24 = 346.6 px/s -> 0.01593 m/px at rider (pelvis) height.
- Perspective: the car's roof-vs-bumper parallax (~16 px over ~1425 px of travel for ~1 m height difference) gives a camera height of
  ~85 m, so the road plane scale is ~1.2 % larger than at the pelvis (~1 m up): ~0.0161 m/px on the ground.
- Check: police car 289 px -> 4.63-4.66 m (a realistic car length).

## Road width (prof.py, intensity profiles at rows y=230, 300, 900, 1000)
- Vertical road asphalt between kerb faces: left x≈1188, right x≈1727-1728 -> ~540 px.
- Its white edge lines are at centres 1205.5/1707 (top) and 1198/1713 (bottom) -> 502-515 px.
- For reference, the horizontal road the bike rides along is 343 -> 751 = ~408 px kerb-to-kerb (≈6.5-6.6 m).

## Answer
540 px x 0.0160 m/px ≈ **8.65 m** (8.60 without perspective correction, 8.70 with it).
Alternative readings: between the edge lines ≈ 8.0-8.2 m; if the bike's own street was meant, ≈ 6.5-6.6 m.
Confidence: moderate. The scale is good to about 2 %; the main uncertainty is which road and which edges the question means.
