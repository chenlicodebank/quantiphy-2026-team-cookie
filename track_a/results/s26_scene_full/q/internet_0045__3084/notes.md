# q3084: diameter of the rolling cylinder (cm)

Prior: velocity = 107.3 cm/s. This is a 2D internet clip, so I used one planar scale (the annotators' convention).
The time base is 30 fps: the file is 30.013 and question_fps is 30, which differ by a negligible amount.

**Pixel speed** (`speed.py`, using the scene-record centroid track with camera drift removed, frames 4-30, all fully visible):
- Mean per-frame speed: 1839 px/s.
- Net displacement / time: 1835 px/s.
- Leading edge (bbox_x0): 1784 px/s.
- The image speed rises from about 1700-1900 px/s (frames 4-8) to about 2000-2100 px/s (frames 23-28) because the
  cylinder rolls toward the camera.

Scale = 107.3 / 1835 = 0.0585 cm/px.

**Pixel diameter** (`diam.py` column profiles, plus zoomed gridded crops):
- Frame 24, end face seen nearly end-on: the face circle runs from y ≈ 735 to y ≈ 918, so its vertical extent is
  183 px. Its horizontal extent is about 185 px, including motion blur.
- Frames 6-8, side view: the width across the axis is about 175-186 px (vertical extents of 182-190 px at a 20°
  axis tilt; minAreaRect gives 183-187).
- Taken together, the diameter is about 183 px.

Diameter = 183 × 0.0585 = **10.7 cm**. That fits a paper-towel roll, which has a hole in its core.

**Second route:** match the diameter to the local speed at the same frames.
- Frame 6: 180 px against about 1840 px/s gives 10.5 cm.
- Frame 24: 183 px against about 1990 px/s gives 9.9 cm.

These local estimates are 0.2-0.8 cm lower because perspective changes the image speed during the clip. I answered
with the whole-clip average-speed scale, following the annotators' single-scale convention.

Confidence: moderate (about ±7%).
