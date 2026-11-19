Bike vertical extent (handlebar top y=424 to front-wheel ground contact y=557 at frame 33) = 133 px; SAM3 mask gives 134.7 px. Scale from the 1.8 m pedestrian (197.5 px at 11.93 m) with a pinhole camera calibrated on his head/feet gives f~1270 and H=0.91-0.96 m; the bike's own wheel (H/wheel=1.40, 0.68 m wheel -> 0.95 m) and cyclist proportion (0.586 x ~1.62 m seated height -> 0.95 m) independently agree. The raw depth_info route (bike at 16.49 m) would give 1.69 m, implausible for a bicycle and inconsistent with the image (bike's ground contact is visibly closer than the pedestrian's feet), so it was rejected.

Final message:
I measured the bicycle's vertical extent (handlebar top to wheel/ground contact) at 133–135 px and cross-checked the metric scale by four independent routes:

1. **Depth_info direct route** → 1.69 m, which is impossible for a bicycle (handlebar 1.7 m above ground) and geometrically inconsistent with the image (the bike's ground contact sits well below the pedestrian's feet, i.e. it is visibly *closer*, while depth_info puts it farther). Rejected per the method card's plausibility check.
2. **Camera calibrated on the 1.8 m pedestrian** → 0.91–1.11 m depending on the horizon estimate.
3. **Bike's own wheel as scale** (H/wheel = 1.40, 700c wheel 0.68 m) → 0.95 m.
4. **Cyclist proportion** (bike/cyclist total = 0.586, seated cyclist ~1.62 m) → 0.95 m.

Routes 2–4 converge on ~0.96 m, which I reported. Notes with the full method, the depth_info inconsistency, and the second-route checks are in `notes.md`.
