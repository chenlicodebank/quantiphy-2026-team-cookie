# q2633 – basketball displacement 0.5 s → 0.6 s (cm)

- question_fps = file fps = 24: t=0.5 → frame 12, t=0.6 → frame 14 (round(14.4)).
- Basketball centres (scene/tracks/basketball.csv, RANSAC circle on bg-bordered edge; checked visually on zoomed
  frames 12 and 14): f12 (771.4, 552.2) diam 75.4 px; f14 (737.3, 534.4) diam 74.1 px. Ball is clear of the foot
  at both frames. The 11→12 dropped-frame jump does not affect 12→14 (steps 19.5, 19.1 px, normal).
- Lab card: f = 0.5959×1280 = 762.8 px, principal point (640, 360). Depth at f14 = 2.270 m (depth_info).
  Depth at f12 not given: scaled by apparent diameter ratio → 2.231 m (linear diameter trend → 2.207 m; constant → 2.270 m).
- Back-projected 3D displacement: ratio 11.13 cm, linear-trend 11.64 cm, constant depth 11.46 cm.
  Image-plane-only check: 38.5 px × 2.25 m / 763 = 11.35 cm.
- Note: 23.2 cm prior with 74.1 px implies Z ≈ 2.39 m vs given 2.27 m (circle fit / keyed edge ~5% large); depth_info used as given.
- Answer: 11.3 cm. Confidence: moderate-high (±5%), main uncertainty is depth change between the frames.
