# q_3057: height of the ground-floor arches (cm)

Prior: middle duck size = 66 cm (taken as bill-to-tail length). Internet video, so I used the planar
single-scale convention (scale = 66 cm / duck pixel length). The question is static, so the time base does not matter.

## Duck length (duck.py, duck2.py, frames/duck24.png, frames/duck_multi.png)
- The scene mask gives 127-130 px, but it cuts off the pale, pointed tail tip (see frames/duck24.png: mask x1 = 2329,
  while the visible tail tip is at about 2342).
- Bill tip to tail tip, read on 5x crops with 10 px ticks: f5 133 (tail faint), f15 142, f24 144, f35 142,
  f50 138, so about **140 px**.
- Scale: 66 / 140 = 0.471 cm/px.

## Arch height (measure.py, prof.py, frames/apex2.png)
- Vertical intensity profiles through the centre of each ground-floor arch (midway between columns), frame 24.
- Apex = front-face intrados, where the lit stone face meets the shaded soffit: y ≈ 860-865. (In one arch the
  edge-finder caught a deeper edge at 899, which is the window frame behind, so I left it out.)
- Floor = the dark opening meeting the paving: y ≈ 1424-1435.
- Heights: 571, 569, 567, 564, 564, 565, 559 px, giving **565 px**.

## Answer
565 x 0.471 = **266 cm**.
Under the other reading of the duck size, the mask length of 130 px (no tail tip), the answer would be
565 x 66/130 = 287 cm. I chose the full visible bill-to-tail length.
Second check: seven separate arches agree to within ±1%, so the uncertainty comes mostly from the duck's pixel
length (±5 px, about ±4%). Confidence: moderate.
