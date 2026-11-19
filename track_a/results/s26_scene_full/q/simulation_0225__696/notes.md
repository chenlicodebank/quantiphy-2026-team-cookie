# q_696: length of the black cat (including tail)

Prior: the cat's speed is 1.041 m/s. The scene is 2D: a static camera, the cat walking along +x, fps 24 (the same as question_fps).

## Scale from the speed (measure.py)
- Linear fit of the mask centroid in scene/tracks/cat.csv: 5.455 px/frame. Fits of the bbox left and right edges: 5.40 and 5.41 px/frame.
- The mean of the per-frame |dx| is 5.49. This is inflated slightly by the gait wobble.
- Second route: best-overlap shift of the dark-fur mask over 12 frames gives 5.38 px/frame.
- Adopted value: 5.43 px/frame = 130.3 px/s, so the scale is 1.041 / 130.3 = 0.00799 m/px.

## Length in pixels
- On zoomed frames 12 and 36, the tail is raised and curves back only slightly. The horizontal extent runs from the hind paw or tail tip to the nose or chest.
- Whole-cat mask bbox width (from the record): median 105 px, range 103–113. At frame 12 the zoomed view reads about 583 to 688, which is about 105 px.
- Dark-fur-only width is about 100 px. It misses the white paws and chest, so it is a lower bound.
- Length: 105 px × 0.00799 = 0.84 m.

## Caveat
If the reference length came from a rest pose with the tail stretched straight back, it would be larger. That cannot be observed in the video, so I used the posed horizontal extent as seen. Confidence: moderate.
