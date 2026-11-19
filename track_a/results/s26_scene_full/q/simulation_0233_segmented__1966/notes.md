# Q1966 — black cat length incl. tail (m)

Prior: cat speed 0.714 m/s. 2D clip, top-down view (cat seen from above, walks right along y≈531), static camera, 24 fps (file fps = question fps).

## Scale (from the prior)
- `measure.py`: dark low-saturation mask per frame; head template (front 90 px, frame 30) tracked by matchTemplate.
- Head speed: linear fit frames 5-49 = 13.37 px/frame (all frames 13.29); scene record centroid fit (frames 22-49) 13.36;
  nose x1 fit frames 22-49 13.32. Use 13.36 px/frame = 320.6 px/s.
- Scale = 0.714 / 320.6 = 0.002227 m/px.

## Length
- Horizontal mask extent (nose tip to tail tip) on frames 22-49 (fully in view): 322-347 px, median 335.5, mean 335.9
  (varies with tail pose/gait). Scene record PCA length median 336 — agrees.
- Length = 336 × 0.002227 = 0.748 m. (Max extent 347 px → 0.773 m; min 322 → 0.717 m.)

## Second route
- Using nose-x1 speed (13.32 px/f) instead: 0.750 m. Net head displacement 0-49 (12.9 px/f, early frames partly cut) would give 0.775 m, considered less reliable.

Confidence: moderate-high; main uncertainty is tail pose (±4%).
