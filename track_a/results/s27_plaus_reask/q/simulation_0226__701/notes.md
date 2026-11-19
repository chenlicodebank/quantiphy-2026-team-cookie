# q_701 – width of the beach chair (m)

Prior: black cat speed = 1.041 m/s. There is no depth_info. The scene is a top-down (2D-style) render at 24 fps; the file fps and question_fps are both 24.

## Scale (speed.py)
- The camera is static (see scene/notes.md). The cat walks straight along +x at a constant speed.
- Linear fit of the body centroid: 5.450 px/frame. The full-mask centroid gives 5.457 and the bbox centre 5.448. The mean per-frame step is 5.46, and net displacement / 49 frames is 5.44.
- I used 5.45 px/frame = 130.8 px/s, which gives 1.041 / 130.8 = 0.00796 m/px.

## Chair width (edges.py: Sobel-x edge peaks across rows y = 130–455 of frame 0)
- The front loungers lie with their long axis vertical in the image, so their width is the x-extent across the frame rails:
  - left: 750–944 = 194 px
  - middle: 1011–1205 = 194 px
  - right: 1271–1466 = 195 px (the outer edge of the right rail is faint; 1450 is the inner rail edge)
- The raised backrest tops measure about 203 px, but this is perspective magnification and not a wider part. The edges nearest the image centre (x ≈ 960) stay put, the outer edges move outward (left 750→741, middle 1205→1215, right 1271→1284), and the magnification is the same ≈1.04 for each chair. So the world width is the seat-level value, about 194.3 px.
- The cat's origin and the seat rails are at similar low heights, so any height correction is below about 1%.

Width = 194.3 px × 0.00796 m/px = **1.546 m**.

## Checks
- Second route: using the mean per-frame step (5.46 px/frame) instead of the fit gives 1.544 m. Using the backrest-top width (203 px) as an upper bound gives 1.616 m.
- Plausibility: at this scale the cat's body (without tail) is about 0.68 m and its full length about 0.85 m. That is about 1.3–1.5× a normal cat. The lounger is about 1.55 m wide and over 2.7 m long, which is large; it is proportionally wide, like a double lounger or daybed.
- The 2D geometry has nothing ill-conditioned: the scale is a clean, constant pixel speed on the same ground plane. So I kept the prior's scale rather than an assumed chair size. If the scene were at true cat or lounger scale the answer would be about 1.0–1.1 m, but that contradicts the exact prior.

Confidence: moderate-high on the measurement (±2%); the main risk is whether the reference used the image-consistent scale.
