# Q1098: height of the streetlight (m). Answer: 4.45 m

The file runs at 29.9966 fps and the question at 30 fps. Frame indices are used throughout (t = 1 s is frame 30).

## Measurements (px, 1080x1080)
- **Lamp:** top finial at y = 328, base bottom (front edge) at y ≈ 892-894, pole x ≈ 191. That gives a pixel height of about 566 (from vert_edges.py and zoomed crops). This confirms the scene record.
- **Man:** head top at y ≈ 650-651 and sole contact at ≈ 866-868, so he is about 217 px tall. The pelvis is at u = 83.7 in frame 0 and 135.8 in frame 30 (from the scene track), with v ≈ 766.
- **Camera pitch:** long vertical edges (pilaster at x≈143, edge at x≈471, the lamp pole) splay outward going down. The slope (dx/dy)/(x−cx) is about 3.5e-5 px⁻¹, which gives tanθ/f. So the camera is pitched up by about 3° (vert_edges2.py).

## Model (solve.py)
- **Setup:** a pinhole camera with cx = cy = 540, pitch θ and height h. The man walks at a constant depth Z. Unknowns: f, θ, h, Z_p, X(f0), X(f30).
- **Constraints:** the two given person distances (13.882 and 13.768), the pelvis pixel positions, the head and sole rows for 1.87 m, and the vertical-line convergence.
- **Fit:** f ≈ 1533 px, θ ≈ 3.0°, h ≈ 2.14 m, Z_p ≈ 13.27 m. Residuals are about 1 px, and the given depths are reproduced to about 1 mm.
- **Lamp, route A (given lamp distance 12.325):** the lamp's distance plus its pole position u and top row v=328 give the height.
  - Origin at the base: Z = 11.84, H = 4.42 m.
  - Origin at the centre: Z = 12.02, H = 4.45 m.
- **Lamp, route B (independent: ground plane):** this places the base contact using the fitted camera height. It gives H = 4.51-4.53 m. It implies a camera distance of 12.7-12.9, about 3% more than the given 12.325, so route B is treated as the less reliable one.
- **Sensitivity:** varying the sole/head rows by ±2 px, the pitch by ±0.5e-5 and the pelvis fraction gives H in the range 4.40-4.48 for route A.

## Answer
The answer is 4.45 m: route A, between the two origin assumptions, and leaning slightly toward route B.

Confidence: about ±3%.
