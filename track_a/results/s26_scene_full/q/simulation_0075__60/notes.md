# Q60: length of the purple car (prior: white car length = 6 m)

This is a 2D, near top-down static view at 24 fps (file fps = question fps). One metres-per-pixel scale comes from the white van ("white car").

## Measurements (profile.py, profile2.py, measure.py)
- **White van length.** The van drives along y. I took the half-max edge of the brightness profile averaged over columns 805-860:
  - f0: 811.6 to 1046.1, which is 234.5 px
  - f36: 619.4 to 850.7, which is 231.4 px
  - f71: 81.8 to 317.0, which is 235.2 px
  - Mean: 233.7 px. The record gives 236 / 233 / 236 at threshold 25, which agrees.
- **Purple parked sedan length.** It lies horizontally, f0.
  - Front edge: the headlight/bumper half-max is at x ≈ 1242.5. The dark band before it, at 1231-1241, is shadow.
  - Rear edge: the purple tint (B-G > 0) ends at x ≈ 1439.5 on every row from 410 to 475.
  - Length: about 197 px. The record gives about 196 px.
- **Scale.** 6 / 233.7 = 0.02567 m/px.
- **Purple car length.** 197 × 0.02567 = 5.06 m.

## Check
The record's values (196 / 236) give 4.98 m. With the van length at its extremes (231-235 px), the answer is 5.03-5.12 m. Vehicle lengths do not change with position in the image, so a single scale is valid. Answer: **5.05 m**. Confidence is high, within about 3%.
