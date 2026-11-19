# q_1789 — average speed of the shark (m/s)

Prior: boat length = 10 m. 2D video; 24 fps (file fps equals question_fps). Question: average shark speed.

## Method (measure.py -> own_extents.csv)
- I segmented the non-white pixels, split the image at y = 740 into the boat (above) and the shark (below), and took the x-extents in every frame.
- Boat length, stern to bow, frames 0–47: **857 px**, which gives a scale of 10/857 = 0.011669 m/px.
- Shark length is 278 px. Its motion is horizontal and uniform:
  - snout fit (frames 1–62): −10.765 px/frame
  - tail fit (frames 1–72): −10.743 px/frame
  - Both fits have max residuals of about 2 px.
- The shark is nearly at rest between frames 0 and 1 (the tail moves 1 px). From frame 2 onward it moves about 10.75 px/frame.

## SAM 3 check
- **Shark**: box centres at f10 = 711.9 and f40 = 388.8, which gives 10.77 px/frame. That is within 0.2% of my fits. SAM gives a horizontal length of 279–280 px against my 278.
- **Boat**: at f10 SAM gives horiz 854 px against my 857 (0.4%). The overlay covers the full hull including the rudder.
- No difference above 3%.

## Result
- Uniform speed: 10.75 px/frame × 24 = 258 px/s, × 0.011669 = **3.01 m/s**.
- Mean of the per-frame backward-difference speeds over frames 1–72, including the near-zero frame-1 step: 10.58 px/frame, which gives 2.96 m/s.
- Answer: **3.0 m/s**. Both readings are within 1.5% of it.

Confidence: high (about ±2%).
