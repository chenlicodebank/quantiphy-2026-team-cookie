# q1006 – length of the plane (simulation_0287)

The prior is the plane's speed, 22.16 m/s. The question frame rate is 25 fps; the file runs at 24 fps. Following the
paper's convention, the per-frame displacement is 22.16 / 25 = 0.8864 m. The video is a 2D scene with no depth_info.

- Pixel speed: the record's rigid frame-to-frame matching gives a steady leftward motion. It is 42.3–42.4 px/frame at
  the image centre (frames 25–45), where the jet is seen side-on, and 41.6–42.1 near the image edges because of mild
  perspective. Side-on value used: 42.35 px/frame.
  Scale = 0.8864 / 42.35 = 0.02093 m/px.
- Pixel length: `measure.py` builds a background-difference mask and takes the x-extent of the jet.
  - Side-on frames 28–34 give 661–681 px. The mask misses the faint nose tip and tail cone by a few px.
  - Reading the zoomed frame 30 by eye (frames/f30.png) gives nose about x 1115 and tail cone about x 1795, so about 680 px.
  - The record gives 676–685 px at frames 28–33.
  - Value used: 680 ± 6 px.
- Length = 680 × 0.02093 = **14.23 m**.
- Second route: at frames 31–34 the length is 680 px, about 16.05 frames of travel. 16.05 × 0.8864 = 14.2 m. This
  agrees with the main result.
- Plausibility check: a Harrier-type jet is about 14 m long, so the result is consistent.
- If 24 fps were used instead, the answer would be 13.7 m. 25 fps is used, as the question states.
- Confidence: about ±3 %.
