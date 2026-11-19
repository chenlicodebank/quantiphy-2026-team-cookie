# Q1034 – fire truck length (prior: speed 11.18 m/s)

2D top-down render; one metres-per-pixel scale from the prior speed.

- measure.py (own segmentation: background diff >25, open 3x3, largest component), frames 0–68.
- Pixel speed (linear fits over fully visible frames 0–47): bbox centre 26.30 px/frame, front edge 26.10, rear edge 26.49
  (small perspective spread, ~1.5%). Rear edge over 0–68: 26.20. Use the centre value of 26.30 px/frame.
- fps: file 24.005 vs question 24.0, a 0.02% difference that doesn't matter. Speed = 26.30 x 24.0 = 631.2 px/s.
- Scale = 11.18 / 631.2 = 0.017712 m/px.
- Length when the truck is centred in the image (frames 23–32, near-pure top view): 534 px (off-centre it reads 545–560 px
  because the sides show through perspective).
- Length = 534 x 0.017712 = **9.46 m**.
- Second route: using the rear-edge speed (26.49) or the front-edge speed (26.10), the length is 9.39 or 9.53 m, so ±0.8%.
  Matches the scene record (534 px, 26.33 px/frame).
- Confidence: high, within ~2%.
