# Q2978 — average speed of the airplane (prior: length = 40 m)

File fps 29.9706, question_fps 30 (used for all timing; frame indices from the file). 2D internet clip, segmentation
version (white sky). The plane flies left->right, fully visible frames 0-89 (nose hits the right edge at f90).

## Measurements (measure.py -> my_track.json, speed.py)
- Segmentation: gray<170 above y=270, largest component plus nearby pieces. Same as the scene record (tail_x, nose_x,
  length) to within 0-1 px.
- Nose-to-tail length grows from 70 px (f0) to 78 (f45) and 88-89 (f85-89); mean 78.3 px over f0-89. The plane is
  coming closer, so the growth is real perspective, not a mask artefact.
- SAM 3 "airplane" masks: f0 box width 68.8 px (my 70, 1.7%), f45 77.4 (78), f85 87.9 (88). The centroids agree
  within 0.3 px. Overlay checked: the mask covers the whole aircraft. All differences are under 3%.
- Camera pans slowly: background shift -12.8 px in x by f85 (scene camera track). I used bg-compensated positions.
- Centroid speed f0-89 (bg-comp): 143.5 px/s (raw 138.9 px/s); mean of per-frame speeds = net (steady motion).

## Speed under each length-scale reading (bg-comp)
- Scale from the f0 length (70 px): 82.0 m/s. Tail tip: 80.4. Nose tip: 84.1.
- Scale from the mean length (78.3 px): 73.3 m/s.
- Perspective-invariant route (per-frame speed / per-frame length x 40 m): 73.1 m/s.
- Raw (not bg-compensated): 79.4 (f0 L) / 71.0 (mean L) / 70.7 (normalised).

## Answer
75 m/s. The answer leans toward the perspective-consistent value (~73, which is also plausible for a 737 on
approach) and hedges toward the f0-length convention (~82). Confidence: moderate. The main uncertainty is which
frame the annotators measured the length on (a spread of about ±8%).
