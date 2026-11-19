# q_2292 – displacement of the soccer ball between 1.0 s and 1.5 s (cm)

File fps = question_fps = 24 → t=1.0 s is frame 24, t=1.5 s is frame 36. Lab camera: f = 0.5959·1280 = 762.8 px,
principal point (640, 360). The gravity prior is not needed for a displacement; the scale comes from depth_info
(ball at 1.402 m at t=1.5 s).

## Measurements (scripts: measure.py, fit24.py, sphere.py, variants.py)
- f36 (ball in flight, motion-blurred): SAM mask blob centroid (812.2, 77.1) (matches scene record). Blob 118 × 95 px.
  The blur runs along the long axis (−22°, same as the f35→f37 motion). Width across the motion = 94.8–95.2 px = true
  ball width in that direction.
- Ball radius: projected-sphere model (off-axis ellipse) at distance 1.402 m along the centroid ray, matched to the
  95 px cross-motion width → R = 7.64–7.71 cm (D ≈ 15.3 cm). Used R = 7.64 cm.
- f24 (bottom of wind-up, ball sharp, hand covers the lower-left): circle fit to the clean green/ball arc (−108°…40°)
  → centre (277.4, 603.3), r = 55.9 px (frames 22–25 all give r 55.5–55.9, so the fit is stable). Projected-sphere fit
  to the same arc with R fixed → centre ray at pixel (268.7, 609.2), camera distance 1.132 m (residual 0.9 px; frames
  22, 23, 25 give 1.127–1.138 m).
- 3D: C24 = (−0.475, 0.319, 0.976) m, C36 = (0.290, −0.477, 1.286) m → |ΔC| = 114.7 cm.

## Checks / alternative routes
- Clicked visual centre (277.4, 603.3) + 1.132 m: 113.6 cm. Record centre (277.2, 604.4): 113.7 cm.
- Naive circle model (dist = f·R/r = 1.042 m): 111.8 cm; Z = f·R/r used as depth: 115.4 cm.
- R ±3 % → 113.9–115.6 cm; f36 point ±8 px → 113.8–115.7 cm.
All routes give 112–115.5 cm. Answer: 114.2 cm, the middle of the sphere-model and clicked-centre routes.

Caveat: the ball's real size implied by the given depth (≈15 cm) is small for a soccer ball, and the people's
depths do not fit neatly with the ball's apparent size. I followed the question's depth_info.
Confidence: moderate-high (about ±4 %).
