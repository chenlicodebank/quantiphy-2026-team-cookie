# Q65: width of the green car (m). Prior: white car length = 6 m

The clip is a 2D top-down render at 24 fps, and question_fps is also 24, so no re-timing is involved. The camera is static. One metres-per-pixel scale applies to the whole ground plane: the van's length stays at 234–237 px everywhere along the road.

- The "white car" is the white van/minibus on the vertical road. I measured its length with `measure.py` using a road-difference mask, 3×3 open, largest component:
  - thr 25: 234 px (f36), 237 px (f60), 237 px (f71).
  - thr 35: 234, 235 and 237 px.
  - The record gives 236 px at f0 and f71.
  - **Length = 236 px**, so the scale is 6/236 = 0.02542 m/px.
- The green car is parked horizontally in the lower lane of the horizontal road. Its width is the vertical pixel extent.
  - Mask: thr 22 gives a median column extent of 75 px; thr 25 gives 74–75 px (bbox y 563–637). thr 12/18 include the shadow halo (89/78 px).
  - Green paint only: 70 px. The car outline on a 4× zoomed crop (frames/green.png) reads about y 565–637, i.e. ~72 px.
  - The record has 73 px.
  - **Width = 73 ± 2 px.**
- Width = 73 × 6/236 = **1.86 m**. Range: 1.78 m (70 px) to 1.91 m (75 px). Answer: 1.85.
- Check: the green car's length is ~200 px, which is 5.1 m. That gives a width/length ratio of 0.36, which fits a sedan. The tan car's width (82 px, 2.1 m) is also consistent.
- Confidence: good, within about ±4%.
