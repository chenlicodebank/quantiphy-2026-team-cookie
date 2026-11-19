# q_304 – width (wingspan) of the white airplane

2D top-down render. The video and the question are both 24 fps. The "car" in the prior is the tug towing the plane.

- **Tug speed.** Measured with my own template matching in `measure.py`. The tug moves up at a constant speed from frame 2 on:
  - frame 2 → 71: 362.1 px over 69 frames = 5.248 px/frame;
  - frame 1 → 71 gives the same, 5.246 px/frame;
  - that is 125.95 px/s.

  This agrees with the scene record (5.247 px/frame).
- **Scale.** 11.155 m/s ÷ 125.95 px/s = 0.08857 m/px.
- **Wingspan at frame 71.** Wingtip brightness profiles put the half-maximum edges at x ≈ 281 and x ≈ 667, giving ≈386 px. A bright-pixel threshold of 200 gives 385 px, and the scene record has 386.5 px.
- **Width.** 386 px × 0.08857 m/px = **34.2 m**.
- **Check.** The fuselage length is 423 px, which is 37.5 m at this scale. The A320 the plane looks like is 37.57 m long with a 34.1 m wingspan, so the scale is realistic.

**Confidence:** high, about ±1 %.
