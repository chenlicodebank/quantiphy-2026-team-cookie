# q_2980 — displacement of the airplane, 0 s to 2.00 s

Time base: file 29.97 fps, question 30 fps. t=2.00 s gives frame 60 at either rate, so the choice makes no difference.

Measurement (measure.py, my own re-segmentation: gray<170 above y=270, largest component plus nearby pieces; the mask
overlay frames/mask0.png covers the whole jet and nothing else):
- Nose-to-tail length at f0 = 70 px (x 356-425). It grows to 80 px by f60 because the plane gets closer.
- bbox centre f0 (390.5, 192.0) -> f60 (653.5, 190.5): 263.0 px in the image. Mask centroid gives 261.5 px.
- The camera pans slowly: the background shifts -9.86 px in x by f60 (scene camera_affine). Measured against the
  background, the displacement is about 272.9 px.

Scale: one factor from the prior, 40 m / 70 px (length at the first frame) = 0.571 m/px.
- Image-only route: 263 px -> 150.3 m. Background-compensated route: 273 px -> 156.0 m.
- Answer 153 m, between the two routes (each is within about 2% of it).

Sensitivity: if the annotators measured the length on a later frame (75-80 px), the answer would be 131-146 m.
Confidence: moderate (about ±10%). The main uncertainty is which frame the annotators used for the prior's length.
