# Q660: acceleration of the vacuum cleaner at t = 0.5 s

- The file and the question both run at 24 fps, so t = 0.5 s is frame 12. This is a 2D top-down scene and the camera is static.
- Prior: the vacuum's diameter is 0.438 m. The vacuum is the white robot disc that moves left from the dock.

## Measurements
- `measure.py` runs my own Otsu threshold on the disc for frames 9-29. Frames 5-8 are not usable because the mask merges
  with the dock. My centroids agree with the scene circle-fit track to within 0.3 px.
- Disc size at frame 12:
  - Vertical extent: 120-121 px. This direction is roughly perpendicular to the frame-centre offset, so it gives the top-disc diameter.
  - Horizontal extent: 124 px, because the side wall shows (the disc is 640 px right of the frame centre).
  - Area-equivalent diameter: 122.25 px. The scene circle fit gives 122.8 px.
  - The side-wall shift is about 3.5 px over a 640 px offset, so h/Z is about 0.5%. The difference between the top plane and
    the origin plane is therefore negligible.
  - I used D = 121 px, so the scale is 0.438/121 = 3.62e-3 m/px.
- SAM 3 check ("white round disc", frame 12): the mask is 134 x 134 px with its centre at (1599.4, 409.2). That is about 9% larger
  than my mask. On a 4x zoomed crop (frames/f12.png) the disc runs from about x 1538 to 1661 and y 347 to 470, so it is about 123 px.
  The SAM outline includes a dark halo and shadow ring. My threshold mask and the circle fit are right, and the SAM extents were not used.
  The SAM centre x agrees with mine to 0.2 px; its y is 1.4 px lower because of the shadow.

## Acceleration (`accel.py`)
- Per-frame speed is |dp| per frame. The raw backward difference at frame 12 is 1.175 px/f² on the scene track and 1.028 px/f²
  on my track. Both are noisy at the ±0.15 level.
- Local polynomial fits of speed around frame 12 (windows ±2 to ±5) give 0.99-1.04 px/f² on both tracks.
- Second route: a cubic fit of arc length against frame gives 0.99-1.01 px/f².
- Adopted value: 1.025 px/f². 1.025 × 576 × 3.62e-3 = 2.14 m/s².
- If D = 122.25 px is used instead, the answer is 2.12 m/s². The routes span 2.04-2.15.

## Confidence
Medium-high, about ±4%.
