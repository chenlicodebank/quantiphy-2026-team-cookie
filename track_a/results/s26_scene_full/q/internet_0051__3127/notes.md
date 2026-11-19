# q3127 — height of the centre tree (internet_0051)

Prior: the scooter rider's average speed is 2.07 m/s. I used the internet convention: one planar scale = prior / pixel speed. fps is 30, the same as question_fps.

- Rider pixel speed (scene track, checked with tree_top.py): mean per-frame speed is 17.43 px/frame in raw image
  coordinates and 17.71 px/frame with the pan removed. The net displacement over 49 frames gives 17.33 and 17.61.
  The camera pan is small (+14 px over the clip). I used ~17.45 px/frame = 523.5 px/s, so the scale is 2.07/523.5 = 0.00395 m/px.
- Tree pixel height at frame 0: the top of the crown is at y ≈ 75–78. tree_top.py finds the first non-sky pixels at
  y = 78 in frame 0 and 81 in frame 25, and a 3x zoom shows twigs at about y = 72. The trunks meet the mulch at
  y ≈ 778–785 on a 3x zoom, so I took 782. Height ≈ 704 px (±6).
- Height = 704 × 0.00395 ≈ 2.78 m. With the pan-removed speed (17.7 px/frame) it would be 2.74 m.
- Check: the rider's height (~300 px) converts to 1.19 m on the same scale. That is small for a real person: the prior
  speed sets a small scale, and the tree stands farther back than the rider. The reference answer uses the same
  single-scale planar convention, so I kept it. Confidence is moderate, about ±5%, from the uncertainty in the pixel speed and the treetop.
