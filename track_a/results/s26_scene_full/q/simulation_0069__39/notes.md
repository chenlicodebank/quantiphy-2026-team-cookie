# Q39: width of the white car (m). Prior: the car's acceleration is 4 m/s^2

Top-down 2D Blender clip, static camera, 24 fps (the file and the question agree, so no re-timing). One m/px scale comes from the prior.

## Pixel acceleration (scripts: fit_record.py, measure.py)
- Record track (`cy`/front edge): quadratic fit over frames 3-71 gives a = 162.9 px/s^2 (rms 0.34 px). Fits over frames 3-40 and 40-71
  give 162.5 and 161.8.
- My own sub-pixel front-edge track (background-median difference with a half-level crossing): frames 3-40 give a = 163.5 px/s^2,
  rms 0.16 px. Mean of the one-frame speed differences over frames 5-71 is 162.8 px/s^2. Later frames are noisier because the car
  is over the crossroad's textures.
- I used a = 163 px/s^2, so the scale is 4 / 163 = 0.02454 m/px.

## Width (width.py, width2.py)
- Frame 0, car difference against frame 71 (the car has gone from that area by then). Per-row extent of the body is 84-86 px
  (median 85). The outer extent is x 788-874 = 87 px, which matches the record's 87 px. The sub-pixel half-level edges of the mean
  profile give 84.3 px.
- A small protrusion on the left at rows 868-871, probably a mirror, makes it 92 px. It shows on one side only.
- Width used: 87 px, which gives 87 x 0.02454 = 2.13 m.
- Other readings: body 85 px gives 2.09 m; including the mirror, 92 px gives 2.26 m.
- Sanity check: length 234 px gives 5.7 m and width 2.1 m, which fits a van/MPV.

## Confidence
Moderate to high. The scale has about 1% error. The main uncertainty is whether mirrors count in the world bounding box (about ±5%).
