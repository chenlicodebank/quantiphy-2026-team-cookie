# q_1789: average speed of the shark (m/s)

- This is a 2D video: one plane, static camera, white background, 24 fps (the file and the question agree).
- **Scale from the prior.** The boat measures 855–859 px stern to bow over frames 0–47 (measure.py), so I take 857 px = 10 m, giving 0.011669 m/px.
- **Shark motion.** The shark moves left at a uniform speed from frame 1 to frame 72.
  - The tail-edge fit gives −10.74 px/frame and the snout-edge fit gives −10.77 px/frame.
  - The mean per-frame tail displacement over frames 2–72 is 10.72 px.
  - Frames 0 and 1 are identical: the shark is at rest there.
- **Speed.**
  - Constant-motion speed: 10.75 px/frame × 24 = 258 px/s, which is 3.01 m/s.
  - If the zero speed at frame 1 is counted in the mean of the per-frame speeds: 10.75 × 71/72 × 24 × 10/857 = 2.97 m/s.
- **Answer: 2.99 m/s**, the midpoint of these two conventions, which differ by about 1.4%.
- **Second route.** Edge fits on two independent points (snout and tail) agree within 0.2%. The scene record agrees too: 258 px/s, boat 857 px.
- **Confidence:** high (about ±2%).
