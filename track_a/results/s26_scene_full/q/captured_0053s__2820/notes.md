# q_2820 – distance white cup ↔ basketball (m)

- Lab clip, 24 fps (file and question fps agree), 1280x720, f = 0.5959*1280 = 762.8 px, c = (640, 360).
- Both objects are static (scene record; checked on frame 10 = t 0.4 s crop, frames/f.png).
  Centres from scene/static_objects.json, verified against the frame grid:
  cup (564.2, 423.8) px, basketball (985.8, 369.8) px.
- Depths from depth_info: cup 2.516 m, basketball 2.925 m.
- Method card back-projection P = ((u-cx)/f, (v-cy)/f, 1) * depth:
  distance = **1.637 m** (answer).
- Alternative reading (depth as Euclidean ray length, normalised ray): 1.476 m. The method card's
  formula is followed for the answer.
- Sensitivity: ±3 px on the centres changes the result by ~±0.018 m (~1 %).
- Sanity: basketball 65.5 px at 2.925 m → 0.25 m diameter, plausible.
- Confidence: moderate-high; main uncertainty is the depth convention (~10 %).
