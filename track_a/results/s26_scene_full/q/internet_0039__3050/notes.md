# q3050 lane rope spacing
Prior: swimmer height 1.68 m. 2D overhead view, static camera, one scale factor (internet convention).
- Swimmer pixel length (cap top to feet), from scene track head_to_feet: median 1041 px (985-1082); I checked it by eye on frame 51 (head top ~1085, feet ~2120, so ~1035 px).
- Lane width between rope centre lines (static_measure): frame 0 is 1322/1364/1405 px at y=0/1920/3840, frame 71 is 1331/1400/1468. The ropes bow, so over the swimmer's y range I take ~1370 px.
- Scale 1.68/1040 = 1.615e-3 m/px, so the distance is 1370 x 1.615e-3 = 2.21 m.
- Check: using 1364 px gives 2.20 m. The stroke-phase range of body length gives 2.12-2.33 m. The fps is irrelevant (static sizes).
Confidence: moderate (~5%); the main uncertainty is where the submerged feet end.
