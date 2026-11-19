# q_3271 — width of the credit card (cm)

Prior: card length = 8.56 cm. Internet-video convention: one scale = 8.56 cm / pixel length of the card, applied to its pixel width. No time is named, so I used the rest frames 33–38, where the card is still, sharp and fully lit (camera static per scene/notes.md).

Measurement (measure2.py): card mask = Lab a* above the midpoint between card (178) and wall (146), which separates the card from the wall, the shadow and the hand (overlay frames/mask38.png).
- Length (horizontal extent at mid rows, frames 35–38): 926/929 → 1355/1359, which gives **429–431 px**, median 430. Tilt is about 1–2°, so this is negligible.
- Width (vertical extent of full columns away from the printed text): 1912→2203, 1914→2205 and 1915→2207, which gives **290–293 px**. Read by eye on the grid, the left edge is about 1906→2195 (≈290) and the right edge about 1914→2203 (≈289). I used 291 px.
- Width = 8.56 × 291 / 430 = **5.79 cm**.

Check: the scene record gives about 432 × ~300 px at rest, which is a ratio of 0.69 → 5.9 cm. That is consistent, but its mask bottom picked up a little shadow, and my edge columns give 291. The real ISO card is 5.40 cm (ratio 0.631). The image ratio is 0.677 because the card is slightly foreshortened/tilted. The benchmark converts pixels with one planar scale, so I report the pixel-based value.

Confidence: moderate. The pixel measurements are ±1%. The main uncertainty is whether the reference used the pixel ratio (5.8) or a value nearer the true 5.4.
