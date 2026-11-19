# q2117: pool width (m), prior: swimmer height = 1.8 m

Internet video shot from a drone looking almost straight down. The camera is essentially static (drift ~1 %). One planar scale comes from the prior.

- Swimmer height in frame 0 (body flat at the surface, 3x zoom, 20 px grid): toes x≈578 to top of head x≈783, so **205 px** (scene record: 205). Including the outstretched arms it would be 256 px, but "height" means feet to head.
  Scale = 1.8 / 205 = 0.00878 m/px.
- Pool width is the shorter extent of the main basin, which runs along y. I read the water/coping edges on 4x zooms at x≈1000–1200: top ≈475–478 (the mask in measure.py gives 477–478), bottom ≈1020–1022. That makes the water width **≈545 px**. The scene record says 542 px.
- Width = 545 × 0.00878 = **4.79 m**. Sanity check: the length is 1159 px, which gives 10.2 m, so the pool is about 10 × 4.8 m, which is plausible.
- Other readings: outer coping to coping (617 px) gives 5.42 m. Using the swimmer length with arms (256 px) gives 3.83 m. I answer with the water width and the feet-to-head height.
- Confidence: moderate. The main uncertainty is the pixel length the annotator used for the swimmer (±5 %).
