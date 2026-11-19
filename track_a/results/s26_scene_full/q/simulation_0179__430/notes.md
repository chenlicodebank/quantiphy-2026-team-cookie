# q430 — length of the trolley (shopping cart)

Prior: acceleration of the trolley = 1.507 m/s^2. This is a 2D side view and the cart rolls horizontally at a constant depth, so one metres-per-pixel scale is used. fps = question_fps = 24.

## Pixel acceleration (fit.py, using scene/tracks/shopping_cart.csv)
Quadratic fits of x(t) to several reference points (residuals of 0.2–0.9 px; starts from rest at t≈0):
- bbox_cx: 296 (frames 0–59), 304 (0–29), 301 (30–59) px/s^2
- bbox_x1 (front edge): 302 / 302 / 307
- wheels_cx: 295 / 302.5 / 299
- bbox_x0 and wheels_x0 (rear end) give 288–306. The rear edge is affected by the apparent length growing near the right edge of the frame (perspective).
Adopted a = 301 px/s^2 (first-half and front-edge fits agree on about 302). Scale = 1.507/301 = 0.00501 m/px.

## Pixel length
The x extent from handle tip to the front of the basket/wheel is 222–223 px over frames 0–30, where the cart is near the image centre and the view is nearly side-on. I checked this on a zoomed frame 12 (778 → about 999 px). Later frames grow to 235 px because the off-axis view shows more of the cart's end, so I did not use them.

Length = 222.5 px × 0.00501 = 1.11 m.

## Second-route check
Using the front-edge fit alone (302 px/s^2) gives 0.00499 m/px → 1.11 m. Using the full-clip centre fit (296) gives 1.13 m. The answer stays within about 2% across these routes.
Confidence: moderate to high. A shopping cart about 1.1 m long is plausible. Uncertainty comes from whether the reference length includes the handle, which the 3D bounding box does.
