# q_921 – height of the red cup (simulation_0262)

The video is a 2D-style fall at 24 fps (question_fps 24, the same as the file rate). The prior says the cup falls at g = 9.8 m/s² before 0.75 s (frames 2–18). There is no depth_info. The scale is metres per pixel = 9.8 / (pixel acceleration).

## Pixel acceleration (fit.py, fit2.py, rings2.py)
- The bbox top and bottom are biased by perspective: the underside ellipse shows above the horizon and the lid top below it. The bbox height goes 175 → 153 → 167 px during the fall. Edge fits therefore range from 5700 to 6700 px/s².
- A bias-free point is the sleeve's ring boundaries (red/tan) at the side silhouettes. These are R−G profile transitions at 6 px inside each edge (rings2.py).
  - The ring midpoint over f12–18 gives 6373 px/s² (max residual 0.05 px).
  - The constant second differences are 10.95–11.10 px/frame², i.e. 6371 px/s².
  - The lower ring alone gives 6378 (left) and 6426 (right).
  - f9–10 were misdetected (blur) and are excluded.
- Result: a = 6371 px/s², so the scale is 1.538e-3 m/px.
- Cross-check: the scene record's bbox-centre fit gives about 6470 (+1.5 %), but it is slightly biased by the ellipse.

## Pixel height (height.py, hfit.py)
- The height is measured from the lid top (frame difference to f0, which includes the lid dome) to the red bottom.
- The scene record's 144 px rest height misses the lid dome. Re-measured, the rest height is 161 px, but that includes the lid's top surface seen from above.
- The minimum apparent height is at the camera horizon (image y ≈ 900–950): 153 px at f13–14.
- A perspective model, h = H + r·sinθ, fitted over f7–18 gives H ≈ 150.7 px.
- I took H ≈ 152 ± 1.5 px.

## Answer
152 px × 1.538e-3 m/px = **0.234 m**. Alternatives: the 153 px minimum gives 0.235 m, the model's H gives 0.232 m, and the record's centre-based acceleration would give 0.230 m.

Plausibility: a tall lidded disposable cup, about 23 cm. That is large for a real cup but is consistent with the gravity scale.

Confidence: moderate-high, about ±3 %.
