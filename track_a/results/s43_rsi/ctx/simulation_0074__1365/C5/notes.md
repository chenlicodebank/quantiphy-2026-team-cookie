Yellow taxi tracked over all 72 frames (scene track + independent orange-colour centroid track, agreeing to 2-3%). Focal length f=1930 px from three independent references (pedestrian 1.75 m tall -> 86 px at 37.9 m; taxi broadside length 322 px at 30.16 m with L~5.1 m; horizon/aspect-ratio consistency). Back-projecting each frame's centroid with the given depths (31.05 m at 0.58 s, 30.43 m at 1.58 s, linear) gives a 3D path of 9.41 m over 3.0 s, i.e. mean per-frame speed 3.20 m/s (net displacement/3 s = 3.09).

Final message:
**Answer: 3.2 m/s** (average speed of the yellow taxi over the 3.0 s clip).

Method summary:
- **Track**: the yellow taxi's centroid over all 72 frames (scene record, cross-checked with my own orange-colour centroid track — agreement 2–3 %).
- **Scale**: focal length f ≈ 1930 px, established from three independent references (pedestrian height 1.75 m → 86 px at 37.9 m; taxi broadside length 322 px at 30.16 m with L ≈ 5.1 m; horizon/aspect-ratio consistency), with sanity checks on the van (~4.2 m/s), cyclist (~6 m/s) and pedestrian (~1.05 m/s).
- **3D**: back-projected every frame using the given depths (31.05 m at 0.58 s → 30.43 m at 1.58 s, linear), giving a 9.41 m path over 3.0 s → 3.20 m/s (net displacement/time = 3.09 m/s; the taxi decelerates from ~240 to ~140 px/s during the clip).
