# q_2131 — distance between baby and man (m)

Prior: total height of the sofa = 90 cm (the red sofa at left; the child sits against its back).
Internet clip, so I used the annotators' convention: one planar scale from the prior, no perspective correction.

## Scale (sofa_edges.py, sofa_profile.py)
- Column profiles of redness and luminance on frame 0 (with frames 14 and 28 as a check):
  - top edge of the sofa back: y ≈ 156 (x = 100–500, stable across frames)
  - bottom/floor contact (dark shadow under the base): y ≈ 530–536 at x = 100–200, and y ≈ 540–548 at x = 500–530
    (near the child)
- Sofa height ≈ 384 px (range 374–392 px), so the scale is 0.90 / 384 = 2.34e-3 m/px.

## Separation
- Bounding boxes from scene.json, checked on the grid frame:
  - child: f0 [275,375,612,668], f28 [345,372,645,670]
  - man (crouching): f0 [1205,95,1655,757], f28 [1300,88,1742,768]
- Centre to centre: f0 dx 987, dy 95, giving 992 px; f28 dx 1026, dy 93, giving 1030 px. The mean is about 1010 px.
- The separation changes slightly because the handheld camera pans with parallax.
- Distance = 1010 × 2.34e-3 ≈ **2.36 m**.

## Other readings
- Torso to torso (child torso x≈330, man torso/hip x≈1460–1580): about 1150–1250 px, or 2.7–2.9 m.
- Closest gap (child's shoe to man's knee): about 630 px, or 1.5 m.
- I answered with the centre-to-centre reading.

## Confidence
- Moderate. The scale is good to about 3%.
- The main uncertainty is which reference points the annotators clicked on the two people.
