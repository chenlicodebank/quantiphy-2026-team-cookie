# q_650: width of the wooden bench (m)

The prior is the vacuum diameter, 0.438 m. The view is a top-down 2D render (static camera, 24 fps; question_fps is the same, so no re-timing).
The bench is the orange slatted bench at the top-left (x 295-582, y 173-289 px). Its long side runs along image x.
So **width = shorter horizontal extent = its image-y extent**.

## Measurements (scripts in this folder)
- `edges2.py`: I averaged the R-B profile over the slat columns and took the half-level crossings at the top and bottom edges.
  The top edge is at 173.2-173.3 px and the bottom edge at 287.8 px, so the width is **114.5-114.6 px**. This is the same in frames 0, 40 and 79.
  The gradient peaks are at 174 and 289, which gives about 115 px. `edges.py` gives the same result. It also gives the length: 295.2 to 581.6 = 286.4 px.
- Vacuum diameter: the scene track's circle fit gives 120.7-120.9 px near the image centre (frames 35-79). Near the dock, at the image edge, it grows to 122.9 px because of a slight perspective/side-wall effect.
  `vac_check.py` uses half-crossings along 12 diameters at frame 79 and gives a median of 120.3 px. I used **D = 120.6 px**.
- Scale: 0.438 / 120.6 = 3.632e-3 m/px.

## Result
- Without perspective correction: 114.6-115.0 px gives 0.416-0.418 m.
- Possible perspective correction: the vacuum's apparent size grows toward the image edge, which hints at a very distant but finite camera.
  If so, the bench top (higher than the vacuum's top) would be magnified about 1-2% more than the vacuum. A thin band at y 288-291 may be the bench's side face.
  With that correction the width would be about 0.409-0.412 m.
- Answer: **0.415 m**, between the two. Length reading for reference: 286.4 px gives about 1.04 m.

Second route: the edge-gradient peaks (115 px) and the half-level crossings (114.5 px) agree. The scale from the track fit (120.8) and from the half-crossings (120.3) differ by 0.4%.
Confidence: about ±3%.
