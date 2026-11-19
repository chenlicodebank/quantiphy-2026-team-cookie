# Q156 — length of the plane (prior: car length 5.67 m)

2D clip, 24 fps (file fps = question_fps, no re-timing issue). Scale from one metres-per-pixel factor
taken from the car prior.

## Measurement (measure_len.py)
- Segmentation |RGB − bg(80,81,88)| > 12/25/40, 2×2 opening, largest component in the plane band (y 330–580)
  and the car band (y 590–650); x-extent = length.
- Car: 91 px (90–92 across thresholds) in frames 0–10, while it is near the image centre. It grows to 96–98 px
  at the right edge (frames 28–34) because perspective shows its front and rear faces off-centre. So I used the
  near-centre value, 91 px.
- Plane: 606–608 px in frames 3–17 (frame 3 is centred at x ≈ 945); 612 px at frame 0 (centre x ≈ 1028). The nose
  and tail-cone tips lie on the fuselage axis, so their projected extent hardly depends on perspective. I used 607.5 px.
- The record's values in scene/ (plane 608 px, car 91 px at frame 0) agree.

## Result
scale = 5.67 / 91 = 0.06231 m/px → plane = 607.5 × 0.06231 = 37.85 m. Answer: 37.8 m.

## Check
- Same-frame ratio, frame 3 (both objects near centre): 607/91 × 5.67 = 37.8 m; frame 0: 612/91 × 5.67 = 38.1 m.
- Sanity check: the car is a Cybertruck (real length 5.68 m, which matches the prior) and the plane is an Air China
  A320 (real length 37.57 m). The real length ratio is 6.61; the measured ratio is 6.68 (+1%), within the ±1 px
  error of the 91 px car.
Confidence: high (about ±2%).
