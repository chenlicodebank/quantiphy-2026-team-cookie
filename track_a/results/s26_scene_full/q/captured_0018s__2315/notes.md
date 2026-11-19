# q_2315 – length of the box (cm)

Box = the white carton held by the far (left) person beside the soccer ball, released f29 and landing at f39, lying on its side by f47–48.
The file runs at 24 fps, the same as question_fps. f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).

## Pixel size (measure.py: |frame − frame0| mask, thresholds 25/40/60 give the same result)
- f39 (just landed, upright): 62 × 31–34 px (maybe slightly blurred)
- f40: 64–65 × 31 (bouncing, blurred). f41: 60 × 26–32 (minAreaRect 59.4–60.5)
- f47 lying: 56–58 × 33. f48 lying: 61 (minAreaRect 61.4) × 27.5
-> long dimension ≈ 61 px; short side ≈ 31 px.

## Depth (the box has no depth_info of its own)
- Held next to the soccer ball (2.80 m given), at almost the same image position (478, 262) vs (541, 265).
  This gives Z_forward ≈ 2.8 / 1.03 ≈ 2.72 m. The box falls straight down, so Z_forward stays the same.
- Ground-plane check: I fitted v_ground = c + k/Z to the two people (far feet row ≈574 at 3.13 m, near feet ≈697 at 2.00 m).
  The box's ground contact row (603 upright, 609 lying) then gives Z_forward ≈ 2.6–2.77 m. That agrees within about 5 %.
- Gravity fits (fitg.py) are unreliable. Frame timing is irregular (one frame probably dropped between f35 and f36), and the
  light carton is slowed by air drag. They are not used.

## Result
- Length = 61 px × 2.72 m / 762.8 = 0.218 m. The method card (Euclidean 2.8 m) gives 0.224 m. The ground-plane depth range
  gives 0.209–0.221 m.
- Answer: **22 cm** (longest dimension). For reference, the short side is ≈ 31 px, about 11 cm.
- On the "length = longer horizontal extent" reading: when the box lies on its side its longest edge is horizontal, so it is the
  same 22 cm. While it is held upright, its horizontal width is ≈ 11 cm.
- Confidence: moderate (about ±6 %, mostly from the depth).
