# q3060 – width of the white car (internet_0042)

Prior: white car length = 4.572 m. Top-down drone view, the car drives down the image, so its length is vertical and its width horizontal in the image. Scale = 4.572 m / pixel length (one planar scale, as the annotators did). The time base doesn't matter for a size.

Measurements (frame 13, car fully visible, camera static; scripts measure.py, sweep.py, edges.py):
- Length, using a half-intensity threshold (140) along the car's centre column x=1045: rear at y=74, front at y=529, so **456 px**. The record gives 457 px for frames 11-17.
- Body width without mirrors, per row: 171-175 px. It is widest across the front wings (174-175 px at y=400-440) and 166-172 px elsewhere. The record's median is 172 px; the mask sweep at thresholds 80-140 gives 174-176 px across the front.
- Width including mirrors: 196 px. That would be 1.96 m, but the "wheel to wheel" convention leaves mirrors out.

Answer: 174 / 456 × 4.572 = **1.745 m**.
Second route: the record's 172 / 457 × 4.572 = 1.721 m. The threshold-mask ratios (frames 13 and 15) give 1.78-1.80 m, but they slightly undercount the length because the dark grille and plate drop out of the mask. The routes agree within about 3%.
Confidence: good, about ±3%.
