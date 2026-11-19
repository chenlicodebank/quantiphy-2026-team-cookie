# q_594: dog length including tail (m)

- The scene record calls the lower animal a "tabby_cat", but frames show it is a brindle **dog** (head drawn as a flat
  light-brown patch). That is the asked object. Top-down 2D view, static camera, 24 fps (file = question fps).
- Scale from prior: the black cat walks steadily at 10.96 px/frame (linear fits: bbox_x1 10.98, body_cx 10.94, cx 10.96)
  = 263.1 px/s, so 0.94 / 263.1 = 0.003573 m/px.
- Dog x-extent (motion axis = length), including head patch and tail. The record's tracks give 254–338 px depending on
  tail swing. My own HSV-saturation background-difference check (check_dog.py) gives 274 px at frame 0
  (tail curled sideways) and 337 px at frame 6 (tail straight back), matching the record.
  The median over frames is ~285 px.
- Readings: frame 0 = 0.98 m; median = 1.02 m; tail straight out (max) = 1.20 m.
  I answer ~300 px, which gives **1.07 m**. This is a compromise between the rest/typical bbox and the straight-tail length.
- Sanity check: black cat 191 px = 0.68 m, so the dog is ~1.5x the cat's length. That is plausible.
- Confidence: moderate. The scale is good to ~2%; the main uncertainty is which tail pose the reference used (±12%).
