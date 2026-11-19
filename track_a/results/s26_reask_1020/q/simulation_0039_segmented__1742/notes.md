# q_1742: eagle wingspan (m)

File is 25 fps (75 frames); question_fps = 24 (the record's duplicate frames 1/26/51 match a 24 fps render resampled to 25).

## Is the eagle visible?
- `find_blobs.py`: connected components of non-white pixels in every frame. Only three objects ever appear: the static
  brown "rock" at the top (bbox ~[683,0]-[1450,313]), the walking person (~25x60 px) and the boat (~480x332 px).
- `top_diff.py`: the brown blob is static for all 75 frames (row widths constant within compression noise, no
  wing beats or growth). The eagle's given distance falls from 179.27 to 177.10 m in 1 s, and an animated eagle would
  change shape, so the blob is not the eagle. It is also heavily defocused, so it is not at the ~178 m sharp-focus depth.
- `edge_strip.py`: frame 0 alone shows a few tiny dark/white specks (5-10 px) on the top image edge at x~1145, 1195
  and 1340, which are gone from frame 1 on. They may be the last bits of the eagle leaving through the top edge. They
  are too small and partial to measure a wingspan from.
- Conclusion: the eagle is outside the field of view during the clip, so its wingspan cannot be measured.

## Scale check (to confirm the scene is at real-world scale)
- Boat: about 8.4 px per render frame, i.e. 201.6 px/s at 24 fps. The prior is 4 m/s, with a radial component of
  about 0.79 m/s from depth_info, which leaves about 3.92 m/s across the view. At about 177.6 m this gives
  f ~ 201.6 / 3.92 x 177.6 ~ 9100 px (horizontal field of view ~9.6 deg).
- With that focal length the boat comes out about 10 m long (512 px), a realistic fishing boat. The person (183 m,
  60 px foreshortened from a steep top-down view, 87 px if upright) is consistent with ~1.75 m.
  So the scene is at real-world scale.
- At this scale (~51 px/m at 179 m), the eagle's whole frame-0 neighbourhood near the top edge is only a few px.

## Answer
The eagle is never measurable, so I took the wingspan from the size of a real eagle (bald / golden / sea eagle:
1.8-2.3 m, typical ~2.0 m). The scene's real-world scale supports a realistic eagle model.
Answer: **2.0 m**. Confidence is low to moderate: this is a prior from typical size, not a measurement. There is no
second independent route, because the eagle never appears.
