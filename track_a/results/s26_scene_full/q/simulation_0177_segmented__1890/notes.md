# q_1890 — height of the elephant (m)

Prior: elephant speed = 1.424 m/s. 2D clip (side-on walk to the right, static camera, plain white background), 24 fps (file = question fps).

## Method (measure.py)
- Mask: min(RGB) < 200, 3x3 opening, every frame (60 frames).
- Pixel speed (origin proxy), steady walk:
  - mask-centroid x linear fit 80.7 px/s; eroded-body centroid fit 81.9 px/s; net centroid 0→59 81.6 px/s; mean per-frame 2D centroid step 82.2 px/s (inflated by gait jitter).
  - Adopted 81.3 px/s (fits average) → scale = 1.424 / 81.3 = 0.01751 m/px.
- Height (top of back/head to lowest foot): median 185 px (range 176–191 px over the gait; mean 184.7).
- Height = 185 × 0.01751 = **3.24 m** (range 3.08–3.35 m across the gait).

## Check
- Scene record (independent script) gives the same figures: mean step 82 px/s, height median 185 px → 1.424/82×185 = 3.21 m, which agrees within 1%.
- A 3.2 m elephant is plausible in the real world.

Confidence: moderate-high. The main uncertainty is the gait-related variation in height (about ±3%).
