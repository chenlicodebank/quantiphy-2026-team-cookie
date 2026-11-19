# Q276: distance between the two cars at 1.0 s

- 2D top-down render, 24 fps (file fps = question_fps). t = 1.0 s → frame 24.
- Scale from the prior: the dark (black) car moves 27.02 ± 0.34 px/frame (mean of frames 4–44, from scene/tracks/dark_car.csv; the record says its speed is nearly constant).
  26.085 m/s / 24 = 1.0869 m/frame → 0.04023 m/px.
- Frame 24 centres: silver (735.15, 436.21), dark (736.22, 542.78) → 106.58 px.
  I drew both centres on frame 24 (frames/f24.png), and each one sits on the middle of its car body.
- Distance = 106.58 × 0.04023 = 4.29 m.
- Second route: a local scale from the dark car's step at frame 24 alone (26.94 px) gives 4.30 m, so the two routes agree within 0.3 %.
- Caveat: if the rig origins are not at the body centres, the result could shift by a few percent. Both cars point roughly the same way, so an offset that is the same on both cars mostly cancels.
- Confidence: high, about ±3 %.
- Scripts: measure.py, check.py.
