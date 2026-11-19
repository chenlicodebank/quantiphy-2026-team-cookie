# q_2271 — height of the person (cm), prior: g = 9.8 m/s^2, no depth_info

File fps = question fps = 24. Lab clip (background replaced). One woman stands still and tosses a plush toy twice.
Scale comes only from gravity: toy free-flight acceleration in px/frame^2 -> m/px, applied to the person's pixel height.

## Person pixel height
Frame 0 crops (frames/head0.png, feet0.png): hair top y≈132–133, shoe soles y≈640–641 -> **508 px** (scene record agrees).

## Toy free-flight acceleration (own measurements)
Flights: frames 17–21(22) and 52–58 (masks checked visually, frames/t1.png, t2.png: toy detached from hands).
- Silhouette (|frame−bg| > 45/60/80, silh.py): bbox mid 5.15–5.21 (flight 2), 4.80–5.21 (flight 1);
  area centroid 4.95–5.44. Top edge accelerates more (5.5–6.0) than bottom (4.4–4.8): the toy pitches,
  its vertical extent shrinks at the ends of flight; the bbox mid cancels this.
- Texture tracking (tm.py ref-template, chain.py adjacent-frame masked SSD): whole body 4.68–4.76,
  upper part 4.93–4.98, lower 4.39–4.59. Texture tracks are biased by the rotation of the visible surface,
  so silhouette mid is preferred.
- Adopted a ≈ 5.1 px/frame^2 (range 4.75–5.2). g per frame^2 = 9.8/576 = 0.017014 m.
  Scale = 0.017014/5.1 = 3.34 mm/px.

## Result
Same-depth (planar) estimate: 508 × 3.34 mm = **169.5 cm** (texture route a=4.75: 182 cm).
Perspective caveat: the woman is in a 3/4 view and tosses the toy in front of her, so the toy is likely
0.1–0.3 m closer to the camera than her body, which would raise the estimate (H ≈ H0 + δ/1.5 with f = 763 px,
Z ≈ 2.5 m) to ~175–190 cm. Real-world plausibility for this person favours the lower end.
Answer: **172 cm** (compromise between the planar gravity estimate ~170 and the small depth correction).
Confidence: moderate-low (±8%); dominated by toy rotation in short flights and toy/person depth difference.
