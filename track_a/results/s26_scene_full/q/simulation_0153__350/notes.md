# q_350 — acceleration of the blue car at t = 1 s

The question's fps and the file's fps are both 24, so t = 1 s is frame 24.
By the convention, a(24) = (v24 - v23)·fps = (x24 - 2·x23 + x22)·fps², which is the second difference centred on frame 23.

## Scene
The video is 2D: a light-blue cart drives side-on from left to right at a constant depth. The ground-contact line stays at y ≈ 947 and the cart's pixel size stays constant. The camera is static.
The cart eases in and out: its speed rises from about 1 px/frame at frame 0 to about 50 px/frame at frames 29–30, then falls.

## Scale (prior: tyre diameter 0.369 m)
- `wheelfit.py`: least-squares circle fits to the outer tyre edge. The front wheel gives D = 110 px (median, frames 29–41). This value is slightly inflated by the floor shadow and by the visible tread.
- `vprof.py`: sub-pixel half-level profiles through the front wheel. I measured from the hub-ring centre (symmetric rings) to the near-face edge:
  - horizontal radius 53.4–53.9 px (frames 33, 36, 41), so D ≈ 107.2 px
  - vertical radius 893.5 → 948.6, i.e. R ≈ 55 px
  - The far side of the silhouette also includes the tread, so I did not use it.
- Adopted D = 108 ± 2 px, giving a scale of 0.369/108 = 3.417e-3 m/px.

## Pixel acceleration
- **Route 1: panel template track** (scene record `panel_x`, frames 18–41, sub-pixel NCC). A Blender Bezier ease (smoothstep) model, x = a + X·(3u² − 2u³) with u = (f − f0)/T, fits with an rms of 0.05 px. Parameters: f0 = −0.15, T = 59.3, X = 1980 px. It gives a(24) = 0.7406 px/frame².
  - Local polynomials on the same data give 0.741–0.746.
  - The raw second difference is 0.71.
- **Route 2: independent NCC track of the front-wheel hub** (`track2.py`, frames 12–36, template from frame 24, the axle point). Cubic fits over 16–32 and 14–34 give 0.742 and 0.739 px/frame². This agrees with route 1 to within 0.5 %.
- Two other patches (front body, canopy) did not track because background was inside the template, so I discarded them. The front-wheel circle-fit centres and the rear-edge track only cover frames ≥ 29 (or ≥ 23 with contamination). They would have to be extrapolated, so I did not use them.

## Result
a = 0.741 px/frame² × 576 frame²/s² × 3.417e-3 m/px = **1.46 m/s²**.
The uncertainty is about ±3 %, mostly from the tyre's pixel diameter: 107–110 px gives 1.43–1.47 m/s². As a sanity check, the peak speed works out to ≈ 4.1 m/s, which is plausible for a cart.
