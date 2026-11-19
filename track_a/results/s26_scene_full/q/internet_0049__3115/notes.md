# q_3115 — canopy height (m)

Prior: rider's average speed = 3.8 m/s. Internet video, 30 fps (file rate = question_fps). I used one planar scale, following the annotators' convention.

## Scale (speed.py)
- Track: scene/tracks/rider_scooter.csv, background-relative torso x (`x_bg_px`), unflagged rows only (97 rows, frames 143–259).
- Average pixel speed:
  - from the endpoints: 941 px/s
  - from a cubic fit over windows 143–260 / 143–255 / 150–250 / 132–264: 938 / 935 / 946 / 917 px/s
  - value used: ≈ 935 px/s
- Scale = 3.8 / 935 = 0.00406 m/px.
- Sanity check: rider cap-to-sole height of 420 px gives 1.71 m, and the scooter's 263 px gives 1.07 m. Both are plausible.

## Canopy pixel height (frame 190, zoomed gridded crops)
- Front-left post: ground contact y ≈ 1583; top of the front beam (top of the pergola structure) at x≈1000 is y ≈ 507. That gives 1076 px.
- Front-right post: ground y ≈ 1597; beam top y ≈ 522. That gives 1075 px.
- Value used: 1076 px, so the height is 1076 × 0.00406 = **4.37 m**.

## Other readings
- Including the vines sticking up above the beams (top ≈ y 460) gives ≈1125 px, or 4.57 m.
- The rider rides behind the front row of posts, so a perspective-corrected value would be lower (roughly 3.5–3.8 m). I did not apply that correction because the annotators used no perspective correction.

## Confidence
Moderate. The speed scale is good to about ±3 %. The main uncertainty is which top and bottom points the annotators chose.
